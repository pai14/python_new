#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

from random import randrange as rnd, choice
from tkinter import *
root = Tk()
root.geometry('800x600+600+200')
canv = Canvas(root, bg='grey')
canv.pack(fill=BOTH, expand = TRUE)

x0 = 0 # точка отсчета координат x
y0 = 0 # точка отсчета координат y
nr = 15 # количество строк
nc = 20 # количество столбцов
m = 30 # размер ячейки
d = 2  # толщина бордюра ячейки
colors = ['blue', 'red', 'white', 'green', 'black', 'yellow']
a = []


class cell():
    def __init__(self, r, c):
#        self.n = rnd(10)
        self.r = r  # номер строки в двумерном массиве
        self.c = c  # номер столбца в двумерном массиве
        self.color = choice(colors)
        self.id = canv.create_rectangle(0, 0, 0, 0, fill = 'grey') # заготовка ячейки с цветом и размерами
        self.txt = str(r*10+c)
        self.id_txt = canv.create_text(0, 0, text = self.txt)
        self.paint()
        
    def paint(self):
        x1 = x0 + self.c * m + d 
        x2 = x1 + m 
        y1 = y0 + self.r * m + d 
        y2 = y1 + m 
        canv.coords(self.id, x1, y1, x2, y2) # ячейку размещаем 
        canv.coords(self.id_txt, (x1+x2)/2, (y1+y2)/2) # текст размещаем по центру ячейки

    def move(self):
        x1, y1, x2, y2 = canv.coords(self.id)
        for ii in range(5):
            y1 += 1
            y2 += 1
            canv.coords(self.id, x1, y1, x2, y2) # ячейку размещаем
  #hu          canv.after(10, self.move())
            print('y1=', y1)
    
def fill_cells():
    for r in range(nr):
        a.append([])
        for c in range(nc):
            a[r].append(cell(r, c))

def work(event):
    global a
    a = []
    fill_cells()
    print(len(a))
    dopcell = canv.create_rectangle(0, 0, 0, 0)
    canv.coords(dopcell, x0+m*nc+d+2*m, y0+d, x0+m*nc+d+2*m+m, y0+d+m)
    canv.create_text(((x0+m*nc+d+2*m)+(x0+m*nc+d+2*m+m))/2, (y0+d + y0+d+m)/2, text = 'aa') 
    cell(1, 25).move()
    

    

fill_cells()
canv.bind('<Button-1>', work)

root.mainloop()
