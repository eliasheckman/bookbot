

from stats import get_num_words
from stats import get_book_text
from stats import make_dictionary

book_text = get_book_text("books/frankenstein.txt")
print(get_num_words(book_text))
print(make_dictionary(book_text))