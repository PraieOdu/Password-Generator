#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

num_of_letter = len(letters)
num_of_numbers = len(numbers)
num_of_symbols = len(symbols)
list1 = []
list2 = []
list3 = []

for a in range (0,nr_letters + 1):
  ran_lett = random.randint(0,num_of_letter - 1) 
  x = letters[ran_lett]                          
  list1.append(x)

for b in range (0,nr_numbers + 1):
  ran_num = random.randint(0,num_of_numbers - 1)
  y = numbers[ran_num]
  list2.append(y)

for c in range (0,nr_symbols + 1):
  ran_sym = random.randint(0,num_of_symbols - 1)
  z = symbols[ran_sym]
  list3.append(z)

list1.extend(list2)
list1.extend(list3)

p = ""
p = str(p)
for d in list1:
  p = p + d 

print (f"Here is your password: {p}")

