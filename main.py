from stats import words_in_book
from stats import count_characters
from stats import sort_dictonary
import sys

if  len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    pass

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read() 
    return file_contents


    
def main():
    path = sys.argv[1]
    text = get_book_text(path)
    word_count = words_in_book(text)
    char_count = count_characters(text)
    nice_count = sort_dictonary(char_count)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for i in nice_count:
        if i["char"].isalpha():
            print(f"{i['char']}: {i['num']}")
    print("============= END ===============")

main()
