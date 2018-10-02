import random
import time
from tkinter import *
import tkinter.messagebox

root = Tk()
root.geometry("1366x768+0+0")
root.title("Restaurant Management System")
root.configure(background='Cadet Blue')

TopF = Frame(root, bg='Cadet Blue', bd=20, pady=5, relief=RIDGE)
TopF.pack(side=TOP)

lblTitle = Label(TopF, font=('arial', 60, 'bold'),
                 text="Restaurant Management System", bd=21, bg='Cadet Blue',
                 fg='Cornsilk', justify=CENTER)
lblTitle.grid(row=0, column=0)

ReceiptCalF = Frame(root, bg='Powder Blue', bd=10, relief=RIDGE)
ReceiptCalF.pack(side=RIGHT)
ButtonsF = Frame(ReceiptCalF, bg='Powder Blue', bd=3, relief=RIDGE)
ButtonsF.pack(side=BOTTOM)
CalF = Frame(ReceiptCalF, bg='Powder Blue', bd=6, relief=RIDGE)
CalF.pack(side=TOP)
ReceiptF = Frame(ReceiptCalF, bg='Powder Blue', bd=4, relief=RIDGE)
ReceiptF.pack(side=BOTTOM)

MenuF = Frame(root, bg='Cadet Blue', bd=10, relief=RIDGE)
MenuF.pack(side=LEFT)
CostF = Frame(MenuF, bg='Powder Blue', bd=4)
CostF.pack(side=BOTTOM)
DrinksF = Frame(MenuF, bg='Cadet Blue', bd=10)
DrinksF.pack(side=TOP)

DrinksF = Frame(MenuF, bg='Powder Blue', bd=10, relief=RIDGE)
DrinksF.pack(side=LEFT)
CakeF = Frame(MenuF, bg='Powder Blue', bd=10, relief=RIDGE)
CakeF.pack(side=RIGHT)

# ============================Variables=========================================================
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()

DateofOrder = StringVar()
ReceiptRef = StringVar()
PaidTax = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
CostofCakes = StringVar()
CostofDrinks = StringVar()
ServiceCharge = StringVar()

textInput = StringVar()
operator = ""

EL = StringVar()
EE = StringVar()
EIL = StringVar()
EVC = StringVar()
EC = StringVar()
EAFC = StringVar()
EAMC = StringVar()
EIC = StringVar()

ESC = StringVar()
ESAC = StringVar()
EJYC = StringVar()
EWAC = StringVar()
ELCC = StringVar()
EKCC = StringVar()
ECHCC = StringVar()
EQPCC = StringVar()

EL.set("0")
EE.set("0")
EIL.set("0")
EVC.set("0")
EC.set("0")
EAFC.set("0")
EAMC.set("0")
EIC.set("0")

ESC.set("0")
ESAC.set("0")
EJYC.set("0")
EWAC.set("0")
ELCC.set("0")
EKCC.set("0")
ECHCC.set("0")
EQPCC.set("0")

DateofOrder.set(time.strftime("%d%m%y"))


# ================================Functions=======================================================================
def i_exit():
    iexit = tkinter.messagebox.askyesno("Exit Restaurant System", "Confirm if you want to exit")
    if iexit > 0:
        root.destroy()
        return


def reset():
    PaidTax.set("0")
    SubTotal.set("0")
    TotalCost.set("0")
    CostofCakes.set("0")
    CostofDrinks.set("0")
    ServiceCharge.set("0")
    txtReceipt.delete("1.0", END)

    EL.set("0")
    EE.set("0")
    EIL.set("0")
    EVC.set("0")
    EC.set("0")
    EAFC.set("0")
    EAMC.set("0")
    EIC.set("0")

    ESC.set("0")
    ESAC.set("0")
    EJYC.set("0")
    EWAC.set("0")
    ELCC.set("0")
    EKCC.set("0")
    ECHCC.set("0")
    EQPCC.set("0")

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)

    txtTea.configure(state=DISABLED)
    txtMilk.configure(state=DISABLED)
    txtCold_Coffee.configure(state=DISABLED)
    txtHot_Coffee.configure(state=DISABLED)
    txtLassi.configure(state=DISABLED)
    txtMango_Shake.configure(state=DISABLED)
    txtMilk_Shake.configure(state=DISABLED)
    txtCold_Drinks.configure(state=DISABLED)

    txtChocolate_Cake.configure(state=DISABLED)
    txtCheese_Cake.configure(state=DISABLED)
    txtIce_Cream_Cake.configure(state=DISABLED)
    txtCarrot_Cake.configure(state=DISABLED)
    txtCoffee_Cake.configure(state=DISABLED)
    txtLemon_Cake.configure(state=DISABLED)
    txtAngel_Food_Cake.configure(state=DISABLED)
    txtWhite_Cake.configure(state=DISABLED)


def cost_of_item():
    Item1 = float(EL.get())
    Item2 = float(EE.get())
    Item3 = float(EIL.get())
    Item4 = float(EVC.get())
    Item5 = float(EC.get())
    Item6 = float(EAFC.get())
    Item7 = float(EAMC.get())
    Item8 = float(EIC.get())

    Item9 = float(ESC.get())
    Item10 = float(ESAC.get())
    Item11 = float(EJYC.get())
    Item12 = float(EWAC.get())
    Item13 = float(ELCC.get())
    Item14 = float(EKCC.get())
    Item15 = float(ECHCC.get())
    Item16 = float(EQPCC.get())

    PriceofDrinks = (Item1 * 1.2) + (Item2 * 1.99) + (Item3 * 2.05) + (Item4 * 1.89) \
                    + (Item5 * 1.99) + (Item6 * 2.99) + (Item7 * 2.39) + (Item8 * 1.29)

    PriceofCakes = (Item9 * 1.35) + (Item10 * 2.2) + (Item11 * 1.99) + (Item12 * 1.49) \
                   + (Item13 * 1.8) + (Item14 * 1.67) + (Item15 * 1.6) + (Item16 * 1.99)

    DrinksPrice = "₹", str('%.2f' % (PriceofDrinks))
    CakesPrice = "₹", str('%.2f' % (PriceofCakes))
    CostofCakes.set(CakesPrice)
    CostofDrinks.set(DrinksPrice)
    SC = "₹", str('%.2f' % (1.59))
    ServiceCharge.set(SC)

    SubTotalofITEMS = "₹", str('%.2f' % (PriceofDrinks + PriceofCakes + 1.59))
    SubTotal.set(SubTotalofITEMS)

    Tax = "₹", str('%.2f' % ((PriceofDrinks + PriceofCakes + 1.59) * 0.15))
    PaidTax.set(Tax)
    TT = ((PriceofDrinks + PriceofCakes + 1.59) * 0.15)
    TC = "₹", str('%.2f' % ((PriceofDrinks + PriceofCakes + 1.59) + TT))
    TotalCost.set(TC)


def chkTea():
    if var1.get() == 1:
        txtTea.configure(state=NORMAL)
        txtTea.focus()
        txtTea.delete('0', END)
        EL.set("")
    elif var1.get() == 0:
        txtTea.configure(state=DISABLED)
        EL.set("0")


def chkMilk():
    if var2.get() == 1:
        txtMilk.configure(state=NORMAL)
        txtMilk.focus()
        txtMilk.delete('0', END)
        EE.set("")
    elif var2.get() == 0:
        txtMilk.configure(state=DISABLED)
        EE.set("0")


def chkCold_Coffee():
    if var3.get() == 1:
        txtCold_Coffee.configure(state=NORMAL)
        txtCold_Coffee.focus()
        txtCold_Coffee.delete('0', END)
        EIL.set("")
    elif var3.get() == 0:
        txtCold_Coffee.configure(state=DISABLED)
        EIL.set("0")


def chkHot_Coffee():
    if var4.get() == 1:
        txtHot_Coffee.configure(state=NORMAL)
        txtHot_Coffee.focus()
        txtHot_Coffee.delete('0', END)
        EVC.set("")
    elif var4.get() == 0:
        txtHot_Coffee.configure(state=DISABLED)
        EVC.set("0")


def chkLassi():
    if var5.get() == 1:
        txtLassi.configure(state=NORMAL)
        txtLassi.focus()
        txtLassi.delete('0', END)
        EC.set("")
    elif var5.get() == 0:
        txtLassi.configure(state=DISABLED)
        EC.set("0")


def chkMango_Shake():
    if var6.get() == 1:
        txtMango_Shake.configure(state=NORMAL)
        txtMango_Shake.focus()
        txtMango_Shake.delete('0', END)
        EAFC.set("")
    elif var6.get() == 0:
        txtMango_Shake.configure(state=DISABLED)
        EAFC.set("0")


def chkMilk_Shake():
    if var7.get() == 1:
        txtMilk_Shake.configure(state=NORMAL)
        txtMilk_Shake.focus()
        txtMilk_Shake.delete('0', END)
        EAMC.set("")
    elif var7.get() == 0:
        txtMilk_Shake.configure(state=DISABLED)
        EAMC.set("0")


def chkCold_Drinks():
    if var8.get() == 1:
        txtCold_Drinks.configure(state=NORMAL)
        txtCold_Drinks.focus()
        txtCold_Drinks.delete('0', END)
        EIC.set("")
    elif var8.get() == 0:
        txtCold_Drinks.configure(state=DISABLED)
        EIC.set("0")


def chkChocolate_Cake():
    if var9.get() == 1:
        txtChocolate_Cake.configure(state=NORMAL)
        txtChocolate_Cake.focus()
        txtChocolate_Cake.delete('0', END)
        ESC.set("")
    elif var9.get() == 0:
        txtChocolate_Cake.configure(state=DISABLED)
        ESC.set("0")


def chkCheese_Cake():
    if var10.get() == 1:
        txtCheese_Cake.configure(state=NORMAL)
        txtCheese_Cake.focus()
        txtCheese_Cake.delete('0', END)
        ESAC.set("")
    elif var10.get() == 0:
        txtCheese_Cake.configure(state=DISABLED)
        ESAC.set("0")


def chkIce_Cream_Cake():
    if var11.get() == 1:
        txtIce_Cream_Cake.configure(state=NORMAL)
        txtIce_Cream_Cake.focus()
        txtIce_Cream_Cake.delete('0', END)
        EJYC.set("")
    elif var11.get() == 0:
        txtIce_Cream_Cake.configure(state=DISABLED)
        EJYC.set("0")


def chkCarrot_Cake():
    if var12.get() == 1:
        txtCarrot_Cake.configure(state=NORMAL)
        txtCarrot_Cake.focus()
        txtCarrot_Cake.delete('0', END)
        EWAC.set("")
    elif var12.get() == 0:
        txtCarrot_Cake.configure(state=DISABLED)
        EWAC.set("0")


def chkCoffee_Cake():
    if var13.get() == 1:
        txtCoffee_Cake.configure(state=NORMAL)
        txtCoffee_Cake.focus()
        txtCoffee_Cake.delete('0', END)
        ELCC.set("")
    elif var13.get() == 0:
        txtCoffee_Cake.configure(state=DISABLED)
        ELCC.set("0")


def chkLemon_Cake():
    if var14.get() == 1:
        txtLemon_Cake.configure(state=NORMAL)
        txtLemon_Cake.focus()
        txtLemon_Cake.delete('0', END)
        EKCC.set("")
    elif var14.get() == 0:
        txtLemon_Cake.configure(state=DISABLED)
        EKCC.set("0")


def chkAngel_Food_Cake():
    if var15.get() == 1:
        txtAngel_Food_Cake.configure(state=NORMAL)
        txtAngel_Food_Cake.focus()
        txtAngel_Food_Cake.delete('0', END)
        ECHCC.set("")
    elif var15.get() == 0:
        txtAngel_Food_Cake.configure(state=DISABLED)
        ECHCC.set("0")


def chkWhite_Cake():
    if var16.get() == 1:
        txtWhite_Cake.configure(state=NORMAL)
        txtWhite_Cake.focus()
        txtWhite_Cake.delete('0', END)
        EQPCC.set("")
    elif var16.get() == 0:
        txtWhite_Cake.configure(state=DISABLED)
        EQPCC.set("0")


def receipt():
    txtReceipt.delete("1.10", END)
    x = random.randint(10903, 609235)
    randomRef = str(x)
    ReceiptRef.set("BILL" + randomRef)

    txtReceipt.insert(END, 'Receipt Ref:\t\t\t' + ReceiptRef.get() + '\t' + DateofOrder.get() + "\n")
    txtReceipt.insert(END, 'Item:\t\t\t' + "Cost of Item\n")

    txtReceipt.insert(END, 'Tea:\t\t\t' + EL.get() + "\n")
    txtReceipt.insert(END, 'Milk:\t\t\t' + EE.get() + "\n")
    txtReceipt.insert(END, 'Cold Coffee:\t\t\t' + EIL.get() + "\n")
    txtReceipt.insert(END, 'Hot Coffee:\t\t\t' + EVC.get() + "\n")
    txtReceipt.insert(END, 'Lassi:\t\t\t' + EC.get() + "\n")
    txtReceipt.insert(END, 'Mango Shake:\t\t\t' + EAFC.get() + "\n")
    txtReceipt.insert(END, 'Milk Shake:\t\t\t' + EAMC.get() + "\n")
    txtReceipt.insert(END, 'Cold Drinks:\t\t\t' + EIC.get() + "\n")

    txtReceipt.insert(END, 'Chocolate Cake:\t\t\t' + ESC.get() + "\n")
    txtReceipt.insert(END, 'Cheese Cake:\t\t\t' + ESAC.get() + "\n")
    txtReceipt.insert(END, 'Ice Cream Cake:\t\t\t' + EJYC.get() + "\n")
    txtReceipt.insert(END, 'Carrot Cake:\t\t\t' + EWAC.get() + "\n")
    txtReceipt.insert(END, 'Coffee Cake:\t\t\t' + ELCC.get() + "\n")
    txtReceipt.insert(END, 'Lemon Cake:\t\t\t' + EKCC.get() + "\n")
    txtReceipt.insert(END, 'Angel Food Cake:\t\t\t' + ECHCC.get() + "\n")
    txtReceipt.insert(END, 'White Cake:\t\t\t' + EQPCC.get() + "\n")

    txtReceipt.insert(END,
                      'Cost of Drinks:\t\t\t' + CostofDrinks.get() + '\nTax Paid:\t\t\t' + PaidTax.get() + "\n")
    txtReceipt.insert(END,
                      'Cost of Cakes:\t\t\t' + CostofCakes.get() + '\nSub Total:\t\t\t' + SubTotal.get() + "\n")
    txtReceipt.insert(END, 'Service Charge:\t\t\t' + ServiceCharge.get() + '\nTotal Cost:\t\t\t' + TotalCost.get())


# ============================Drinks=========================================================
Tea = Checkbutton(DrinksF, text="Tea", variable=var1, onvalue=1, offvalue=0,
                  font=('arial', 18, 'bold'), bg='Powder Blue', command=chkTea).grid(row=0, sticky=W)
Milk = Checkbutton(DrinksF, text="Milk", variable=var2, onvalue=1, offvalue=0,
                   font=('arial', 18, 'bold'), bg='Powder Blue', command=chkMilk).grid(row=1, sticky=W)
Cold_Coffee = Checkbutton(DrinksF, text="Cold Coffee", variable=var3, onvalue=1, offvalue=0,
                          font=('arial', 18, 'bold'), bg='Powder Blue', command=chkCold_Coffee).grid(row=2, sticky=W)
Hot_Coffee = Checkbutton(DrinksF, text="Hot Coffee", variable=var4, onvalue=1, offvalue=0,
                         font=('arial', 18, 'bold'), bg='Powder Blue', command=chkHot_Coffee).grid(row=3, sticky=W)
Lassi = Checkbutton(DrinksF, text="Lassi", variable=var5, onvalue=1, offvalue=0,
                    font=('arial', 18, 'bold'), bg='Powder Blue', command=chkLassi).grid(row=4, sticky=W)
Mango_Shake = Checkbutton(DrinksF, text="Mango Shake", variable=var6, onvalue=1, offvalue=0,
                          font=('arial', 18, 'bold'), bg='Powder Blue', command=chkMango_Shake).grid(row=5,
                                                                                                     sticky=W)
Milk_Shake = Checkbutton(DrinksF, text="Milk Shake", variable=var7, onvalue=1, offvalue=0,
                         font=('arial', 18, 'bold'), bg='Powder Blue', command=chkMilk_Shake).grid(row=6,
                                                                                                   sticky=W)
Cold_Drinks = Checkbutton(DrinksF, text="Cold Drinks", variable=var8, onvalue=1, offvalue=0,
                          font=('arial', 18, 'bold'), bg='Powder Blue', command=chkCold_Drinks).grid(row=7,
                                                                                                     sticky=W)

# ============================Entry Box for Drinks=========================================================
txtTea = Entry(DrinksF, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED, textvariable=EL)
txtTea.grid(row=0, column=1)
txtMilk = Entry(DrinksF, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED, textvariable=EE)
txtMilk.grid(row=1, column=1)
txtCold_Coffee = Entry(DrinksF, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED,
                       textvariable=EIL)
txtCold_Coffee.grid(row=2, column=1)
txtHot_Coffee = Entry(DrinksF, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED,
                      textvariable=EVC)
txtHot_Coffee.grid(row=3, column=1)
txtLassi = Entry(DrinksF, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED, textvariable=EC)
txtLassi.grid(row=4, column=1)
txtMango_Shake = Entry(DrinksF, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED,
                       textvariable=EAFC)
txtMango_Shake.grid(row=5, column=1)
txtMilk_Shake = Entry(DrinksF, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED,
                      textvariable=EAMC)
txtMilk_Shake.grid(row=6, column=1)
txtCold_Drinks = Entry(DrinksF, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED,
                       textvariable=EIC)
txtCold_Drinks.grid(row=7, column=1)

# ============================Cakes=========================================================
Chocolate_Cake = Checkbutton(CakeF, text="Chocolate Cake", variable=var9, onvalue=1, offvalue=0,
                             font=('arial', 18, 'bold'), bg='Powder Blue', command=chkChocolate_Cake).grid(row=0, sticky=W)
Cheese_Cake = Checkbutton(CakeF, text="Cheese Cake", variable=var10, onvalue=1, offvalue=0,
                          font=('arial', 18, 'bold'), bg='Powder Blue', command=chkCheese_Cake).grid(row=1,
                                                                                                     sticky=W)
Ice_Cream_Cake = Checkbutton(CakeF, text="Ice Cream Cake", variable=var11, onvalue=1, offvalue=0,
                             font=('arial', 18, 'bold'), bg='Powder Blue', command=chkIce_Cream_Cake).grid(row=2,
                                                                                                           sticky=W)
Carrot_Cake = Checkbutton(CakeF, text="Carrot Cake", variable=var12, onvalue=1, offvalue=0,
                          font=('arial', 18, 'bold'), bg='Powder Blue', command=chkCarrot_Cake).grid(row=3,
                                                                                                     sticky=W)
Coffee_Cake = Checkbutton(CakeF, text="Coffee Cake", variable=var13, onvalue=1, offvalue=0,
                          font=('arial', 18, 'bold'), bg='Powder Blue', command=chkCoffee_Cake).grid(
    row=4, sticky=W)
Lemon_Cake = Checkbutton(CakeF, text="Lemon Cake", variable=var14, onvalue=1, offvalue=0,
                         font=('arial', 18, 'bold'), bg='Powder Blue',
                         command=chkLemon_Cake).grid(row=5, sticky=W)
Angel_Food_Cake = Checkbutton(CakeF, text="Angel Food Cake", variable=var15, onvalue=1, offvalue=0,
                              font=('arial', 18, 'bold'), bg='Powder Blue', command=chkAngel_Food_Cake).grid(row=6,
                                                                                                             sticky=W)
White_Cake = Checkbutton(CakeF, text="White Cake", variable=var16, onvalue=1, offvalue=0,
                         font=('arial', 18, 'bold'), bg='Powder Blue', command=chkWhite_Cake).grid(row=7,
                                                                                                   sticky=W)

# ============================Entry Box for Cakes=========================================================
txtChocolate_Cake = Entry(CakeF, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED, textvariable=ESC)
txtChocolate_Cake.grid(row=0, column=1)
txtCheese_Cake = Entry(CakeF, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED,
                       textvariable=ESAC)
txtCheese_Cake.grid(row=1, column=1)
txtIce_Cream_Cake = Entry(CakeF, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED,
                          textvariable=EJYC)
txtIce_Cream_Cake.grid(row=2, column=1)
txtCarrot_Cake = Entry(CakeF, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED,
                       textvariable=EWAC)
txtCarrot_Cake.grid(row=3, column=1)
txtCoffee_Cake = Entry(CakeF, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED,
                       textvariable=ELCC)
txtCoffee_Cake.grid(row=4, column=1)
txtLemon_Cake = Entry(CakeF, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED,
                      textvariable=EKCC)
txtLemon_Cake.grid(row=5, column=1)
txtAngel_Food_Cake = Entry(CakeF, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED,
                           textvariable=ECHCC)
txtAngel_Food_Cake.grid(row=6, column=1)
txtWhite_Cake = Entry(CakeF, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED,
                      textvariable=EQPCC)
txtWhite_Cake.grid(row=7, column=1)

# ================================Totals Cost=======================================================================
lblCostofDrinks = Label(CostF, font=('arial', 14, 'bold'),
                        text="Cost of Drinks\t   ", bd=21, bg='Powder Blue', fg='black', justify=CENTER)
lblCostofDrinks.grid(row=0, column=0, sticky=W)

txtCostofDrinks = Entry(CostF, bg="white", bd=7, font=('arial', 14, 'bold'), insertwidth=2, justify=RIGHT,
                        textvariable=CostofDrinks)
txtCostofDrinks.grid(row=0, column=1)

lblCostofCakes = Label(CostF, font=('arial', 14, 'bold'),
                       text="Cost of Cakes   ", bd=21, bg='Powder Blue', fg='black', justify=CENTER)
lblCostofCakes.grid(row=1, column=0, sticky=W)

txtCostofCakes = Entry(CostF, bg="white", bd=7, font=('arial', 14, 'bold'), insertwidth=2, justify=RIGHT,
                       textvariable=CostofCakes)
txtCostofCakes.grid(row=1, column=1)

lblServiceCharge = Label(CostF, font=('arial', 14, 'bold'),
                         text="ServiceCharge   ", bd=21, bg='Powder Blue', fg='black', justify=CENTER)
lblServiceCharge.grid(row=2, column=0, sticky=W)

txtServiceCharge = Entry(CostF, bg="white", bd=7, font=('arial', 14, 'bold'), insertwidth=2, justify=RIGHT,
                         textvariable=ServiceCharge)
txtServiceCharge.grid(row=2, column=1)

# ================================Payment Information======================================================================
lblPaidTax = Label(CostF, font=('arial', 14, 'bold'),
                   text="\tPaid Tax\t", bd=7, bg='Powder Blue', fg='black')
lblPaidTax.grid(row=0, column=2, sticky=W)

txtPaidTax = Entry(CostF, bg="white", bd=7, font=('arial', 14, 'bold'), insertwidth=2, justify=LEFT,
                   textvariable=PaidTax)
txtPaidTax.grid(row=0, column=3)

lblSubTotal = Label(CostF, font=('arial', 14, 'bold'),
                    text="\tSub Total", bd=7, bg='Powder Blue', fg='black')
lblSubTotal.grid(row=1, column=2, sticky=W)

txtSubTotal = Entry(CostF, bg="white", bd=7, font=('arial', 14, 'bold'), insertwidth=2, justify=LEFT,
                    textvariable=SubTotal)
txtSubTotal.grid(row=1, column=3)

lblTotalCost = Label(CostF, font=('arial', 14, 'bold'),
                     text="\tTotal Cost", bd=7, bg='Powder Blue', fg='black')
lblTotalCost.grid(row=2, column=2, sticky=W)

txtTotalCost = Entry(CostF, bg="white", bd=7, font=('arial', 14, 'bold'), insertwidth=2, justify=LEFT,
                     textvariable=TotalCost)
txtTotalCost.grid(row=2, column=3)

# ================================Receipt=======================================================================
txtReceipt = Text(ReceiptF, width=46, height=12, bg="white", bd=4, font=('arial', 16, 'bold'))
txtReceipt.grid(row=0, column=0)

# ================================Buttons=======================================================================
btnTotal = Button(ButtonsF, padx=16, pady=1, bd=7, fg="black", font=('arial', 16, 'bold'), width=4, text="Total",
                  bg="powder blue", command=cost_of_item).grid(row=0, column=0)
btnReceipt = Button(ButtonsF, padx=16, pady=1, bd=7, fg="black", font=('arial', 16, 'bold'), width=4, text="Receipt",
                    bg="powder blue", command=receipt).grid(row=0, column=1)
btnReset = Button(ButtonsF, padx=16, pady=1, bd=7, fg="black", font=('arial', 16, 'bold'), width=4, text="Reset",
                  bg="powder blue", command=reset).grid(row=0, column=2)
btnExit = Button(ButtonsF, padx=16, pady=1, bd=7, fg="black", font=('arial', 16, 'bold'), width=4, text="Exit",
                 bg="powder blue", command=i_exit).grid(row=0, column=3)

# ===============================Calculator Display================================================================================
txtDisplay = Entry(CalF, width=45, bg="white", bd=4, font=('arial', 16, 'bold'), justify=RIGHT, textvariable=textInput)
txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
txtDisplay.insert(0, "0")


def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    textInput.set(operator)


def btnClear():
    global operator
    operator = ""
    textInput.set("")


def btnEquals():
    global operator
    sumup = str(eval(operator))
    textInput.set(sumup)
    operator = ""


# ================================Calculator Buttons=======================================================================
btn7 = Button(CalF, padx=16, pady=1, bd=7, fg="black", font=('arial', 16, 'bold'), width=4, text="7",
              bg="powder blue", command=lambda: btnClick(7)).grid(row=2, column=0)
btn8 = Button(CalF, padx=16, pady=1, bd=7, fg="black", font=('arial', 16, 'bold'), width=4, text="8",
              bg="powder blue", command=lambda: btnClick(8)).grid(row=2, column=1)
btn9 = Button(CalF, padx=16, pady=1, bd=7, fg="black", font=('arial', 16, 'bold'), width=4, text="9",
              bg="powder blue", command=lambda: btnClick(9)).grid(row=2, column=2)
btnAdd = Button(CalF, padx=16, pady=1, bd=7, fg="black", font=('arial', 16, 'bold'), width=4, text="+",
                bg="powder blue", command=lambda: btnClick("+")).grid(row=2, column=3)

# ================================Calculator Buttons=======================================================================
btn4 = Button(CalF, padx=16, pady=1, bd=7, fg="black", font=('arial', 16, 'bold'), width=4, text="4"
              , command=lambda: btnClick(4)).grid(row=3, column=0)
btn5 = Button(CalF, padx=16, pady=1, bd=7, fg="black", font=('arial', 16, 'bold'), width=4, text="5"
              , command=lambda: btnClick(5)).grid(row=3, column=1)
btn6 = Button(CalF, padx=16, pady=1, bd=7, fg="black", font=('arial', 16, 'bold'), width=4, text="6"
              , command=lambda: btnClick(6)).grid(row=3, column=2)
btnSub = Button(CalF, padx=16, pady=1, bd=7, fg="black", font=('arial', 16, 'bold'), width=4, text="-"
                , command=lambda: btnClick("-"), bg="powder blue").grid(row=3, column=3)

# ================================Calculator Buttons=======================================================================
btn1 = Button(CalF, padx=16, pady=1, bd=7, fg="black", font=('arial', 16, 'bold'), width=4, text="1"
              , command=lambda: btnClick(1)).grid(row=4, column=0)
btn2 = Button(CalF, padx=16, pady=1, bd=7, fg="black", font=('arial', 16, 'bold'), width=4, text="2"
              , command=lambda: btnClick(2)).grid(row=4, column=1)
btn3 = Button(CalF, padx=16, pady=1, bd=7, fg="black", font=('arial', 16, 'bold'), width=4, text="3"
              , command=lambda: btnClick(3)).grid(row=4, column=2)
btnMul = Button(CalF, padx=16, pady=1, bd=7, fg="black", font=('arial', 16, 'bold'), width=4, text="*",
                bg="powder blue", command=lambda: btnClick("*")).grid(row=4, column=3)

# ================================Calculator Buttons=======================================================================
btn0 = Button(CalF, padx=16, pady=1, bd=7, fg="black", font=('arial', 16, 'bold'), width=4, text="0",
              bg="powder blue", command=lambda: btnClick(0)).grid(row=5, column=0)
btnClear = Button(CalF, padx=16, pady=1, bd=7, fg="black", font=('arial', 16, 'bold'), width=4, text="C",
                  command=btnClear, bg="powder blue").grid(row=5, column=1)
btnEquals = Button(CalF, padx=16, pady=1, bd=7, fg="black", font=('arial', 16, 'bold'), width=4, text="=",
                   bg="powder blue", command=btnEquals).grid(row=5, column=2)
btnDiv = Button(CalF, padx=16, pady=1, bd=7, fg="black", font=('arial', 16, 'bold'), width=4, text="/",
                bg="powder blue", command=lambda: btnClick("/")).grid(row=5, column=3)

root.mainloop()
