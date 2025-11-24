from tkinter import *
# from tkinter.ttk import *
from tkinter.messagebox import askyesno

word = ""
win = False
word_list = []
dash_list = []
dash = ""
correct=0
incorrect = 0
Time = 60
gTime = 60
# dash_new = ""
def choose_word(*args):
    global word,word_list,dash_list,dash,Time,gTime
    if word== "":
        word = word_entry.get()
        word_entry.delete(0,END)
        print(word)
        length =len(word)
        for i in range(length):
            dash_list.append("_ ")
        for s in dash_list:
            dash+=s
        word_label.configure(text=dash)
        for chr in word:
            word_list.append(chr)
        print(word_list)
        label1.configure(text="Guess the word")
        gTime=0
        ch_time()
    else:
        guess_word()

def guess_word():
    global incorrect,dash_list,dash
    ltr = word_entry.get()
    i = 0
    for l in word_list:
        if l ==ltr:
            dash_list.pop(i)
            dash_list.insert(i,ltr)
        word_entry.delete(0,END)
        i+=1
    if ltr not in word_list:
        incorrect +=1
        draw_hngman(incorrect)
        print(incorrect)
    
    if incorrect == 8:
        lose_game()

    dash_new = "" 
    for s in dash_list:
        dash_new +=s
    word_label.configure(text=dash_new)
    print(dash_new)
    if dash_new == word:
        win_game()
    
def win_game():
    global Time,gTime
    gTime = 60
    Time = 60
    label1.configure(text="Congrats you guessed the word",font='Ubuntu  10 bold')
    Message = askyesno(title="You win",message="Click yes to restart the game")
    if Message:
        restart()
    else:
        window.destroy()

def ch_time():
    global Time,gTime
    print(Time)
    if gTime == 0:
        if Time>0:
            Time = Time-1
            Time_label.configure(text=f"Time: {Time}")
            Time_label.after(1000,ch_time)
        else:
            lose_game()


def lose_game():
    global Time,gTime
    gTime = 60

    Time = 60 
    
    label1.configure(text="OOPS you lose",font='Ubuntu  10 bold')
    Message = askyesno(title=f"OOPS you lose Word was {word}",message="Click yes to restart the game")
    if Message:
        restart()
    else:
        window.destroy()


def restart():
    global incorrect,correct,win,word,word_list,dash_list,dash,Time,gTime
    gTime = 60
    Time = 60
    incorrect = 0
    correct = 0
    win = False
    word = ""
    word_list = []
    dash_list = []
    dash = ""
    canvas.delete("all")
    canvas.create_line(15,25,150,25,fill="white")
    canvas.create_line(150,80,150,25,fill="white")
    label1.configure(text = "Choose a word",font="Ubuntu 20 bold") 
    Time_label.configure(text="Time: 60")
    word_label.configure(text = "_ _ _ _ _ _ _ ")
def draw_hngman(inc):
    if inc==1:
        canvas.create_oval(110,80,190,160,outline="white")
    if inc==2:
        canvas.create_line(150,160,150,200,fill="white")
    # if inc==3:
    #     canvas.create_line(150,160,150,200,fill="white")
    if inc==3:
        canvas.create_line(150,200,100,220,fill="white")
    if inc==4:
        canvas.create_line(150,200,200,220,fill="white")
    if inc==5:
        canvas.create_line(150,160,150,250,fill="white")
    if inc==6:
        canvas.create_line(150,160,150,250,fill="white")
    if inc==7:
        canvas.create_line(150,250,100,260,fill="white")
    if inc==8:
        canvas.create_line(150,250,200,260,fill="white")
    

window = Tk()
window.geometry("800x400")
window.configure(bg="black")
window.wm_resizable(False,False)


# word_btn = Button(window,text = "Choose a word",font="ubuntu 20 bold",fg="White",bg="Black")
# word_btn.grid(row=0,column=0,padx=(140,0),pady=(50,0))

title_label = Label(window,text = "Welcome to hangman game",font="ubuntu 20 bold",fg="White",bg="Black")
title_label.grid(row=0,column=0,columnspan=10,padx=(100,0),pady=(20,0))

Time_label = Label(window,text = f"Time: {Time}",font="ubuntu 20 bold",fg="White",bg="Black")
Time_label.grid(row=0,column=11,columnspan=11,padx=(100,0),pady=(20,0))

label1 = Label(window,text = "Choose a word",font="ubuntu 20 bold",fg="White",bg="Black")
label1.grid(row=1,column=1,columnspan=5,padx=(20,0),pady=(50,0))

word_entry = Entry(window,width=20,font="Monospace 15 bold",fg="Black" ,bg='WHite')
word_entry.focus()
word_entry.grid(row=2,column=0,columnspan=4,padx=(130,0),pady=(30,0))

word_label = Label(window,text = "_ _ _ _ _ _ ",font="ubuntu 20 bold",foreground="White",bg="Black")

word_label.grid(row=3,column=1,columnspan=5,padx=(20,0),pady=(30,0))

canvas = Canvas(window,bg="black")
canvas.create_line(15,25,150,25,fill="white")
canvas.create_line(150,80,150,25,fill="white")
# canvas.create_oval(110,80,190,160,outline="white")
# canvas.create_line(150,160,150,200,fill="white")
# canvas.create_line(150,200,100,220,fill="white")
# canvas.create_line(150,200,200,220,fill="white")
# canvas.create_line(150,160,150,250,fill="white")
# canvas.create_line(150,250,100,260,fill="white")
# canvas.create_line(150,250,200,260,fill="white")


canvas.grid(row=1,rowspan=15,column=15,columnspan=10,padx=(30,0))

word_entry.bind("<Return>", choose_word)

window.mainloop()