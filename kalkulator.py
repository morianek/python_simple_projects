from tkinter import *
import tkinter
import keyboard as kb
#from tkinter.ttk import *

global znak
znak=0
global zmiana_calc


root = Tk()
root.geometry('380x263')
root.config(bg='black')
root.title("prosty kalkulator")


e = Entry(root, width=40, borderwidth=5,bg='black',fg='white')
e.grid (row=0, column=0, columnspan=3,padx=10,pady=10)


znakwys = Label(root,text='',bg='black',fg='white')
znakwys.place(x=280, y=12)


o = Entry(root, width=8, borderwidth=1,bg='black',fg='white')
o.grid(row=0, column=3,columnspan=3, padx=8, pady=2)
o.insert(0, 0)


def click(num):
    if num<=9:
        text = e.get()
        e.delete(0, END)
        e.insert(0,str(text)+str(num))
    return None


def usuwanie():
    znakwys.config(text="c")
    e.delete(0, END)
    global f_num,f_num2,znak
    f_num = 0
    f_num2 = 0
    znak = 0
    o.delete(0,END)
    o.insert(0,0)
    return None


def dodawanie():
    znakwys.config(text="+")

    global f

    f=e.get()
    e.delete(0, END)

    global f_num
    f_num = float(f)

    global f_num2
    f_num2 = o.get()
    o.delete(0, END)

    global znak

    math()

    znak=1


global lol
lol = False


def rowna():
    znakwys.config(text="=")
    c=0
    global lol

    g=e.get()
    zmiennew0=o.get()

    if g == '' and zmiennew0.find(".")!=-1:
        c=1
        lol=True
    elif g == '':
        lol=True
        c=2

    o.delete(0,END)
    o.insert(0, 0)

    e.delete(0, END)

    if c==1 :
        e.insert(0,float(zmiennew0))
    elif c==2:
        e.insert(0,int(zmiennew0))

    global znak

    if znak==1 and lol==False:
        if g.find(".")!=-1 or zmiennew0.find(".")!=-1:
            e.insert(0,float(zmiennew0)+float(g))
        else:
            e.insert(0,int(zmiennew0)+int(g))
    elif znak==2 and lol==False:
        if g.find(".")!=-1 or zmiennew0.find(".")!=-1:
            e.insert(0,float(zmiennew0)-float(g))
        else:
            e.insert(0,int(zmiennew0)-int(g))
    elif znak==0 and lol==False:
        if g.find(".")!=-1:
            e.insert(0,float(g))
        else:
            e.insert(0,int(g))
    elif znak==3 and lol==False:
        if g.find(".")!=-1 or zmiennew0.find(".")!=-1:
            e.insert(0,float(zmiennew0)*float(g))
        else:
            e.insert(0,int(zmiennew0)*int(g))
    elif znak==4 and lol==False:
        if g.find(".")!=-1 or zmiennew0.find(".")!=-1:
            e.insert(0,float(zmiennew0)/float(g))
        else:
            e.insert(0,int(zmiennew0)/int(g))
    elif znak==5 and lol==False:
        if g.find(".")!=-1:
            e.insert(0,float(g))
        else:
            e.insert(0,int(g))

    lol=False
    znak=5
    return None


def odejmowanie():
    znakwys.config(text="-")

    global f

    f=e.get()
    e.delete(0, END)

    global f_num
    f_num = float(f)

    global f_num2
    f_num2 = o.get()

    o.delete(0, END)
    global znak

    math()

    znak=2
    return None

def math():
    
    global f
    global f_num
    global f_num2

    if znak==1:
        d=int(f_num.is_integer())
        xd=int(float(f_num2).is_integer())
        if f.find(".")!=-1 or f_num2.find(".")!=-1:
            if xd==0 or d==0:
                o.insert(0, float(f_num2) + f_num)
            else:
                o.insert(0, int(float(f_num2)) + int(f_num))
        else:
            o.insert(0, int(float(f_num2)) + int(f_num))
    elif znak==2:
        d=int(f_num.is_integer())
        xd=int(float(f_num2).is_integer())
        if f.find(".")!=-1 or f_num2.find(".")!=-1:
            if xd==0 or d==0:
                o.insert(0, float(f_num2) - f_num)
            else:
                o.insert(0, int(float(f_num2)) - int(f_num))
        else:
            o.insert(0, int(float(f_num2)) - int(f_num))
    elif znak==0:
        d=int(f_num.is_integer())
        xd=int(float(f_num2).is_integer())
        if f.find(".")!=-1 or f_num2.find(".")!=-1:
            if xd==0 or d==0:
                o.insert(0, float(f_num2) + f_num)
            else:
                o.insert(0, int(float(f_num2)) + int(f_num))
        else:
            o.insert(0, int(float(f_num2)) + int(f_num))
    elif znak==3:
        d=int(f_num.is_integer())
        xd=int(float(f_num2).is_integer())
        if f.find(".")!=-1 or f_num2.find(".")!=-1:
            if xd==0 or d==0:
                o.insert(0, float(f_num2) * f_num)
            else:
                o.insert(0, int(float(f_num2)) * int(f_num))
        else:
            o.insert(0, int(float(f_num2)) * int(f_num))
    elif znak==4:
            o.insert(0, float(f_num2) / f_num)
    elif znak==5:
        d=int(f_num.is_integer())
        xd=int(float(f_num2).is_integer())
        if f.find(".")!=-1 or f_num2.find(".")!=-1:
            if xd==0 or d==0:
                o.insert(0, f_num)
            else:
                o.insert(0, int(f_num))
        else:
            o.insert(0, int(f_num))



def mnozenie():
    znakwys.config(text="*")

    global f

    f=e.get()
    e.delete(0, END)

    global f_num
    f_num = float(f)

    global f_num2
    f_num2 = o.get()

    o.delete(0, END)
    global znak

    math()

    znak=3
    return None


def dzielenie():
    znakwys.config(text="/")

    f=e.get()
    e.delete(0, END)

    global f_num
    f_num = float(f)

    global f_num2
    f_num2 = o.get()

    o.delete(0, END)

    global znak

    if znak==1:
        o.insert(0, float(f_num2) + f_num)
    elif znak==2:
        o.insert(0, float(f_num2) - f_num)
    elif znak==0:
        o.insert(0, float(f_num2) + f_num)
    elif znak==3:
        o.insert(0, float(f_num2) * f_num)
    elif znak==4:
        o.insert(0, float(f_num2) / f_num)
    elif znak==5:
       o.insert(0, f_num)
    znak=4
    return None


#def zmiana():
#    pass


button_1 = Button(root,text="1", padx=40,pady=15,bg='grey',fg='white',command=lambda: click(1))
button_2 = Button(root,text="2", padx=40,pady=15,bg='grey',fg='white',command=lambda: click(2))
button_3 = Button(root,text="3", padx=40,pady=15,bg='grey',fg='white',command=lambda: click(3))
button_4 = Button(root,text="4", padx=40,pady=15,bg='grey',fg='white',command=lambda: click(4))
button_5 = Button(root,text="5", padx=40,pady=15,bg='grey',fg='white',command=lambda: click(5))
button_6 = Button(root,text="6", padx=40,pady=15,bg='grey',fg='white',command=lambda: click(6))
button_7 = Button(root,text="7", padx=40,pady=15,bg='grey',fg='white',command=lambda: click(7))
button_8 = Button(root,text="8", padx=40,pady=15,bg='grey',fg='white',command=lambda: click(8))
button_9 = Button(root,text="9", padx=40,pady=15,bg='grey',fg='white',command=lambda: click(9))
button_0 = Button(root,text="0", padx=40,pady=15,bg='grey',fg='white',command=lambda: click(0))
button_c = Button(root,text="c", padx=40,pady=15,bg='grey',fg='white',command=lambda: usuwanie())
button_plus = Button(root,text="+", padx=40,pady=15,bg='grey',fg='white',command=lambda: dodawanie())
button_minus = Button(root,text="-", padx=40,pady=15,bg='grey',fg='white',command=lambda: odejmowanie())
button_razy = Button(root,text="*", padx=40,pady=15,bg='grey',fg='white',command=lambda: mnozenie())
button_dzielic = Button(root,text="/", padx=40,pady=15,bg='grey',fg='white',command=lambda: dzielenie())
button_rowna = Button(root,text="=", padx=40,pady=15,bg='grey',fg='white',command=lambda: rowna())
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

button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_dzielic.grid(row=1, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_razy.grid(row=2, column=3)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_plus.grid(row=3, column=3)

button_c.grid(row=4, column=0)
button_0.grid(row=4, column=1)
button_rowna.grid(row=4, column=2)
button_minus.grid(row=4, column=3)
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