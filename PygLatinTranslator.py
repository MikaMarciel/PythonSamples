# Word to be added
pyg = 'ay'

# User to input word 
original = raw_input('Enter a word:')

# Check if there is input and, it is all letters
if len(original) > 0 and original.isalpha():
  # Lower case
  word = original.lower()
  # Get first letter
  first = word[0]
  # Concatenate (get 2nd letter until the last + first letter + "ay"
  new_word = word[1:len(word)] + first + pyg
  # Print result
  print new_word
else:
  # Print if invalid input
  print 'empty'