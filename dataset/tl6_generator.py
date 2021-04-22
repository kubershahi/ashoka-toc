# program to generate test language 6 i.e words only having characters 'a', 'b', 
# and of length either 2 or 7

import random

NUMBER_OF_SAMPLES_1 = 500
NUMBER_OF_SAMPLES_2 = 500
NUMBER_OF_SAMPLES_3 = 200
MAX_STR_LENGTH_1 = 8
MAX_STR_LENGTH_2 = 29
MAX_STR_LENGTH_3 = 29

# generate random strings only containing characters 'a', 'b'
def generate_random_string(length):
  s = ''
  for x in range(length):
    s += chr(97 + random.randint(0, 1))
  return s

# function to check whether the string is valid or not
def is_valid(string):
  return (len(string) % 2 == 0 or len(string) % 7 == 0)

f = open('tl6_dataset.txt', 'w')

# generate 500 random strings of length 1 to 8
for x in range(NUMBER_OF_SAMPLES_1):
  l = random.randint(1, MAX_STR_LENGTH_1)
  s = generate_random_string(l)
  targetValue = int(is_valid(s))
  f.write(s + ' ' + str(targetValue) + '\n')

# generate 500 random strings of length 1 to 29
for x in range(NUMBER_OF_SAMPLES_2):
  l = random.randint(1, MAX_STR_LENGTH_2)
  s = generate_random_string(l)
  targetValue = int(is_valid(s))
  f.write(s + ' ' + str(targetValue) + '\n')

# generate 200 valid string of length 1 to 29
for x in range(NUMBER_OF_SAMPLES_3):
  l = random.randint(1, MAX_STR_LENGTH_3)
  s = generate_random_string(l)
  while(is_valid(s)):
    l = random.randint(1, MAX_STR_LENGTH_3)
    s = generate_random_string(l)
  targetValue = int(is_valid(s))
  f.write(s + ' ' + str(targetValue) + '\n')