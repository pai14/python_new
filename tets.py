from tkinter import *

numrows = 6         # общее количество строк
numcolumns = 10     # общее количество столбцов
cell_width = 26     # ширина ячейки
cell_border = 2     # ширина бордюра
initx = 0           # начальная позиция
inity = 0           # начальная позиция

class cell():
    def __init__(self, r, c):
        self.r = r 
        self.c = c 
        self.cid = canva.create_rectangle(0, 0, cell_width, cell_width, fill='grey', width=0, tag=str(self.r)) # размечаем ячейку
        self.paint()

    def paint(self):
        self.x1 = initx + cell_border + (cell_width + cell_border) * self.c
        self.x2 = self.x1 + cell_width
        self.y1 = inity + cell_border + (cell_width + cell_border) * self.r
        self.y2 = self.y1 + cell_width
        canva.coords(self.cid, self.x1, self.y1, self.x2, self.y2)

root = Tk()
root.geometry('300x300')
canva = Canvas(root, width = 300, height = 300, bg = 'black')
canva.pack(fill =  BOTH)

ac = []
for r in range(numrows):
    ac.append([])
    for c in range (numcolumns):
        ac[r].append(cell(r,c).paint())

#id0 = cell(2,2).paint()
#cx1, cy1, cx2, cy2 = canva.coords(cell(2,2).paint())
canva.destroy('3')
#ii = canva.coords(cell(7,3))


bottom = inity + (cell_width + cell_border) * numrows
#id1 = cell (1,1).id
#idd = canva.create_rectangle(id1)



root.mainloop()