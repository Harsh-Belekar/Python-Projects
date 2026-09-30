import caesar_art as art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
            'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 
            'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p','q', 'r', 's', 't', 'u', 'v', 
            'w', 'x','y', 'z']

def caesar(select,start_text,shift_no):
        end_text=""
        if select=="Decode":
            shift_no *= -1

        for char in start_text:
            if char in alphabet:
                position=alphabet.index(char)
                new_position=position+shift_no
                new_letter=alphabet[new_position]
                end_text+=new_letter
            else:
                end_text+=char

        print(f"\nThe {select}d message is: {end_text}")

def start():
    select=input("\nWhat you want to do ? [Encode or Decode ] : ").capitalize()
    
    if select =="Encode" or select=="Decode":
        start_text=input("Type Your Message: ").lower()
        shift_no=int(input("Enter the shift Number: "))
        shift_no=shift_no%26
        caesar(select,start_text,shift_no)
    else:
        print("\nPlease Enter Valid Text!")
        start()
        
print(art.logo)
start()
over=False
while not over:
    choice=input("\nDid you want to Continue ? [Yes or No]: ").lower()
    if choice=="yes":
        start()
    else:
        over=True
