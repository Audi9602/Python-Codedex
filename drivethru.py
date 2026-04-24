
def get_item(i):
  if i == 1:
    print("🍔 Cheeseburger")
  elif i == 2:
    print("🍟 Fries")
  elif i == 3:
    print("🥤 Soda")
  elif i == 4:
    print("🍦 Ice Cream")
  elif i == 5:
    print("🍪 Cookie")
  else:
    print("Invalid!")

def welcome():
  print("Hey there! This is Addie's Diner 🤗")
  print("\nHere's the menu: ")
  print("\n1. Cheeseburger\n2. Fries\n3. Soda\n4. Ice Cream\n5. Cookie")

welcome()

choice = int(input("\nWhat will you order? "))

get_item(choice)
