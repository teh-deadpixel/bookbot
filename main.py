from stats import word_count
from stats import char_dict
from stats import to_sorted_list
import sys
def get_book_text(path):
    with open(path) as f:
        file_content = f.read()
    return file_content

def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1) 
    
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = word_count(text)
    chars_dict = char_dict(text)
    chars_sorted_list = to_sorted_list(chars_dict)
    print_report(book_path, num_words, chars_sorted_list)
    # print(f"Found {num_words} total words")
    # print(char_dict(text))

def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

main()