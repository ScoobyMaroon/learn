from graph import *
x = 40
y = 50
stroka = 1
for i in range(5):
	brushColor('green')
	circle(x,y,20)
	for g in range(stroka):
		circle(x,y,20)
		x += 50
	y += 50
	x = 40
	stroka += 1
run()