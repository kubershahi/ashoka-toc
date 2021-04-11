# program to generate test language 1 i.e words having no same neighboring characters of alphabet 
# 'a' and 'b'

import random

NUMBER_OF_SAMPLES_1 = 50
NUMBER_OF_SAMPLES_2 = 475
NUMBER_OF_SAMPLES_3 = 475
NUMBER_OF_SAMPLES_4 = 500

MAX_STR_LENGTH_1 = 3
MAX_STR_LENGTH_2 = 10
MAX_STR_LENGTH_3 = 10
MAX_STR_LENGTH_4 = 10

# generate random strings only containing characters 'a' and 'b' of specified length
def generate_random_string(length):
  s = ''                                  # varaible to hold the string
  for x in range(length):                 # until the length of the string
    s += chr(97 + random.randint(0, 1))   # pick a/b and add to the string
  return s


# generate strings of characters 'a' and 'b' with no same neighboring characters
def generate_valid_string(length):
  s = ''                          # variable to hold desired string
  x = random.random()             # get a floating number between 0 and 1
  ch1 = 'a'
  ch2 = 'b'
  if(x > 0.5):
    ch1, ch2 = ch2, ch1           # swap the characters if random number is > 0.5
  cnt = 0                         # counter to track length
  while (cnt != length):          # until you get the required length
    if(cnt % 2 == 0):            
      s += ch1                    # append ch1 at even places
    else:
      s += ch2                    # append ch2 at odd places
    cnt += 1
  return s


# generate strings which looks like it belongs to the language but doesn't upon closer inspection
def generate_quasi_string(length):
  s = generate_valid_string(length - 1)   # generate valid string of (length - 1) length
  j = random.randint(0, length - 2)        # get a random integer between [0, length -2]
  return s[:j] + s[j] + s[j:]              # join the string around j such that it is not valid


# function to check whether the string is valid or not
def is_valid(string):
  result = True                            # initially assumed true
  for x in range(len(string) - 1):         # for characters till the second last character
    if(string[x] == string[x + 1]):        # if the current character and the next character is same, 
      result = False                       # render the string invalid
      break
  return result


f = open('tl1_dataset.txt', 'w')          # opening a file to save the generated strings

# generating random strings
for x in range(NUMBER_OF_SAMPLES_1):      # for specified number of samples
  l = random.randint(1, MAX_STR_LENGTH_1) # choose a random int between the given range as length of the string to be generated
  s = generate_random_string(l)           # generate random string of length l
  targetValue = int(is_valid(s))          # check whether the string is valid or not
  f.write(s + ' ' + str(targetValue) + '\n') # write the generated string in the file with its acceptance value


# generating valid strings
for x in range(NUMBER_OF_SAMPLES_2):      
    l = random.randint(MAX_STR_LENGTH_1 + 1, MAX_STR_LENGTH_2) # choose a random int between the given range as length of the string to be generated
    s = generate_valid_string(l)           # generate random string of length l
    targetValue = int(is_valid(s))          # check whether the string is valid or not
    f.write(s + ' ' + str(targetValue) + '\n') # write the generated string and its acceptance value


# generate random strings
for x in range(NUMBER_OF_SAMPLES_3):
    l = random.randint(MAX_STR_LENGTH_1 + 1, MAX_STR_LENGTH_3)
    s = generate_random_string(l)
    targetValue = int(is_valid(s))
    f.write(s + ' ' + str(targetValue) + '\n')

# generate quasi strings i.e strings which look like they belong to the language but they don't
for x in range(NUMBER_OF_SAMPLES_4):
    l = random.randint(MAX_STR_LENGTH_1 + 1, MAX_STR_LENGTH_4)
    s = generate_quasi_string(l)
    targetValue = int(is_valid(s))
    f.write(s + ' ' + str(targetValue) + '\n')