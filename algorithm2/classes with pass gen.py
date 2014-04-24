import random
from tkinter import *

def callback():
    print ("click!") 

class Password():

	def __init__ (self):

		self.choice = []
		self.k = 0
 		# puts passwords in button form
		global master 
		master= Tk()

		self.b = Button(master,command= callback)
		self.c = Button (master, command = callback)
		self.d = Button(master, command = callback)
		self.e = Button(master, command = callback)
		self.f = Button (master, command = callback)
		self.g = Button (master, text = "New Passwords", command = self.updatePassword) 
		self.l = Label (master, text ='')

		self.b.grid(row = 0, column = 0)
		self.c.grid(row = 1, column = 0)
		self.d.grid(row = 2, column = 0)
		self.e.grid(row = 3, column = 0)
		self.f.grid(row = 4, column = 0)
		self.g.grid(row = 7, column = 0)
		self.l.grid (row = 6, column = 0 )
		self.updatePassword()

		mainloop()

	def updatePassword (self):
		
		wordsList = []

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

		# puts passwords in buttons
		self.b.config(text = bb)
		self.c.config(text = cb)
		self.d.config(text = db)
		self.e.config(text = eb)
		self.f.config(text = fb)

		# self.b.config(command = self.chosen(bb))
		self.k = self.k + 1

		self.l.config(text = self.k)
	# def chosen(self, password1):
	# 	#self.choice.append(password1)
	# 	self.l.config(text = password1)





WT = Password()

# master = Tk()

# def callback():
#     print ("click!")

# b = Button(master, text=a, command=callback)
# b.pack()

# mainloop()

