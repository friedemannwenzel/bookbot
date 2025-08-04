def words_in_book(text):
    words = text.split()
    word_count = 0
    for i in words:
        word_count += 1

    return word_count

def count_characters(text):
    lower_case_text = text.lower()
    char_counts = {}
    for i in lower_case_text:
        if i in char_counts:
            char_counts[i] += 1
        else:
            char_counts[i] = 1
    
    return char_counts

def sort_dictonary(char_counts):
    funny_empty_list = []
    for char, count in char_counts.items():
        funny_empty_list.append({"char": char, "num": count})

    def sort_on(item):
        return item["num"]
        
    funny_empty_list.sort(key=sort_on, reverse=True)
    
    return funny_empty_list



