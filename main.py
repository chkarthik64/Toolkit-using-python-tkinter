import calculator
import currency_converter
import tkinter as tk

from PIL import ImageTk,Image

import notepad
import clock
import calender


root = tk.Tk()
root.title("MULTI TASKING APP")
root.geometry(f"{500}x{500}")

calc_img = tk.PhotoImage(file="calc_img.png")
cur_img = tk.PhotoImage(file="converter_img.png")
note_img = tk.PhotoImage(file="note_img.png")
clock_img = tk.PhotoImage(file="clock_img.png")
calen_img = tk.PhotoImage(file="calender.img.png")

'''img=Image.open("calc_img.png")
img=img.resize((500,500),Image.ANTIALIAS)
back_g=ImageTk.photoImage(img)'''


title = tk.Label(root, text="py.toolkit",
                 font=("arial", 20), anchor="center")
title.grid(row=0, column=0, columnspan=2, sticky="nsew")

calculator_button = tk.Button(
    root, text="Calculator", command=lambda: calculator.Calculator().main(), image=calc_img, compound="top")
calculator_button.grid(row=1, column=0, sticky="nsew")

currency_converter_button = tk.Button(
    root, text="Currency Converter", command=lambda: currency_converter.CurrencyConverter(root), image=cur_img, compound="top")
currency_converter_button.grid(row=1, column=1, sticky="nsew")


notepad_button = tk.Button(root, text="Note Pad",
                           command=lambda: notepad.Notepad(root), image=note_img, compound="top")
notepad_button.grid(row=2, column=0, columnspan=1, sticky="nsew")

clock_button = tk.Button(
    root, text="Clock", command=lambda: clock.Clock().main(), image=clock_img, compound="top")
clock_button.grid(row=2, column=1, columnspan=1, sticky="nsew")

calendar_button = tk.Button(
    root, text="Calender", command=lambda: calender.CalenderProg(), image=calen_img, compound="top")
calendar_button.grid(row=3, column=0, columnspan=2, sticky="nsew")


for i in range(4):
    root.rowconfigure(i, weight=1)
for i in range(2):
    root.columnconfigure(i, weight=1)

root.mainloop()
