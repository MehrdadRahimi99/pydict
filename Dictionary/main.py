
from PyDictionary import PyDictionary

dict = PyDictionary()


def print_meaning(word):

    meanings = dict.meaning(word)
    
    if meanings:
        for part_of_speech, meaning_list in meanings.items():
            print(f"{part_of_speech} meanings:")

            for index, meaning in enumerate(meaning_list, start=1):
                print(f"{index}. {meaning}")
            print('#'*15)
    else:
        print("No meanings found for the given word.")

def print_synonym(word):

    synonyms = dict.synonym(word)
    
    if synonyms:
        synonyms_str = ", ".join(synonyms)
        print(f"Synonyms: {synonyms_str}")
    else:
        print("No synonyms found for the given word.")


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