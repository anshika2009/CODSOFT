import tkinter
from tkinter import *

root=Tk()
root.title("CALCULATOR")
root.geometry("570x600+100+200")
root.resizable(False,False)
root.configure(bg="#17161b")

label_result = Label(root,anchor='e',width=25,height=2,text="",font=("arial",30),justify=RIGHT)
label_result.pack()

equation = ""

def display(value):
    global equation
    equation += value 
    label_result.config(text=equation,justify=RIGHT)

def clear():
    global equation
    equation = ""
    label_result.config(text=equation,justify=RIGHT)

def calculate():
    #label_result.config(text='',justify=RIGHT)
    global equation
    result = ""
    if equation != "":
        try:
            result = eval(equation)
        except:
            result = "ERROR"
            equation = ""
    label_result.config(text=result,justify=RIGHT)

def delete():
    global equation
    equation = equation[:-1]
    label_result.config(text=equation,justify=RIGHT)

Button(root,text="C", width=5, height=1, font=("arial",30,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda: clear()).place(x=10,y=100)
Button(root,text="/", width=5, height=1, font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: display("/")).place(x=290,y=100)
Button(root,text="DEL", width=5, height=1, font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: delete()).place(x=150,y=100)
Button(root,text="*", width=5, height=1, font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: display("*")).place(x=430,y=100)

Button(root,text="7", width=5, height=1, font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: display("7")).place(x=10,y=200)
Button(root,text="8", width=5, height=1, font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: display("8")).place(x=150,y=200)
Button(root,text="9", width=5, height=1, font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: display("9")).place(x=290,y=200)
Button(root,text="-", width=5, height=1, font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: display("-")).place(x=430,y=200)

Button(root,text="4", width=5, height=1, font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: display("4")).place(x=10,y=300)
Button(root,text="5", width=5, height=1, font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: display("5")).place(x=150,y=300)
Button(root,text="6", width=5, height=1, font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: display("6")).place(x=290,y=300)
Button(root,text="+", width=5, height=1, font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: display("+")).place(x=430,y=300)

Button(root,text="1", width=5, height=1, font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: display("1")).place(x=10,y=400)
Button(root,text="2", width=5, height=1, font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: display("2")).place(x=150,y=400)
Button(root,text="3", width=5, height=1, font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: display("3")).place(x=290,y=400)
Button(root,text="0", width=11, height=1, font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: display("0")).place(x=10,y=500)

Button(root,text=".", width=5, height=1, font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: display(".")).place(x=290,y=500)
Button(root,text="=", width=5, height=3, font=("arial",30,"bold"),bd=1,fg="#fff",bg="#fe9037",command=lambda: calculate()).place(x=430,y=400)

root.mainloop()