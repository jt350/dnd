#! python3

import random

while True:
  droller = input ('\nType d100, d20, d12,\
  d10, d8, d6 or d4 to roll the dice: ')

  if droller == 'd100':
    print('\n\t100 sided die: ', random.randint(1,100))
  elif droller == 'd20':
    print('\n\t20 sided die: ', random.randint(1,20))
  elif droller == 'd12':
    print('\n\t12 sided die: ', random.randint(1,12))
  elif droller == 'd10':
   print('\n\t10 sided die: ', random.randint(1,10))
  elif droller == 'd8':
    print('\n\t8 sided die: ', random.randint(1,8))
  elif droller == 'd6':
    print('\n\t6 sided die: ', random.randint(1,6))
  elif droller == 'd4':
   print('\n\t4 sided die: ', random.randint(1,4))
  else:
    print('\n\tInvalid entry.')