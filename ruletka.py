from ast import While
from tkinter import *
import time
from turtle import color
import random
import tkinter

global d 
d=0

root = Tk()
root.geometry("150x70")

def rejestracja():
    global d 
    d=1
    root.destroy()

def login42():
    global d
    d=2 
    root.destroy()

register_button = Button(root, text="rejestracja", padx=30, pady=5, command = lambda: rejestracja())
login_button = Button(root, text="logowanie", padx=30, pady=5, command = lambda: login42())

register_button.pack()
login_button.pack()

root.mainloop()
if d==1:
    root = Tk()
    root.geometry('250x120')

    def register():
        a = open("dane.txt","a")
        a.close()
        a = open("dane.txt")
        b = a.read()
        a.close()
        global d
        o = password_entry.get()
        e = login_Entry.get()
        
        if b == "" and e!="" and o!="":
            a=open("dane.txt","a")
            writefile = e+" "+o+" "+'100'
            a.write(writefile)
            a.close()
            d=2
            root.destroy()
        elif e!="" and o!="":
            a=open("dane.txt","a")
            writefile2 = "\n"+e+" "+o+" "+'100'
            a.write(writefile2)
            a.close()
            d=2
            root.destroy()
        else:
            print("sus")

    login_Entry = Entry(root,width=40,borderwidth=5)
    password_entry = Entry(root,width=40,borderwidth=5)
    register_button = Button(root,text="register",padx=30, pady=5,command=lambda: register())

    login_Entry.pack()
    password_entry.pack()
    register_button.pack()

    root.mainloop()
if d==2:
    root = Tk()
    root.geometry('250x120')
    root.title("logowanie")

    def zaloguj():
        login=login_entry.get()
        password=pass_entry.get()

        a = open("dane.txt")
        b = a.read()
        a.close()
        tablica = ['']
        o=0
        sds=0
        global kox
        kox=-1
        global lolsd
        lolsd=[]
        for lol in range(len(b)):
            if b[lol] == " " or b[lol]=="\n":
                o+=1
                tablica.append('')
            tablica[o] += b[lol]
        tablica[0].replace(" ","")
        for xd in tablica:
            xd2=xd.replace(" ","")
            xd3=xd2.replace("\n",'')
            tablica[sds]=xd3
            sds+=1
            lolsd.append(xd)
        zle_haslo.config(text="złe hasło ",fg="red")
        for lo324 in tablica:
            kox+=1
            if login == lo324:
                if tablica[kox+1] == password:
                    global kasa
                    kasa = int(tablica[kox+2])
                    global kox2
                    kox2=kox
                    global d
                    d=3
                    root.destroy()

    zle_haslo = Label(root,text='')
    login_entry = Entry(root, width=40,borderwidth=5)
    pass_entry = Entry(root, width=40,borderwidth=5)
    zaloguj_button = Button(root,text='zaloguj',padx=10,pady=5,command=lambda: zaloguj())

    login_entry.grid(row=1,column=2)
    pass_entry.grid(row=2,column=2)
    zaloguj_button.grid(row=3, column=2)
    zle_haslo.grid(row=4, column=2)

    root.mainloop()
global kox2
print(kox2)
kox2+=2
if d==3:
    root=Tk()
    root.geometry('380x150')
    root.title("ruletka")
    global kasa
    global czerwonyile
    czerwonyile=0
    global zielonyile
    zielonyile=0
    global czarnyile
    czarnyile=0

    def czarny():
        ile_text = ile.get()
        global kasa
        if kasa==0:
            root.destroy()
        if kasa >= int(ile_text):
            global czarnyile
            czarnyile+=int(ile_text)
            kasa-=int(ile_text)
            czarnyile_label.config(text=czarnyile)
            saldo_label.config(text ="saldo: {}".format(kasa))
        return None

    def zielony():
        ile_text = ile.get()
        global kasa
        if kasa==0:
            root.destroy()
        if kasa >= int(ile_text):
            global zielonyile
            zielonyile += int(ile_text)
            kasa-=int(ile_text)
            zielonyile_label.config(text=zielonyile)
            saldo_label.config(text ="saldo: {}".format(kasa))
        return None

    def czerwony():
        ile_text = ile.get()
        global kasa
        if kasa==0:
            root.destroy()
        if kasa >= int(ile_text):
            global czerwonyile
            czerwonyile+=int(ile_text)
            kasa-=int(ile_text)
            czerwonyile_label.config(text=czerwonyile)
            saldo_label.config(text ="saldo: {}".format(kasa))
        return None

    def losowanie():
        global kasa
        if kasa==0:
            root.destroy()
        global czerwonyile
        global czarnyile
        global zielonyile
        global lolsd
        global kox2
        o=''

        if czerwonyile>0 or czarnyile>0 or zielonyile>0:
            losowanko = random.randint(1,25)
            saldo_label.config(text ="saldo: {}".format(kasa))
            error_label.config(text = "")
            if losowanko <=12:
                if czarnyile>0:
                    kasa+=czarnyile*2
                    wyniktext_label.config(text="wygrałeś",fg="green")
                    saldo_label.config(text ="saldo: {}".format(kasa))
                else:
                    wyniktext_label.config(text="przegrałeś",fg="red")
                czarnyile=0
                czerwonyile=0
                zielonyile=0
                czerwonyile_label.config(text=0)
                czarnyile_label.config(text=0)
                zielonyile_label.config(text=0)
                wynik_label.config(bg="black")
                lolsd[kox2] = ' ' + str(kasa)
                for lollollol in lolsd:
                    o+=lollollol
                a = open("dane.txt","w")
                a.write(o)
                a.close()
            elif losowanko == 13:
                if zielonyile > 0:
                    kasa += zielonyile*14
                    wyniktext_label.config(text="wygrałeś",fg="green")
                    saldo_label.config(text ="saldo: {}".format(kasa))
                else:
                    wyniktext_label.config(text="przegrałeś",fg="red")
                czarnyile=0
                czerwonyile=0
                zielonyile=0
                czerwonyile_label.config(text=0)
                czarnyile_label.config(text=0)
                zielonyile_label.config(text=0)
                wynik_label.config(bg="green")
                lolsd[kox2] = ' ' + str(kasa)
                for lollollol in lolsd:
                    o+=lollollol
                a = open("dane.txt","w")
                a.write(o)
                a.close()
            elif losowanko > 13:
                if czerwonyile>0:
                    kasa += czerwonyile*2
                    wyniktext_label.config(text="wygrałeś",fg="green")
                    saldo_label.config(text ="saldo: {}".format(kasa))
                else:
                    wyniktext_label.config(text="przegrałeś",fg="red")
                czarnyile=0
                czerwonyile=0
                zielonyile=0
                czerwonyile_label.config(text=0)
                czarnyile_label.config(text=0)
                zielonyile_label.config(text=0)
                wynik_label.config(bg="red")
                lolsd[kox2] = ' ' + str(kasa)
                for lollollol in lolsd:
                    o+=lollollol
                a = open("dane.txt","w")
                a.write(o)
                a.close()

            else:
                print("cos się zjebało")
        else:
            error_label.config(text = "musisz coś obstawić", fg="red")
        return None

    saldo_label=Label(root, text = "saldo: {}".format(kasa))
    ile = Entry(root,width = 20, borderwidth=5)
    czarny_button = Button(root,text="czarne",padx=40,pady=10,fg="black",command = lambda: czarny())
    czerwony_button = Button(root,text="czerwone",padx=40,pady=10,fg="black",command = lambda: czerwony())
    zielony_button = Button(root,text="zielone",padx=40,pady=10,fg="black",command = lambda: zielony())
    czarnyile_label = Label(root, text = czarnyile)
    czerwonyile_label = Label(root, text = czerwonyile)
    zielonyile_label = Label(root, text = zielonyile)
    losuj_button = Button(root,text="losuj", padx = 40, pady = 5, fg = "black", command = lambda: losowanie())
    error_label = Label(root,text='')
    wynik_label = Label(root,text='                  ')
    wyniktext_label = Label(root,text='')

    saldo_label.grid(row=1, column=3)
    czarny_button.grid(row=2,column=1)
    czarnyile_label.grid(row=3,column=1)
    czerwony_button.grid(row=2,column=3)
    czerwonyile_label.grid(row=3,column=3)
    zielony_button.grid(row=2,column=2)
    zielonyile_label.grid(row=3, column=2)
    ile.grid(row=1,column=2)
    losuj_button.grid(row=1,column=1)
    error_label.grid(row=4,column=1)
    wynik_label.grid(row=4, column=2)
    wyniktext_label.grid(row=4, column=3)

    root.mainloop()