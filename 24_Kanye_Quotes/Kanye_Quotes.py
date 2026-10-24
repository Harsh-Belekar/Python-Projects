import tkinter as tk
import requests

root=tk.Tk()
root.title("Kanye Says..")
root.config(padx=50,pady=50)

def get_quote():
    responce=requests.get(url="https://api.kanye.rest")
    responce.raise_for_status()

    data=responce.json()
    quote=data["quote"]
    canvas.itemconfig(quote_text,text=quote)

canvas=tk.Canvas(width=300,height=414)

background_img=tk.PhotoImage(file="./Assets/background.png")
canvas.create_image(150,207,image=background_img)
quote_text=canvas.create_text(150,207,text="Kanye Quote Goes HERE",width=250,font=("arial",20,"italic"),fill="white")
canvas.grid(row=0,column=0)

kanye_img=tk.PhotoImage(file="./Assets/kanye.png")
kanye_button=tk.Button(image=kanye_img,highlightthickness=0,command=get_quote)
kanye_button.grid(row=1,column=0)
root.mainloop()