# Repracticing/Revising python after 1 year since i completed it an year ago, because I started JS in the middle -_-
# Python 3.8

# * Mad Libs Generator *
# Author: Obaid Nadeem
# Library used: Random-word.py
# Link to library: https://pypi.org/project/Random-Word/

from random_word import RandomWords

r = RandomWords()
num_of_words = int(input("Enter number of words: "))


# / Using for loop (slower method) /
# for i in range(num_of_words):
#     word = r.get_random_word()
#     print(word)


# / Using the inbuild limit() function (faster method) /
words = r.get_random_words( limit = num_of_words)
print(words)


# I never played mad libs game so this is what I understood about it and this is what I came up with






