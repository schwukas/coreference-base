# coding=utf-8

""" General properties

Tagset values for each language as specified in resources/tagset. Currently, we use POS, Syntactic Constituents
and NER types tagsets. The nomenclature for the files in resources/target is used to instantiate the variables
below. For example, pos_tag_set will expect a file end in '_pos', such as 'tagset_pos'. The same applies to
'_constituent' and '_ner'.

"""

__author__ = 'Josu Bermudez <josu.bermudez@deusto.es>'


lang = "es"

pos_tag_set = "ancora"
constituent_tag_set = "ancora"
