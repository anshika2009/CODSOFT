from tkinter import *
import string
import random
import pyperclip

#method to generate password
def generator():
    
    passwordField.delete(0,END)
    
    small=string.ascii_lowercase 
    captial=string.ascii_uppercase
    numbers=string.digits
    special=string.punctuation
    all=small+captial+numbers+special
    
    passwordlen=int(length_Box.get())
    password=''
    
    if choice.get()==1:
        #passwordField.insert(0,random.sample(small,passwordlen))
        for i in range(passwordlen):
            c=random.choice(small)
            password+=c
        passwordField.insert(0,password)
        
    if choice.get()==2:
        #passwordField.insert(0,random.sample(small+captial+numbers+special,passwordlen))
        for i in range(passwordlen):
            c=random.choice(small+captial+numbers+special)
            password+=c
        passwordField.insert(0,password)

#method to copy to clipboard
def copy():
    password= passwordField.get()
    pyperclip.copy(password)

#window
window=Tk()
window.config(bg='lightskyblue')
window.geometry("380x380")

choice=IntVar()
Font=('arial',13,'bold')

passwordLabel=Label(window,text='PASSWORD GENERATOR',font=('times new roman',20,'bold'),bg='gray20',fg='white')
passwordLabel.grid(pady=10,padx=10)

strengthLabel=Label(window,text='Password Strength',font=Font,bg='gray20',fg='white')
strengthLabel.grid(pady=5,padx=5)

weakradioButton=Radiobutton(window,text='Weak',value=1,variable=choice)
weakradioButton.grid(pady=5,padx=5)

strongradioButton=Radiobutton(window,text='Strong',value=2,variable=choice)
strongradioButton.grid(pady=5,padx=5)

lengthLabel=Label(window,text='Password Length',font=Font,bg='gray20',fg='white')
lengthLabel.grid(pady=5,padx=5)

length_Box=Spinbox(window,from_=5,to_=18,width=5,font=Font)
length_Box.grid(pady=5,padx=5)

generateButton=Button(window,text='Generate',font=Font,command=generator)
generateButton.grid(pady=5,padx=5)

passwordField=Entry(window,width=35,bd=2,font=Font)
passwordField.grid(pady=10,padx=10)

copyButton=Button(window,text='Copy to Clipboard',font=Font,command=copy)
copyButton.grid(pady=5,padx=5)

window.mainloop()