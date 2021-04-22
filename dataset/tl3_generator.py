# program to generate test language 3 i.e words having only characters  'a', 'b', and 'c', and length
# multiple of 3.

import random

NUMBER_OF_SAMPLES_1 = 500
NUMBER_OF_SAMPLES_2 = 500
MAX_STR_LENGTH_1 = 5
MAX_STR_LENGTH_2 = 15

# generate random strings containing characters 'a', 'b', and 'c'
def generate_random_string(length):
  s = ''
  for x in range(length):
    s += chr(97 + random.randint(0, 2))
  return s


# function to check whether the generated string is valid or not i.e length multiple of 3 or not
def is_valid(string):
  return (len(string) % 3 == 0)


f = open('tl3_dataset.txt', 'w')


# generate random strings of length 1 to 5
for x in range(NUMBER_OF_SAMPLES_1):
  l = random.randint(1, MAX_STR_LENGTH_1)
  s = generate_random_string(l)
  targetValue = int(is_valid(s))
  f.write(s + ' ' + str(targetValue) + '\n')

# generate random strings of length 6 to 15
for x in range(NUMBER_OF_SAMPLES_2):
  l = random.randint(MAX_STR_LENGTH_1 + 1, MAX_STR_LENGTH_2)
  s = generate_random_string(l)
  targetValue = int(is_valid(s))
  f.write(s + ' ' + str(targetValue) + '\n')