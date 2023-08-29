
from PyDictionary import PyDictionary

dictionary = PyDictionary()


def print_meaning(word):

    meanings = dictionary.meaning(word)
    
    if meanings:
        for part_of_speech, meaning_list in meanings.items():
            print(f"{part_of_speech} meanings:")

            for index, meaning in enumerate(meaning_list, start=1):
                print(f"{index}. {meaning}")
            print('#'*15)
    else:
        print("No meanings found for the given word.")

def print_synonym(word):

    synonyms = dictionary.synonym(word)
    print(synonyms)


def main():
    while True:
        word = input("Enter a word: ")

        if word.strip():
            print_meaning(word)
            print_synonym(word)
        else:
            print("please write a word")

if __name__ == "__main__":
    main()