import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
# Unsupervised machine learning tokenizer

'''
Regex Cheatsheet:

Identifiers:

\d = any number
\D = anything but a number
\s = space
\S = anything but a space
\w = any letter
\W = anything but a letter
. = any character, except for a new line
\b = space around whole words
\. = period. must use backslash, because . normally means any character.
Modifiers:

{1,3} = for digits, u expect 1-3 counts of digits, or "places"
+ = match 1 or more
? = match 0 or 1 repetitions.
* = match 0 or MORE repetitions
$ = matches at the end of string
^ = matches start of a string
| = matches either/or. Example x|y = will match either x or y
[] = range, or "variance"
{x} = expect to see this amount of the preceding code.
{x,y} = expect to see this x-y amounts of the precedng code
White Space Charts:

\n = new line
\s = space
\t = tab
\e = escape
\f = form feed
\r = carriage return
Characters to REMEMBER TO ESCAPE IF USED!

. + * ? [ ] $ ^ ( ) { } | \
Brackets:

[] = quant[ia]tative = will find either quantitative, or quantatative.
[a-z] = return any lowercase letter a-z
[1-5a-qA-Z] = return all numbers 1-5, lowercase letters a-q and uppercase A-Z
'''

train_text = state_union.raw('2006-GWBush.txt')
test_text = state_union.raw('2006-GWBush.txt')

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = custom_sent_tokenizer.tokenize(test_text)


def process_content():
    try:
        for _ in tokenized:
            words = nltk.word_tokenize(_)
            tagged = nltk.pos_tag(words)

            # chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""
            chunkGram = r"""Chunk: {<.*>+}
                                    }<VB.?|IN|DT>+{"""
            # {} => inclusion, }{ -> exclusion

            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)

            print(chunked)
            chunked.draw()

            # print(tagged)

    except Exception as e:
        print(str(e))


process_content()






