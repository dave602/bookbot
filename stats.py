def get_word_count(book_text):
    word_list = book_text.split()
    return len(word_list)

def get_character_count(book_text):
    count_dict = {}
    for character in book_text:
        character = character.lower()
        if character in count_dict:
            count_dict[character] += 1
        else:
            count_dict[character] = 1
    return count_dict

def dict_sort(dict):
    new_list = []
    for character, count in dict.items():
        new_list.append({"character": character, "count": count})
    new_list.sort(reverse=True, key=lambda dict: dict["count"])
    return new_list
