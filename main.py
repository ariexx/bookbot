def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = splitWords(text)
    countChars = countChar(text)
    wordTuple = list(countChars.items())
    print(f"--- Bein report of books/frankenstein.txt ---\n")
    #print(f"{countChars} words found in the document\n\n")
    words = sorted(countChars.items(), key=lambda x: x[1], reverse=True)
    for word, count in words:
        print(f"The word '{word}' was found {count} times")

    print("--- End report ---")

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def splitWords(file_contents):
    words = len(file_contents.split())
    return words

def countChar(words):
    chars = {}
    lowered = words.lower()
    for char in lowered:
        if char.isalpha():
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
    return chars

def sort_on(dict):
    return dict["num"]

main()
