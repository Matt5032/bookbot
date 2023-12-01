
books = r'C:\workspace\github.com\Matt5032\bookbot\frankenstein.txt'

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
    letter_list = count_letters(file_contents)
    sorted_list = sorted(letter_list.items(), key=lambda x: x[1], reverse=True)
    for letter, count in sorted_list:
        if letter.isalpha():
            print(f"The '{letter}' character was found {count} times")
    
print_report(file_contents)