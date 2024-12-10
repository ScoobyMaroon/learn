from graph import *

def update():
	y = 30
	number = 1
	for i in range(8):
		x = 30
		rectangle(x,y,x+25,y+25)
		for g in range(8):
			color = number % 2
			if color == 0:
				brushColor('Black')
				rectangle(x,y,x+25,y+25)
				number+=1
			else:
				brushColor('White')	
				rectangle(x,y,x+25,y+25)
				number+=1
			x +=25
		y +=25
		number+=1
onTimer(update,60)		
run()