#!/usr/bin/env python
# coding: utf8
"""Rough russian adjectives detector written in python."""

import re
from collections import Counter


class RAdj:
    """RAdj base class."""

    def __init__(self, list_of_words):
        self.text = list_of_words
        self.text_len = self.text

    def detect(self, what=list("PQR")):
        """Rerurn tuple of positions with predictions.
        
        Predictions are combination of codes:
        1 - possessive code
        3 - qualitative code
        5 - relative and qualitative code
        """

        forecast = Counter()
        forecast_func = {"P": self.detect_pos_adj,
                         "Q": self.detect_qrel_adj,
                         "R": self.detect_rel_adj}
        for wt in what:
            forecast.update(dict( forecast_func[wt]() ))

        return forecast.most_common()
    
    def detect_pos_adj(self):
        """Detection of possessive adjectives."""

        code = 1
        endings = ('ий', 'ья', 'ью', 'ьи', 'ьим', 'ьими', 'ьих', 'ьем', 'ьей',
                   'ьего', 'ьему', 'ин', 'ина', 'ину', 'ино', 'иной', 'ином',
                   'иному', 'иного', 'ины', 'иным', 'иных', 'иными', 'ов', 
                   'ова', 'ову', 'ово', 'овой', 'овому', 'овом', 'ового', 'овы',
                   'овым', 'овых', 'овыми')

        return ((idx, code) for idx, wd in enumerate(self.text) \
            if wd.endswith(endings))

    def detect_rel_adj(self):
        """Detection of relative adjectives only."""

        code = 3
        pattern = r'''
            ([а-я]+)
            (((е|о)нн)|((те)?льн)|(((ин)|(ен)|(ов)|(иче))ск)|(озн)|(аст)|(ист))
            ([а-я]{2,3})'''
        suffixes = re.compile(pattern)

        return ((idx, code) for idx, wd in enumerate(self.text) \
            if re.match(suffixes, wd))

    def detect_qrel_adj(self):
        """Detection of qualitative and relative adjectives."""

        code = 5
        endings = ('ый', 'ым', 'ий', 'им', 'ой', 'ом', 'ей', 'ем', 'ая',
                   'яя', 'ую', 'юю', 'ого', 'его', 'ему', 'ому', 'ые',
                   'ых', 'ым', 'ие', 'их', 'им', 'ыми', 'ими')

        return ((idx, code) for idx, wd in enumerate(self.text) \
            if wd.endswith(endings))
