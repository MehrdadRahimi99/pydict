# Download PyDictionary then import it
from PyDictionary import PyDictionary

pydict = PyDictionary()

#get the word
word = input("Type your word: ")

meanings = pydict.meaning(word)

print(meanings)
