from stats import get_num_words
from stats import get_book_text

def main():
	book_text = get_book_text("bookbot/books/frankenstein.txt")
	list_of_words = str.split(book_text)
	num_words = get_num_words(list_of_words)
	print(f"Found {num_words} total words")

main()

