def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    num_words = get_word_count(text)
    frequencies = count_dict_to_list(get_character_count(text))
    frequencies.sort(reverse=True, key=sort_on)
    print(f"{num_words} words found in the document\n")
    for dict in frequencies:
        print(f"The '{dict["char"]}' character was found {dict["count"]} times")

def sort_on(dict: dict):
    return dict["count"]

def get_word_count(text: str) -> int:
    words = text.split()
    return len(words)

def get_character_count(text: str) -> dict:
    frequency_dict = {}
    for word in text.lower().split():
        for char in word:
            if not char.isalpha():
                continue
            if char in frequency_dict:
                frequency_dict[char] += 1
            else:
                frequency_dict[char] = 1
    return frequency_dict

def count_dict_to_list(dict: dict) -> list:
    frequency_list = []
    for k in dict:
        frequency_list.append({"char": k, "count": dict[k]})
    return frequency_list

def get_text(path) -> str:
    with open("books/frankenstein.txt") as f:
        return f.read()

main()