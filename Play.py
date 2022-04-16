from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import time

TotalAmount = 0.0 # Total Money Amount 
Budget = 0.0 # Current Money Amount
Increase = 0.0 # Money Increase in 100 milliseconds 
Running = False 
Path1 = 'Data/background-3.jpg'
Path2 = 'Data/MoneyBag.png' 
AchiveRes1 = 0 # Flag for first 4 achivements to occur only once
AchiveRes2 = 0 # Flag for 5 - 8 achivements to occur only once
CaseRes = 0 # Flag for Clicker Mode to delete previous image

root = Tk()
root.geometry('2000x1500')
root.title('Money_Clicker')

fileBG = Image.open(Path1)
BG = ImageTk.PhotoImage(fileBG)

Window = Canvas(root, height = 1000, width = 1000)
Window.pack(expand = True, fill = "both")
Window.create_image(0, 0, image = BG, anchor = "nw")
MoneyBag = PhotoImage(file = Path2)

Window.create_text(1000, 35, text = "Welcome To Money Clicker Game", font = ("helvetica", 20), fill = "white")

ShowBudget = Window.create_text(350, 250, text = f'Budget = {Budget}$', font = ("helvetica", 20), fill = "white")

MoneyPerSecond = Window.create_text(350, 350, text = f'Income = {Increase * 10}$ p.s', font = ("helvetica", 20), fill = "white")

def New():
	"""Restarts the Game"""
	global TotalAmount
	global Budget
	global Increase
	global Running
	global Window
	global ShowBudget
	global MoneyPerSecond
	global C1

	Begin = messagebox.askquestion('New Game', 'Start Again?', icon = 'question')
	if Begin == "yes":
		Running = False
		TotalAmount = 0.0
		Budget = 0.0
		Increase = 0.0
		Window.itemconfig(ShowBudget, text = f'Budget = {Budget}$')	
		Window.itemconfig(MoneyPerSecond, text = f'Income = {Increase * 10}$ p.s')
		C1.invoke()

def Help():
	""" Brings the new window with short information about the game"""
	FAQ = Toplevel()
	FAQ.geometry("800x300")
	FAQ.title("Help")

	Info = Text(FAQ)
	Sym = Label(Info, text = "info", bitmap = "info", height = 33, width = 33)
	Sym.place(x = 0, y = 0)
	Info.insert(INSERT, "  It is a Clicker game, Player should Click on Money Bag Using Cursor or by Pressing the Space Button to Get Money. Player can buy Clickers, Factories, Shops, SuperMarkets, Factories and MoneyPrinters to Gain money automatically.")
	Info.config(state = DISABLED)
	Info.pack()

	CloseButton = Button(Info, text = "Close", command = FAQ.destroy, height = 1, width = 5, cursor = "arrow")
	CloseButton.place(x = 340, y = 170)	
	FAQ.bind("<Return>", lambda event: CloseButton.invoke())
	FAQ.mainloop()	

def Exit():
	"""Bring window with option to close the program"""
	global StopCond
	Quit = messagebox.askquestion('Exit Game', 'Quit?', icon = 'question')
	if Quit == "yes":
		Running = False
		Window.destroy()
		root.destroy()

def Achivement1():
	global TotalAmount
	global Budget
	global Window
	global ShowBudget

	A1 = Label(Window, text = "First 100 Dollar Achivement, You get 50 Dollars", height = 2, font = "bold", bg = "green")
	A1.pack(side = BOTTOM)
	Budget += 50
	TotalAmount += 50
	Window.itemconfig(ShowBudget, text = f'Budget = {Budget}$')	
	Window.after(5000, A1.destroy)

def Achivement2():
	global TotalAmount
	global Budget
	global Window	
	global ShowBudget

	A2 = Label(Window, text = "First 1000 Dollar Achivement, You get 500 Dollars", height = 2, font = "bold", bg = "green")
	A2.pack(side = BOTTOM)
	Budget += 500
	TotalAmount += 500
	Window.itemconfig(ShowBudget, text = f'Budget = {Budget}$')	
	Window.after(5000, A2.destroy)

def Achivement3():
	global TotalAmount
	global Budget
	global Window
	global ShowBudget

	A3 = Label(Window, text = "First 10000 Dollar Achivement, You get 5000 Dollars", height = 2, font = "bold", bg = "green")
	A3.pack(side = BOTTOM)
	Budget += 5000
	TotalAmount += 5000
	Window.itemconfig(ShowBudget, text = f'Budget = {Budget}$')	
	Window.after(5000, A3.destroy)

def Achivement4():
	global TotalAmount
	global Budget
	global Window
	global ShowBudget

	A4 = Label(Window, text = "First 100000 Dollar Achivement, You get 50000 Dollars", height = 2, font = "bold", bg = "green")
	A4.pack(side = BOTTOM)
	Budget += 50000
	TotalAmount += 50000
	Window.itemconfig(ShowBudget, text = f'Budget = {Budget}$')	
	Window.after(5000, A4.destroy)

def Achivement5():
	global TotalAmount
	global Budget
	global Window
	global ShowBudget

	A1 = Label(Window, text = "Total Money Amount 10000 Dollar Achivement, You get 3000 Dollars", height = 2, font = "bold", bg = "green")
	A1.pack(side = BOTTOM)
	Budget += 3000
	TotalAmount += 3000
	Window.itemconfig(ShowBudget, text = f'Budget = {Budget}$')	
	Window.after(5000, A1.destroy)

def Achivement6():
	global TotalAmount
	global Budget
	global Window	
	global ShowBudget

	A2 = Label(Window, text = "First 100000 Dollar Achivement, You get 30000 Dollars", height = 2, font = "bold", bg = "green")
	A2.pack(side = BOTTOM)
	Budget += 30000
	TotalAmount += 30000
	Window.itemconfig(ShowBudget, text = f'Budget = {Budget}$')	
	Window.after(5000, A2.destroy)

def Achivement7():
	global TotalAmount
	global Budget
	global Window
	global ShowBudget

	A3 = Label(Window, text = "First 1000000 Dollar Achivement, You get 300000 Dollars", height = 2, font = "bold", bg = "green")
	A3.pack(side = BOTTOM)
	Budget += 300000
	TotalAmount += 300000
	Window.itemconfig(ShowBudget, text = f'Budget = {Budget}$')	
	Window.after(5000, A3.destroy)

def Achivement8():
	global TotalAmount
	global Budget
	global Window
	global ShowBudget

	A4 = Label(Window, text = "First 10000000 Dollar Achivement, You get 3000000 Dollars", height = 2, font = "bold", bg = "green")
	A4.pack(side = BOTTOM)
	Budget += 3000000
	TotalAmount += 3000000
	Window.itemconfig(ShowBudget, text = f'Budget = {Budget}$')	
	Window.after(5000, A4.destroy)

def AutoIncrease():
	"""Increases the Budget and TotalAmount with depending on total adjustment"""
	global Budget
	global TotalAmount
	global Increase
	global Running
	global Window
	global ShowBudget		
	global AchiveRes1
	global AchiveRes2
	
	if Running is True:
		Budget = round(Budget + Increase, 2)
		TotalAmount = round(TotalAmount + Increase, 2)		
		if Budget >= 100 and AchiveRes1 == 0:
			AchiveRes1 += 1
			Achivement1()
		elif Budget >= 1000 and AchiveRes1 == 1:
			AchiveRes1 += 1
			Achivement2()
		elif Budget >= 10000 and AchiveRes1 == 2:
			AchiveRes1 += 1
			Achivement3()
		elif Budget >= 100000 and AchiveRes1 == 3:
			AchiveRes1 += 1
			Achivement4()
		elif TotalAmount >= 10000 and AchiveRes2 == 0:
			AchiveRes2 += 1
			Achivement5()
		elif TotalAmount >= 100000 and AchiveRes2 == 1:
			AchiveRes2 += 1
			Achivement6()
		elif TotalAmount >= 1000000 and AchiveRes2 == 2:
			AchiveRes2 += 1
			Achivement7()
		elif TotalAmount >= 10000000 and AchiveRes2 == 3:
			AchiveRes2 += 1
			Achivement8()
		Window.itemconfig(ShowBudget, text = f'Budget = {Budget}$')	
		Window.after(100, AutoIncrease)

def Click():
	"""Function to be called when the main button is clicked 
	or when the 'space' key is pressed"""
	global TotalAmount
	global Budget
	global Window
	global ShowBudget
	global AchiveRes1
	global AchiveRes2

	TotalAmount += 1
	Budget += 1	
	if Budget >= 100 and AchiveRes1 == 0:
		AchiveRes1 += 1
		Achivement1()
	elif Budget >= 1000 and AchiveRes1 == 1:
		AchiveRes1 += 1
		Achivement2()
	elif Budget >= 10000 and AchiveRes1 == 2:
		AchiveRes1 += 1
		Achivement3()
	elif Budget >= 100000 and AchiveRes1 == 3:
		AchiveRes1 += 1
		Achivement4()
	elif TotalAmount >= 10000 and AchiveRes2 == 0:
		AchiveRes2 += 1
		Achivement5()
	elif TotalAmount >= 100000 and AchiveRes2 == 1:
		AchiveRes2 += 1
		Achivement6()
	elif TotalAmount >= 1000000 and AchiveRes2 == 2:
		AchiveRes2 += 1
		Achivement7()
	elif TotalAmount >= 10000000 and AchiveRes2 == 3:
		AchiveRes2 += 1
		Achivement8()	
	Window.itemconfig(ShowBudget, text = f'Budget = {Budget}$')	

def BuyClicker():
	global Budget
	global Increase
	global Running
	global Window
	global ShowBudget
	global MoneyPerSecond
	price = 50
	adjust = 0.1
	res = 0
	if Increase == 0:
		res = 1 #flag for first enter

	if Budget >= price:
		Budget = round(Budget - price, 2)
		Increase = round(Increase + adjust, 2)
		Window.itemconfig(ShowBudget, text = f'Budget = {Budget}$')
		Window.itemconfig(MoneyPerSecond, text = f'Income = {Increase * 10}$ p.s')
		if res == 1:
			Running = True
			AutoIncrease()

def BuyShop():
	global Budget
	global Increase
	global Running
	global Window
	global ShowBudget
	global MoneyPerSecond
	price = 1000
	adjust = 5
	res = 0
	if Increase == 0:
		res = 1 #flag for first enter

	if Budget >= price:
		Budget = round(Budget - price, 2)
		Increase += adjust
		Window.itemconfig(ShowBudget, text = f'Budget = {Budget}$')	
		Window.itemconfig(MoneyPerSecond, text = f'Income = {Increase * 10}$ p.s')
		if res == 1:
			Running = True
			AutoIncrease()

def BuySuperMarket():
	global Budget
	global Increase
	global Running
	global Window
	global ShowBudget
	global MoneyPerSecond
	price = 5000	
	adjust = 50
	res = 0
	if Increase == 0:
		res = 1 #flag for first enter

	if Budget >= price:
		Budget = round(Budget - price, 2)
		Increase = round(Increase + adjust, 2)
		Window.itemconfig(ShowBudget, text = f'Budget = {Budget}$')
		Window.itemconfig(MoneyPerSecond, text = f'Income = {Increase * 10}$ p.s')
		if res == 1:
			Running = True
			AutoIncrease()
def BuyFactory():
	global Budget
	global Increase
	global Running
	global Window
	global ShowBudget
	global MoneyPerSecond
	price = 10000	
	adjust = 100
	res = 0
	if Increase == 0:
		res = 1 #flag for first enter

	if Budget >= price:
		Budget = round(Budget - price, 2)
		Increase = round(Increase + adjust, 2)
		Window.itemconfig(ShowBudget, text = f'Budget = {Budget}$')
		Window.itemconfig(MoneyPerSecond, text = f'Income = {Increase * 10}$ p.s')
		if res == 1:
			Running = True
			AutoIncrease()

def BuyBank():
	global Budget
	global Increase
	global Running
	global Window
	global ShowBudget
	global MoneyPerSecond
	price = 50000
	adjust = 500
	res = 0
	if Increase == 0:
		res = 1 #flag for first enter

	if Budget >= price:
		Budget = round(Budget - price, 2)
		Increase = round(Increase + adjust, 2)
		Window.itemconfig(ShowBudget, text = f'Budget = {Budget}$')	
		Window.itemconfig(MoneyPerSecond, text = f'Income = {Increase * 10}$ p.s')
		if res == 1:
			Running = True
			AutoIncrease()

def BuyMoneyPrinter():
	global Budget
	global Increase
	global Running
	global Window
	global ShowBudget
	global MoneyPerSecond
	price = 100000	
	adjust = 1000
	res = 0
	if Increase == 0:
		res = 1 #flag for first enter

	if Budget >= price:
		Budget = round(Budget - price, 2)
		Increase = round(Increase + adjust, 2)
		Window.itemconfig(ShowBudget, text = f'Budget = {Budget}$')
		Window.itemconfig(MoneyPerSecond, text = f'Income = {Increase * 10}$ p.s')
		if res == 1:
			Running = True
			AutoIncrease()

def Case1():
	global CaseRes
	global MoneyWad
	global Window
	global C1
	global C2
	if CaseRes == 2:
		MoneyWad.destroy()
	CaseRes = 1
	
	C1.config(state = DISABLED)
	C2.config(state = NORMAL)
	MoneyWad = Window.create_image(1000, 600, image = MoneyBag)
	def set_state(state):
		Window.itemconfigure(MoneyWad, state=state)
	def Appear():
		set_state(HIDDEN)
		Window.after(1, set_state, NORMAL)

	Window.tag_bind(MoneyWad, "<Button-1>", lambda event: (Appear(), Click()))
	root.bind("<space>", lambda event: (Appear(), Click()))

def Case2():
	global CaseRes
	global MoneyWad
	global Window
	global C1
	global C2

	if CaseRes == 1:
		Window.delete(MoneyWad)	
	CaseRes = 2

	C2.config(state = DISABLED)
	C1.config(state = NORMAL)

	ImageWidth = MoneyBag.width()
	ImageHeight = MoneyBag.height()
	MoneyWad = Button(Window, image = MoneyBag, height = ImageHeight, width = ImageWidth, command = Click, borderwidth = 10)
	MoneyWad.place(x = 650, y = 220)
	def Press_button(MoneyWad):
		MoneyWad.config(relief = "sunken")
		root.update_idletasks()
		MoneyWad.invoke()	
		time.sleep(0.1)
		MoneyWad.config(relief = "raised")
	
	root.bind("<space>", lambda event: Press_button(MoneyWad))

CheckVar1 = IntVar()
C1 = Checkbutton(Window, text = 'Clicker Mode - 1', variable = CheckVar1, onvalue = 1, offvalue = 0, width = 15, command = Case1)
C2 = Checkbutton(Window, text = 'Clicker Mode - 2', variable = CheckVar1, onvalue = 0, offvalue = 1, width = 15, command = Case2)
C1.place(x = 0, y = 0)
C2.place(x = 0, y = 38)
C1.invoke()

Menubar = Menu(Window)
Menubar.add_command(label = "New", command = New)
Menubar.add_command(label = "Help", command = Help)
Menubar.add_command(label = "Exit", command = Exit)
root.config(menu = Menubar)

Clicker = Button(Window, text = "Clicker - 50$", command = BuyClicker)
Shop = Button(Window, text = "Shop - 1000$", command = BuyShop) 
SuperMarket = Button(Window, text = "SuperMarket - 5000$", command = BuySuperMarket)
Factory = Button(Window, text = "Factory - 10000$", command = BuyFactory)
Bank = Button(Window, text = "Bank - 50000$", command = BuyBank)
MoneyPrinter = Button(Window, text = "MoneyPrinter - 100000$", command = BuyMoneyPrinter)
Clicker.place(x = 1600, y = 10)
Shop.place(x = 1600, y = 70)
SuperMarket.place(x = 1600, y = 130)
Factory.place(x = 1600, y = 190)
Bank.place(x = 1600, y = 250)
MoneyPrinter.place(x = 1600, y = 310)

root.mainloop()

