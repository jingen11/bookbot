def countChar(s):
  sl = s.lower()
  chars = {}
  for c in sl:
    if c.isalpha():
      if(c not in chars):
        chars[c] = 1
      else:
        chars[c] = chars[c] + 1
  return chars

def sort_on(dict):
  return dict['count']

def main():
  with open('books/frankenstein.txt') as f:
    file_content = f.read()
    # print(file_content)
    # print(len(file_content.split()))
    print('--- Begin report of books/frankenstein.txt ---')
    print(f'{len(file_content.split())} words found in the document\n')
    chars = countChar(file_content)
    arr = []
    print(chars)
    for c in chars:
      arr.append({'char': c, 'count': chars[c]})
    arr.sort(reverse=True, key=sort_on)
    for r in arr:
      print(f'The \'{r['char']}\' character was found {r['count']} times')
    print('--- End report ---')

main()