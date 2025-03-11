
import sys
from stats import get_num_words
from stats import get_book_text
from stats import make_dictionary

#location = "books/frankenstein.txt"
location = sys.argv[1]
book_text = get_book_text(location)
print(get_num_words(book_text))
#print(make_dictionary(book_text))
dictionary = make_dictionary(book_text)

print("============ BOOKBOT ============")
print(f"Analyzing book found at {location}...")
print("----------- Word Count ----------")
print(f"Found {get_num_words(book_text)} total words")
print("--------- Character Count -------")

for index, value in dictionary.items():
    print(f"{index}: {value}")

print("============= END ===============")