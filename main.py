import sys
from stats import *

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    def main():
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {file_path}...")
        print("----------- Word Count ----------")
        print(f"Found {word_amount} total words")
        print("--------- Character Count -------")
        for i in sorted_list:
            print(f"{i['char']}: {i['num']}")
                
    main() 