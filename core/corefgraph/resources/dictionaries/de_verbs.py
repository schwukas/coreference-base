# -*- coding: utf-8 -*-

__author__ = 'josubg'

##de
copulative = set(("ist", "bin", "bist", "sind", "seid", "war", "warst", "waren", "wart","gewesen","wird", "werde", "werden",
                  "wirst", "werdet", "wurde", "wurdest", "wurden", "wurdet","geworden","scheint", "scheinen", "schien", "schienen",
                  "aussehe", "aussiehst", "aussieht", "aussehen", "aussah","aussahst","aussaht","aussahen","ausgesehen","auszusehen",
                  "fuehle", "fuehlt", "fuehlst", "fuehlen", "fuehlte","fuehltest","fuehltet","fuehlten","gefuehlt",
                  "fühle", "fühlt", "fühlst", "fühlen", "fühlte","fühltest","fühltet","fühlten","gefühlt",  "bleibe",
                  "bleibst", "bleibt", "blieben", "blieb", "bliebst", "bliebt", "blieben", "geblieben",  "rieche", "riechst", "riecht",
                  "riechen", "roch", "rochst", "rocht", "rochen", "gerochen", "hoere", "hoerst", "hoert", "hoeren", "hoerte", "hoertest",
                  "hoertet", "hoerten", "gehoert",  "höre", "hörst", "hört", "hören", "hörte", "hörtest", "hörtet", "hörten", "gehört",
                  "klinge", "klingt", "klingst", "klingen", "klang","klangst","geklungen", "schmecke", "schmeckst", "schmeckt", "schmecken",
                  "schmeckte", "schmecktest", "schmecktet", "schmeckten", "geschmeckt"))

# From StanfordCoreNLP
reporting = set(("accuse", "acknowledge", "add", "admit", "advise", "agree", "alert",
      "allege", "announce", "answer", "apologize", "argue",
      "ask", "assert", "assure", "beg", "blame", "boast",
      "caution", "charge", "cite", "claim", "clarify", "command", "comment",
      "compare", "complain", "concede", "conclude", "confirm", "confront", "congratulate",
      "contend", "contradict", "convey", "counter", "criticize",
      "debate", "decide", "declare", "defend", "demand", "demonstrate", "deny",
      "describe", "determine", "disagree", "disclose", "discount", "discover", "discuss",
      "dismiss", "dispute", "disregard", "doubt", "emphasize", "encourage", "endorse",
      "equate", "estimate", "expect", "explain", "express", "extoll", "fear", "feel",
      "find", "forbid", "forecast", "foretell", "forget", "gather", "guarantee", "guess",
      "hear", "hint", "hope", "illustrate", "imagine", "imply", "indicate", "inform",
      "insert", "insist", "instruct", "interpret", "interview", "invite", "issue",
      "justify", "learn", "maintain", "mean", "mention", "negotiate", "note",
      "observe", "offer", "oppose", "order", "persuade", "pledge", "point", "point out",
      "praise", "pray", "predict", "prefer", "present", "promise", "prompt", "propose",
      "protest", "prove", "provoke", "question", "quote", "raise", "rally", "read",
      "reaffirm", "realise", "realize", "rebut", "recall", "reckon", "recommend", "refer",
      "reflect", "refuse", "refute", "reiterate", "reject", "relate", "remark",
      "remember", "remind", "repeat", "reply", "add_report", "request", "respond",
      "restate", "reveal", "rule", "say", "see", "show", "signal", "sing",
      "slam", "speculate", "spoke", "spread", "state", "stipulate", "stress",
      "suggest", "support", "suppose", "surmise", "suspect", "swear", "teach",
      "tell", "testify", "think", "threaten", "told", "uncover", "underline",
      "underscore", "urge", "voice", "vow", "warn", "welcome",
      "wish", "wonder", "worry", "write"))

generics_you_verbs = "know"
pleonastic_verbs = ("is", "was", "became", "become")
alternative_a_pleonastic_verbs = ("seems", "appears", "means", "follows")
alternative_b_pleonastic_verbs = ("turns",)
