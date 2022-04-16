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




