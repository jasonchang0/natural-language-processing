from nltk.corpus import wordnet

syns = wordnet.synsets('program')

'''
from nltk.corpus import wordnet

def get_wordnet_pos(treebank_tag):

    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    elif treebank_tag.startswith('S'):
        return wordnet.ADJ_SAT
    else:
        return ''
'''

print(syns)

# synset
print(syns[0].name())

# just the word
print(syns[0].lemmas()[0].name())

# definition
print(syns[0].definition())

# examples
print(syns[0].examples())


synonyms = []
antonyms = []

for syn in wordnet.synsets('good'):
    for l in syn.lemmas():
        synonyms.append(l.name())
        print("l: {}".format(l))
        # get top antonyms of the synonyms
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())

print(set(synonyms))
print(set(antonyms))


w1 = wordnet.synset('ship.n.01')
w2 = wordnet.synset('boat.n.01')
w3 = wordnet.synset('car.n.01')

# Wu-Palmer Similarity
print(w1.wup_similarity(w2))
print(w1.wup_similarity(w3))





