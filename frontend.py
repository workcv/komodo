from Tkinter import *

window=Tk()

l1=Label(window,text="Title")
l1.grid(row=0,column=0)

l2=Label(window,text="Number")
l2.grid(row=0,column=2)

title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

number_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=3)

list1=Listbox(window,height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

b1=Button(window,text="View all",width=12)
b1.grid(row=2,column=3)

b1=Button(window,text="Add",width=12)
b1.grid(row=3,column=3)

b1=Button(window,text="Update",width=12)
b1.grid(row=4,column=3)

b1=Button(window,text="Delete",width=12)
b1.grid(row=5,column=3)

b1=Button(window,text="Close",width=12)
b1.grid(row=6,column=3)


window.mainloop()