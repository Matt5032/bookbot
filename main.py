
books = "frankenstein.txt"

with open(books) as f:
    file_contents = f.read()


def count_words(file_contents):
    i = 0
    for word in file_contents.split():
        i += 1
    
    return i
    
def count_letters(file_contents):
    word_list = file_contents.lower().split()
    letter_list = {}
    for word in word_list:
        for letter in word:
            if letter in letter_list:
                letter_list[letter] += 1
            else:
                letter_list[letter] = 1
    return letter_list
    
def print_report(file_contents):
    word_count = count_words(file_contents)
    
    print(f"--- Begin report of {books} ---")
    print(f"{word_count} words found in the document")
    
    
print_report(file_contents)