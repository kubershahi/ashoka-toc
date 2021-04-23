# program to generate test language 8 i.e words only having characters 'a', 'b', 'c', 'd', 'e' 
# and are sorted in the lexicographical order.

import random

NUMBER_OF_SAMPLES_1 = 650
NUMBER_OF_SAMPLES_2 = 350
MAX_STR_LENGTH_1 = 10
MAX_STR_LENGTH_2 = 10

# generate random strings, only containing characters 'a', 'b', 'c', 'd', 'e'
def generate_random_string(length):
  s = ''
  for x in range(length):
    s += chr(97 + random.randint(0, 4))
  return s

# generate valid strings 
def generate_valid_strings(length):
  s = generate_random_string(length)
  return ''.join(sorted(s))

# get state numbers for each character in w 
def w(char):
	if(char == 'a'):
		return 1
	if(char == 'b'):
		return 2
	if(char == 'c'):
		return 3
	if(char == 'd'):
		return 4
	if(char == 'e'):
		return 5

# check whether the generated string is valid or not
def is_valid(string):
  result = True
  for x in range(len(string) - 1):
    if(w(string[x]) > w(string[x + 1])):
      result = False
      break
  return result

f = open('tl8_dataset.txt', 'w')

# generate 650 random strings of length between 1 to 10
for x in range(NUMBER_OF_SAMPLES_1):
  l = random.randint(1, MAX_STR_LENGTH_1)
  s = generate_random_string(l);
  targetValue = int(is_valid(s))
  f.write(s + ' ' + str(targetValue) + '\n')

# generate 350 valid strings of length between 1 to 10
for x in range(NUMBER_OF_SAMPLES_2):
  l = random.randint(1, MAX_STR_LENGTH_2)
  s = generate_valid_strings(l)
  targetValue = int(is_valid(s))
  f.write(s + ' ' + str(targetValue) + '\n')