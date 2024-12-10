from graph import *
def krugi(x,y,R,c):
	brushColor(c)
	stroka = 1
	for i in range(6):
		circle(x,y,R)
		for g in range(4):
			circle(x,y,R)
			x += 22
		y += 20
		x = 10 + 10*stroka
		stroka += 1
def treugol(x,y,с):
	brushColor(с)
	for i in range(5):
		x1 = x
		polygon([(x1,y),(x1,y-22),(x1-20,y),(x1,y)])
		for g in range(20):
			polygon([(x1,y),(x1,y-22),(x1-20,y),(x1,y)])
			x1 += 20
		y += 20	
def rombi(x,y,c):
	brushColor(c)
	for i in range(6):
		x1 = x
		polygon([(x,y),(x+15,y-15),(x+30,y),(x+15,y+15),(x,y)])
		polygon([(x+17,y-17),(x+32,y-32),(x+47,y-17),(x+32,y-2),(x+17,y-17)])
		polygon([(x+17,y+17),(x+32,y+32),(x+47,y+17),(x+32,y+2),(x+17,y+17)])
		polygon([(x+34,y),(x+49,y-15),(x+64,y),(x+49,y+15),(x+34,y)])
		for g in range(5):
			polygon([(x1,y),(x1+15,y-15),(x1+30,y),(x1+15,y+15),(x1,y)])
			polygon([(x1+17,y-17),(x1+32,y-32),(x1+47,y-17),(x1+32,y-2),(x1+17,y-17)])
			polygon([(x1+17,y+17),(x1+32,y+32),(x1+47,y+17),(x1+32,y+2),(x1+17,y+17)])
			polygon([(x1+34,y),(x1+49,y-15),(x1+64,y),(x1+49,y+15),(x1+34,y)])
			x1 += 70
		y += 70
rombi(20,60,'turquoise')
run()