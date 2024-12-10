from graph import *
x = 100
y = 30
R = 10
x1 = x
y2 = 30
stroka = 0
def elochka(g):	
	global x,y,R,x1,y2,stroka
	for i in range(g):
		circle(x,y,R)
		y += 30
		stroka += 1
		for b in range(stroka):
				x = x - 20*stroka
				x1 = x
				print(x1)
				circle(x,y,R)
				x += 30			
print('Нужна точка,которая будет уходить влево на определенное кол-во , а затем уже по циклу возвращаться в правую сторону')
elochka(3)	
run()