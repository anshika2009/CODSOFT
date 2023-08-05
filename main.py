import tkinter
import tkinter.messagebox
import pickle
from tkinter.messagebox import askyesno

#creating window
window=tkinter.Tk()
window.title("MY TO DO LIST")

#method to add
def task_adding():
    todo = task_add.get()
    i=1
    if todo != "":
        todobox.insert(tkinter.END,todo)
        task_add.delete(0,tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="ATTENTION!",message="Please enter your task")

#method to delete      
def task_deleting():
    try:
         #index_todo = todobox.selection()[0]
         index_todo = todobox.curselection()
         todobox.delete(index_todo)
        #todobox.delete(tkinter.ANCHOR)
    except:
        tkinter.messagebox.showwarning(title="ATTENTION!",message="Please select a task to delete")

def task_editing():
    selected_index = todobox.curselection()
    task = todobox.get(selected_index)
    todobox.delete(selected_index)
    task_add.insert(0,task)
    

# function to clear the list  
def clear_list():  
    answer = askyesno(title='confirmation',
                    message='Are you sure you want to clear the list?')
    if answer:
        todobox.delete(0,tkinter.END)

#creating frame
list_frame = tkinter.Frame(window)
list_frame.pack()

header_label = tkinter.Label(window, text="To-Do List", font=("times", 18, "bold"))
header_label.pack(pady=10)

#display the to-dos
todobox = tkinter.Listbox(list_frame,height=20,width=50,font=('Times', 14)) 
todobox.pack(side=tkinter.LEFT,fill=tkinter.BOTH)

#scrollbar
scroller = tkinter.Scrollbar(list_frame)
scroller.pack(side=tkinter.RIGHT, fill=tkinter.Y)

todobox.config(yscrollcommand=scroller.set)
#scroller.config(command=list_frame.yview)

#typing box
def on_click(event):
    task_add.configure(state=tkinter.NORMAL)
    task_add.delete(0, tkinter.END)

    # make the callback only work once
    task_add.unbind('<Button-1>', on_click_id)
    


task_add = tkinter.Entry(window, width=52, font=('times', 14))
task_add.insert(0,"Enter your task")
task_add.configure(state=tkinter.DISABLED)

on_click_id = task_add.bind('<Button-1>', on_click)
task_add.pack()

add_task_button = tkinter.Button(window, text="ADD TASK",font=("arial",20,"bold"),background="aquamarine",width=40,command=task_adding)
add_task_button.pack()

load_task_button = tkinter.Button(window, text="EDIT TASK",font=("arial",20,"bold"),background="yellow",width=40,command=task_editing)
load_task_button.pack()

remove_task_button = tkinter.Button(window, text="DELETE TASK",font=("arial",20,"bold"),background="red",width=40,command=task_deleting)
remove_task_button.pack()

load_task_button = tkinter.Button(window, text="CLEAR THE LIST",font=("arial",20,"bold"),background="gray57",width=40,command=clear_list)
load_task_button.pack()

window.mainloop()