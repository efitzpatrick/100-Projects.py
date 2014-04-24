import random
from tkinter import *

def callback():
    print ("click!") 


def updatePassword ():



	wordsList = ["python", "programming", "ellie", "bosta", "bear", "bella", "charlie",
	  "theater", "techie", "Harpeth", "Hall", "Oak", "Hill", "2001", "01", "16", "2016", "bears", "honeybears"
	  ,"lights", "stage", "manage", "sm", "asm","tennis", "soccer", "TNFC", "backstage", 
	  "badger"]

	x = len(wordsList) -1
	x = int(x)
	tempPass = []
	for i in range(0, 5):
		y = random.randint(0,x)
		z = random.randint(0,x)
		zz = random.randint(0,x)
		tempPass.append(wordsList[int(y)] + wordsList[int(z)] + wordsList[int(zz)])
		random

	bb= tempPass[0]
	cb = tempPass[1]
	db = tempPass[2]
	eb = tempPass[3]
	fb = tempPass [4]

	button.b["text"] = bb
	# puts passwords in button form
	#master = Tk()

	# b = Button(master, text=bb, command=callback)
	# c = Button (master, text = cb, command = callback)
	# d = Button(master, text = db, command = callback)
	# e = Button(master, text = eb, command = callback)
	# f = Button (master, text = fb, command = callback)
	g = Button (master, text = "New Passwords", command = updatePassword) 
	l = Label (master, text ='')
	#opens in new window, how do I avoid this? ^^^^^^

	b.grid_forget()
	c.grid_forget()
	d.grid_forget()
	e.grid_forget()
	f.grid_forget()
	g.grid_forget()
	l.grid_forget()

	b.grid(row = 0, column = 0)
	c.grid(row = 1, column = 0)
	d.grid(row = 2, column = 0)
	e.grid(row = 3, column = 0)
	f.grid(row = 4, column = 0)
	g.grid(row = 7, column = 0)
	l.grid (row = 6, column = 0 )
	mainloop()

tempPass = []
def genPassword ():
	wordsList = ["python", "programming", "ellie", "bosta", "bear", "bella", "charlie",
	  "theater", "techie", "Harpeth", "Hall", "Oak", "Hill", "2001", "01", "16", "2016", "bears", "honeybears"
	  ,"lights", "stage", "manage", "sm", "asm","tennis", "soccer", "TNFC", "backstage", 
	  "badger"]

	x = len(wordsList) -1
	x = int(x)
	tempPass = []
	for i in range(0, 5):
		y = random.randint(0,x)
		z = random.randint(0,x)
		zz = random.randint(0,x)
		tempPass.append(wordsList[int(y)] + wordsList[int(z)] + wordsList[int(zz)])
		random

	bb= tempPass[0]
	cb = tempPass[1]
	db = tempPass[2]
	eb = tempPass[3]
	fb = tempPass [4]


	# puts passwords in button form
	global master 
	master= Tk()
	b = Button(master, text=bb, command=callback)
	c = Button (master, text = cb, command = callback)
	d = Button(master, text = db, command = callback)
	e = Button(master, text = eb, command = callback)
	f = Button (master, text = fb, command = callback)
	g = Button (master, text = "New Passwords", command = updatePassword) 
	l = Label (master, text ='')
	#opens in new window, how do I avoid this? ^^^^^^
	b.grid(row = 0, column = 0)
	c.grid(row = 1, column = 0)
	d.grid(row = 2, column = 0)
	e.grid(row = 3, column = 0)
	f.grid(row = 4, column = 0)
	g.grid(row = 7, column = 0)
	l.grid (row = 6, column = 0 )
	mainloop()

genPassword()

# master = Tk()

# def callback():
#     print ("click!")

# b = Button(master, text=a, command=callback)
# b.pack()

# mainloop()

