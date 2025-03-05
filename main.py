from stats import get_word_count, get_character_count, dict_sort
import sys
def get_book_text(file_path):
    with open(file_path) as f:
        file_text = f.read()
        return file_text

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)
    character_count = get_character_count(text)
    character_sort = dict_sort(character_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_word_count(text)} total words")
    print("--------- Character Count -------")
    for dict in character_sort:
        character = dict["character"]
        count = dict["count"]
        if character.isalpha():
            print(f"{character}: {count}")
    print("============= END ===============")

main()