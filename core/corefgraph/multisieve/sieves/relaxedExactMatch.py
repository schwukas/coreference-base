# coding=utf-8

__author__ = 'Josu Bermudez <josu.bermudez@deusto.es>'


from ...multisieve.sieves.base import Sieve
from ...resources.tagset import pos_tags


class RelaxedExactMatch(Sieve):
    """ Two mentions are coreferent if their surfaces are equals."""
    sort_name = "REM"
    #filter in options
    DISCOURSE_SALIENCE = True
    ONLY_FIRST_MENTION = False
    NO_PRONOUN = True
    NO_STOP_WORDS = True

    DEBUG = False

    def relaxed_form(self, mention):
        """ Return the form of the mention without the words after the head word.
        The form is lowered and all words are space separated.

        @param mention: The mention where the words are extracted.
        @return: a string of word forms separated by spaces.
        """
        mention_words = self.graph_builder.get_words(mention)
        mention_head = self.graph_builder.get_head_word(mention)
        relaxed_form = []
        head_index = 0
        comma_index = 0
        wh_index = 0
        for index, word in enumerate(mention_words):
            word_pos = word["pos"]
            if word["id"] == mention_head["id"]:
                head_index = index
            if not wh_index and pos_tags.wh_words(word_pos):
                wh_index = index
            if not comma_index and word == ",":
                comma_index = index

        if comma_index and comma_index > head_index:
            relaxed_form = [word["form"] for word in mention_words[:comma_index]]

        if not comma_index and wh_index and wh_index > head_index:
            relaxed_form = [word["form"] for word in mention_words[:wh_index]]

        return " ".join(relaxed_form).lower()

    def are_coreferent(self, entity, mention, candidate):
        """ Candidate and any mention of the entity have the same relaxed form are coreferent.
        """
        if not super(self.__class__, self).are_coreferent(entity, mention, candidate):
            return False

        candidate_form = self.relaxed_form(candidate)
        if candidate_form == "":
            return False
        for mention_x in entity:
            mention_x = self.graph.node[mention_x]
            mention_x_form = self.relaxed_form(mention_x)
            if mention_x_form == "":
                continue
            if (mention_x_form == candidate_form) or \
                    (mention_x_form + " 's" == candidate_form)or \
                    (mention_x_form == candidate_form + " 's"):
                self._print(mention_x["form"] + mention_x_form, candidate["form"] + candidate_form)
                return True
        return False

    def _print(self, mention, candidate):
        if self.DEBUG:
            print "R ", mention, candidate
