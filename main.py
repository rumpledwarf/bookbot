def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_counter(text)
    chars_dict = letter_counter(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_counter(text):
    words = text.split()
    return (len(words))

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def letter_counter(text):
    lowercase_string = text.lower()
    letter_dict = {}
    for letters in lowercase_string:
        if letters not in letter_dict:
            letter_dict[letters] = 1
        else:
            letter_dict[letters] +=1
    return letter_dict

def sort_on(d):
    return d["num"]

main()