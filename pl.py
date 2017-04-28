from tkinter import *
from random import choice, randrange as rnd
import time



colors = ['red', 'green', 'black', 'blue']
wid = 50                # ширина ячейки
hei = 50                # высота ячейки
grid_rows = 4           # количество строк
grid_columns = 5        # количество столбцов

tk = Tk()
xm = 500    #максимальный размер пространства по 
ym = 500
gmt = str(xm) + 'x' + str(ym) + '+600+100'
tk.geometry(gmt)

cv = Canvas(tk, bg='grey', width=xm, height=ym)
cv.pack()



class grid():
# ячейки сетки
    def __init__(self, row, col):
        self.r = row 
        self.c = col
        self.w = wid
        self.x0 = 0
        self.y0 = 0
        self.x1 = self.w
        self.y1 = self.w
        self.id = cv.create_rectangle(self.x0, self.y0, self.x1, self.y1)
        self.paint()
        
    def paint(self):
        self.x0 = self.x0 + self.c * self.w
        self.y0 = self.y0 + self.r * self.w
        self.x1 = self.x0+self.w
        self.y1 = self.y0+self.w
        cv.coords(self.id, self.x0, self.y0, self.x1, self.y1)

cells =[]    
for r in range(grid_rows):
    cells.append([])
    for c in range(grid_columns):
        cell = grid(r,c)
        cells[r].append(cell)
        print(c)



class plat():
# платформа
    def __init__(self):
        self.w = wid
        self.h = hei
        self.x1 = 200
        self.y1 = 0
        self.x2 = self.x1+self.w
        self.y2 = self.y1+self.h
        self.c = choice(colors)
        self.id = cv.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill = self.c)

    def move(self):
        self.vx = 0
        self.vy = 1
        self.x1 += self.vx
        self.y1 += self.vy
        self.x2 = self.x1+self.w
        self.y2 = self.y1+self.h
        cv.coords(self.id, self.x1, self.y1, self.x2, self.y2)

# сделаем массив с шагами по х
gridx = []
for i in range(0,xm,wid):
    gridx.append(i)

ymax = grid_rows*hei

# расстановка списка платформ по случайному порядку    
# lpl = []
# for i in range(3):
#     p = plat()
#     p.x = choice(gridx)
#     lpl.append(p)

p = plat()
while p.y2 < ymax:
    p.move()
    time.sleep(0.01)
    cv.update()


def keypress(event):
    if event.keycode == 113 and p.x >= p.w:
        p.x -= p.w
    if event.keycode == 114 and (p.x+p.w) < xm:
        print(p.x+p.w)
        p.x += p.w



# 
# 
#     
# while (p.y+p.h) < ym:
#     p.move()
#     cv.update()
#     tk.bind('<Key>', keypress)
#     time.sleep(0.05)


tk.mainloop()

