from graph import *
import time
x = 30
y = 30
x1 = 1
y2 = 1
vrem = 1
def chess2():
	global x, y, x1, y2
	rectangle(x,y,x+25,y+25)
	chess() 
	y+=20
def chess():
	global x, y, x1, y2
	x+=25
	x1 += 1
	rectangle(x,y,x+25,y+25)
while vrem <= 8:
	onTimer(chess,60)
	vrem+=1
else:
	print('error')
run()