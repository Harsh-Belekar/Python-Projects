import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
            'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 
            'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 
            'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password_list=[]
password=""

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("\nHow many letters would you like in your password ? :")) 
nr_symbols = int(input("\nHow many symbols would you like ? : "))
nr_numbers = int(input("\nHow many numbers would you like ? : "))

def generate(num,data):
    for i in range(num):
        password_list.append(random.choice(data))

generate(nr_letters,letters)
generate(nr_numbers,numbers)
generate(nr_symbols,symbols)

random.shuffle(password_list)
for i in password_list:
    password += i

print(f"\nYour Password is : {password}")