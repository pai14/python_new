from turtle import *
from random import randrange as rnd

speed(10)

for i in range(10):
    color('blue','red')
    begin_fill()
    pu()
    x = rnd(-200,200)
    y = rnd(-200,200)
    r = rnd(100)
    setpos(x,y)
    pd()
    circle(r)
    pu()
    end_fill()


done()

'''

def sq():
    l = rnd(5, 100)
    pu()
    rt(rnd(360))
    color('green', 'lightgreen')
    begin_fill()
    pd()
    for i in range (4):
        fd(l)
        rt(90)
    pu()
    end_fill()

for u in range(10):
    pu()
    setpos(rnd(-200, 200),rnd(-200, 200))
    sq()

done()


from turtle import *
speed(1)
 
def c1():
    x,y = pos()
    pu()
    setpos(x, y+30)
    pd()
    setpos(x+30, y+60)
    setpos(x+30, y)
    pu()

def c2():
    x,y = pos()
    pu()
    setpos(x, y+60)
    pd()
    setpos(x+30, y+60)
    setpos(x+30, y+30)
    setpos(x,y)
    setpos(x+30,y)
    pu()
    
def c0():
    x,y = pos()
    pd()
    setpos(x,y+60)
    setpos(x+30,y+60)
    setpos(x+30,y)
    setpos(x,y)
    pu()
    setpos(x+30,y)

def c6():    
    x,y = pos()
    pd()
    setpos(x,y+30)
    setpos(x+30, y+60)
    pu()
    setpos(x,y+30)
    pd()
    setpos(x+30,y+30)
    setpos(x+30,y)
    setpos(x,y)
    pu()
    setpos(x+30,y)
    
    
    
    
c1()
x,y = pos()
setpos(x+10,y)
c2()
x,y = pos()
setpos(x+10,y)
c0()
x,y = pos()
setpos(x+10,y)
c6()

done()
'''