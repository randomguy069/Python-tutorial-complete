"""
program storing book info
user needs to input title, author, year, ISBN

user can view records, search, add, update, delete and close the program


to make .exe -> pyinstaller --onefile --windowed frontend.py
"""
from tkinter import *
import backend #importing from the backend script

def get_selected_row(event): #holds info about the type of event
    try:
        global selected_tuple #declaring selected_tuple
        index=list1.curselection()[0] #returns the index of the selected item. [0] returns the index from the given tuple
        selected_tuple = list1.get(index)
        #displaying all the stuff in the entry boxes
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
    except IndexError:
        pass




def view_command():
    list1.delete(0,END) #making sure list is empty before displaying

    for row in backend.view(): #accessing each tuple from the list returned from backend.view
        list1.insert(END,row) #inserting from the end

def search_command():
    list1.delete(0,END)
    for row in backend.search(title_text.get(),author_text.get(), isbn_text.get(), year_text.get()):
        list1.insert(END,row)

def add_command():
    backend.insert(title_text.get(),author_text.get(), isbn_text.get(), year_text.get())
    list1.delete(0,END)
    list1.insert(END,(title_text.get(),author_text.get(), isbn_text.get(), year_text.get()))

def delete_command():
    backend.delete(selected_tuple[0])
    #view_command()
def update_command():
    backend.update(selected_tuple[0],title_text.get(),author_text.get(), isbn_text.get(), year_text.get())
    #view_command()

window = Tk()

window.wm_title("Book Store")
l1 = Label(window,text="Title")
l1.grid(row=0,column=0)
l2 = Label(window,text="Year")
l2.grid(row=1,column=0)
l3 = Label(window,text="Author")
l3.grid(row=0,column=2)
l4 = Label(window,text="ISBN")
l4.grid(row=1,column=2)

title_text=StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0,column=1)

author_text=StringVar()
e2 = Entry(window, textvariable=author_text)
e2.grid(row=0,column=3)

isbn_text=StringVar()
e3 = Entry(window, textvariable=isbn_text)
e3.grid(row=1,column=3)

year_text=StringVar()
e4 = Entry(window, textvariable=year_text)
e4.grid(row=1,column=1)

b1=Button(window,text="View All",width =12, command=view_command)
b1.grid(row=2,column=3)

b2=Button(window,text="Search Entry",width =12,command=search_command)
b2.grid(row=3,column=3)

b3=Button(window,text="Add Entry",width =12,command=add_command)
b3.grid(row=4,column=3)

b4=Button(window,text="Update an Entry",width =12, command=update_command)
b4.grid(row=5,column=3)

b5=Button(window,text="Delete An Entry",width =12, command=delete_command)
b5.grid(row=6,column=3)

b6=Button(window,text="Close",width =12,command=window.destroy)
b6.grid(row=7,column=3)

list1 = Listbox(window,height =6, width =75)
list1.grid(row=2,column=0,rowspan=6,columnspan=2) #spanning the entire list box

sb1 =Scrollbar(window) #creating a Scrollbar
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand = sb1.set) #vertical scrollbar set
sb1.configure(command=list1.yview) #configuring the scrollbar
list1.bind('<<ListboxSelect>>',get_selected_row) #to get the id of the selected row in the list

window.mainloop()
