  
import random
from tkinter import *
import winsound

# Initialise the window size
window = Tk()
window.minsize(width=1000, height = 200)
drawing = Canvas(window, width =1200, height = 200)

# Outline the respective coordinates.
xrand  = random.randrange(20,480)
yrand = random.randrange(20,480)
rect = drawing.create_rectangle(20,40,70,60,fill = 'red')
rect2 = drawing.create_rectangle(20,140,70,160,fill = 'blue')
finish = drawing.create_rectangle(950,0,1500,1500)
line = drawing.create_rectangle(0,100,950,100)

finishco = drawing.coords(finish)
busco = drawing.coords(rect)
busco2 = drawing.coords(rect2)

drawing.itemconfig(finish,state = HIDDEN)

# Draw the options
def on_click(event):
        drawing.itemconfig(rect, fill= '#ffb6c1')
def on_click2(event):
    drawing.itemconfig(rect, fill = '#32cd32')

def on_clickn(event):
        drawing.itemconfig(rect, fill= '#ffb6c1')
def on_clickn2(event):
    drawing.itemconfig(rect, fill = '#32cd32')

def right(event):
    global busco
    drawing.move(rect,5,0)
    busco = drawing.coords(rect)
    drawing.after(1)
    drawing.update()
    if busco[0] == 950:
        drawing.itemconfig(rect, fill='yellow')
        drawing.itemconfig(rect2,state = HIDDEN)
        buttonFin.pack()
        window.bind("<Key-z>", on_click)
        window.bind("<Key-x>", on_click2)


def right2(event):
    global busco2
    drawing.move(rect2,5,0)
    busco2 = drawing.coords(rect2)
    drawing.after(1)
    drawing.update()
    if busco2[0] == 950:
        drawing.itemconfig(rect2, fill = 'yellow')
        drawing.itemconfig(rect, state = HIDDEN)
        buttonFin2.pack()
        window.bind("<Key-.>", on_clickn)
        window.bind("<Key-/>", on_clickn2)

def start():
    buttonA.pack_forget()
    buttonB.pack_forget()
    buttonC.pack_forget()
    buttonD.pack_forget()
    buttonStart.pack_forget()
    window.bind("<Key-z>", right)
    window.bind("<Key-x>", right)
    window.bind("<Key-/>", right2)
    window.bind("<Key-.>", right2)
    drawing.itemconfig(finish,state = NORMAL)

def start2():
    global busco
    global busco2
    while busco != 20:
        drawing.move(rect,-20,0)
        busco = drawing.coords(rect)
        drawing.after(1)
        drawing.update()

    while busco2 != 20:
            drawing.move(rect2,-20,0)
            busco = drawing.coords(rect2)
            drawing.after(1)
            drawing.update()

    starting2()

def starting():
    global buttonA
    global buttonB
    global buttonC
    global buttonD
    global buttonStart
    global buttonFin
    global buttonFin2
    buttonFin = Button(window,text = "z/x WINS!",
                       command = start2)
    buttonFin2 = Button(window,text = ". and / WINS!",
                        command = start2)
    buttonA = Button(window,text = "RACER")
    buttonB = Button(window,text = "Player 1: Top Car: z/x")
    buttonC = Button(window,text = "Player 2: Bottom Car: . and /")
    buttonD = Button(window,text = "First to the end wins!")
    buttonStart = Button(window,text = "Click to start",
                         command = start)
    buttonA.pack()
    buttonB.pack()
    buttonC.pack()
    buttonD.pack()
    buttonStart.pack()

def starting2():
    buttonA.pack()
    buttonB.pack()
    buttonC.pack()
    buttonD.pack()
    buttonStart.pack()
    drawing.itemconfig(line,state = NORMAL)
    drawing.itemconfig(rect,state = NORMAL)
    drawing.itemconfig(rect2,state = NORMAL)


starting()
drawing.pack()
window.mainloop() # Waits for events from the players, updating it.