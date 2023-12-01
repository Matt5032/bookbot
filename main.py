
books = "frankenstein.txt"

with open(books) as f:
    file_contents = f.read()


def count_words(file_contents):
    i = 0
    for word in file_contents.split():
        i += 1
    
    print(i)
    
def count_letters(file_contents):
    word_list = file_contents.lower().split()
    letter_list = {}
    for word in word_list:
        for letter in word:
            if letter in letter_list:
                letter_list[letter] += 1
            else:
                letter_list[letter] = 1
    print(letter_list)
    
count_words(file_contents)
count_letters(file_contents)