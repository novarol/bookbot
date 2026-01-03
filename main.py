def get_book_text(filepath):
  with open(filepath) as f:
    return f.read()

from stats import count_words_in_book, count_characters_in_book

def main():
  book_text = get_book_text('books/frankenstein.txt')
  word_count = count_words_in_book(book_text)
  character_count = count_characters_in_book(book_text)
  
  print(f'Found {word_count} total words')
  print(character_count)

main()
