# program to generate test language 5 i.e words only having characters of 
# 'a', 'b', and 'c', and given by DFA M

import random

NUMBER_OF_SAMPLES_1 = 100
NUMBER_OF_SAMPLES_2 = 900
MAX_STR_LENGTH_1 = 5
MAX_STR_LENGTH_2 = 12
MAX_STR_LENGTH_3 = 12

# generate random strings containing characters 'a', 'b', and 'c'
def generate_random_string(length):
  s = ''
  for x in range(length):
    s += chr(97 + random.randint(0, 2))
  return s

DFA = { 0:{'a':1, 'b':2, 'c':2},
        1:{'a':3, 'b':2, 'c':0},
        2:{'a':3, 'b':2, 'c':1},
        3:{'a':0, 'b':3, 'c':3},}

def run_DFA(string):
  curr_state = 0
  for char in s:
    curr_state = DFA[curr_state][char]

  return (curr_state == 1 or curr_state == 2)

# def DFA(pos, char):
#   if (pos == 0):
#     if(char == 'a'):
#       return 1
#     if(char == 'b'):
#         return 2
#     if(char == 'c'):
#         return 2
#   if (pos == 1):
#     if(char == 'a'):
#         return 3
#     if(char == 'b'):
#         return 2
#     if(char == 'c'):
#         return 0
#   if (pos == 2):
#     if(char == 'a'):
#         return 3
#     if(char == 'b'):
#         return 2
#     if(char == 'c'):
#         return 1
#   if (pos == 3):
#     if(char == 'a'):
#         return 0
#     if(char == 'b'):
#         return 3
#     if(char == 'c'):
#         return 3

# function to check whether the string is valid
def is_valid(string):
  # curr_pos = 0
  # for i in range(len(string)):
  curr_state = run_DFA(string)
  return (curr_state == 1 or curr_state == 2)


f = open('tl5_dataset.txt', 'w')

needed_result = True

# generating 100 strings of length 1 to 5 
for x in range(NUMBER_OF_SAMPLES_1):
  l = random.randint(1, MAX_STR_LENGTH_1)
  s = generate_random_string(l)
  while (is_valid(s) != needed_result):
    l = random.randint(1, MAX_STR_LENGTH_1)
    s = generate_random_string(l)
  targetValue = int(is_valid(s))
  f.write(s + ' ' + str(targetValue) + '\n')
  needed_result = not needed_result

# generating 900 strings of length 6 to 12 
for x in range(NUMBER_OF_SAMPLES_2):
  l = random.randint(MAX_STR_LENGTH_1 + 1, MAX_STR_LENGTH_2)
  s = generate_random_string(l)
  while (is_valid(s) != needed_result):
    l = random.randint(MAX_STR_LENGTH_1 + 1, MAX_STR_LENGTH_2)
    s = generate_random_string(l)
  targetValue = int(is_valid(s))
  f.write(s + ' ' + str(targetValue) + '\n')
  needed_result = not needed_result