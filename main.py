def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    sorted_list = get_list(chars_dict)
    print(f"--- Start of assignment for {book_path} ---")
    print(f"{num_words} of words found in this document")
    for i in sorted_list:
        print(f"The{i['char']} was found {i['num']} of times.")
    print("This took me a while to understand how all the code works together.")
    print("--- This is the end of the assignment ---")


def get_list(num_chars_dict):
    chars_list = []
    for chars in num_chars_dict:
        if chars.isalpha() == True:
            chars_list.append({"char": chars, "num": num_chars_dict[chars]})
    chars_list.sort(key=sort_on, reverse=True)
    return chars_list


def sort_on(d):
    return d["num"]


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_character_sums(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()