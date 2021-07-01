import random

def r(l):
    n = random.randint(0,3)
    if n in l:
        n = r(l)

    return n

def makeMaze(x, y, s):
    no = []

    if y == 0 or (x, y-2) in s:
        no.append(0)
    if x == 0 or (x-2, y) in s:
        no.append(1)
    if y == 10 or (x, y+2) in s:
        no.append(2)
    if x == 10 or (x+2, y) in s:
        no.append(3)
    
    if len(no) >= 4:
        return s
    else:
        n = r(no)

    if n == 0:
        s.add((x,y-1))
        s.add((x,y-2))
        s = makeMaze(x,y-2,s)
        
    elif n == 1:
        s.add((x-1,y))
        s.add((x-2,y))
        s = makeMaze(x-2,y,s)
        
    elif n == 2:
        s.add((x,y+1))
        s.add((x,y+2))
        s = makeMaze(x,y+2,s)
        
    elif n == 3:
        s.add((x+1,y))
        s.add((x+2,y))
        s = makeMaze(x+2,y,s)

    if len(no) < 3:
        if (x, y-2) not in s and n != 0:
            s.add((x,y-1))
            s.add((x,y-2))
            s = makeMaze(x,y-2,s)
            
        if (x-2, y) not in s and n != 1:
            s.add((x-1,y))
            s.add((x-2,y))
            s = makeMaze(x-2,y,s)
            
        if (x, y+2) not in s and n != 2:
            s.add((x,y+1))
            s.add((x,y+2))
            s = makeMaze(x,y+2,s)
            
        if (x+2, y) not in s and n != 3:
            s.add((x+1,y))
            s.add((x+2,y))
            s = makeMaze(x+2,y,s)

    return s

xy = set()
xy.add((0,0))
a = makeMaze(0,0,xy)
l = []
l = list(a)
print(l)
