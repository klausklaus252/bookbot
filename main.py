from stats import get_num_words
from stats import get_num_characters
from stats import sort_char
import sys


def sort_on(items):
    return items["num"]
    
    
def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:

        path_to_book = sys.argv[1]


        #chars = {}
        count = get_num_words(path_to_book)
    
        chars = get_num_characters(path_to_book)
        sorted_chars = sort_char(chars)
        sorted_chars.sort(reverse=True, key=sort_on)
        
        #print (chars)

        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        print("Found " + str(count) + " total words")
        print("--------- Character Count -------")
        for i in sorted_chars:
            print (i["char"] + ": " + str(i["num"]))

main()