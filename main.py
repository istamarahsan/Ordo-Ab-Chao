import turtle
from tkinter import *
from tkinter import colorchooser

#thseuhfushf

def_bg = '#ffffed'
def_ink = '#16264c'

#Window Setup
wn = turtle.Screen() # Set up the window and its attributes
wn.bgcolor(def_bg)

#Turtles
turtle.pensize(1)
turtle.color(def_ink)
turtle.speed(0)
turtle.hideturtle()
turtle.title("Ordo Ab Chao")

class Pattern():
    """docstring for Pattern."""

    def __init__(self, size, d):
        self.size = size
        self.d = d

    def draw(self):
        size = self.size
        d = self.d
        for i in range(2,size*d,d):
            if drawing == True:
                turtle.forward(i/(100*d))
                turtle.left(i)
            else:
                break


    def reset(self):
        turtle.reset()
        turtle.hideturtle()
        turtle.pensize(1)
        turtle.speed(0)

    def reset_color():
        turtle.color(def_ink)
        wn.bgcolor(def_bg)

drawing = False

oPattern = Pattern(0, 0)

#Command to start drawing pattern
def start_pattern():
    global drawing
    drawing = True
    seed = seedEntry.get()
    if type(int(seed)) is int:
        startButton.grid_remove()
        seed = int(seed)
        oPattern = Pattern(1000*seed, seed)
        oPattern.draw()
    else:
        pass

def reset_pattern():
    startButton.grid()
    oPattern.reset()
    global drawing
    drawing = False

def stop_pattern():
    global drawing
    drawing = False

def mod_seed(dir):
    seed = int(seedEntry.get())
    if dir is True:
        seed += 1
    if dir is False:
        if seed-1 < 0:
            pass
        else:
            seed -= 1
    seedEntry.delete(0, END)
    seedEntry.insert(0, str(seed))

def pen_color_pick():
    #turtle.color(colorchooser.askcolor(title = "Recolour Pen"))
    #colorChosen = (colorchooser.askcolor(title = "Recolour Pen"))
    #print(str(colorChosen[1]))
    colorChosen = colorchooser.askcolor(title = "Pen Colour")
    turtle.color(str(colorChosen[1]))

def canvas_color_pick():
    colorChosen = colorchooser.askcolor(title = "Canvas Colour")
    wn.bgcolor(str(colorChosen[1]))

def close_all():
    sys.exit()

#########################
#MENU#
########################
root = Tk()
root.title("Control Panel")
root.resizable(False, False)
#root.geometry('300x300')

#root.resizable(height = 0, width = 0)

seedLabel = Label(root, text="Seed")
seedLabel.grid(row=0,column=0)

seedEntry = Entry(root)
seedEntry.grid(row=0,column=2)
seedEntry.insert(0, 0)

seedPlus = Button(root, text=">", command = lambda: mod_seed(True))
seedPlus.grid(row=0,column=3, ipadx=1)

seedMinus = Button(root, text="<", command = lambda: mod_seed(False))
seedMinus.grid(row=0,column=1, ipadx=1)

startButton = Button(root, text="start", command = start_pattern)
startButton.grid(row=0, column=4, sticky=N+S+E+W)

stopButton = Button(root, text="stop", command = stop_pattern)
stopButton.grid(row=1, column=0, columnspan=5, sticky=N+S+E+W)

resetButton = Button(root, text="reset", command = reset_pattern)
resetButton.grid(row=2, column=0, columnspan=5, sticky=N+S+E+W)

pencolourButton = Button(root, text="Pen Colour..", command = pen_color_pick)
pencolourButton.grid(row=3, column=0, columnspan=2, sticky=N+S+E+W)

canvascolourButton = Button(root, text="Canvas Colour.", command = canvas_color_pick)
canvascolourButton.grid(row=3, column=2, columnspan=3, sticky=N+S+E+W)

exitButton = Button(root, text="exit", command = close_all)
exitButton.grid(row=4, column=0, columnspan=5, sticky=N+S+E+W)

root.mainloop()
########################
#MENU#
########################
