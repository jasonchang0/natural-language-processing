import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
# Unsupervised machine learning tokenizer


train_text = state_union.raw('2006-GWBush.txt')
test_text = state_union.raw('2006-GWBush.txt')

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = custom_sent_tokenizer.tokenize(test_text)


def process_content():
    try:
        for _ in tokenized:
            words = nltk.word_tokenize(_)
            tagged = nltk.pos_tag(words)

            # Options: Search for nouns v.s. NE_Chunk
            namedENt = nltk.ne_chunk(tagged, binary=True)
            # *WARNING*: High false positive and error rates

            namedENt.draw()

    except Exception as e:
        print(str(e))

"""
NE Type and Examples:

ORGANIZATION - Georgia-Pacific Corp., WHO
PERSON - Eddy Bonte, President Obama
LOCATION - Murray River, Mount Everest
DATE - June, 2008-06-29
TIME - two fifty a m, 1:30 p.m.
MONEY - 175 million Canadian Dollars, GBP 10.40
PERCENT - twenty pct, 18.75 %
FACILITY - Washington Monument, Stonehenge
GPE - South East Asia, MidlothianNE Type and Examples
ORGANIZATION - Georgia-Pacific Corp., WHO
PERSON - Eddy Bonte, President Obama
LOCATION - Murray River, Mount Everest
DATE - June, 2008-06-29
TIME - two fifty a m, 1:30 p.m.
MONEY - 175 million Canadian Dollars, GBP 10.40
PERCENT - twenty pct, 18.75 %
FACILITY - Washington Monument, Stonehenge
GPE - South East Asia, Midlothian
"""

process_content()





