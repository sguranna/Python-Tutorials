import tkinter

""" Creating a window and displaying some text"""

# window = tkinter.Tk()
# window.title("GUI")
# label = tkinter.Label(window, text="Hello!\n World", fg="red", bg="white")
# label.pack()
# label1 = tkinter.Label(window, text="Good morning", fg="white", bg="blue")
# label1.pack()
# label2 = tkinter.Label(window, text="Good morning", fg="red", bg="blue")
# label2.pack()
# window.mainloop()


"""Adding buttons"""

# def addition(a=10,b=20):
#     print("Addition is:\n")
#     print(a+b)
#     win1 = tkinter.Tk()
#     label1 = tkinter.Label(win1, text=f"The addition is \n{a+b}").pack()
#     win1.mainloop()
# def sub(a=10,b=20):
#     print(a-b)
# def mul(a=10,b=20):
#     print(a*b)
# def div(a=10,b=20):
#     print(a/b)


# root=tkinter.Tk()

# button1 = tkinter.Button(root, picture="sample.jpg", fg="red", width=25, bg="white",activebackground="green",command=addition)
# button2 = tkinter.Button(root, text="Sub", fg="blue", width=25,bg="red",command=sub)
# button3 = tkinter.Button(root, text="Mul", fg="green", width=25,bg="blue",command=mul)
# button4 = tkinter.Button(root, text="Div", fg="purple", width=25,bg="green",command=div)

# # button1.grid(row=0, column=0)
# # button2.grid(row=0, column=1)
# # button3.grid(row=1, column=0)
# # button4.grid(row=1, column=1)
# button1.place(x=0, y=0)
# button2.place(x=500, y=0)
# button3.place(x=10, y=200)
# button4.place(x=10, y=100)

# # button1.pack(side=tkinter.RIGHT)
# # button2.pack()
# # button3.pack()
# # button4.pack(side=tkinter.RIGHT)

# root.mainloop()

""" Fitting the widgets. Ex: label"""

# root=tkinter.Tk()
# one = tkinter.Label(root, text="One", fg="red", bg="white")
# one.pack(side=tkinter.RIGHT)
# two = tkinter.Label(root, text="TWO", fg="black", bg="white")
# two.pack(fill=tkinter.X, side=tkinter.RIGHT)
# three = tkinter.Label(root, text="Three", fg="blue", bg="yellow")
# three.pack(fill=tkinter.Y, side=tkinter.RIGHT)
# root.mainloop()

""" Grid Layout"""

# from tkinter import *
# root = Tk()

# label1 = Label(root,text="UserName :")
# label2 = Label(root,text="Password :")

# entry1 = Entry(root)
# entry2 = Entry(root)

# label1.grid(row=0, column=0)
# label2.grid(row=1, column=0)

# entry1.grid(row=0, column=1)
# entry2.grid(row=1, column=1)

# c = Checkbutton(root, text="Keep me logged in")
# # c.grid(row=2, column=0)
# c.grid(columnspan=2)

# b = Button(root, text="Login", activebackground="green", fg="red", bg="white")
# b.grid(row=3, column=0)
# # b.grid(columnspan=2)

# b2 = Button(root, text="Cancel", activebackground="red", fg="black", bg="white")
# b2.grid(row=3, column=1)
# # b2.grid(columnspan=2)

# root.mainloop()

"""Binding functions to gui"""

# from tkinter import *

# root=Tk()

# def sample():
#     print("My name is shiva!")

# button1 = Button(root, text="Print your name", command=sample)
# button1.pack()

# root.mainloop()

# from tkinter import *

# root=Tk()

# def sample(event):
#     print("My name is shiva!")

# button1 = Button(root, text="Print your name")
# button1.bind("<Button-1>", sample)
# button1.pack()

# root.mainloop()

"""Adding menus to gui"""

# from tkinter import *

# def doNothing():
#     win1 = tkinter.Tk()
#     label1 = tkinter.Label(win1, text=f"Open file").pack()
#     win1.mainloop()

# root=Tk()

# menu = Menu(root)
# root.config(menu=menu)

# fileMenu = Menu(menu)
# menu.add_cascade(label="File", menu=fileMenu)
# fileMenu.add_command(label="New File            ctrl+n", command=doNothing)
# fileMenu.add_command(label="Open File", command=doNothing)
# fileMenu.add_separator()
# fileMenu.add_command(label="Save File", command=doNothing)
# fileMenu.add_command(label="Close File", command=doNothing)
# fileMenu.add_command(label="Exit", command=doNothing)

# editMenu = Menu(menu)
# menu.add_cascade(label="Edit", menu=editMenu)
# editMenu.add_command(label="Undo", command=doNothing)
# editMenu.add_command(label="Redo", command=doNothing)

# root.mainloop()


# import tkinter

# main_win = tkinter.Tk()
# listbox = tkinter.Listbox(main_win)
# listbox.insert(1, "c++")
# listbox.insert(2, "Python")
# listbox.insert(3, "java")
# listbox.pack()

# main_win.mainloop()

# from tkinter import *

# root = Tk()
# rb = Radiobutton(root, text="Yes")
# rb.place(x=10, y=200)
# rb2 = Radiobutton(root, text="No")
# rb2.pack()

# root.mainloop()


""" Adding sclaes"""
# from tkinter import *

# root=Tk()
# s = Scale(root, from_=0, to=200, orient=HORIZONTAL)
# s.pack(fill=X)

# root.mainloop()

""" Spinbox"""
# from tkinter import *

# root=Tk()
# s = Spinbox(root, from_=0, to=200)
# s.pack(fill=Y)

# root.mainloop()


""" Scrollbar"""
# from tkinter import *

# root = Tk()

# s = Scrollbar(root)
# s.pack(side=RIGHT,fill=Y)
# mylist = Listbox(root, yscrollcommand=s.set)
# for x in range(1000):
#     mylist.insert(END, "This is line number "+str(x))
# mylist.pack(side=LEFT,fill=BOTH)
# s.config(command=mylist.yview)
# root.mainloop()
