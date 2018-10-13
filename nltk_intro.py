import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

# nltk.download()

# tokenizing = word tokenizers... sentence tokenizers
# lexicon and corporas
# corpora - body of text.
#       ex: medical journals, presidential speeches, English language
# lexicon - words and their meanings

# investor-speak... regular English-speak
# investor speak 'bull' - someone who is positive about the market
# English-speak 'bull' - a type of animal

example_text = 'Hello Mr. Smith, how are you doing today? ' \
               'THe weather is great and Python is awesome. ' \
               'The sky is pinkish-blue. ' \
               'You should not each cardboards.'

print(sent_tokenize(example_text))

print(word_tokenize(example_text))

for _ in word_tokenize(example_text):
    print(_)


