import sys
from stats import count_words_in_book, count_characters_in_book, get_sorted_character_count_list

def get_book_text(filepath):
  with open(filepath) as f:
    return f.read()

def main():
  if len(sys.argv) != 2:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)

  path_to_book = sys.argv[1]
  book_text = get_book_text(path_to_book)
  word_count = count_words_in_book(book_text)
  character_count = count_characters_in_book(book_text)
  sorted_character_count = get_sorted_character_count_list(character_count)

  print('============ BOOKBOT ============')
  print(f'Analyzing book found at {path_to_book}...')
  
  print('----------- Word Count ----------')
  print(f'Found {word_count} total words')

  print('--------- Character Count -------')
  for item in sorted_character_count:
    char = item['char']
    if not char.isalpha():
      continue

    print(f'{char}: {item['num']}')

  print('============= END ===============')

main()
