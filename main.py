def main():
    book_path="books/frankenstein.txt"
    text=get_book_text(book_path)
    word_count=count_words(text)
    print(word_count)
    char_dictionary=count_characters(text)
    print(char_dictionary)

def count_words (file_contents):
    words=file_contents.split()
    return len(words)


def get_book_text(path):
    with open(path) as f :
        file_contents = f.read()
        return file_contents


def count_characters(text):
    lowered_text=text.lower()
    char_count={}

    for char in lowered_text:
        char_count[char]=char_count.get(char, 0) + 1
    return char_count


main()
