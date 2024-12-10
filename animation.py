from graph import *
import time
xcentr = 20
ycentr = 50
R = 10
brushColor('blue')
rectangle(0,0,400,400)
penColor('yellow')
brushColor('Yellow')
def KeyPressed(event):
	if event.keycode == VK_ESCAPE:
		close()
def update():
	global xcentr
	obj = circle(xcentr,ycentr,R)
	xcentr += 5
	moveObjectBy(obj, 5,0)
	if xcentr >= 400 - R:
		close()
onTimer(update, 20)	
onKey(KeyPressed)
run()

# Шахматная доска,клетки которой,буду появляться спустя небольшой промежуток времени