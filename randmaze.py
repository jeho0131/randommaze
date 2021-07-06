import pygame
import random

pygame.init()
size = [600, 600]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Maze")
clock = pygame.time.Clock()
color = (255,255,255)

big_wall_image = pygame.image.load("wall.png")
wall_image = pygame.transform.scale(big_wall_image, (10,10))

def r(l):
    n = random.randint(0,3)
    if l[n] == 1:
        n = r(l)

    return n

def Maze(x, y, s):
    no = [0,0,0,0]

    if y == 0 or (x, y-20) in s:
        no[0] = 1
    if x == 0 or (x-20, y) in s:
        no[1] = 1
    if y == 500 or (x, y+20) in s:
        no[2] = 1
    if x == 500 or (x+20, y) in s:
        no[3] = 1
    
    if no.count(1) >= 4:
        return s
    else:
        n = r(no)

    if n == 0:
        s.add((x,y-10))
        s.add((x,y-20))
        s = Maze(x,y-20,s)
        
    elif n == 1:
        s.add((x-10,y))
        s.add((x-20,y))
        s = Maze(x-20,y,s)
        
    elif n == 2:
        s.add((x,y+10))
        s.add((x,y+20))
        s = Maze(x,y+20,s)
        
    elif n == 3:
        s.add((x+10,y))
        s.add((x+20,y))
        s = Maze(x+20,y,s)
        
    if y == 0 or (x, y-20) in s:
        no[0] = 1
    if x == 0 or (x-20, y) in s:
        no[1] = 1
    if y == 500 or (x, y+20) in s:
        no[2] = 1
    if x == 500 or (x+20, y) in s:
        no[3] = 1
        
    if no.count(1) < 3:
        if (x, y-20) not in s and n != 0:
            s.add((x,y-10))
            s.add((x,y-20))
            s = Maze(x,y-20,s)

        if y == 0 or (x, y-20) in s:
            no[0] = 1
        if x == 0 or (x-20, y) in s:
            no[1] = 1
        if y == 500 or (x, y+20) in s:
            no[2] = 1
        if x == 500 or (x+20, y) in s:
            no[3] = 1
            
        if (x-20, y) not in s and n != 1:
            s.add((x-10,y))
            s.add((x-20,y))
            s = Maze(x-20,y,s)

        if y == 0 or (x, y-20) in s:
            no[0] = 1
        if x == 0 or (x-20, y) in s:
            no[1] = 1
        if y == 500 or (x, y+20) in s:
            no[2] = 1
        if x == 500 or (x+20, y) in s:
            no[3] = 1
            
        if (x, y+20) not in s and n != 2:
            s.add((x,y+10))
            s.add((x,y+20))
            s = Maze(x,y+20,s)

        if y == 0 or (x, y-20) in s:
            no[0] = 1
        if x == 0 or (x-20, y) in s:
            no[1] = 1
        if y == 500 or (x, y+20) in s:
            no[2] = 1
        if x == 500 or (x+20, y) in s:
            no[3] = 1
            
        if (x+20, y) not in s and n != 3:
            s.add((x+10,y))
            s.add((x+20,y))
            s = Maze(x+20,y,s)

    return s

def drawMaze(l):
    for i in range(52):
        for j in range(52):
            if (j*10,i*10) not in l:
                screen.blit(wall_image, (j*10 + 50, i*10 + 50))


xy = set()
xy.add((0,0))
a = Maze(0,0,xy)
l = []
l = list(a)
print(l)

while True:
    clock.tick(30)
    screen.fill(color)

    drawMaze(l)
    pygame.display.update()

    break

#3pygame.quit()
