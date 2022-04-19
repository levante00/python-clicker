from tkinter import *
from tkinter import messagebox
from Globals import Globals
from PIL import Image, ImageTk
import time

TotalAmount = Globals.TotalAmount  
Budget = Globals.Budget
Increase = Globals.Increase 
Running = Globals.Running
Path1 = Globals.Path1
Path2 = Globals.Path2
AchiveRes1 = Globals.AchiveRes1
AchiveRes2 = Globals.AchiveRes2
CaseRes = Globals.CaseRes

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

class Achivement:
	"""Class of all Achivements in the game"""
	def __init__(self, Adjustment: int, Required_Budget: int = 0,  Required_TotalAmount: int = 0):
		self.Adjustment = Adjustment
		self.Required_Budget = Required_Budget	
		self.Required_TotalAmount = Required_TotalAmount
	
	def Add(self):
		"""Called when Required_Budget or Required_TotalAmount are 
		satisfied. Increases Budget and TotalAmount by Object 
		Adjustment"""
		global Budget
		global TotalAmount

		if self.Required_TotalAmount == 0:
			A = Label(Window, text = f'First {self.Required_Budget} Dollar Achivement, You get {self.Adjustment} Dollars', height = 2, font = "bold", bg = "green")
		elif self.Required_Budget == 0:
			A = Label(Window, text = f'Total Money Amount {self.Required_TotalAmount} Dollar Achivement, You get {self.Adjustment} Dollars', height = 2, font = "bold", bg = "green")
		else:
			raise Exeption("Wrong Class Creation") 
			
		A.pack(side = BOTTOM)
		Budget += self.Adjustment
		TotalAmount += self.Adjustment
		Window.itemconfig(ShowBudget, text = f'Budget = {Budget}$')	
		Window.after(5000, A.destroy)
	
Achivement1 = Achivement(50, 100)
Achivement2 = Achivement(500, 1000)
Achivement3 = Achivement(5000, 10000)
Achivement4 = Achivement(50000, 100000)
Achivement5 = Achivement(3000, 0 ,10000)
Achivement6 = Achivement(30000, 0, 100000)
Achivement7 = Achivement(300000, 0 ,1000000)
Achivement8 = Achivement(3000000, 0 ,10000000)

class Property:
	"""Class of all AutoClickers"""
	def __init__(self, Price: int, Adjust: int):
		self.Price = Price
		self.Adjust = Adjust
	
	def Buy(self):
		"""Buy AutoClicker"""
		global Budget
		global Running
		global Increase
		res = 0
		if Increase == 0:
			res = 1 #flag for first enter

		if Budget >= self.Price:
			Budget = round(Budget - self.Price, 2)
			Increase = round(Increase + self.Adjust, 2)
			Window.itemconfig(ShowBudget, text = f'Budget = {Budget}$')
			Window.itemconfig(MoneyPerSecond, text = f'Income = {Increase * 10}$ p.s')
			if res == 1:
				Running = True
				AutoIncrease()
	
Clicker = Property(50, 0.1)
Shop = Property(1000, 5)
SuperMarket = Property(5000, 50)
Factory = Property(10000, 100)
Bank = Property(50000, 500)
MoneyPrinter = Property(100000, 1000)
	
def New():
	"""Restarts the Game, which means that it nullifies 
	Budget, TotalAmount, Increase, return C1 button to 
	starting possition and disables AutoIncrease function"""
	global TotalAmount
	global Budget
	global Increase
	global Running

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
	global Running
	Quit = messagebox.askquestion('Exit Game', 'Quit?', icon = 'question')
	if Quit == "yes":
		Running = False
		Window.destroy()
		root.destroy()

def CheckAchivement():
	"""Checks for Achviement Requirements and if they are statisfied
	increases the Budget and TotalAmount """
	global Budget
	global AchiveRes1
	global AchiveRes2
	global TotalAmount

	if Budget >= Achivement1.Required_Budget and AchiveRes1 == 0:
		AchiveRes1 += 1
		Achivement1.Add()
	elif Budget >= Achivement2.Required_Budget and AchiveRes1 == 1:
		AchiveRes1 += 1
		Achivement2.Add()
	if Budget >= Achivement3.Required_Budget and AchiveRes1 == 2:
		AchiveRes1 += 1
		Achivement3.Add()
	elif Budget >= Achivement4.Required_Budget and AchiveRes1 == 3:
		AchiveRes1 += 1
		Achivement4.Add()
	elif TotalAmount >= Achivement5.Required_TotalAmount and AchiveRes2 == 0:
		AchiveRes2 += 1
		Achivement5.Add()
	elif TotalAmount >= Achivement6.Required_TotalAmount and AchiveRes2 == 1:
		AchiveRes2 += 1
		Achivement6.Add()
	elif TotalAmount >= Achivement7.Required_TotalAmount and AchiveRes2 == 2:
		AchiveRes2 += 1
		Achivement7.Add()
	elif TotalAmount >= Achivement8.Required_TotalAmount and AchiveRes2 == 3:
		AchiveRes2 += 1
		Achivement8.Add()

def AutoIncrease():
	"""Increases the Budget and TotalAmount depending on total Increase"""
	global Budget
	global TotalAmount
	global Increase
	global Running

	if Running is True:
		Budget = round(Budget + Increase, 2)
		TotalAmount = round(TotalAmount + Increase, 2)
		CheckAchivement()	
		Window.itemconfig(ShowBudget, text = f'Budget = {Budget}$')	
		Window.after(100, AutoIncrease)

def Click():
	"""Function that is called when the MoneyWad button is clicked 
	or when the 'space' key is pressed. Its increasing the
	Budget and TotalAmount by 1"""
	global TotalAmount
	global Budget
	global AchiveRes1
	global AchiveRes2

	TotalAmount += 1
	Budget += 1	
	CheckAchivement()
	Window.itemconfig(ShowBudget, text = f'Budget = {Budget}$')	

def Case1():
	""" Function to be called when C1 button is pressed
	that changes the MoneyWad button style and way that it
	is working"""
	global CaseRes
	global MoneyWad
	if CaseRes == 2:
		MoneyWad.destroy()
	CaseRes = 1
	
	C1.config(state = DISABLED)
	C2.config(state = NORMAL)
	MoneyWad = Window.create_image(1000, 600, image = MoneyBag)
	def set_state(state):
		"""Changes MoneyWad button state to given one"""
		Window.itemconfigure(MoneyWad, state=state)
	def Appear():
		"""Function called when MoneyWad button is pressed
		that make button to disappear and appear in given time"""
		set_state(HIDDEN)
		Window.after(1, set_state, NORMAL)

	Window.tag_bind(MoneyWad, "<Button-1>", lambda event: (Appear(), Click()))
	root.bind("<space>", lambda event: (Appear(), Click()))

def Case2():
	""" Function that is called when C2 button is pressed
	that changes the MoneyWad button style and way of it
	is working"""
	global CaseRes
	global MoneyWad

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
		"""Function that imitates the way the Tkinter button motion 
		when user click on it"""
		MoneyWad.config(relief = "sunken")
		root.update_idletasks()
		MoneyWad.invoke()	
		time.sleep(0.1)
		MoneyWad.config(relief = "raised")
	
	root.bind("<space>", lambda event: Press_button(MoneyWad)) #Enable pressing MoneyBag button with "space" key

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

Clicker_Button = Button(Window, text = "Clicker - 50$", command = Clicker.Buy)
Shop_Button = Button(Window, text = "Shop - 1000$", command = Shop.Buy) 
SuperMarket_Button = Button(Window, text = "SuperMarket - 5000$", command = SuperMarket.Buy)
Factory_Button = Button(Window, text = "Factory - 10000$", command = Factory.Buy)
Bank_Button = Button(Window, text = "Bank - 50000$", command = Bank.Buy)
MoneyPrinter_Button = Button(Window, text = "MoneyPrinter - 100000$", command = MoneyPrinter.Buy)
Clicker_Button.place(x = 1600, y = 10)
Shop_Button.place(x = 1600, y = 70)
SuperMarket_Button.place(x = 1600, y = 130)
Factory_Button.place(x = 1600, y = 190)
Bank_Button.place(x = 1600, y = 250)
MoneyPrinter_Button.place(x = 1600, y = 310)

root.mainloop()

