def main():
    book_path=input("Insert path to book")
    text=get_book_text(book_path)
    word_count=count_words(text)
    char_dictionary=count_characters(text)
    print(f'--- Begin report of {book_path} ---')
    print(f"{word_count} words found in the document")
    print("")
    print("")
    print_report(char_dictionary)
    print("--- End report ---")
    

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

def print_report(char_dict):
    list_to_sort=[]

    for char, count in char_dict.items():
        if char.isalpha():
            list_to_sort.append({"char": char, "num": count})

    list_to_sort.sort(reverse=True, key=sort_on)

    for char in list_to_sort:
        print(f"The '{char["char"]}' character was found {char["num"]} times")


def sort_on(dict):
    return dict["num"]
        
main()
