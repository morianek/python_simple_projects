from ssl import OP_ENABLE_MIDDLEBOX_COMPAT
from tkinter import *

def start():
    root = Tk()
    root.geometry("200x110")
    root.title('wybór stron')
    # tu ma być pole na 2 playerów nazwy ich i przycisk do zaczęcia
    def bot():
        #bot czyli ai która gra (może kiedyś zrobię)
        print('narazie nic tu nie ma')
    def nick():
        root.destroy()
        gracze()

    button_bot = Button(root,text='1 osobowy',padx=60,pady=30,command=lambda:bot())
    button_nick = Button(root,text='2 osobowy',padx=60,pady=30,command=lambda:nick())
    button_bot.place(x=10,y=0)
    button_nick.place(x=10,y=55)
    root.mainloop()




def gracze():
    root = Tk()
    root.geometry("200x130")
    root.title('wybór nicków')
    

    def graj():
        global nick1
        global nick2
        nick1 = Entry_nick1.get()
        nick2 = Entry_nick2.get()
        if nick1 != '' and nick2 != '' and nick1!=nick2:
            root.destroy()
            gra()

    button_graj = Button(root,text='graj',padx=60,pady=10,command=lambda:graj())
    Entry_nick1 = Entry(root,width=30,borderwidth=5)
    Entry_nick2 = Entry(root,width=30,borderwidth=5)

    button_graj.place(x=25,y=80)
    Entry_nick2.place(x=5,y=40)
    Entry_nick1.place(x=5,y=0)

    root.mainloop()

def wynik(player):
    root = Tk()
    root.title("wynik")
    root.geometry("200x120")

    global nick1
    global nick2
    b=[nick1,nick2]
    if player!=3:
        tekst = f'wygrał player {b[player-1]}'
    else:
        tekst = f'remis'

    def again():
        root.destroy()
        gra()

    def the_end():
        root.destroy()

    button_again = Button(root,text='zagraj ponownie',padx=20,pady=10,command=lambda:again())
    button_koniec = Button(root,text="koniec",padx=46,pady=7,command = lambda: the_end())
    Label_wynik = Label(root,text=tekst)

    button_again.place(x=40,y=0)
    button_koniec.place(x=40,y=50)
    Label_wynik.place(x=40,y=100)

    root.mainloop()





def gra():
    root=Tk()
    root.geometry("380x250")
    root.title("tic tac toe")

    global player
    player = True

    global odp
    odp = [0,0,0,0,0,0,0,0,0]

    def change_symbol(click):
        global player
        global odp
        if click == 1:
            if player:
                button_lewygorny.config(text="X",command=lambda:nic())
                odp[click-1] = 1
            else:
                button_lewygorny.config(text="O",command=lambda:nic())
                odp[click-1] = 2
        if click == 2:
            if player:
                button_gorna.config(text="X",command=lambda:nic())
                odp[click-1] = 1
            else:
                odp[click-1] = 2
                button_gorna.config(text="O",command=lambda:nic())
        if click == 3:
            if player:
                button_prawygorny.config(text="X",command=lambda:nic())
                odp[click-1] = 1
            else:
                button_prawygorny.config(text="O",command=lambda:nic())
                odp[click-1] = 2
        if click == 4:
            if player:
                button_lewymid.config(text="X",command=lambda:nic())
                odp[click-1] = 1
            else:
                odp[click-1] = 2
                button_lewymid.config(text="O",command=lambda:nic())
        if click == 5:
            if player:
                button_mid.config(text="X",command=lambda:nic())
                odp[click-1] = 1
            else:
                odp[click-1] = 2
                button_mid.config(text="O",command=lambda:nic())
        if click == 6:
            if player:
                odp[click-1] = 1
                button_prawymid.config(text="X",command=lambda:nic())
            else:
                odp[click-1] = 2
                button_prawymid.config(text="O",command=lambda:nic())
        if click == 7:
            if player:
                button_lewydolny.config(text="X",command=lambda:nic())
                odp[click-1] = 1
            else:
                odp[click-1] = 2
                button_lewydolny.config(text="O",command=lambda:nic())
        if click == 8:
            if player:
                odp[click-1] = 1
                button_dolny.config(text="X",command=lambda:nic())
            else:
                odp[click-1] = 2
                button_dolny.config(text="O",command=lambda:nic())
        if click == 9:
            if player:
                odp[click-1] = 1
                button_prawydolny.config(text="X",command=lambda:nic())
            else:
                odp[click-1] = 2
                button_prawydolny.config(text="O",command=lambda:nic())


    def wincheck():
        global odp
        sus82 = 0
        if odp[0]==odp[1]==odp[2] and odp[0]!=0:
            sus82 = odp[0]
            #print(f"win {odp[0]} gora poziom")
        if odp[0]==odp[3]==odp[6] and odp[0]!=0:
            sus82 = odp[0]
            #print(f"win {odp[0]} lewo pion")
        if odp[0]==odp[4]==odp[8] and odp[0]!=0:
            sus82 = odp[0]
            #print(f"win {odp[0]} skos prawo")
        if odp[2]==odp[5]==odp[8] and odp[2]!=0:
            sus82 = odp[2]
            #print(f"win {odp[2]} prawo pion")
        if odp[1]==odp[4]==odp[7] and odp[1]!=0:
            sus82 = odp[1]
            #print(f"win {odp[1]} mid pion")
        if odp[6]==odp[7]==odp[8] and odp[6]!=0:
            sus82 = odp[6]
            #print(f"win {odp[6]} doł poziom")
        if odp[3]==odp[4]==odp[5] and odp[3]!=0:
            sus82 = odp[3]
            #print(f"win {odp[3]} mid poziom")
        if odp[2]==odp[4]==odp[6] and odp[2]!=0:
            sus82 = odp[2]
            #print(f"win {odp[2]} skos lewo")
        return sus82

    def nic():
        pass

    def klikanie(key):
        sus=0
        global player
        change_symbol(key)
        global odp
        #print(odp)
        win=wincheck()
        if player:
            player=False
        else:
            player=True
        for _ in odp:
            if _ != 0:
                sus+=1
        if win!=0:
            #print("koniec")
            root.destroy()
            wynik(win)
        if sus==9:
            root.destroy()
            wynik(3)


    button_lewygorny = Button(root,text='.',padx=60,pady=30,command=lambda:klikanie(1))
    button_gorna = Button(root,text='.',padx=60,pady=30,command=lambda:klikanie(2))
    button_prawygorny = Button(root,text='.',padx=60,pady=30,command=lambda:klikanie(3))
    button_lewymid = Button(root,text='.',padx=60,pady=30,command=lambda:klikanie(4))
    button_mid = Button(root,text='.',padx=60,pady=30,command=lambda:klikanie(5))
    button_prawymid = Button(root,text='.',padx=60,pady=30,command=lambda:klikanie(6))
    button_lewydolny = Button(root,text='.',padx=60,pady=30,command=lambda:klikanie(7))
    button_dolny = Button(root,text='.',padx=60,pady=30,command=lambda:klikanie(8))
    button_prawydolny = Button(root,text='.',padx=60,pady=30,command=lambda:klikanie(9))

    button_lewygorny.grid(column=0,row=0)
    button_gorna.grid(column=1,row=0)
    button_prawygorny.grid(column=2,row=0)
    button_lewymid.grid(column=0,row=1)
    button_mid.grid(column=1,row=1)
    button_prawymid.grid(column=2,row=1)
    button_lewydolny.grid(column=0,row=2)
    button_dolny.grid(column=1,row=2)
    button_prawydolny.grid(column=2,row=2)



    root.mainloop()

start()