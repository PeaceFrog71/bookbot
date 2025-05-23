from stats import count_words, count_chars
import sys

def main():
    #temp_dict = {'p': 6121, 'r': 20818, 'o': 25225}
    #book_path = "books/frankenstein.txt"

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        # Exit with error code 1
        sys.exit(1) 
        
    book_path = sys.argv[1]
    file_contents = get_book_text(book_path)
    #print(file_contents)

    print_char_report(book_path)
    
def get_book_text(path):
    with open(path) as f:
        return f.read()

def convert_to_list(dictionary):
    return_list =  []
    for key, value in dictionary.items():
        if key.isalpha():
            return_list.append({"name":key, "value":value})
    return_list.sort(key=lambda x: x["value"], reverse=True)
    return return_list

def print_char_report(book_path):

    file_contents = get_book_text(book_path)
    word_count = count_words(file_contents)
    char_count = count_chars(file_contents)
    char_list = convert_to_list(char_count)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print(f"----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print(f"----------- Character Count -----")
    for char in char_list:
        print(f"{char['name']}: {char['value']}")
    print("============= END ===============")
    
if __name__ == "__main__":
    main()