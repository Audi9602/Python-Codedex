# WITH IF ELSE
import random
def fortune():
  num = random.randint(0,8)
  if num == 1:
    print("Don't pursue happiness – create it.")
  elif num == 2:
    print("All things are difficult before they are easy.")
  elif num == 3:
    print("The early bird gets the worm, but the second mouse gets the cheese.")
  elif num == 4:
    print("Someone in your life needs a letter from you.")
  elif num == 5:
    print("Don't just think. Act!")
  elif num == 6:
    print("Your heart will skip a beat.")
  elif num == 7:
    print("The fortune you search for is in another cookie.")
  elif num == 8:
    print("Help! I'm being held prisoner in a Chinese bakery!")
fortune()
fortune()
fortune()
'''
for i in range(3):
  fortune()
'''
# WITHOUT IF-ELSE
import random
def fortune():
  fortunes = ['Do not pursue happiness – create it.','All things are difficult before they are easy.',
  'The early bird gets the worm, but the second mouse gets the cheese.'
  ,'Someone in your life needs a letter from you.', 'Do not just think. Act!','Your heart will skip a beat.','The fortune you search for is in another cookie.',
'Help! I am being held prisoner in a Chinese bakery!'
  ]
  #print(fortunes)
  print(fortunes[random.randint(0,7)])
  
fortune()
