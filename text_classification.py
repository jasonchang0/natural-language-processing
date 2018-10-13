import nltk
import random
from nltk.corpus import movie_reviews
import pickle

# document = [([w1, w2,..., wn], 'neg'), ([w1, w2,..., wn], 'pos')]
documents = [(list(movie_reviews.words(file_id)), category) for category in movie_reviews.categories()
             for file_id in movie_reviews.fileids(category)]

# documents = []

# for category in movie_reviews.categories():
#     for file_id in movie_reviews.file_ids(category):
#         documents.append(list(movie_reviews.words(file_id)), category)

random.shuffle(documents)

print(documents[1])

all_words = []
for w in movie_reviews.words():

    # append without categorical label
    all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)
# print(all_words.keys())

print(all_words.most_common(30))
# print(all_words['ridiculous'])1

# Check against the top 3000 words of the document
word_features = list(all_words.keys())[:3000]
# print('Word Features: {}'.format(word_features))


# convert [([w1, w2,..., wn], 'neg'), ([w1, w2,..., wn], 'pos')]
# ->
def find_features(document):
    words = set(document)
    features = {}

    for _ in word_features:
        features[_] = (_ in words)

    return features


print((find_features(movie_reviews.words('neg/cv000_29416.txt'))))

# print(documents)
# for (rev, category) in documents:
#     print(rev)
#     print(category)

feature_sets = [(find_features(rev), category) for (rev, category) in documents]
print(feature_sets[:5])

train_set = feature_sets[:1900]
test_set = feature_sets[1900:]

# Naive Bayes classifier
# posterior = prior occurrences * likelihood / evidence

# classifier = nltk.NaiveBayesClassifier.train(train_set)
classifier_f = open('naivebayes.pickle', 'rb')
classifier = pickle.load(classifier_f)
classifier_f.close()

accuracy = nltk.classify.accuracy(classifier, test_set)

print('Naive Bayes Algorithm accuracy percentage: {}%'.format(accuracy * 100))
classifier.show_most_informative_features(15)

save_classifier = open('naivebayes.pickle', 'wb')
pickle.dump(classifier, save_classifier)
save_classifier.close()







