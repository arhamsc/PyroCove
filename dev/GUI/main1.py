from tkinter import *
from tkinter import ttk 

top = Tk()  
top.geometry("500x400")
top.title("Pyro Cove Predictor Simulator")

# s = ttk.Style(top)
# s.theme_use("clam")   

label = Label(text="PyroCove", font=("Helvetica", 20))
label.place(anchor=CENTER)
label.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

menu_value = StringVar(top)
menu_value.set("Type of Check")


label = Label(top, text="Choose an option above.", font=("Arial 16")).grid(column=0, row=2, sticky=W)

def setState(y):
    global label
    label = Label(top, text = menu_value.get(),font=('Arial 16')).grid(column=0, row=2)


drop = OptionMenu(top, menu_value, "IP Address", "URL", command=setState)
drop.grid(row=1, column=0)



# status_name= Label(top,  text = "Status",font=('Arial 16')).place(x = 40,  y = 240) 
   

   
# url_area = Entry(top,font=('Arial 16'),width = 30).place(x = 110,  y = 180) 
   
# status_area = Entry(top,font=('Arial 16'),width = 30).place(x = 110, y = 240) 

# def print_answers():
#     print("Selected Option: {}".format(menu_value.get()))
#     return None
  
  
# Submit button
# Whenever we click the submit button, our submitted
# option is printed ---Testing purpose
# submit_button = Button(top, text='Submit', command=print_answers)
# submit_button.grid(row=4, column=0)
     
top.mainloop()


