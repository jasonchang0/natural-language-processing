import sentiment_module as s_mod

pos_ex = 'The movie was good. ' \
         'The movie had a happy ending.' \
         'Sound of the movie was perfect.' \
         'Lovely movie, every should go watch it once.' \
         'The acting was great, plot was wonderful, and the casting was splendid.'

neg_ex = 'The movie was horrible. ' \
         'Nothing is good about the moive. ' \
         'This movie is not worth the time to watch. ' \
         'The movie is a waste of time.'

print(s_mod.sentiment(pos_ex))
print(s_mod.sentiment(neg_ex))





