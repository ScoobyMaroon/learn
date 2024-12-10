import time
#import keyboard
import adminsystem
card = ['Visa', 'Mastercard', 'Yota'] # Список доступных карт
money = ['10', '15000', '1000000'] # Баланс карт
password = ['2206', '2206', '2206'] # Пароли к картам
blcard = [] # Заблокированные карты
blmoney = [] # Деньги на заблокированных картах
blcomment = [] # Причина блокировки карт
prcard = [] # Подача заявки на блокировку карты
prmoney = [] # деньги на карте отправленная на проверку
blnb = 0 # Переменные для циклов
nbcard = 2 # <---
logcard1 = [] # Карта с которой был совершен перевод
logcard2 = [] # Карта на которую поступил перевод
logmoney1 = [] # Количество денег 
admin = False  # Статус администратора, если тру то дается доступ к админ системам
def pokazcheta(): # Просто выводит счета , без возвращения в меню
	global blnb 
	global nbcard
	global card
	global money
	global blcard
	global blmoney
	nb = 0 # разобраться с ошибкой выводв
	nb2 = 0
	nb3 = 0
	nb4 = 1
	print('Ваши счета:')
	for i in card: # Цикл выводящий все карты и баланс
			print('{}) {} - {}'.format(nb,card[nb2],money[nb3])) # Выводит карты с их балансом 
			nb += 1 # Переменные для того,чтобы отсчитать кол-во кард
			nb2 += 1
			nb3 += 1
def schet(): # Выводит доступные счета и возвращает в меню
	global blnb
	global nbcard
	global card
	global money
	global blcard
	global blmoney
	nb = 0 
	nb2 = 0
	nb3 = 0
	nb4 = 1
	print('Ваши счета:')
	for i in card:
			print('{}) {} - {}'.format(nb,card[nb2],money[nb3])) # Выводит карты с их балансом 
			nb += 1 # Переменные для того,чтобы отсчитать кол-во кард
			nb2 += 1
			nb3 += 1
	print('Перенаправление в гланое меню...')
	time.sleep(3)
	menu()	
# Можно добавить какими купюрами выдавать снятые деньги	
def create(): # создание новой карты
	print('Введите название карты') 
	name = input() # Получаем желаемое название
	card.append(name) # Добавляем в список
	money.append('0') # Устанавливаем баланс 
	print('Вы создали карту с названием {}'.format(name))
	time.sleep(1) 
	print('Перенаправление в гланое меню...')
	time.sleep(3)
	menu()
def delete(): # Удаляем уже созданную ранее карту
	pokazcheta() # выводим доступные карты
	print('Выберите карту,которую хотите закрыть(навсегда)') 
	ch = int(input())
	if money[ch] != '0': # Проверка , есть ли баланс на карте
		print('У вас есть средства на счету,переведите или снимите их')
	else:	# Если карта пустая , то удаляем ее из списков
		del card[ch]
		del money[ch]
	menu()
def zprblock():	# Функция для запроса блокировки карты
	global blcomment
	global prcard
	global numcard
	pokazcheta()
	print('Выберите карту ,которую хотите заблокировать')
	numcard = int(input())
	print('Введите причину блокировки')
	ch2 = input()
	blcomment.append(ch2) # Комментарий для проверки модераторами
	prcard.append(card[numcard]) # Добавляем карту в проверочный блок
	prmoney.append(money[numcard]) # Сохраняем деньги 
	comment = ch2 
	name = card[numcard] 
	print('Была подана заявка на блокировку карты {} . Причина: {}'.format(name,comment))
	menu()
def aban(): # Блок блокировки карт
	global nbcard
	global blnb
	global numcard
	chisla = 0
	waitcard = len(prcard)
	if waitcard > 0:
		print('Выберите карту,которую хотите заблокировать')
		for i in prcard: # Выводим все заявки на блокировку
			print('Карта {} .Причина: {} '.format(prcard[chisla],blcomment[chisla]))
			chisla += 1
		ch = int(input())
		blcard.append(prcard[ch]) # Добавляем в список заблокированных
		blmoney.append(prmoney[ch]) # Сохраняем баланс
		name = prcard[ch] 
		balance = prmoney[ch]
		del card[numcard]     # Удаляем все ненужное из списков
		del money[numcard]
		del prcard[ch]
		del prmoney[ch]
		del blcomment[ch]
		blnb += 1
		nbcard -= 1
		print('Карта {}  с балансом {} заблокирована!'.format(name,balance))
		time.sleep(1)
		menu()
	else:
		print('Нет карт на блокировку')
		print('Перенаправляю в админ меню...')
		time.sleep(1)
		osnmenu()

def blockedcard(): # Выводит заблокированные карты
	print('Ваши заблокированные карты:')
	nb = 0
	nb2 = 0
	nb3 = 0
	for i in blcard:
		print('{}) {} - {}'.format(nb3,blcard[nb], blmoney[nb2]) )	
		nb += 1
		nb2 += 1
		nb3 += 1
# adminsystem/////////////////////////////////////////////////////////////////////////////////////////////		
def log_in(): # Админ авторизация 
	global admin # при верном пароле дает полный доступ
	print('Введите имя пользователя')
	aname = input()
	check = aname in adminsystem.admins
	if check == True:
		print('Введите пароль')
		apassword = input()
		check2 = apassword in adminsystem.admins.values()
		if check2 == True:
			print('Вы вошли в систему как Администратор')
			admin = True
			menu()
	else: 
		print("Error")
		print("Back to menu...")
		time.sleep(1)
def log():
	print('Логи:')
	ab = 0
	for i in ab:
		print('{}.С карты {} совершен перевод в размере {} на карту {}'.format(ab, logcard1, logmoney1, logcard2))
		ab +=1	
	print('Вернуться в меню?y/n')
	ch = input()
	if ch == y:
		menu()
	else:
		pass		
def admbalance():
	print('Выберите карту с которой хотите провести операцию')
	
def osnmenu(): # Админ панель
	print('1)Карты на блокировку')
	print('2)Карты на разблолкировку')
	print('3)Удалить карту человеку')
	print('4)Положить/снять деньги на карту')	
	print('5)Совершенные переводы')	
	print('6)В главное меню')
	ch = input()
	if ch == '1': # Заявки на блокировку
		aban()
	if ch == '4':
		admadd()	
	if ch == '5':
		log()	
	if ch == '6': # Выход в обычное меню
		menu()	

#adminsystem////////////////////////////////////////////////////////////////////////////////////////////// 
def unblocked(): # Разблокировка карты
	print('Хотите разблокировать карту?')
	ch = input('y/n') 
	if ch == 'y':
		blockedcard() # выводит заблокированные карты
		print('Выберите карту')
		ch2 = int(input()) 
		card.append(blcard[ch2]) # Добавляем карту из заблокированных в обычный список
		money.append(blmoney[ch2]) # Деньги тоже возвращаем
		name = blcard[ch2] 
		del blcard[ch2] # Удаляем из заблокированных
		del blmoney[ch2]
		print('Карта {} разблокированна!'.format(name)) 
		print('Переход в меню')
		time.sleep(1)
		menu()
	else:  # Если пользователь отказался, то выходим в меню
		print('Переход в меню...')
		time.sleep(1)
		menu()	
############################################################ ФИНАНСОВЫЙ ОТДЕЛ ##################################################################################
def moneyfunction(): # Денежная функция (Управление картой)
	global card
	global money
	global logcard2
	global logmoney1
	global logcard1
	print('выберите карту')
	pokazcheta()
	numbercard = int(input())
	def pereveod_na_schet():
		print('Введите номер карты,на которую хотите перевести деньги') 
		pokazcheta()
		perevod = int(input())		
		if perevod == numbercard:
			print('Вы не можете перевести деньги на эту карту')
			menucard()
		else: 
			name = card[perevod] # Карта на которую поступает перевод
			name2 = card[numbercard] # карта с которой идет перевод
			print('Введите сумму перевода')
			balance = int(money[numbercard])
			summa = int(input()) # Сохраняем сумму перевода в числовом виде
			if summa == balance: 
				balance2 = int(money[perevod]) # Если сумма равна балансу,то сразу ставим баланс основной карты на ноль
				card2 = card[perevod]
				logcard1.append(name2)
				logcard2.append(name)
				logmoney1.append(summa)
				del card[numbercard]
				del money[numbercard]
				money.append('0')
				card.append(name2)
				del money[perevod]
				del card[perevod]
				summa = summa + balance2
				money.append(summa)
				card.append(name)
				print('Перевод совершен на карту {}'.format(name))
				menu()
			elif summa < balance:
				balance = balance - summa
				logcard1.append(name2)
				logcard2.append(name)
				logmoney1.append(summa)
				del card[numbercard]
				del money[numbercard]
				money.append(balance)
				card.append(name2)
				balance2 = money[perevod]
				del money[perevod]
				del card[perevod]
				balance2 = int(balance2) + summa
				money.append(balance2)
				card.append(name)
				print('Перевод совершен на карту {}'.format(name))
				time.sleep(0.5)
				menu()
			else:
				print('Недостаточно средств для перевода')
				time.sleep(0.5)
				menucard()	
	def menucard(): # Меню после авторизации,чтобы не пришлось постоянно выбирать карту
		balance = int(money[numbercard]) # баланас выбранной карты
		remcard = card[numbercard] # Запоминаем карту
		print('Меню Карты {}'.format(card[numbercard]))	
		print('1)Пополнить')
		print('2)Снять ')
		print('3)Баланс')
		print('4)Перевести деньги на другую карту')
		ch2 = int(input())
		if ch2 == 1: # Пополнение счета
			print('Введите сумму')
			add = int(input()) # кол-во денег , которое надо пополнить
			if add > 0:
				print('Пожалуйста,подождите')
				add = add + balance # Количество денег на пополнение
				del money[numbercard] # Удаляем из списков
				del card[numbercard]
				money.append(add) # Добавляем заново , т.к иначе списки не будут сходиться
				card.append(remcard)
				print('Успешно пополнено')
				menu()
		if ch2 == 2:	# Снятие денег
			print('Введите сумму') 
			minus = int(input()) 
			if minus < balance: # Проверка хватит ли денег на то,что бы снять деньги  
				print('Пожалуйста,подождите')
				minus = balance - minus # Находим остаток на счету
				del money[numbercard]  # Удаляем карту и деньги из списков
				del card[numbercard] # Чтобы они неотделялись друг от друга
				money.append(minus) # Добавляем остаток
				card.append(remcard) # Возвращаем карту
				print('Успешно снято')
				menu()	
			elif balance == minus: # Если баланс равен минусу
				del money[numbercard] # Удаляем карту и деньги из списков
				del card[numbercard] # Чтобы они неотделялись друг от друга
				money.append('0') # Устанавливаем значение ноль
				card.append(remcard) # Возвращаем карту на место
				menu()
			else: # Если запрос больше чем есть средств на балансе
				print('Недостаточно средств') # Выводим ошибку
				menucard()	 # Перенаправлем в гл.меню карты
		if ch2 == 3: # Просто выводим баланс с помощью переменной
			print('Баланс карты: {}'.format(balance))	
			menucard()
		if ch2 == 4:  # Перевод денег между счетами
			pereveod_na_schet()		
	menucard()			
def log_admin():
	admin = True
	menu()		
################################################################################################################################################################					
def menu(): # обычное меню пользователя
	if admin == False:
		print('Статус:Пользователь')
		print('Выберите действие:')
		print('1)Показать карты')
		print('2)Создать новую карту')
		print('3)Удалить созданную ранее карту')
		print('4)Заблокировать карту')
		print('5)Пополнить/снять средства')
		print('6)Перевод между счетами')
		print('7)Разблокировать карту')
		print('8)выход')
		ch = input()
		if ch == '1':
			schet()
		elif ch == '2':
			create()
		elif ch == '3':
			delete()
		elif ch == '4':
			zprblock()
		elif ch == '5':
			moneyfunction()
		elif ch == '6':
			pereveod_na_schet()
		elif ch == '7':	
			unblocked()
		elif ch == '8':
			print('Завершаем работу')
		elif ch == 'ap':
			log_in()
		else:
			print('Error')
			menu()		
	else:		# Выводит админ-панель 
		print('Статус:Администратор')
		print('Выберите действие:')
		print('1)Показать карты')
		print('2)Создать новую карту')
		print('3)Удалить созданную ранее карту')
		print('4)Заблокировать карту')
		print('5)Пополнить/снять средства')
		print('6)Перевод между счетами')
		print('7)Разблокировать карту')
		print('8)Админ-панель')
		print('9)Основные команды')
		print('10)выход')
		ch = input()
		if ch == '1':
			schet()
		elif ch == '2':
			create()
		elif ch == '3':
			delete()
		elif ch == '4':
			zprblock()
		elif ch == '5':
			moneyfunction()
		elif ch == '6':
			pereveod_na_schet()
		elif ch == '7':	
			unblocked()
		elif ch == '10':
			print('Завершаем работу')
		elif ch == '8':
			osnmenu()
		else:
			print('Error')
			menu()
menu()	


