from tkinter import *	
from tkinter import messagebox
from Globals import Globals
from PIL import Image, ImageTk
import time

class ClickerGame(Tk):
	"""Class that contains the whole program"""
	def __init__(self):
		"""Class Constructor where all the variables are defined
		and all class methods are called"""
		super().__init__()
		
		self.TotalAmount = 0.0 # Total Money Amount 
		self.Budget = 0.0 # Current Money Amount
		self.Increase = 0.0 # Money Increase in 100 milliseconds 
		self.Running = False
		self.AchiveRes1 = 0 # Flag for first 4 achivements to occur only once
		self.AchiveRes2 = 0 # Flag for 5 - 8 achivements to occur only once
		self.CaseRes = 0 # Flag for Clicker Mode to delete
	
		self.StartGame()
	
	def CreateGUI(self):
		"""Creates the Window, Canvas, added main buttons"""			
		Path1 = 'Data/background-3.jpg' # Path of background image in repository
		Path2 = 'Data/MoneyBag.png'  # Path of  photo in repository
		WindowWidth = 2000 # Window width
		WindowHeight = 1500 # Window height
		CanvasWidth = 1000 # Canvas width
		CanvasHeight = 1000 # Canvas height
		LabelPosX = 1000 # The top label x coordinate on canvas
		LabelPosY = 35 # The top label y coordinate on canvas
		ShowBudgetPosX = 350 # ShowBudget buttons location x coordinate on canvas
		ShowBudgetPosY = 250 # ShowBudget buttons location y coordinate on canvas
		TextFont= ("helvetica", 20) # The font used for texts showed on canvas
		MoneyPerSecondPosX = 350 # MoneyPerSecond buttons location x coordinate on canvas
		MoneyPerSecondPosY = 350 # MoneyPerSecond buttons location y coordinate on canvas

		self.geometry(f'{WindowWidth}x{WindowHeight}')
		self.title('Money_Clicker')
		
		self.Window = Canvas(self, height = CanvasHeight, width = CanvasWidth)
		self.Window.pack(expand = True, fill = "both")
		
		fileBG = Image.open(Path1)
		self.BG = ImageTk.PhotoImage(fileBG)
		self.Window.create_image(0, 0, image = self.BG, anchor = "nw")
		self.MoneyBag = PhotoImage(file = Path2)

		self.Window.create_text(LabelPosX, LabelPosY, text = "Welcome To Money Clicker Game", font = TextFont, fill = "white")
		self.ShowBudget = self.Window.create_text(ShowBudgetPosX, ShowBudgetPosY, text = f'Budget = {self.Budget}$', font = TextFont, fill = "white")
		self.MoneyPerSecond = self.Window.create_text(MoneyPerSecondPosX, MoneyPerSecondPosY, text = f'Income = {self.Increase * 10}$ p.s', font = TextFont, fill = "white")

	def StartGame(self):
		"""Calls all the ClickerGame methods that run
		the game, which includes creating Window,
		Canvas, placing all buttons on them and so on"""	
		self.CreateGUI()
		self.CreateMenuBar()
		self.CreateProperty()
		self.AddButtons()
		self.CreateAchivements()
		self.ChangeView()

	class Achivement:
		"""Class of all Achivements in the game"""
		def __init__(self, Adjustment: int, Required_Budget: int = 0,  Required_TotalAmount: int = 0):
			self.Adjustment = Adjustment
			self.Required_Budget = Required_Budget	
			self.Required_TotalAmount = Required_TotalAmount
	
	def AchivementAdd(self, Achive):
		"""Called when Required_Budget or Required_TotalAmount are 
		satisfied. Increases Budget and TotalAmount by Object 
		Adjustment"""
		LabelHeight = 2
		DestroyDelay = 5000

		if Achive.Required_TotalAmount == 0:
			A = Label(self.Window, text = f'First {Achive.Required_Budget} Dollar Achivement, You get {Achive.Adjustment} Dollars', height = LabelHeight, font = "bold", bg = "green")
		elif Achive.Required_Budget == 0:
			A = Label(self.Window, text = f'Total Money Amount {Achive.Required_TotalAmount} Dollar Achivement, You get {Achive.Adjustment} Dollars', height = LabelHeight, font = "bold", bg = "green")
		else:
			raise Exeption("Wrong Class Creation") 
			
		A.pack(side = BOTTOM)
		self.Budget += Achive.Adjustment
		self.TotalAmount += Achive.Adjustment
		self.Window.itemconfig(self.ShowBudget, text = f'Budget = {self.Budget}$')	
		self.Window.after(DestroyDelay, A.destroy)
	
	def CreateAchivements(self):	
		"""Creating Achivement object for further using"""
		self.BudgetAchiveNum = 4
		self.AmountAchiveNum = 4
		self.AchivementArr = []
		MinAdjust1 = 5
		MinAdjust2 = 300
		MinBudget = 10
		MinTotalAmount = 1000
		MultIncrease = 10
		Mult1 = 10
		Mult2 = 10
 
		for i in range(self.BudgetAchiveNum + self.AmountAchiveNum):
			if i <= self.BudgetAchiveNum - 1:
				AchiveBudget = MinBudget * Mult1
				AchiveAdjust = MinAdjust1 * Mult1
				Mult1 *= MultIncrease
				self.AchivementArr.append(self.Achivement(AchiveAdjust, AchiveBudget))		
			else:
				AchiveTotalAmount = MinTotalAmount * Mult2
				AchiveAdjust = MinAdjust2 * Mult2
				Mult2 *= MultIncrease	
				self.AchivementArr.append(self.Achivement(AchiveAdjust, 0, AchiveTotalAmount))

	class Property:
		"""Class of all AutoClickers"""
		def __init__(self, Price: int, Adjust: int):
			self.Price = Price
			self.Adjust = Adjust

	def BuyProperty(self, Proper):
		"""Get one more AutoClicker"""
		res = 0
		if self.Increase == 0:
			res = 1 #flag for first enter

		if self.Budget >= Proper.Price:
			self.Budget = round(self.Budget - Proper.Price, 2)
			self.Increase = round(self.Increase + Proper.Adjust, 2)
			self.Window.itemconfig(self.ShowBudget, text = f'Budget = {self.Budget}$')
			self.Window.itemconfig(self.MoneyPerSecond, text = f'Income = {self.Increase * 10}$ p.s')
			if res == 1:
				self.Running = True
				self.AutoIncrease()

	def CreateProperty(self):
		"""Creating Property object for further using"""	
		Properties = {50: 0.1, 1000: 2, 5000: 10, 10000: 20, 50000: 100, 100000: 200}
		self.PropertieNames = ["Clicker", "Shop", "SuperMarket", "Factory", "Bank", "MoneyPrinter"]
		self.PropertyNum = 6
		self.PropertyArr = []
		price_list = list(Properties.keys())
		adjust_list = list(Properties.values())

		for i in range(self.PropertyNum):
			self.PropertyArr.append(self.Property(price_list[i], adjust_list[i]))

	def New(self):
		"""Restarts the Game, which means that it nullifies 
		Budget, TotalAmount, Increase, return C1 button to 
		starting possition and disables AutoIncrease function"""
		Begin = messagebox.askquestion('New Game', 'Start Again?', icon = 'question')
		if Begin == "yes":
			self.Running = False
			self.TotalAmount = 0.0
			self.Budget = 0.0
			self.Increase = 0.0
			self.Window.itemconfig(self.ShowBudget, text = f'Budget = {self.Budget}$')	
			self.Window.itemconfig(self.MoneyPerSecond, text = f'Income = {self.Increase * 10}$ p.s')
			self.C1.invoke()

	def Help(self):
		"""Creating Achivement object for further using"""
		SymHeight = 33
		SymWidth = 33
		FAQHeight = 300
		FAQWidth = 800
		ClosePosX = 340
		ClosePosY = 170
		CloseHeight = 1
		CloseWidth = 5

		FAQ = Toplevel()
		FAQ.geometry(f'{FAQWidth}x{FAQHeight}')
		FAQ.title("Help")

		Info = Text(FAQ)
		Sym = Label(Info, text = "info", bitmap = "info", height = SymHeight, width = SymWidth)
		Sym.place(x = 0, y = 0)
		Info.insert(INSERT, "  It is a Clicker game, Player should Click on Money Bag Using Cursor or by Pressing the Space Button to Get Money. Player can buy Clickers, Factories, Shops, SuperMarkets, Factories and MoneyPrinters to Gain money automatically.")
		Info.config(state = DISABLED)
		Info.pack()

		CloseButton = Button(Info, text = "Close", command = FAQ.destroy, height = CloseHeight, width = CloseWidth, cursor = "arrow")
		CloseButton.place(x = ClosePosX, y = ClosePosY)	
		FAQ.bind("<Return>", lambda event: CloseButton.invoke())
		FAQ.mainloop()	

	def Exit(self):
		"""Creating Achivement object for further using"""
		Quit = messagebox.askquestion('Exit Game', 'Quit?', icon = 'question')
		if Quit == "yes":
			self.Running = False
			self.Window.destroy()
			self.destroy()

	def CheckAchivement(self):
		"""Checks for Achviement Requirements and if they are statisfied
		increases the Budget and TotalAmount"""
		for i in range(self.BudgetAchiveNum + self.AmountAchiveNum):
			if i <= self.BudgetAchiveNum - 1:
				if self.Budget >= self.AchivementArr[i].Required_Budget and self.AchiveRes1 == i:
					self.AchiveRes1 += 1
					self.AchivementAdd(self.AchivementArr[i])
			else:
				if self.TotalAmount >= self.AchivementArr[i].Required_TotalAmount and self.AchiveRes2 == i:
					self.AchiveRes2 += 1
					self.AchivementAdd(self.AchivementArr[i])

	def AutoIncrease(self):
		"""Increases the Budget and TotalAmount depending on total Increase"""
		ActivationDelay = 100

		if self.Running is True:
			self.Budget = round(self.Budget + self.Increase, 2)
			self.TotalAmount = round(self.TotalAmount + self.Increase, 2)
			self.CheckAchivement()	
			self.Window.itemconfig(self.ShowBudget, text = f'Budget = {self.Budget}$')	
			self.Window.after(ActivationDelay, self.AutoIncrease)

	def Click(self):
		"""Function that is called when the MoneyWad button is clicked 
		or when the 'space' key is pressed. Its increasing the
		Budget and TotalAmount by 1"""
		self.TotalAmount += 1
		self.Budget += 1	
		self.CheckAchivement()
		self.Window.itemconfig(self.ShowBudget, text = f'Budget = {self.Budget}$')	

	def Case1(self):
		"""Function to be called when C1 button is pressed
		that changes the MoneyWad button style and way that it
		is working"""
		MoneyWadHeight = 600
		MoneyWadWidth = 1000	
	
		if self.CaseRes == 2:
			self.MoneyWad.destroy()
		self.CaseRes = 1
	
		self.C1.config(state = DISABLED)
		self.C2.config(state = NORMAL)
		self.MoneyWad = self.Window.create_image(MoneyWadWidth, MoneyWadHeight, image = self.MoneyBag)
		def set_state(state):
			"""Changes MoneyWad button state to given one"""
			self.Window.itemconfigure(self.MoneyWad, state=state)
		def Appear():
			"""Function called when MoneyWad button is pressed
			that make button to disappear and appear in given time"""
			ActivationDelay = 1
			set_state(HIDDEN)
			self.Window.after(1, set_state, NORMAL)

		self.Window.tag_bind(self.MoneyWad, "<Button-1>", lambda event: (Appear(), self.Click()))
		self.bind("<space>", lambda event: (Appear(), self.Click()))

	def Case2(self):
		""" Function that is called when C2 button is pressed
		that changes the MoneyWad button style and way of it
		is working"""
		BorderSize = 10
		MoneyWadPosX = 650
		MoneyWadPosY = 220

		if self.CaseRes == 1:
			self.Window.delete(self.MoneyWad)	
		self.CaseRes = 2

		self.C2.config(state = DISABLED)
		self.C1.config(state = NORMAL)

		ImageWidth = self.MoneyBag.width()
		ImageHeight = self.MoneyBag.height()
		self.MoneyWad = Button(self.Window, image = self.MoneyBag, height = ImageHeight, width = ImageWidth, command = self.Click, borderwidth = BorderSize)
		self.MoneyWad.place(x = MoneyWadPosX, y = MoneyWadPosY)

		def Press_button(MoneyWad):
			"""Function that imitates the way the Tkinter button motion 
			when user click on it"""	
			Delay = 0.1	

			MoneyWad.config(relief = "sunken")
			self.update_idletasks()
			MoneyWad.invoke()	
			time.sleep(Delay)
			MoneyWad.config(relief = "raised")
	
		self.bind("<space>", lambda event: Press_button(self.MoneyWad)) #Enable pressing MoneyBag button with "space" key

	def ChangeView(self):
		"""Creates Checkbuttons for switching between MneyWad
		Button style"""
		C1Width = 15
		C2Width = 15
		C1PosX = 0
		C1PosY = 0
		C2PosX = 0
		C2PosY = 38

		CheckVar1 = IntVar()
		self.C1 = Checkbutton(self.Window, text = 'Clicker Mode - 1', variable = CheckVar1, onvalue = 1, offvalue = 0, width = C1Width, command = self.Case1)
		self.C2 = Checkbutton(self.Window, text = 'Clicker Mode - 2', variable = CheckVar1, onvalue = 0, offvalue = 1, width = C2Width, command = self.Case2)
		self.C1.place(x = C1PosX, y = C1PosY)
		self.C2.place(x = C2PosX, y = C2PosY)
		self.C1.invoke()

	def CreateMenuBar(self):
		"""Creates MenuBar on top of the Window"""
		Menubar = Menu(self.Window)
		Menubar.add_command(label = "New", command = self.New)
		Menubar.add_command(label = "Help", command = self.Help)
		Menubar.add_command(label = "Exit", command = self.Exit)
		self.config(menu = Menubar)

	def AddButtons(self):
		"""Creates Buttons for Buying Property"""
		PropertiePosX = 1600
		PropertieMinPosY = 10
		YPosAdjust = 60
		PropertyButtons = []
		ResAdjust = 0	

		for i in range(self.PropertyNum):
			ResButton = Button(self.Window, text = f'{self.PropertieNames[i]} - {self.PropertyArr[i].Price}$', command = lambda j = i: self.BuyProperty(self.PropertyArr[j]))
			PropertyButtons.append(ResButton)

		for i in range(self.PropertyNum):
			PosY = PropertieMinPosY + ResAdjust
			PropertyButtons[i].place(x = PropertiePosX, y = PosY)
			ResAdjust += YPosAdjust

	
if __name__ == "__main__":
	app = ClickerGame()
	app.mainloop()

