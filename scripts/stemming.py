from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
# Founded in 1969

# I was taking a "ride" in the car.
# I was "riding" in the car.

ps = PorterStemmer()

example_words = ['python', 'pythoner', 'pythoning', 'pythoned', 'pythonly']

for _ in example_words:
    print(ps.stem(_))

example_text = 'It is very important to the pythonly while you are pythoning with python.' \
               'All pythoners have pythoned poorly at least once.'

stop_words = set(stopwords.words('english'))

for _ in word_tokenize(example_text):
    if _ not in stop_words:
        print(ps.stem(_))





