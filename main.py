
def main():
    temp_dict = {'p': 6121, 'r': 20818, 'o': 25225}
    book_path = "books/frankenstien.txt"
    file_contents = get_file_text(book_path)
    #print(file_contents)

    print_char_report(book_path)

    
def get_file_text(path):
    with open(path) as f:
        return f.read()

def count_words(book):
    return len(book.split())

def count_chars(book):
    char_count = {}
    
    book_lowercase = book.lower()
    for token in book_lowercase:
        if token not in char_count:
            char_count[token] = 1
        else:
            char_count[token] += 1
    return char_count

def convert_to_list(dictionary):
    return_list =  []
    for key, value in dictionary.items():
        if key.isalpha():
            return_list.append({"name":key, "value":value})
    return_list.sort(key=lambda x: x["value"], reverse=True)
    return return_list

def print_char_report(book_path):

    file_contents = get_file_text(book_path)
    word_count = count_words(file_contents)
    char_count = count_chars(file_contents)
    char_list = convert_to_list(char_count)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n\n")
    for char in char_list:
        print(f"The '{char['name']}' character was found {char['value']} times")
    print("--- End report ---")
    
if __name__ == "__main__":
    main()