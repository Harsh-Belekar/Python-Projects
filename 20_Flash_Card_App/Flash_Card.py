#Import modules
import tkinter as tk
import pandas
import random
from tkinter import messagebox

#Constants
background_color="#B1DDC6"

#Setup screen
root=tk.Tk()
root.title("Flash Card")
root.config(padx=50,pady=50,bg=background_color)

try:
    data=pandas.read_csv("./Assets/word_to_learn.csv")

except:
    try:
        original_data=pandas.read_csv("./Assets/data.csv")

    except:
        messagebox.showinfo(title="File not Found",message="Data Does not Exit")

    else:
        data_dic=original_data.to_dict(orient="records") 
        new_data=pandas.DataFrame(data_dic) 
        new_data.to_csv("./Assets/word_to_learn.csv") 

else:
    data_dic=data.to_dict(orient="records")

current_card={}

#To restart the App
def restart():
    next_card() 
    global data,data_dic

    try:
        data=pandas.read_csv("./Assets/data.csv")

    except:
        messagebox.showinfo(title="File not Found",message="Data Does not Exit")

    else:
        data_dic=data.to_dict(orient="records")
        
        new_data=pandas.DataFrame(data_dic)
        new_data.to_csv("./Assets/word_to_learn.csv") 

def next_card():
    global current_card,flip_timer
    root.after_cancel(flip_timer) 
    current_card=random.choice(data_dic)
    canva.itemconfig(card_title,text="French",fill="black") 
    canva.itemconfig(card_word,text=current_card["French"],fill="black")
    canva.itemconfig(card_background,image=card_font)
    flip_timer=root.after(3000,func=flip_card)

def is_known():
    global data_dic
    data_dic.remove(current_card)
    new_data=pandas.DataFrame(data_dic)
    new_data.to_csv("./Assets/word_to_learn.csv",index=False)
    next_card()

def flip_card():
    canva.itemconfig(card_background,image=card_back)
    canva.itemconfig(card_title,text="English",fill="white")
    canva.itemconfig(card_word,text=current_card["English"],fill="white")

#Flip card after 3 seconds
flip_timer=root.after(3000,func=flip_card)

#Setup image on screen
canva=tk.Canvas(width=608,height=400)
card_font=tk.PhotoImage(file="./Assets/card_front.png")
card_back=tk.PhotoImage(file="./Assets/card_back.png")
card_background=canva.create_image(304,200,image=card_font)
canva.config(bg=background_color,highlightthickness=0)

#Display text on image
card_title=canva.create_text(304,100,text="title",font=("Arial",40,"italic"))
card_word=canva.create_text(304,200,text="word",font=("Arial",40,"bold"))
canva.grid(row=0,column=0,columnspan=2)

#Display Wrong mark button on Screen
wrong_image=tk.PhotoImage(file="./Assets/wrong.png")
wrong_button=tk.Button(image=wrong_image,command=next_card,highlightthickness=0)
wrong_button.grid(row=1,column=0)

#Display Right mark button on Screen
right_image=tk.PhotoImage(file="./Assets/right.png")
right_button=tk.Button(image=right_image,command=is_known,highlightthickness=0)
right_button.grid(row=1,column=1)

#Display Restart button on Screen
restart_button=tk.Button(text="Restart",command=restart)
restart_button.grid(row=2,column=2)

next_card()
root.mainloop()