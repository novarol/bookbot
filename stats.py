def count_words_in_book(book_text):
  return len(book_text.split())

def count_characters_in_book(book_text):
  character_count = {}
  for char in book_text.lower():
    if char not in character_count:
      character_count[char] = 0
    character_count[char] += 1

  return character_count
