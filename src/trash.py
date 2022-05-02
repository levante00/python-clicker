#Changing image size when mouse is on it
"""
def ChangeSize(button: Button, current_width, current_height):
    button.bind("<Enter>", func = lambda e: button.config(width = current_width, height = current_height))
    button.bind("<Leave>", func = lambda e: button.config(width = current_width, height = current_height))
"""

#def Help() another interpretation
"""
   #messagebox.showinfo("Information", "It is a Clicker game, Player should Click on Money Wad Using Cursor or by Pressing the Space Button to Get Money\n Player can buy Clickers, Factories, Shops, Bussinesses and another things to Gain money automatically") 
"""

#ShowBudget Using Label instead of Canvas.text_create
"""
ShowBudget = Label(Window, text = f'{Budget}$', )
ShowBudget.place(x = 10, y = 100)
ShowBudget.config(text = f'{Budget}$')
"""

#Achivement System Without Classes
'''
def Achivement1():
    global TotalAmount
    global Budget
    global Window
    global ShowBudget

    A1 = Label(Window, text = "First 100 Dollar Achivement, You get 50 Dollars", height = 2, font = "bold", bg = "green")
    A1.pack(side = BOTTOM)
    Budget += 50
    TotalAmount += 50
    Window.itemconfig(ShowBudget, text = f"Budget = {Budget}$") 
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
    Window.itemconfig(ShowBudget, text = f"Budget = {Budget}$") 
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
    Window.itemconfig(ShowBudget, text = f"Budget = {Budget}$") 
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
    Window.itemconfig(ShowBudget, text = f"Budget = {Budget}$") 
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
    Window.itemconfig(ShowBudget, text = f"Budget = {Budget}$") 
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
    Window.itemconfig(ShowBudget, text = f"Budget = {Budget}$") 
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
    Window.itemconfig(ShowBudget, text = f"Budget = {Budget}$") 
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
    Window.itemconfig(ShowBudget, text = f"Budget = {Budget}$") 
    Window.after(5000, A4.destroy)
'''


#Properties Buy Without Classes
"""
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
"""

#Using Threades in Program
"""
from tkinter import *
from tkinter import messagebox
import time
from threading import Thread

TotalAmount = 50
Budget = 50
Increase = 0
StopCond = True

root = Tk()
root.geometry('2000x2000')
root.title('Money_Clicker')

Window = Canvas(root, bg = 'yellow', height = 1000, width = 1000)
Window.pack(expand = True, fill = 'both')

def New():
    global TotalAmount
    global Bugdet
    global Increase
    global StopCond

    Begin = messagebox.askquestion('New Game', 'Start Again?', icon = 'question')
    if Begin == 'yes':
        StopCond = True
        TotalAmount = 0
        Budget = 0
        Increase = 0
        ShowBudget.config(text = f'{Budget}')

def Help():
    FAQ = Toplevel()
    FAQ.geometry('800x300')
    FAQ.title('Help')

    Info = Text(FAQ)
    Sym = Label(Info, text = 'info', bitmap = 'info', height = 33, width = 33)
    Sym.place(x = 0, y = 0)
    Info.insert(INSERT, '   It is a Clicker game, Player should Click on Money Wad Using Cursor or by Pressing the Space Button to Get Money. Player can buy Clickers, Factories, Shops, Bussinesses and another things to Gain money automatically.')
    Info.config(state = DISABLED)
    Info.pack()

    Button1 = Button(Info, text = 'Close', command = FAQ.destroy, height = 1, width = 5, cursor = 'arrow')
    Button1.place(x = 400, y = 150)

    FAQ.mainloop()
    #messagebox.showinfo("Information", "It is a Clicker game, Player should Click on Money Wad Using Cursor or by Pressing the Space Button to Get Money\n Player can buy Clickers, Factories, Shops, Bussinesses and another things to Gain money automatically")

def Exit():
    global StopCond
    Quit = messagebox.askquestion('Exit Game', 'Quit?', icon = 'question')
    if Quit == "yes":
        StopCond = True
        time.sleep(3)
        Window.destroy()
        root.destroy()

def Achivement1():
    global TotalAmount
    global Budget
    A1 = Label(Window, text = 'First 100 Clicks Achivement')
    A1.pack(side = BOTTOM)
    Budget += 50
    TotalAmount += 50
    ShowBudget.config(text = f'{Budget}')

def Achivement2():
    global TotalAmount
    global Budget
    A2 = Label(Window, text = 'First 1000 Clicks Achivement')
    A2.pack(side = BOTTOM)
    Budget += 500
    TotalAmount += 500
    ShowBudget.config(text = f'{Budget}')

def Achivement3():
    global TotalAmount
    global Budget
    A3 = Label(Window, text = 'First 10000 Clicks Achivement')
    A3.pack(side = BOTTOM)
    Budget += 5000
    TotalAmount += 5000
    ShowBudget.config(text = f'{Budget}')

def Achivement4():
    global TotalAmount
    global Budget
    A4 = Label(Window, text = 'First 100000 Clicks Achivement')
    A4.pack(side = BOTTOM)
    Budget += 50000
    TotalAmount += 50000
    ShowBudget.config(text = f'{Budget}')

def Threading():
    t1 = Thread(target = AutoIncrease)
    t1.start()

def AutoIncrease():
    global Budget
    global TotalAmount
    global Increase
    global StopCond
    while StopCond is False:
        Budget += Increase
        TotalAmount += Increase
        time.sleep(0.1)
        ShowBudget.config(text = f'{Budget}')
    Budget = 0
    TotalAmount = 0
    Increase = 0
    ShowBudget.config(text = f'{Budget}')


def Click():
    global TotalAmount
    global Budget
    TotalAmount += 1
    Budget += 1
    ShowBudget.config(text = f'{Budget}')

    if TotalAmount == 100:
        Achivement1()
    elif TotalAmount == 1000:
        Achivement2()
    elif TotalAmount == 10000:
        Achivement3()
    elif TotalAmount == 100000:
        Achivement4()

def BuyClicker():
    global Budget
    global Increase
    global StopCond
    price = 50
    adjust = 0.1

    if Budget >= price:
        if Increase == 0:
            StopCond = False
            Threading()
        Budget -= price
        Increase += adjust
        ShowBudget.config(text = f'{Budget}')

def BuyShop():
    global Budget
    global Increase
    global StopCond
    price = 1000
    adjust = 10

    if Budget >= price:
        if Increase == 0:
            StopCond = False
            Threading()
        Budget -= price
        Increase += adjust
        ShowBudget.config(text = f'{Budget}')

def BuySuperMarket():
    global Budget
    global Increase
    global StopCond
    price = 5000
    adjust = 50

    if Budget >= price:
        if Increase == 0:
            StopCond = False
            Threading()
        Budget -= price
        Increase += adjust
        ShowBudget.config(text = f'{Budget}')

def BuyFactory():
    global Budget
    global Increase
    global StopCond
    price = 10000
    adjust = 100

    if Budget >= price:
        if Increase == 0:
            StopCond = False
            Threading()
        Budget -= price
        Increase += adjust
        ShowBudget.config(text = f'{Budget}')
def BuyBank():
    global Budget
    global Increase
    global StopCond
    price = 50000
    adjust = 500

    if Budget >= price:
        if Increase == 0:
            StopCond = False
            Threading()
        Budget -= price
        Increase += adjust
        ShowBudget.config(text = f'{Budget}')
def BuyMoneyPrinter():
    global Budget
    global Increase
    global StopCond
    price = 100000
    adjust = 1000

    if Budget >= price:
        if Increase == 0:
            StopCOnd = False
            Threading()
        Budget -= price
        Increase += adjust
        ShowBudget.config(text = f'{Budget}')

Name = Label(Window, text = 'Welcome To Money Clicker Game', bg = 'green', font = ('bold', 15))
Name.pack(side = TOP)

ShowBudget = Label(Window, text = f'{Budget}', height = 10, width = 100)
ShowBudget.place(x = 10, y = 100)

MoneyWad = Button(Window, text = 'Click!', bg = 'brown', font = 'bold', command = Click)
MoneyWad.place(x = 1000, y = 500)

Menubar = Menu(Window)
Menubar.add_command(label = 'New', command = New)
Menubar.add_command(label = 'Help', command = Help)
Menubar.add_command(label = 'Exit', command = Exit)
root.config(menu = Menubar)

Clicker = Button(Window, text = 'Buy Clicker', command = BuyClicker)
Shop = Button(Window, text = 'Buy Shop', command = BuyShop)
SuperMarket = Button(Window, text = 'Buy SuperMarket', command = BuySuperMarket)
Factory = Button(Window, text = 'Buy Factory', command = BuyFactory)
Bank = Button(Window, text = 'Buy Bank', command = BuyBank)
MoneyPrinter = Button(Window, text = 'Buy Money Printer', command = BuyMoneyPrinter)
Clicker.place(x = 1700, y = 10)
Shop.place(x = 1700, y = 50)
SuperMarket.place(x = 1700, y = 90)
Factory.place(x = 1700, y = 130)
Bank.place(x = 1700, y = 170)
MoneyPrinter.place(x = 1700, y = 210)
Shop = Button()

root.mainloop()
"""


#Working version without putting all program in class and with named variables
"""
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

#def Create_Gui():
WindowWidth = 2000
WindowHeight = 1500
CanvasWidth = 1000
CanvasHeight = 1000
LabelPosX = 1000
LabelPosY = 35
ShowBudgetPosX = 350
ShowBudgetPosY = 250
TextFont= ("helvetica", 20)
MoneyPerSecondPosX = 350
MoneyPerSecondPosY = 350

root = Tk()
root.geometry(f'{WindowWidth}x{WindowHeight}')
root.title('Money_Clicker')

fileBG = Image.open(Path1)
BG = ImageTk.PhotoImage(fileBG)

Window = Canvas(root, height = CanvasHeight, width = CanvasWidth)
Window.pack(expand = True, fill = "both")
Window.create_image(0, 0, image = BG, anchor = "nw")
MoneyBag = PhotoImage(file = Path2)

Window.create_text(LabelPosX, LabelPosY, text = "Welcome To Money Clicker Game", font = TextFont, fill = "white")

ShowBudget = Window.create_text(ShowBudgetPosX, ShowBudgetPosY, text = f'Budget = {Budget}$', font = TextFont, fill = "white")

MoneyPerSecond = Window.create_text(MoneyPerSecondPosX, MoneyPerSecondPosY, text = f'Income = {Increase * 10}$ p.s', font = TextFont, fill = "white")

class Achivement:
    def __init__(self, Adjustment: int, Required_Budget: int = 0,  Required_TotalAmount: int = 0):
        self.Adjustment = Adjustment
        self.Required_Budget = Required_Budget
        self.Required_TotalAmount = Required_TotalAmount

    def Add(self):
        global Budget
        global TotalAmount
        LabelHeight = 2
        DestroyDelay = 5000

        if self.Required_TotalAmount == 0:
            A = Label(Window, text = f'First {self.Required_Budget} Dollar Achivement, You get {self.Adjustment} Dollars', height = LabelHeight, font = "bold", bg = "green")
        elif self.Required_Budget == 0:
            A = Label(Window, text = f'Total Money Amount {self.Required_TotalAmount} Dollar Achivement, You get {self.Adjustment} Dollars', height = LabelHeight, font = "bold", bg = "green")
        else:
            raise Exeption("Wrong Class Creation")

        A.pack(side = BOTTOM)
        Budget += self.Adjustment
        TotalAmount += self.Adjustment
        Window.itemconfig(ShowBudget, text = f'Budget = {Budget}$')
        Window.after(DestroyDelay, A.destroy)

Achivement1 = Achivement(50, 100)
Achivement2 = Achivement(500, 1000)
Achivement3 = Achivement(5000, 10000)
Achivement4 = Achivement(50000, 100000)
Achivement5 = Achivement(3000, 0 ,10000)
Achivement6 = Achivement(30000, 0, 100000)
Achivement7 = Achivement(300000, 0 ,1000000)
Achivement8 = Achivement(3000000, 0 ,10000000)

class Property:
    def __init__(self, Price: int, Adjust: int):
        self.Price = Price
        self.Adjust = Adjust

    def Buy(self):
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

def Exit():
    global Running
    Quit = messagebox.askquestion('Exit Game', 'Quit?', icon = 'question')
    if Quit == "yes":
        Running = False
        Window.destroy()
        root.destroy()

def CheckAchivement():
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
    global Budget
    global TotalAmount
    global Increase
    global Running
    ActivationDelay = 100

    if Running is True:
        Budget = round(Budget + Increase, 2)
        TotalAmount = round(TotalAmount + Increase, 2)
        CheckAchivement()
        Window.itemconfig(ShowBudget, text = f'Budget = {Budget}$')
        Window.after(ActivationDelay, AutoIncrease)

def Click():
    global TotalAmount
    global Budget
    global AchiveRes1
    global AchiveRes2

    TotalAmount += 1
    Budget += 1
    CheckAchivement()
    Window.itemconfig(ShowBudget, text = f'Budget = {Budget}$')

def Case1():
    global CaseRes
    global MoneyWad
    MoneyWadHeight = 600
    MoneyWadWidth = 1000

    if CaseRes == 2:
        MoneyWad.destroy()
    CaseRes = 1

    C1.config(state = DISABLED)
    C2.config(state = NORMAL)
    MoneyWad = Window.create_image(MoneyWadWidth, MoneyWadHeight, image = MoneyBag)
    def set_state(state):
        Window.itemconfigure(MoneyWad, state=state)
    def Appear():
        ActivationDelay = 1
        set_state(HIDDEN)
        Window.after(1, set_state, NORMAL)

    Window.tag_bind(MoneyWad, "<Button-1>", lambda event: (Appear(), Click()))
    root.bind("<space>", lambda event: (Appear(), Click()))

def Case2():
    global CaseRes
    global MoneyWad
    BorderSize = 10
    MoneyWadPosX = 650
    MoneyWadPosY = 220

    if CaseRes == 1:
        Window.delete(MoneyWad)
    CaseRes = 2

    C2.config(state = DISABLED)
    C1.config(state = NORMAL)

    ImageWidth = MoneyBag.width()
    ImageHeight = MoneyBag.height()
    MoneyWad = Button(Window, image = MoneyBag, height = ImageHeight, width = ImageWidth, command = Click, borderwidth = BorderSize)
    MoneyWad.place(x = MoneyWadPosX, y = MoneyWadPosY)
    def Press_button(MoneyWad):
        Delay = 0.1

        MoneyWad.config(relief = "sunken")
        root.update_idletasks()
        MoneyWad.invoke()
        time.sleep(Delay)
        MoneyWad.config(relief = "raised")

    root.bind("<space>", lambda event: Press_button(MoneyWad)) #Enable pressing MoneyBag button with "space" key

#def Change_View():
C1Width = 15
C2Width = 15
C1PosX = 0
C1PosY = 0
C2PosX = 0
C2PosY = 38

CheckVar1 = IntVar()
C1 = Checkbutton(Window, text = 'Clicker Mode - 1', variable = CheckVar1, onvalue = 1, offvalue = 0, width = C1Width, command = Case1)
C2 = Checkbutton(Window, text = 'Clicker Mode - 2', variable = CheckVar1, onvalue = 0, offvalue = 1, width = C2Width, command = Case2)
C1.place(x = C1PosX, y = C1PosY)
C2.place(x = C2PosX, y = C2PosY)
C1.invoke()

#def Create_MenuBar():
Menubar = Menu(Window)
Menubar.add_command(label = "New", command = New)
Menubar.add_command(label = "Help", command = Help)
Menubar.add_command(label = "Exit", command = Exit)
root.config(menu = Menubar)

#def Add_Buttons():
ClickerPosX = 1600
ClickerPosY = 10
ShopPosX = 1600
ShopPosY = 70
SuperMarketPosX = 1600
SuperMarketPosY = 130
FactoryPosX = 1600
FactoryPosY = 190
BankPosX = 1600
BankPosY = 250
MoneyPrinterPosX = 1600
MoneyPrinterPosY = 310

Clicker_Button = Button(Window, text = "Clicker - 50$", command = Clicker.Buy)
Shop_Button = Button(Window, text = "Shop - 1000$", command = Shop.Buy)
SuperMarket_Button = Button(Window, text = "SuperMarket - 5000$", command = SuperMarket.Buy)
Factory_Button = Button(Window, text = "Factory - 10000$", command = Factory.Buy)
Bank_Button = Button(Window, text = "Bank - 50000$", command = Bank.Buy)
MoneyPrinter_Button = Button(Window, text = "MoneyPrinter - 100000$", command = MoneyPrinter.Buy)
Clicker_Button.place(x = ClickerPosX, y = ClickerPosY)
Shop_Button.place(x = ShopPosX, y = ShopPosY)
SuperMarket_Button.place(x = SuperMarketPosX, y = SuperMarketPosY)
Factory_Button.place(x = FactoryPosX, y = FactoryPosY)
Bank_Button.place(x = BankPosX, y = BankPosY)
MoneyPrinter_Button.place(x = MoneyPrinterPosX, y = MoneyPrinterPosY)

#def End_Loop():
root.mainloop()
"""

