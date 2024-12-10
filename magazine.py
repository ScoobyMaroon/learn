#print('Введите секунды')
#time = int(input())
#minut = time // 60
#sek = time % 60
#print('В {} секундах {} минут и {} секунд'.format(time,minut,sek))
from graph import *
from random import *
for i in range(10):
	x = randint(1,300)
	y = randint(1,300)
	r = randint(1,40)
	c = randint(0,255)
	c1 = randint(0,255)
	c2 = randint(0,255)
	brushColor(c,c1,c2)
	circle(x,y,r)
run()