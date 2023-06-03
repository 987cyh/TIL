# -*- coding: utf-8 -*-
"""
□ 참고 : https://wikidocs.net/64517
□ 기능 : NLP Preprocessing
□ 목적 : NLP Preprocessing 학습
"""
#%%
en_text = "A Dog Run back corner near spare bedrooms"

import spacy
spacy_en = spacy.load('en')

def tokenize(en_text):
    return [tok.text for tok in spacy_en.tokenizer(en_text)]

print(tokenize(en_text))


