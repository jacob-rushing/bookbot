def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return (file_contents)
    
text = get_book_text("books/frankenstein.txt")
words = text.split()
character_count = {}

def get_num_words():
   num_words = len(words)
   print (f"Found {num_words} total words")
get_num_words()

def unique_character():
    #needed help on this function, what I did wrong was I tried to do each step individually instead of nesting my functions together to make them work together. 
    # I tried to store everything as an indididual variable to then add into the dictionary at the end, instead of iterating over the word, and then over the character, and adding
    # to the dict when necessary.
    for word in words:
        for char in word.lower():
            if char in character_count:
                character_count[char] += 1
            else:
                character_count[char] = 1
    #print (character_count)
unique_character()

sorted_list = []

def status_report():
    for char, count in character_count.items():
        sorted_character_count = {}
        if char not in sorted_list:
            sorted_character_count["char"] = char
            sorted_character_count["num"] = count
            sorted_list.append(sorted_character_count)
    def sort_on(sorted_character_count):
        return sorted_character_count["num"]
    sorted_list.sort(reverse=True, key = sort_on)
    print(sorted_list)

status_report()

