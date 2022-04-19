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

Window = Canvas(root, bg = "yellow", height = 1000, width = 1000)
Window.pack(expand = True, fill = "both")

def New():
    global TotalAmount
    global Bugdet
    global Increase
    global StopCond

    Begin = messagebox.askquestion('New Game', 'Start Again?', icon = 'question')
    if Begin == "yes":
        StopCond = True
        TotalAmount = 0
        Budget = 0
        Increase = 0
        ShowBudget.config(text = f'{Budget}')

def Help():
    FAQ = Toplevel()
    FAQ.geometry("800x300")
    FAQ.title("Help")

    Info = Text(FAQ)
    Sym = Label(Info, text = "info", bitmap = "info", height = 33, width = 33)
    Sym.place(x = 0, y = 0)
    Info.insert(INSERT, "  It is a Clicker game, Player should Click on Money Wad Using Cursor or by Pressing the Space Button to Get Money. Player can buy Clickers, Factories, Shops, Bussinesses and another things to Gain money automatically.")
    Info.config(state = DISABLED)
    Info.pack()

    Button1 = Button(Info, text = "Close", command = FAQ.destroy, height = 1, width = 5, cursor = "arrow")
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
    A1 = Label(Window, text = "First 100 Clicks Achivement")
    A1.pack(side = BOTTOM)
    Budget += 50
    TotalAmount += 50
    ShowBudget.config(text = f'{Budget}')

def Achivement2():
    global TotalAmount
    global Budget
    A2 = Label(Window, text = "First 1000 Clicks Achivement")
    A2.pack(side = BOTTOM)
    Budget += 500
    TotalAmount += 500
    ShowBudget.config(text = f'{Budget}')

def Achivement3():
    global TotalAmount
    global Budget
    A3 = Label(Window, text = "First 10000 Clicks Achivement")
    A3.pack(side = BOTTOM)
    Budget += 5000
    TotalAmount += 5000
    ShowBudget.config(text = f'{Budget}')

def Achivement4():
    global TotalAmount
    global Budget
    A4 = Label(Window, text = "First 100000 Clicks Achivement")
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

Name = Label(Window, text = "Welcome To Money Clicker Game", bg = "green", font = ("bold", 15))
Name.pack(side = TOP)

ShowBudget = Label(Window, text = f'{Budget}', height = 10, width = 100)
ShowBudget.place(x = 10, y = 100)

MoneyWad = Button(Window, text = "Click!", bg = "brown", font = "bold", command = Click)
MoneyWad.place(x = 1000, y = 500)

Menubar = Menu(Window)
Menubar.add_command(label = "New", command = New)
Menubar.add_command(label = "Help", command = Help)
Menubar.add_command(label = "Exit", command = Exit)
root.config(menu = Menubar)

Clicker = Button(Window, text = "Buy Clicker", command = BuyClicker)
Shop = Button(Window, text = "Buy Shop", command = BuyShop)
SuperMarket = Button(Window, text = "Buy SuperMarket", command = BuySuperMarket)
Factory = Button(Window, text = "Buy Factory", command = BuyFactory)
Bank = Button(Window, text = "Buy Bank", command = BuyBank)
MoneyPrinter = Button(Window, text = "Buy Money Printer", command = BuyMoneyPrinter)
Clicker.place(x = 1700, y = 10)
Shop.place(x = 1700, y = 50)
SuperMarket.place(x = 1700, y = 90)
Factory.place(x = 1700, y = 130)
Bank.place(x = 1700, y = 170)
MoneyPrinter.place(x = 1700, y = 210)
Shop = Button()

root.mainloop()
"""




