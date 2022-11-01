from tkinter import *
import keyboard as kb

global lastsign
lastsign = 0

root = Tk()
root.geometry('451x283')
root.config(bg='black')
root.title("prosty kalkulator")

znakwys = Label(root,text='',bg='black',fg='gray',font=("Arial", 10))
znakwys.grid(row=0,column=3,sticky=E,padx=10)

sec_input = Entry(root, width=8, borderwidth=0,bg='black',fg='white', justify= RIGHT)
sec_input.place(y=4,x=380)

main_input = Entry(root, width=72, borderwidth=5,bg='black',fg='white', justify= RIGHT)
main_input.insert(0,0)
main_input.grid (row=1, column=0, columnspan=4,padx=4,pady=10,sticky=W)


def click(num):
    if num<=9:
        text = main_input.get()
        main_input.delete(0, END)
        if text == "0":
            text = ""
        main_input.insert(0,text+str(num))
    return None

def getnums():
    main = main_input.get()
    sec = sec_input.get()
    if main == "":
        main = 0
    main = float(main)
    if sec == "":
        sec = 0
    sec = float(sec)
    main_input.delete(0, END)
    sec_input.delete(0, END)
    return sec,main

def check():
    return not (main_input.get() == "" and sec_input.get()!="")

def usuwanie():
    znakwys.config(text="")
    global lastsign
    main_input.delete(0,END)
    sec_input.delete(0,END)
    main_input.insert(0,0)
    lastsign = 0

def rowna():
    znakwys.config(text="")
    global lastsign
    main_input.insert(0,math())
    lastsign = 0

def dodawanie():
    znakwys.config(text="+")
    global lastsign
    if check():
        sec_input.insert(0,math())
    lastsign = 1


def odejmowanie():
    znakwys.config(text="-")
    global lastsign
    if check():
        sec_input.insert(0,math())
    lastsign = 2

def mnozenie():
    znakwys.config(text="*")
    global lastsign
    if check():
        sec_input.insert(0,math())
    lastsign = 3


def dzielenie():
    znakwys.config(text="/")
    global lastsign
    if check():
        sec_input.insert(0,math())
    lastsign = 4

def math():
    nums = getnums()
    out = nums[1]
    if lastsign == 1:
        out = nums[0]+nums[1]
    if lastsign == 2:
        out = nums[0]-nums[1]
    if lastsign == 3:
        out = nums[0]*nums[1]
    if lastsign == 4:
        out = nums[0]/nums[1]
    if out.is_integer():
        out = int(out)
    return out
            
button_1 = Button(root,text="1", width=15,pady=15,bg='grey',fg='white',command=lambda: click(1))
button_2 = Button(root,text="2", width=15,pady=15,bg='grey',fg='white',command=lambda: click(2))
button_3 = Button(root,text="3", width=15,pady=15,bg='grey',fg='white',command=lambda: click(3))
button_4 = Button(root,text="4", width=15,pady=15,bg='grey',fg='white',command=lambda: click(4))
button_5 = Button(root,text="5", width=15,pady=15,bg='grey',fg='white',command=lambda: click(5))
button_6 = Button(root,text="6", width=15,pady=15,bg='grey',fg='white',command=lambda: click(6))
button_7 = Button(root,text="7", width=15,pady=15,bg='grey',fg='white',command=lambda: click(7))
button_8 = Button(root,text="8", width=15,pady=15,bg='grey',fg='white',command=lambda: click(8))
button_9 = Button(root,text="9", width=15,pady=15,bg='grey',fg='white',command=lambda: click(9))
button_0 = Button(root,text="0", width=15,pady=15,bg='grey',fg='white',command=lambda: click(0))
button_c = Button(root,text="c", width=15,pady=15,bg='grey',fg='white',command=lambda: usuwanie())
button_plus = Button(root,text="+", width=15,pady=15,bg='grey',fg='white',command=lambda: dodawanie())
button_minus = Button(root,text="-", width=15,pady=15,bg='grey',fg='white',command=lambda: odejmowanie())
button_razy = Button(root,text="*", width=15,pady=15,bg='grey',fg='white',command=lambda: mnozenie())
button_dzielic = Button(root,text="/", width=15,pady=15,bg='grey',fg='white',command=lambda: dzielenie())
button_rowna = Button(root,text="=", width=15,pady=15,bg='grey',fg='white',command=lambda: rowna())
#button_miara = Button(root, text='_-`', padx=2, pady=3,bg='grey',fg='white', command = lambda: zmiana())

kb.add_hotkey('1',lambda: click(1))
kb.add_hotkey('2',lambda: click(2))
kb.add_hotkey('3',lambda: click(3))
kb.add_hotkey('4',lambda: click(4))
kb.add_hotkey('5',lambda: click(5))
kb.add_hotkey('6',lambda: click(6))
kb.add_hotkey('7',lambda: click(7))
kb.add_hotkey('8',lambda: click(8))
kb.add_hotkey('9',lambda: click(9))
kb.add_hotkey('0',lambda: click(0))
kb.add_hotkey('c',lambda: usuwanie())
kb.add_hotkey('+',lambda: dodawanie())
kb.add_hotkey('shift + =',lambda: dodawanie())
kb.add_hotkey('-',lambda: odejmowanie())
kb.add_hotkey('*',lambda: mnozenie())
kb.add_hotkey('shift + 8',lambda: mnozenie())
kb.add_hotkey('/',lambda: dzielenie())
kb.add_hotkey('=',lambda: rowna())
kb.add_hotkey('enter',lambda: rowna())

button_1.grid(row=2, column=0,sticky=W)
button_2.grid(row=2, column=1,sticky=E)
button_3.grid(row=2, column=2,sticky=E)
button_dzielic.grid(row=2, column=3,sticky=E)

button_4.grid(row=3, column=0,sticky=W)
button_5.grid(row=3, column=1,sticky=E)
button_6.grid(row=3, column=2,sticky=E)
button_razy.grid(row=3, column=3,sticky=E)

button_7.grid(row=4, column=0,sticky=W)
button_8.grid(row=4, column=1,sticky=E)
button_9.grid(row=4, column=2,sticky=E)
button_plus.grid(row=4, column=3,sticky=E)

button_c.grid(row=5, column=0,sticky=W)
button_0.grid(row=5, column=1,sticky=E)
button_rowna.grid(row=5, column=2,sticky=E)
button_minus.grid(row=5, column=3,sticky=E)
#button_miara.place(x=0,y=0)


root.mainloop()


'''
root = Tk()
root.geometry('380x263')
root.title("prosty kalkulator")
e = Entry(root,width = 20, borderwidth=5)
e.grid(row=0,column=0)
button_miara = Button(root, text='_-`', padx=2, pady=3, command = lambda: zmiana())
def zmiana():
    root.destroy()
root.mainloop()
'''