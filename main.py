def get_book_text(path):
    with open(path) as f:
        file_contents = f.read() 
    return file_contents

def words_in_book(text):
    words = text.split()
    word_count = 0
    for i in words:
        word_count += 1

    return word_count
    
def main():
    path = "./books/frankenstein.txt"
    text = get_book_text(path)
    word_count = words_in_book(text)
    print(f"{word_count} words found in the document")

main()
