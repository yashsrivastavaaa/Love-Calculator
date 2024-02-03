import customtkinter
import tkinter
from tkinter import messagebox 
import random

def calculate():
    a=name1_entry.get()
    b=name2_entry.get()

    if(a=="" and b =="") :
        messagebox.showerror("Error","Please Enter Any Name")
        return
    
    if(a=="" or b =="") :
        messagebox.showerror("Error","Please Enter Any Name")

    elif(a==b):
        messagebox.showerror("Error","You and Your Partner's Name Should be unique")

    else:
        percentage = random.randint(50,100)
        messagebox.showinfo("Love Percentage",f"You have love percentage of {percentage} with your partner")

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")
app = customtkinter.CTk()
app.geometry("510x185")
app.title("Love Calculator")
app.config(padx=20,pady=20)

name1_label = customtkinter.CTkLabel(master = app ,text="Enter Your Name : ",pady=20,padx=20)
name2_label = customtkinter.CTkLabel(master=app,text="Enter Your Partner's Name : ",pady=20,padx=20)
name1_label.grid(column=0,row=0)
name2_label.grid(column=0,row=1)

name1_entry = customtkinter.CTkEntry(master=app,corner_radius=10)
name2_entry = customtkinter.CTkEntry(master=app,corner_radius=10)

a=name1_entry.get()
b=name2_entry.get()

name1_entry.place(relx = 0.45,rely = 0.07,relwidth=0.4)
name2_entry.place(relx = 0.45,rely = 0.38,relwidth=0.4)

submit_button = customtkinter.CTkButton(master=app,text="Calculate",command=calculate)
submit_button.place(relx=0.4,rely=0.74)

app.mainloop()
