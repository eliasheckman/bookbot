
def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents
        #return len(file_contents.split())

def get_num_words(book_text):
    
    #book_text = get_book_text("books/frankenstein.txt")
    # print(output)
    word_count = len(book_text.split())
    #word_count = 42 #testing number
    return f"{word_count} words found in the document"

def make_dictionary(book_text):
    #dictionary = {
    #    "a": 0, "b": 0, "c": 0, "d": 0,
    #    "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0,
    #    "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0,  "w": 0, "x": 0, "y": 0, "z": 0
    #}
    dictionary = {
        #'a': 0, 'b': 0, 'c': 0, 'd': 0,
        #'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0,
        #'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0, 
        #'æ': 0, 'ë': 0, 'â': 0, 'ê': 0, 'ô': 0
        #" ": 0, ";": 0, ",": 0, ".": 0, "\n": 0, "-": 0, ":": 0,
        #"0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0
    }
    #print(book_text)
    
    character_list = list(book_text.lower())
    #print(character_list)
    
    for character in character_list:
        #print(character)
        if character.isalpha():
            if character in dictionary:
                dictionary[character] += 1
            else:
                dictionary[character] = 1
    
    return dictionary
    

