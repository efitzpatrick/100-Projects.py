import random
wordsList = ["python", "programming", "ellie", "bosta", "bear", "bella", "charlie",
 "theater", "techie", "Harpeth", "Hall", "Oak", "Hill", "2001", "01", "16", "2016"]




x = len(wordsList) -1
x = int(x)
tempPass = []
for i in range(0, 4):
	y = random.randint(0,x)
	z = random.randint(0,x)
	tempPass.append(wordsList[int(y)] + wordsList[int(z)])
	random
print (tempPass)