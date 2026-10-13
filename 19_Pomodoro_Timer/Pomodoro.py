#Import Molule
import tkinter as tk
import math

#Constants
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25 #Working Minutes
SHORT_BREAK_MIN = 5 #Short Break Minutes
LONG_BREAK_MIN = 20 #Long Break Minutes
reps=0
timer=None

#Setup screen
root=tk.Tk()
root.title("Pomodoro App")
root.config(padx=100,pady=50,bg=YELLOW)

#Timer Reset
def reset_timer():
    global reps
    root.after_cancel(timer)
    canva.itemconfig(timer_text,text="00:00") #Set Timer to 00:00 
    title_text.config(text="Timer",fg=GREEN)  #Set title text to Timer
    check_mark.config(text="") #Remove Check Marks
    reps=0 


#Timer Machanism
def start_timer():
    global reps
    reps += 1
    work_sec=WORK_MIN*60 #Convert Minutes Working into Seconds
    short_break_sec=SHORT_BREAK_MIN*60 #Convert Short Break Minutes into Seconds
    long_break_sec=LONG_BREAK_MIN*60 #Convert Long Break Minutes into Seconds

    if reps % 8 == 0:
        title_text.config(text="Break",fg=RED) #Set Title text to Break
        count_down(long_break_sec) #Start Long Break Coundown
    elif reps % 2 == 0:
        title_text.config(text="Break",fg=PINK) #Set Title text to Break
        count_down(short_break_sec) #Start Short Break Coundown
    else:
        title_text.config(text="Work",fg=GREEN) #Set Title text to Work
        count_down(work_sec) #Start Work Coundown

#Countdown Machanism
def count_down(count):
    count_min=math.floor(count / 60) 
    count_sec=count % 60

    if count_sec<10:
        count_sec=f"0{count_sec}"

    canva.itemconfig(timer_text,text=f"{count_min}:{count_sec}") #Start Timer on Screen
    if count > 0:
        global timer
        timer=root.after(1000,count_down,count - 1)
    else:
        start_timer()
        marks=""
        work_sessions=math.floor(reps/2)
        for _ in range(work_sessions):
            marks+="✔"
        check_mark.config(text=marks) #Display Check marks on Screen

#UI Setup
title_text=tk.Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,50,"bold")) #Display Title text on screen
title_text.grid(row=0,column=1)

check_mark=tk.Label(fg=GREEN,bg=YELLOW) #Make Check marks  
check_mark.grid(row=4,column=1)

b1=tk.Button(text="Start",highlightthickness=0,command=start_timer)
b1.grid(row=3,column=0) #Display Start Butten on Screen
b2=tk.Button(text="Reset",highlightthickness=0,command=reset_timer)
b2.grid(row=3,column=2) #Display Reset Butten on Screen

#Setup Image on screen
canva=tk.Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0) #Setup Canva Screen
tomato_image=tk.PhotoImage(file="./Assets/tomato.png") #Take Image
canva.create_image(100,112,image=tomato_image) #Display Image on Screen
timer_text=canva.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,30,"bold")) #Display Timer Text on Screen
canva.grid(row=1,column=1)


root.mainloop()