
from PyDictionary import PyDictionary

word = input("Enter a word: ")

dictionary = PyDictionary()


def meaning():

    meanings = dictionary.meaning(word)

    if meanings:
        for part_of_speech, meaning_list in meanings.items():
            print(f"{part_of_speech} meanings:")

            for index, meaning in enumerate(meaning_list, start=1):
                print(f"{index}. {meaning}")
            print('#'*15)
    else:
        print("No meanings found for the given word.")

meaning()        