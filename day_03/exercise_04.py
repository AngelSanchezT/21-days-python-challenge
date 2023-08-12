def print_triangle(size, character):
  BLANK = ' '
  ENTER = '\n'
  triangle = ''
  i = 1
  space = 1
  while i <= size:
    triangle += ((size - i) * BLANK) + (space * character)
    if i < size:
      triangle += ENTER
    i += 1
    space += 2
  return triangle


print(print_triangle(3, "*"))
print(print_triangle(6, '$'))


