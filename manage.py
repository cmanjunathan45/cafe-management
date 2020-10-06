from tkinter import *
import tkinter as tk
from tkinter import messagebox,filedialog
from datetime import datetime,date
import calendar

now=datetime.now()
current_time = now.strftime("%H:%M:%S")
today = date.today()
dat = today.strftime("%d/%m/%Y")
tdat=calendar.day_name[today.weekday()]
root=tk.Tk()
root.title("CAFE Management System | Manjunathan C")
root.geometry("1360x705")
ico=PhotoImage(file="icon.png")
root.iconphoto(True,ico)
root.config(bg="#ffd480")

tit=Label(root,text="CAFE MANAGEMENT SYSTEM",font=("font awesome",30,"bold italic underline"),bg="#ffd480",fg="#cc0000")
tit.place(x=350,y=20)
tea=5
coffee=8
pizza=30
burger=25
sandwich=20
def calculate():
	try:
		if(entryTea.get()==""):
			a=0
		else:
			a=int(entryTea.get())*tea
		if(entryCoffee.get()==""):
			b=0
		else:
			b=int(entryCoffee.get())*coffee
		if(entryPizza.get()==""):
			c=0
		else:
			c=int(entryPizza.get())*pizza
		if(entryBurger.get()==""):
			d=0
		else:
			d=int(entryBurger.get())*burger
		if(entrySandwich.get()==""):
			e=0
		else:
			e=int(entrySandwich.get())*sandwich
		total=a+b+c+d+e
		tax=total*(3/100)
		total+=tax
		entryTotal.delete(0,END)
		entryTotal.insert(END,total)
		amt=Text(root,width=26,height=19,font=("fontawesome",15,"italic"),borderwidth=5)
		aText=f"                        Your Bill\n\nDate    :  {dat}\nDay     :  {tdat}\nTime  :  {current_time}\n------------------------------------------------\n\nTea\t-\t${a}\nCoffee\t-\t${b}\nPizza\t-\t${c}\nBurger\t-\t${d}\nSandwich\t-\t${e}\n\n------------------------------------------------\nTax(3%)\t-\t${tax}\n\nTotal\t-\t${total}"
		amt.insert(END,aText)
		amt.place(x=460,y=130)
		def save_as():
			root.filename = filedialog.asksaveasfile(mode="w",defaultextension='.txt')
			if root.filename is None:
				return
			file_save =  str(amt.get(1.0,END))
			root.filename.write(file_save)
			root.filename.close()
		buttonPrint=Button(root,text="Print",font=("font awesome",15,"bold italic"),bg="#cc0000",fg="#ffd480",width=15,borderwidth=5,activebackground="red",command=save_as)
		buttonPrint.place(x=510,y=560)
	except:
		messagebox.showerror("Error","Please Enter Valid Data")
def clear():
	entryTea.delete(0,END)
	entryCoffee.delete(0,END)
	entryBurger.delete(0,END)
	entryPizza.delete(0,END)
	entrySandwich.delete(0,END)
	entryTotal.delete(0,END)
try:
	def press(key):
		current=entryCal.get()
		entryCal.delete(0,END)
		entryCal.insert(0,str(current)+str(key))
	#addition function
	def add():
		first_num=entryCal.get()
		global fnum
		global math
		math="addition"
		fnum=int(first_num)
		entryCal.delete(0,END)

	#minus function
	def minus():
		first_num=entryCal.get()
		global fnum
		global math
		math="minus"
		fnum=int(first_num)
		entryCal.delete(0,END)

	#multiply function
	def multiply():
		first_num=entryCal.get()
		global fnum
		global math
		math="multiply"
		fnum=int(first_num)
		entryCal.delete(0,END)

	#addition function
	def divide():
		first_num=entryCal.get()
		global fnum
		global math
		math="divide"
		fnum=int(first_num)
		entryCal.delete(0,END)
	def equal():
		sec_num=entryCal.get()
		entryCal.delete(0,END)
		if(math=="addition"):
			entryCal.insert(0,fnum+int(sec_num))
		if(math=="minus"):
			entryCal.insert(0,fnum-int(sec_num))
		if(math=="multiply"):
			entryCal.insert(0,fnum*int(sec_num))

		try:
			if(math=="divide"):
				e.insert(0,fnum/int(sec_num))
		except:
			messagebox.showerror("Zero Division Error","Unable to Divide a number by '0'. The Value is infinite")
except:
	messagebox.showerror("Error","Please Enter Valid Data")

def close():
	if messagebox.askyesno("Confirm","Do You Want To Close ?"):
		root.destroy()

name=Label(root,text="Name 	 -     Items",font=("font awesome",17,"bold"),bg="#ffd480",fg="#cc0000")
name.place(x=20,y=100)

teaLabel=Label(root,text=f"Tea({tea})",font=("font awesome",15,"bold italic"),bg="#ffd480",fg="#cc0000")
teaLabel.place(x=20,y=150)

entryTea=Entry(root,width=5,borderwidth=6,font=("fontawesome",15,"bold italic"),bg="#cc0000",fg="#ffd480")
entryTea.insert(END,"0")
entryTea.place(x=190,y=145)

coffeeLabel=Label(root,text=f"Coffee({coffee})",font=("font awesome",15,"bold italic"),bg="#ffd480",fg="#cc0000")
coffeeLabel.place(x=20,y=200)

entryCoffee=Entry(root,width=5,borderwidth=6,font=("fontawesome",15,"bold italic"),bg="#cc0000",fg="#ffd480")
entryCoffee.insert(END,"0")
entryCoffee.place(x=190,y=195)

pizaaLabel=Label(root,text=f"Pizza({pizza})",font=("font awesome",15,"bold italic"),bg="#ffd480",fg="#cc0000")
pizaaLabel.place(x=20,y=250)

entryPizza=Entry(root,width=5,borderwidth=6,font=("fontawesome",15,"bold italic"),bg="#cc0000",fg="#ffd480")
entryPizza.insert(END,"0")
entryPizza.place(x=190,y=245)

burgerLabel=Label(root,text=f"Burger({burger})",font=("font awesome",15,"bold italic"),bg="#ffd480",fg="#cc0000")
burgerLabel.place(x=20,y=300)

entryBurger=Entry(root,width=5,borderwidth=6,font=("fontawesome",15,"bold italic"),bg="#cc0000",fg="#ffd480")
entryBurger.insert(END,"0")
entryBurger.place(x=190,y=295)

sandwichLabel=Label(root,text=f"Sandwich({sandwich})",font=("font awesome",15,"bold italic"),bg="#ffd480",fg="#cc0000")
sandwichLabel.place(x=20,y=350)

entrySandwich=Entry(root,width=5,borderwidth=6,font=("fontawesome",15,"bold italic"),bg="#cc0000",fg="#ffd480")
entrySandwich.insert(END,"0")
entrySandwich.place(x=190,y=345)

buttonTotal=Button(root,text="Total",font=("font awesome",15,"bold italic"),bg="#cc0000",fg="#ffd480",width=5,borderwidth=5,activebackground="red",command=calculate)
buttonTotal.place(x=20,y=400)

entryTotal=Entry(root,width=7,borderwidth=6,font=("fontawesome",15,"bold italic"),bg="#cc0000",fg="#ffd480")
entryTotal.place(x=175,y=400)

buttonClear=Button(root,text="Clear",font=("font awesome",15,"bold italic"),bg="#cc0000",fg="#ffd480",width=10,borderwidth=5,activebackground="red",command=clear)
buttonClear.place(x=60,y=460)

buttonExit=Button(root,text="Exit",font=("font awesome",15,"bold italic"),bg="#cc0000",fg="#ffd480",width=10,borderwidth=5,activebackground="red",command=close)
buttonExit.place(x=60,y=515)

#buttons 0-9
entryCal=Entry(root,width=23,borderwidth=6,font=("fontawesome",15,"bold italic"),bg="#cc0000",fg="#ffd480")
entryCal.place(x=990,y=160)

button_0=Button(text="0",font=("fontawesome",15,"bold italic"),bg="#cc0000",fg="#ffd480",command=lambda :press(0),width=5,borderwidth=5)
button_0.place(x=990,y=225)

button_1=Button(text="1",font=("fontawesome",15,"bold italic"),bg="#cc0000",fg="#ffd480",width=5,borderwidth=5,command=lambda: press(1))
button_1.place(x=1105,y=225)

button_2=Button(text="2",font=("fontawesome",15,"bold italic"),bg="#cc0000",fg="#ffd480",width=5,borderwidth=5,command=lambda: press(2))
button_2.place(x=1220,y=225)

button_3=Button(text="3",font=("fontawesome",15,"bold italic"),bg="#cc0000",fg="#ffd480",width=5,borderwidth=5,command=lambda: press(3))
button_3.place(x=990,y=280)

button_4=Button(text="4",font=("fontawesome",15,"bold italic"),bg="#cc0000",fg="#ffd480",width=5,borderwidth=5,command=lambda: press(4))
button_4.place(x=1105,y=280)

button_5=Button(text="5",font=("fontawesome",15,"bold italic"),bg="#cc0000",fg="#ffd480",width=5,borderwidth=5,command=lambda: press(5))
button_5.place(x=1220,y=280)

button_6=Button(text="6",font=("fontawesome",15,"bold italic"),bg="#cc0000",fg="#ffd480",width=5,borderwidth=5,command=lambda: press(6))
button_6.place(x=990,y=335)

button_7=Button(text="7",font=("fontawesome",15,"bold italic"),bg="#cc0000",fg="#ffd480",width=5,borderwidth=5,command=lambda: press(7))
button_7.place(x=1105,y=335)

button_8=Button(text="8",font=("fontawesome",15,"bold italic"),bg="#cc0000",fg="#ffd480",width=5,borderwidth=5,command=lambda: press(8))
button_8.place(x=1220,y=335)

button_9=Button(text="9",font=("fontawesome",15,"bold italic"),bg="#cc0000",fg="#ffd480",width=5,borderwidth=5,command=lambda: press(9))
button_9.place(x=990,y=390)

button_eql=Button(text="=",font=("fontawesome",15,"bold italic"),bg="#cc0000",fg="#ffd480",width=5,borderwidth=5,command=equal)
button_eql.place(x=1105,y=390)

button_p=Button(text="+",font=("fontawesome",15,"bold italic"),bg="#cc0000",fg="#ffd480",width=5,borderwidth=5,command=add)
button_p.place(x=990,y=445)

button_m=Button(text="-",font=("fontawesome",15,"bold italic"),bg="#cc0000",fg="#ffd480",width=5,borderwidth=5,command=minus)
button_m.place(x=1105,y=445)

button_mul=Button(text="x",font=("fontawesome",15,"bold italic"),bg="#cc0000",fg="#ffd480",width=5,borderwidth=5,command=multiply)
button_mul.place(x=1220,y=445)

button_d=Button(text="/",font=("fontawesome",15,"bold italic"),bg="#cc0000",fg="#ffd480",width=5,borderwidth=5,command=divide)
button_d.place(x=1220,y=390)

buttonCalClear=Button(root,text="Clear",font=("fontawesome",15,"bold italic"),bg="#cc0000",fg="#ffd480",width=21,borderwidth=5,command=lambda: entryCal.delete(0,END))
buttonCalClear.place(x=992,y=500)

buttonCalExit=Button(root,text="Exit",font=("font awesome",15,"bold italic"),bg="#cc0000",fg="#ffd480",width=21,borderwidth=5,activebackground="red",command=close )
buttonCalExit.place(x=992,y=555)

root.mainloop()