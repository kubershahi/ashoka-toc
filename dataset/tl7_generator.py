# program to generate test language 7 i.e words only having characters 'a', 'b', and 'c'
# and having 'abacaba' 

import random

NUMBER_OF_SAMPLES_1 = 150
NUMBER_OF_SAMPLES_2 = 700
NUMBER_OF_SAMPLES_3 = 550
MAX_STR_LENGTH_1 = 10
MAX_STR_LENGTH_2 = 20
MAX_STR_LENGTH_3 = 20

# generate random strings only containing characters 'a', 'b', 'c'
def generate_random_string(length):
  s = ''
  for x in range(length):
    s += chr(97 + random.randint(0, 2))
  return s

# generate valid strings 
def generate_valid_strings(length):
  s = generate_random_string(length - 7)
  j = random.randint(0, length - 8)
  return s[:j] + 'abacaba' + s[j:]


# function to check whether the generated strings are valid or not
def is_valid(string):
  result = False
  for x in range(len(string) - 6):
    if(string[x] == 'a' and string[x + 1] == 'b' and string[x + 2] == 'a' and string[x + 3] == 'c' and string[x + 4] == 'a' and string[x + 5] == 'b' and string[x + 6] == 'a'):
      result = True
      break
  return result


f = open('tl7_dataset.txt', 'w')

# generate 150 random strings of length 1 to 10
for x in range(NUMBER_OF_SAMPLES_1):
  l = random.randint(1, MAX_STR_LENGTH_1)
  s = generate_random_string(l);
  targetValue = int(is_valid(s))
  f.write(s + ' ' + str(targetValue) + '\n')

# generate 700 valid strings of length 8 to 20
for x in range(NUMBER_OF_SAMPLES_2):
  l = random.randint(8, MAX_STR_LENGTH_2)
  s = generate_valid_strings(l)
  targetValue = int(is_valid(s))
  f.write(s + ' ' + str(targetValue) + '\n')

# generate 500 random strings of length 11 to 20
for x in range(NUMBER_OF_SAMPLES_3):
  l = random.randint(MAX_STR_LENGTH_1 + 1, MAX_STR_LENGTH_3)
  s = generate_random_string(l)
  targetValue = int(is_valid(s))
  f.write(s + ' ' + str(targetValue) + '\n')
