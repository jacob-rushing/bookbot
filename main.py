from stats import *
def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print (f"Found {word_amount} total words")
    print("--------- Character Count -------")
    for i in sorted_list:
        print(f"{i['char']}: {i['num']}")
        
main()  