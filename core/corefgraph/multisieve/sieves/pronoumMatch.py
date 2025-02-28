# coding=utf-8
""" The sieves that check pronouns.

"""
__author__ = 'Josu Bermudez <josu.bermudez@deusto.es>'

from ...multisieve.sieves.base import Sieve
from ...resources.tagset import ner_tags
from ...resources.demonym import locations_and_demonyms
from ...resources.dictionaries import pronouns


class PronounMatch(Sieve):
    """ To mentions are coreferent if their surfaces are equals."""
    sort_name = "PNM"
    #Filter options
    NO_PRONOUN = False
    ONLY_FIRST_MENTION = True
    DISCOURSE_SALIENCE = True
    NO_STOP_WORDS = False

    SENTENCE_DISTANCE_LIMIT = 3

    def validate(self, mention, mention_index):
        """ Only pronouns can be used for this sieve

        :param mention: The mention to check.
        :param mention_index: Index of the mention inside entity:
        """
        if not super(self.__class__, self).validate(mention, mention_index):
            return False
            #TODO CHECK PRONOUN FORMS
        if mention["mention"] != "pronoun_mention":
            self.debug("MENTION FILTERED Not a pronoun: %s", mention["form"])
            return False
        return True

    def are_coreferent(self, entity, mention, candidate):
        """A pronoun is correfent with a candidate?

        :param candidate: The candidate that may corefer the entity.
        :param mention: The selected mention to represent the entity.
        :param entity: The entity that is going to be evaluated.
        :@return True or False
        """

        candidate_entities = [[self.graph.node[candidate_mention] for candidate_mention in candidate_entity]
                              for candidate_entity in self.entities_of_a_mention(candidate)]
        entity_mentions = [self.graph.node[m] for m in entity]

        if not super(self.__class__, self).are_coreferent(entity, mention, candidate):
            return False

        if candidate["form"].lower() in locations_and_demonyms and \
                mention["form"].lower() not in pronouns.no_organization:
            self.debug("LINK FILTERED Candidate is location and mention is not organization valid: %s",
                       candidate["form"])
            return False
        sentence_distance = self.graph_builder.sentence_distance(mention, candidate)
        if sentence_distance > self.SENTENCE_DISTANCE_LIMIT \
                and not self.is_first_person(mention) and not self.is_you(mention):
            self.debug("LINK FILTERED Candidate to far%s and not I or You:  %s", sentence_distance, candidate["form"])
            return False

        if self.i_within_i(mention, candidate):
            self.debug("LINK FILTERED I within I construction: %s",
                       candidate["form"])
            return False

        if self.entity_person_disagree(entity_mentions, candidate_entities):
            self.debug("LINK FILTERED Person Disagree: %s",
                       candidate["form"])
            return False

        #if not self.agree_attributes(entity, candidate):
        #    return False
        if ((
                self.UNKNOWN in self.entity_property(entity, "gender") or
                self.UNKNOWN in self.candidate_property(candidate, "gender") or
                self.candidate_property(candidate, "gender").intersection(
                self.entity_property(entity, "gender"))) and
           (
                self.UNKNOWN in self.entity_property(entity, "number") or
                self.UNKNOWN in self.candidate_property(candidate, "number") or
                self.candidate_property(candidate, "number").intersection(
                    self.entity_property(entity, "number"))) and
           (
                self.UNKNOWN in self.entity_property(entity, "animacy") or
                self.UNKNOWN in self.candidate_property(candidate, "animacy") or
                self.candidate_property(candidate, "animacy").intersection(
                    self.entity_property(entity, "animacy"))) and
           (
                ner_tags.no_ner in self.entity_property(entity, "ner") or
                ner_tags.no_ner in self.candidate_property(candidate, "ner") or
                self.candidate_property(candidate, "ner").intersection(self.entity_property(entity, "ner")))):
            self.debug("LINK MATCH: %s", candidate["form"])
            return True
        self.debug("LINK IGNORED: %s", candidate["form"])
        return False

    def entity_person_disagree(self, mention_entity, candidate_entities):
        """ Any mention of the entity or the candidate entity disagrees?
        @param mention_entity: The original cluster of mentions
        @param candidate_entities: The cluster of mentions that candidate is coreferent
        @return: True or False
        """
        for candidate_entity in candidate_entities:
            for candidate in candidate_entity:
                for mention in mention_entity:
                    if self.mention_person_disagree(mention, candidate, candidate_entities, mention_entity):
                        return True
        return False

    @staticmethod
    def get_person(mention):
        """ Extract the person of a mention.
        @param mention: A mention
        @return: A string representing the person I, we, you...
        """
        form = mention["form"].lower()
        gender = mention["gender"]
        number = mention["number"]
        animacy = mention["animacy"]
        if form in pronouns.first_person:
            if number == "singular":
                return "I"
            if number == "plural":
                return "we"
        if form in pronouns.second_person:
            return "you"
        if form in pronouns.third_person:
            if gender == "male" and number == "singular":
                return "he"
            if gender == "female" and number == "singular":
                return "she"
            if gender == "neutral" or animacy == "inanimate" and number == "singular":
                return "it"
            if number == "plural":
                return "they"
        return "UNKNOWN"

    def mention_person_disagree(self, mention, candidate, candidate_entities, mention_entity):
        """ Check if the person of the mention and the candidate disagrees.

        @param mention:
        @param candidate:
        @param candidate_entities:
        @param mention_entity:
        @return:
        """
        same_speaker = self.same_speaker(mention, candidate)
        mention_person = self.get_person(mention)
        candidate_person = self.get_person(candidate)
        if same_speaker and mention_person != candidate_person:
            if (mention_person == "it" and candidate_person == "they") or \
                    (mention_person == "they" and candidate_person == "it") or \
                    (mention_person == "they" and candidate_person == "they"):
                return False
            else:
                if mention_person != "UNKNOWN" and candidate_person != "UNKNOWN":
                    return True
        if same_speaker:
            if not self.is_pronoun(mention):
                if candidate_person in ("I", "we", "you"):
                    return True
            if not self.is_pronoun(candidate):
                if mention_person in ("I", "we", "you"):
                    return True
        if mention_person == "you" and candidate["span"] < mention["span"]:
            head_word = self.graph_builder.get_head_word(mention)
            utterance = head_word["utterance"]
            if utterance == 0:
                return True
            prev_speaker = head_word["prev_speaker"]
            if "mention" not in prev_speaker:
                return True
            for candidate_entity in candidate_entities:
                if prev_speaker in candidate_entity and candidate_person != "I":
                    return True

        elif candidate_person == "you" and mention["span"] < candidate["span"]:
            head_word = self.graph_builder.get_head_word(candidate)
            utterance = head_word["utterance"]
            if utterance == 0:
                return True
            prev_speaker = head_word["prev_speaker"]
            if "mention" not in prev_speaker:
                return True
            if prev_speaker in mention_entity and mention_person != "I":
                return True
        return False
