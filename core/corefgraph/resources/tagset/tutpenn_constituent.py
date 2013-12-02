# coding=utf-8
__author__ = 'Valeria Quochi <valeria.quochi@ilc.cnr.it>'
__date__= '5/16/2013'

from ..lambdas import equality_checker, list_checker

# Clauses

""" simple declarative clause, i.e. one that is not introduced by a (possible empty) subordinating conjunction or a
wh-word and that does not exhibit subject-verb inversion"""
simple = "S"

"""Clause introduced by a (possibly empty) subordinating conjunction."""
subordinated = "SBAR"

"""Direct question introduced by a wh-word or a wh-phrase. Indirect questions and relative clauses should be
bracketed as SBAR, not SBARQ."""
#direct_question = "SBARQ"

"""Inverted declarative sentence, i.e. one in which the subject follows the tensed verb or modal."""
#inverted_declarative = "SINV"

"""Inverted yes/no question, or main clause of a wh-question, following the wh-phrase in SBARQ."""
#inverted_question = "SQ"

# Phrases

noun_phrase = "NP"
wh_noun_phrase = "NP"

adjetival_phrase = "ADJP"
adverb_phrase = "ADVP"
conjuntion_phrase = "CONJ"
#fragment = "FRAG"
#interjection = "INTJ"
#list_marker = "LST"
#not_a_constituent = "NAC"
#noun_phrase_mark = "NX"
prepositional_phrase = "PP"
parenthetical = "PRN"
#particle = "PRT"
#quantifier_phrase = "QP"
#reduced_relative_clause = "RRC"
#unlike_coordinated_phrase = "UCP"
verb_phrase = "VP"
#wh_adjective_phrase = "WHADJP"
#wh_adverb = "WHAVP"
#wh_prepositional_phrase = "WHPP"
#unknown = "X"


#clauses = list_checker((simple, subordinated, direct_question, inverted_declarative, inverted_question))

clauses = list_checker((simple, subordinated))

verb_phrases = equality_checker(verb_phrase)
noun_phrases = equality_checker(noun_phrase)

mention_constituents = list_checker((noun_phrase, wh_noun_phrase))

root= list_checker(("root", "top", "ROOT", "TOP"))

phrases = list_checker((noun_phrase,  adjetival_phrase, adverb_phrase, conjuntion_phrase, prepositional_phrase, parenthetical, verb_phrase))
