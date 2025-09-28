from stats import count_words
from stats import count_letter_usage
from stats import sort_by_count

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
    usage_data = { }
    sorted_data = [ ]
    location = "books/frankenstein.txt"
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {location}...")
    
    w = count_words( 
    get_book_text(location) ) 
   
    print("----------- Word Count ----------")
    print(f"Found {w} total words")
    print("--------- Character Count -------")
    usage_data = count_letter_usage( get_book_text(location) )
    sorted_data = sort_by_count(usage_data)
    
    for letter, num in sorted_data:
        print(f"{letter["name"]}: {num["num"]}")
    
    print("============= END ===============")



main()