from tkinter import *
import random
from tkinter import ttk

PuzzleWindow=Tk()

PuzzleWindow.title('Memory Puzzle Game By Devonte & Nezzy')

tabs = ttk.Notebook(PuzzleWindow) 
easy= ttk.Frame(tabs)

#create easy level I will start, and you finish.

def draw(a,l,m):
    global base1
    if a=='A':
        d=base1.create_rectangle(100*l+20,m*100+20,100*l+100-20,100*m+100-20,fill='red')
    elif a=='B':
        d=base1.create_rectangle(100*l+20,m*100+20,100*l+100-20,100*m+100-20,fill='yellow')
    elif a=='C':
        d=base1.create_rectangle(100*l+20,m*100+20,100*l+100-20,100*m+100-20,fill='blue')
    elif a=='D':
        d=base1.create_oval(100*l+20,m*100+20,100*l+100-20,100*m+100-20,fill='red')
    elif a=='E':
        d=base1.create_oval(100*l+20,m*100+20,100*l+100-20,100*m+100-20,fill='yellow')
    elif a=='F':
        d=base1.create_oval(100*l+20,m*100+20,100*l+100-20,100*m+100-20,fill='blue')
    elif a=='G':
        d=base1.create_polygon(100*l+50,m*100+20,100*l+20,100*m+100-20,100*l+100-20,100*m+100-20,fill='red')
    elif a=='H':
        d=base1.create_polygon(100*l+50,m*100+20,100*l+20,100*m+100-20,100*l+100-20,100*m+100-20,fill='green')
    
def quizboard():
