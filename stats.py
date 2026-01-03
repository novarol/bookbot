def count_words_in_book(book_text):
  return len(book_text.split())

def count_characters_in_book(book_text):
  character_count = {}
  for char in book_text.lower():
    if char not in character_count:
      character_count[char] = 0
    character_count[char] += 1

  return character_count

def sort_on_num(dict):
  return dict['num']

def get_sorted_character_count_list(character_count_dict):
  character_count_list = []

  for char in character_count_dict:
    character_count_list.append({ 'char': char, 'num': character_count_dict[char] })

  character_count_list.sort(reverse=True, key=sort_on_num)

  return character_count_list
