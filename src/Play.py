from tkinter import *	
from tkinter import messagebox
from PIL import Image, ImageTk
import time


class CreateGUI(Tk):
	"""Creates the Window, Canvas, added main buttons"""			
	def __init__(self, cls):
		PATH_1 = 'Data/background-3.jpg' # Path of background image in repository
		PATH_2 = 'Data/MoneyBag.png'  # Path of  photo in repository
		WINDOW_WIDTH = 2000 # Window width
		WINDOW_HEIGHT = 1500 # Window height
		CANVAS_WIDTH = 1000 # Canvas width
		CANVAS_HEIGHT = 1000 # Canvas height
		LABEL_POS_X = 1000 # The top label x coordinate on canvas
		LABEL_POS_Y = 35 # The top label y coordinate on canvas
		SHOW_BUDGET_POS_X = 350 # ShowBudget buttons location x coordinate on canvas
		SHOW_BUDGET_POS_Y = 250 # ShowBudget buttons location y coordinate on canvas
		TEXT_FONT= ("helvetica", 20) # The font used for texts showed on canvas
		MONEY_PER_SECOND_POS_X = 350 # MoneyPerSecond buttons location x coordinate on canvas
		MONEY_PER_SECOND_POS_Y = 350 # MoneyPerSecond buttons location y coordinate on canvas

		cls.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}')
		cls.title('Money_Clicker')
		
		cls.window = Canvas(cls, height = CANVAS_HEIGHT, width = CANVAS_WIDTH)
		cls.window.pack(expand = True, fill = "both")
		
		file_bg = Image.open(PATH_1)
		cls.bg = ImageTk.PhotoImage(file_bg)
		cls.window.create_image(0, 0, image = cls.bg, anchor = "nw")
		cls.money_bag = PhotoImage(file = PATH_2)

		cls.window.create_text(
			LABEL_POS_X, LABEL_POS_Y, 
			text = "Welcome To Money Clicker Game", 
			font = TEXT_FONT, fill = "white")

		cls.show_budget = cls.window.create_text(
							  SHOW_BUDGET_POS_X, SHOW_BUDGET_POS_Y, 
							  text = f'Budget = {cls.budget}$', 
							  font = TEXT_FONT, fill = "white")
		cls.money_per_second = cls.window.create_text(
								   MONEY_PER_SECOND_POS_X, 
							 	   MONEY_PER_SECOND_POS_Y, 
							 	   text = f'Income = {cls.increase * 10}$ p.s', 
							 	   font = TEXT_FONT, fill = "white")

class Achivement:
	"""Class of all Achivements in the game"""
	def __init__(
			self, adjustment: int, required_budget: int = 0,  
			required_total_amount: int = 0):

		self.adjustment = adjustment
		self.required_budget = required_budget	
		self.required_total_amount = required_total_amount
	
	def achivement_add(self, cls):
		"""Called when required_budget or required_total_amount are 
		satisfied. Increases budget and total_amount by Object 
		adjustment"""
		TEXT_1 = (f'First {self.required_budget} Dollar Achivement,'
				   f' You get {self.adjustment} Dollars')
		TEXT_2 = (f'Total Money Amount {self.required_total_amount} Dollar Achivement,' 
				   f' You get {self.adjustment} Dollars')
		LABEL_HEIGHT = 2
		DESTROY_DELAY = 5000

		if self.required_total_amount == 0:
			achive_label = Label(
							   cls.window, text = TEXT_1,
							   height = LABEL_HEIGHT, font = "bold", 
							   bg = "green")
		elif self.required_budget == 0:
			achive_label = Label(
							   cls.window, text = TEXT_2,
							   height = LABEL_HEIGHT, font = "bold",
							   bg = "green")
		else:
			raise Exception("Wrong Class Creation") 
			
		achive_label.pack(side = BOTTOM)
		cls.budget += self.adjustment
		cls.total_amount += self.adjustment
		cls.window.itemconfig(cls.show_budget, text = f'Budget = {cls.budget}$')	
		cls.window.after(DESTROY_DELAY, achive_label.destroy)
	
	@classmethod
	def create_achivements(cls, clicker): #clicker is for ClickerGame object
		"""Creating Achivement object for further using"""
		MIN_ADJUST_1 = 5
		MIN_ADJUST_2 = 300
		MIN_BUDGET = 10
		MIN_TOTAL_AMOUNT = 1000
		MULT_INCREASE = 10
		
		clicker.budget_achive_num = 4
		clicker.amount_achive_num = 4
		clicker.achivement_arr = []
		mult_1 = 10
		mult_2 = 10
 
		for i in range(clicker.budget_achive_num + clicker.amount_achive_num):
			if i <= clicker.budget_achive_num - 1:
				achive_budget = MIN_BUDGET * mult_1
				achive_adjust = MIN_ADJUST_1 * mult_1
				mult_1 *= MULT_INCREASE
				clicker.achivement_arr.append(
					Achivement(achive_adjust, achive_budget))		
			else:
				achive_total_amount = MIN_TOTAL_AMOUNT * mult_2
				achive_adjust = MIN_ADJUST_2 * mult_2
				mult_2 *= MULT_INCREASE	
				clicker.achivement_arr.append(
					Achivement(achive_adjust, 0, achive_total_amount))

	@classmethod
	def check_achivement(cls, clicker): #clicker again is for ClickerGame object
		'''Checks for Achviement requirements and if they are statisfied
		increases the budget and total_amount'''
		for i in range(clicker.budget_achive_num):
			if (clicker.budget >= clicker.achivement_arr[i].required_budget and
				clicker.achive_res_1 == i):
					clicker.achive_res_1 += 1
					clicker.achivement_arr[i].achivement_add(clicker)
		for i in range(clicker.budget_achive_num, 
					   clicker.amount_achive_num + clicker.budget_achive_num):
			index = i - clicker.budget_achive_num
			if (clicker.total_amount >= clicker.achivement_arr[i].required_total_amount 
					and clicker.achive_res_2 == index):
				clicker.achive_res_2 += 1
				clicker.achivement_arr[i].achivement_add(clicker)


class Property:
	"""Class of all AutoClickers"""
	def __init__(self, price: int, adjust: int):
		self.price = price
		self.adjust = adjust

	def buy_property(self, cls):
		"""Get one more AutoClicker"""
		res = 0

		if cls.increase == 0:
			res = 1 #flag for first enter

		if cls.budget >= self.price:
			cls.budget = round(cls.budget - self.price, 2)
			cls.increase = round(cls.increase + self.adjust, 2)
			cls.window.itemconfig(cls.show_budget, text = f'Budget = {cls.budget}$')
			cls.window.itemconfig(
				cls.money_per_second, 
				text = f'Income = {cls.increase * 10}$ p.s')
			if res == 1:
				cls.running = True
				cls.auto_increase()

	@classmethod
	def create_property(cls, clicker): #clicker is for ClickerGame object
		"""Creating Property object for further using"""	
		properties = {50: 0.1, 1000: 2, 5000: 10, 10000: 20, 50000: 100, 100000: 200}
		clicker.propertie_names = [
			"Clicker", "Shop", "SuperMarket", 
			"Factory", "Bank", "MoneyPrinter"]
		clicker.property_num = 6
		clicker.property_arr = []
		price_list = list(properties.keys())
		adjust_list = list(properties.values())

		for i in range(clicker.property_num):
			clicker.property_arr.append(Property(price_list[i], adjust_list[i]))


class ClickerGame(Tk):
	"""Class that contains the whole game logic"""
	def __init__(self):
		"""Class Constructor where all the variables are defined
		and all class methods are called"""
		super().__init__()
		
		self.total_amount = 0.0 # Total Money Amount 
		self.budget = 0.0 # Current Money Amount
		self.increase = 0.0 # Money Increase in 100 milliseconds 
		self.running = False
		self.achive_res_1 = 0 # Flag for first 4 achivements to occur only once
		self.achive_res_2 = 0 # Flag for 5 - 8 achivements to occur only once
		self.case_res = 0 # Flag for Clicker Mode to delete
	
		self.start_game()
	
	def start_game(self):
		"""Calls all the ClickerGame methods that run
		the game, which includes creating Window,
		Canvas, placing all buttons on them and so on"""	
		CreateGUI(self)
		self.create_menubar()
		Property.create_property(self)
		self.add_buttons()
		Achivement.create_achivements(self)
		self.change_view()

	def new(self):
		"""Restarts the Game, which means that it nullifies 
		budget, total_amount, increase, return c1 button to 
		starting possition and disables auto_increase function"""
		begin = messagebox.askquestion('New Game', 'Start Again?', icon = 'question')
		if begin == "yes":
			self.running = False
			self.total_amount = 0.0
			self.budget = 0.0
			self.increase = 0.0
			self.achive_res_1 = 0
			self.achive_res_2 = 0
			self.window.itemconfig(self.show_budget, text = f'Budget = {self.budget}$')	
			self.window.itemconfig(
				self.money_per_second, 
				text = f'Income = {self.increase * 10}$ p.s')
			self.c1.invoke()

	def help(self):
		"""Creating Achivement object for further using"""
		SYM_HEIGHT = 33
		SYM_WIDTH = 33
		FAQ_HEIGHT = 300
		FAQ_WIDTH = 800
		CLOSE_POS_X = 340
		CLOSE_POS_Y = 170
		CLOSE_HEIGHT = 1
		CLOSE_WIDTH = 5
		TEXT_INSERT = ("  It is a Clicker game, Player should Click on Money Bag"
					   " Using Cursor or by Pressing the Space Button to Get Money."
					   " Player can buy Clickers, Factories, Shops, SuperMarkets," 
					   " Factories and MoneyPrinters to Gain money automatically.")

		faq = Toplevel()
		faq.geometry(f'{FAQ_WIDTH}x{FAQ_HEIGHT}')
		faq.title("Help")

		info = Text(faq)
		sym = Label(
				  info, text = "info", bitmap = "info", 
				  height = SYM_HEIGHT, width = SYM_WIDTH)
		sym.place(x = 0, y = 0)
		info.insert(INSERT, TEXT_INSERT)
		info.config(state = DISABLED)
		info.pack()

		close_button = Button(
						   info, text = "Close", command = faq.destroy, 
						   height = CLOSE_HEIGHT, width = CLOSE_WIDTH, cursor = "arrow")
		close_button.place(x = CLOSE_POS_X, y = CLOSE_POS_Y)	
		faq.bind("<Return>", lambda event: close_button.invoke())
		faq.mainloop()	

	def exit(self):
		"""Creating Achivement object for further using"""
		quit = messagebox.askquestion('Exit Game', 'Quit?', icon = 'question')
		if quit == "yes":
			self.running = False
			self.window.destroy()
			self.destroy()

	def auto_increase(self):
		"""Increases the budget and total_amount depending on total increase"""
		ACTIVATION_DELAY = 100

		if self.running is True:
			self.budget = round(self.budget + self.increase, 2)
			self.total_amount = round(self.total_amount + self.increase, 2)
			Achivement.check_achivement(self)	
			self.window.itemconfig(self.show_budget, text = f'Budget = {self.budget}$')	
			self.window.after(ACTIVATION_DELAY, self.auto_increase)

	def click(self):
		"""Function that is called when the MoneyWad button is clicked 
		or when the 'space' key is pressed. Its increasing the
		budget and total_amount by 1"""
		CLICK_INCREASE = 1
		self.total_amount += CLICK_INCREASE 
		self.budget += CLICK_INCREASE	
		Achivement.check_achivement(self)
		self.window.itemconfig(self.show_budget, text = f'Budget = {self.budget}$')	

	def button_config_1(self):
		"""Function to be called when c1 button is pressed
		that changes the MoneyWad button style and way that it
		is working"""
		MONEY_WAD_HEIGHT = 600
		MONEY_WAD_WIDTH = 1000	
	
		if self.case_res == 2:
			self.money_wad.destroy()
		self.case_res = 1
	
		self.c1.config(state = DISABLED)
		self.c2.config(state = NORMAL)
		self.money_wad = self.window.create_image(
							 MONEY_WAD_WIDTH, MONEY_WAD_HEIGHT, 
							 image = self.money_bag)
		def set_state(state):
			"""Changes money_wad button state to given one"""
			self.window.itemconfigure(self.money_wad, state = state)
		def appear():
			"""Function called when MoneyWad button is pressed
			that make button to disappear and appear in given time"""
			ACTIVATION_DELAY = 1
			set_state(HIDDEN)
			self.window.after(ACTIVATION_DELAY, set_state, NORMAL)

		self.window.tag_bind(
			self.money_wad, "<Button-1>", 
			lambda event: (appear(), self.click()))
		self.bind("<space>", lambda event: (appear(), self.click()))

	def button_config_2(self):
		""" Function that is called when c2 button is pressed
		that changes the MoneyWad button style and way of it
		is working"""
		BORDER_SIZE = 10
		MONEY_WAD_POS_X = 650
		MONEY_WAD_POS_Y = 220

		if self.case_res == 1:
			self.window.delete(self.money_wad)	
		self.case_res = 2

		self.c2.config(state = DISABLED)
		self.c1.config(state = NORMAL)

		image_width = self.money_bag.width()
		image_height = self.money_bag.height()
		self.money_wad = Button(
							 self.window, image = self.money_bag, 
							 height = image_height, width = image_width, 
							 command = self.click, borderwidth = BORDER_SIZE)
		self.money_wad.place(x = MONEY_WAD_POS_X, y = MONEY_WAD_POS_Y)

		def press_button(money_wad):
			"""Function that imitates the way the Tkinter button motion 
			when user click on it"""	
			DELAY = 0.1	

			money_wad.config(relief = "sunken")
			self.update_idletasks()
			money_wad.invoke()	
			time.sleep(DELAY)
			money_wad.config(relief = "raised")

	 	#Enable pressing MoneyBag button with "space" key
		self.bind("<space>", lambda event: press_button(self.money_wad))

	def change_view(self):
		"""Creates Checkbuttons for switching money_wad
		Button style"""
		C1_WIDTH = 15
		C2_WIDTH = 15
		C1_POS_X = 0
		C1_POS_Y = 0
		C2_POS_X = 0
		C2_POS_Y = 38

		check_var_1 = IntVar()
		self.c1 = Checkbutton(
					  self.window, text = 'Clicker Mode - 1', 
					  variable = check_var_1, onvalue = 1, offvalue = 0,
					  width = C1_WIDTH, command = self.button_config_1)
		self.c2 = Checkbutton(
					  self.window, text = 'Clicker Mode - 2', 
					  variable = check_var_1, onvalue = 0, offvalue = 1, 
					  width = C2_WIDTH, command = self.button_config_2)
		self.c1.place(x = C1_POS_X, y = C1_POS_Y)
		self.c2.place(x = C2_POS_X, y = C2_POS_Y)
		self.c1.invoke()

	def create_menubar(self):
		"""Creates MenuBar on top of the Window"""
		menubar = Menu(self.window)
		menubar.add_command(label = "New", command = self.new)
		menubar.add_command(label = "Help", command = self.help)
		menubar.add_command(label = "Exit", command = self.exit)
		self.config(menu = menubar)

	def add_buttons(self):
		"""Creates Buttons for Buying Property"""
		PROPERTIE_POS_X = 1600
		PROPERTIE_MIN_POS_Y = 10
		POS_Y_ADJUST = 60
		property_buttons = []
		res_adjust = 0	

		for i in range(self.property_num):
			res_button = Button(
							 self.window, 
							 text = f'{self.propertie_names[i]} - {self.property_arr[i].price}$',
							 command = lambda j = i: self.property_arr[j].buy_property(self))
			property_buttons.append(res_button)

		for i in range(self.property_num):
			pos_y = PROPERTIE_MIN_POS_Y + res_adjust
			property_buttons[i].place(x = PROPERTIE_POS_X, y = pos_y)
			res_adjust += POS_Y_ADJUST

	
if __name__ == "__main__":
	app = ClickerGame()
	app.mainloop()

