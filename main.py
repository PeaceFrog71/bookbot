
def main():
    book_path = "./books/frankenstien.txt"
    file_contents = get_file_text(book_path)
    #print(file_contents)
    
    word_count = count_words(file_contents)
    char_count = count_chars(file_contents)
    print(f"word count = {word_count}")
    print(f"char count = {char_count}")
    print(f"number of unique chars = {len(char_count)}")
    

def get_file_text(path):
    with open("./books/frankenstien.txt") as f:
        return f.read()

def count_words(book):
    """
    Alternative method that strips punctuation and removes empty words left after punctuation removal. 
    import string
    
    strip_chars = string.punctuation
    
    #split the book into words and strip punctuation from begining and trailing edge of word strings
    #words = [word.strip(strip_chars) for word in book.split()] 
    words = [word for word in book.split()] 
    words = [word for word in words if word] #only passes word if it is not an empty string
    print(words[:100]) """
    
    words = book.split()
    return len(words)

def count_chars(book):
    char_count = {}
    
    book_lowercase = book.lower()
    for token in book_lowercase:
        if token not in char_count:
            char_count[token] = 1
        else:
            char_count[token] += 1
    return char_count

if __name__ == "__main__":
    main()