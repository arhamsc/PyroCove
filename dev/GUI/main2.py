from tkinter import *
from tkinter import ttk 
 
top = Tk()  
top.geometry("500x400") 

style = ttk.Style(top)
print(style.theme_names())
style.theme_use("default")


   

label=Label(text="Pyrocove-A dynamic Firewall", width="30", height="2", font=("Calibri", 20))
label.pack()

label1=Label(text="Change Policy", width="30", height="2", font=("Calibri", 15))
label1.pack()
cp = Label(top, text = "Policy",font=('Arial 12')).place(x = 40,   y = 120)
cp_area = Entry(top,font=('Arial 12'),width = 30).place(x = 110,  y = 120) 

add_button = Button(top,text = "add",width=10).place(x = 400,  y = 200)

reset_button = Button(top,text = "reset",width=10).place(x = 150,  y = 250)

add_button = Button(top,text = "save",width=10).place(x = 250,  y = 250)

top.mainloop()