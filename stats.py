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