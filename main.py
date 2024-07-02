
def main():
    book_path = "./books/frankenstien.txt"
    file_contents = get_file_text(book_path)
    print(file_contents)


def get_file_text(path):
    with open("./books/frankenstien.txt") as f:
        return f.read()
    

if __name__ == "__main__":
    main()