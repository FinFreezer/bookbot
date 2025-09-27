from stats import count_words
from stats import count_letter_usage

def get_book_text(path_to_file):
    #print("Enter file path:")
    #path_to_file = input()
    #print("\n")

    full_string = None

    with open(path_to_file) as f:
        lines = f.read()
        "".join(lines)

    #print(lines)
    return lines

def main():
    count_letter_usage( get_book_text("books/frankenstein.txt") )
    w = count_words( 
        get_book_text("books/frankenstein.txt") ) 
    print(f"Found {w} total words")

main()