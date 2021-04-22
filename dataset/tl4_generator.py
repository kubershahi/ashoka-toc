# program to generate test language 4 i.e words only having characters 'a', 'b', and 'c', 
# and which has substring 'bac'

import random

NUMBER_OF_SAMPLES_1 = 150
NUMBER_OF_SAMPLES_2 = 300
NUMBER_OF_SAMPLES_3 = 550
MAX_STR_LENGTH_1 = 5
MAX_STR_LENGTH_2 = 12
MAX_STR_LENGTH_3 = 12

# generate random strings containing characters 'a', 'b', and 'c'
def generate_random_string(length):
  s = ''
  for x in range(length):
    s += chr(97 + random.randint(0, 2))
  return s

# generate string which has 'bac' as its substring
def generate_valid_string(length):
  s = generate_random_string(length - 3)
  j = random.randint(0, length - 4)
  return s[:j] + 'bac' + s[j:]


# function to check whether a string is valid or not
def is_valid(string):
  result = False
  for x in range(len(string) - 2):
    if(string[x] == 'b' and string[x + 1] == 'a' and string[x + 2] == 'c'):
      result = True
      break
  return result

f = open('tl4_dataset.txt', 'w')

# generate random strings os length 1 to 5
for x in range(NUMBER_OF_SAMPLES_1):
  l = random.randint(1, MAX_STR_LENGTH_1)
  s = generate_random_string(l);
  targetValue = int(is_valid(s))
  f.write(s + ' ' + str(targetValue) + '\n')


# generate valid strings of length 4 to 12
for x in range(NUMBER_OF_SAMPLES_2):
  l = random.randint(4, MAX_STR_LENGTH_2)
  s = generate_valid_string(l)
  targetValue = int(is_valid(s))
  f.write(s + ' ' + str(targetValue) + '\n')

# generate random strings og length 6 to 12
for x in range(NUMBER_OF_SAMPLES_3):
  l = random.randint(MAX_STR_LENGTH_1 + 1, MAX_STR_LENGTH_3)
  s = generate_random_string(l)
  targetValue = int(is_valid(s))
  f.write(s + ' ' + str(targetValue) + '\n')