from graph import *
x = 100
y = 100
xcentr = 100
ycentr = 200
R = 10
brushColor('Blue')
polygon([(0,0), (300,300)])
def update():
	global x
	global xcentr
	global ycentr
	global R
	obj1 = circle(xcentr,ycentr,R)
	x += 5
	xcentr += 10
	moveObjectBy(obj1,5,0)
	if xcentr >= 200:
		ycentr+= 5
	elif ycentr >= 200:
		ycentr -= 5
		xcentr -=10		
def romb(x,y):
	polygon([ (x,y), (x+30,y-60), (x+30,y),(x+30,y+60),(x,y)])

onTimer(update, 100)		
run()	