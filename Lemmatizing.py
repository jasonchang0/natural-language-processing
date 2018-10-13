from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

'''
Lemmatizer is similar to stemming in that
both techniques return some universal form
of a word while lemmatization guarantees complete
words as compared to partial words in stemming.
'''

print(lemmatizer.lemmatize('cats'))
print(lemmatizer.lemmatize('cacti'))
print(lemmatizer.lemmatize('geese'))
print(lemmatizer.lemmatize('rocks'))
print(lemmatizer.lemmatize('python'))
print(lemmatizer.lemmatize('better'))
print(lemmatizer.lemmatize('better', pos='a'))

# Default parameter: pos='n'
print(lemmatizer.lemmatize('run'))
print(lemmatizer.lemmatize('run', pos='v'))







