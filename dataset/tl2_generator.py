import random

NUMBER_OF_SAMPLES_1 = 50
NUMBER_OF_SAMPLES_2 = 750
NUMBER_OF_SAMPLES_3 = 200
NUMBER_OF_SAMPLES_4 = 500
MAX_STR_LENGTH_1 = 3
MAX_STR_LENGTH_2 = 10
MAX_STR_LENGTH_3 = 10
MAX_STR_LENGTH_4 = 10

# generate random strings containing characters 'a', 'b', & 'c'
def generate_random_string(length):
  s = ''                                   # varaible to hold the string
  for x in range(length):                  # until the length of the string
      s += chr(97 + random.randint(0, 2))  # pick a/b/c and add to the string
  return s


# generate strings of characters 'a', 'b' & 'c' with no same neighboring characters
def generate_valid_string(length):
  s = ''                                 # varaible to hold the string
  x = random.random()                    # pick a random number between 0 and 1
  DICT = ['a', 'b', 'c']                 # dictionary of three characters to choose from
  last = ''                              # variable for last character                             
  if (x > 0.66):                         
    s += 'c'                             # if random number is more thatn 0.66 add c to string s
    last = 'c'                           # make last chosen character as c
  else:
    if (x > 0.33):                       # else if random number if between 0.34 to 0.66
      s += 'b'                           # add b to string s make it the last chosen character
      last = 'b'
    else:
      s += 'a'                           # else make a the last chosen character and add it to the string s
      last = 'a'
  while(len(s) != length):               # until the length of string is reached
    local_dict = ['a', 'b', 'c']         # form a local dict
    local_dict.remove(last)              # remove the last chosen character from the local dict
    x = random.random()                  # pick a random int again between 0 to 1
    if (x > 0.5):                        # if ranodm int greater than 0.5 
      s += local_dict[1]                 # add second element of local dict to the string s
      last = local_dict[1]               # make it the last chosen character
    else:
      s += local_dict[0]                 # else add the first element of local dict to the string s
      last = local_dict[0]               # make it the last chose character
  return s


# generate strings which looks like it belongs to the language but doesn't upon closer inspection
def generate_quasi_string(length):
  s = generate_valid_string(length - 1)
  j = random.randint(0, length - 2)
  return s[:j] + s[j] + s[j:]


# function that checks whether the generated strings are valid or not
def is_valid(string):
  result = True
  for x in range(len(string) - 1):
    if(string[x] == string[x + 1]):
      result = False
      break
  return result

f = open('tl2_dataset.txt', 'w')

# generate random strings
for x in range(NUMBER_OF_SAMPLES_1):
    l = random.randint(1, MAX_STR_LENGTH_1)
    s = generate_random_string(l);
    targetValue = int(is_valid(s))
    f.write(s + ' ' + str(targetValue) + '\n')


# generate valid strings 
for x in range(NUMBER_OF_SAMPLES_2):
    l = random.randint(MAX_STR_LENGTH_1 + 1, MAX_STR_LENGTH_2)
    s = generate_valid_string(l)
    targetValue = int(is_valid(s))
    f.write(s + ' ' + str(targetValue) + '\n')


# generate random strings
for x in range(NUMBER_OF_SAMPLES_3):
    l = random.randint(MAX_STR_LENGTH_1 + 1, MAX_STR_LENGTH_3)
    s = generate_random_string(l)
    targetValue = int(is_valid(s))
    f.write(s + ' ' + str(targetValue) + '\n')


# generate quasi strings
for x in range(NUMBER_OF_SAMPLES_4):
    l = random.randint(MAX_STR_LENGTH_1 + 1, MAX_STR_LENGTH_4)
    s = generate_quasi_string(l)
    targetValue = int(is_valid(s))
    f.write(s + ' ' + str(targetValue) + '\n')