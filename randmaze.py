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

g = 0
xm = 500
ym = 500

def r(l):
    n = random.randint(0,3)
    if l[n] == 1:
        n = r(l)

    return n

def Maze(x, y, s):
    global g
    no = [0,0,0,0]

    if y == 0 or (x, y-20) in s:
        no[0] = 1
    if x == 0 or (x-20, y) in s:
        no[1] = 1
    if y == ym or (x, y+20) in s:
        no[2] = 1
    if x == xm or (x+20, y) in s:
        no[3] = 1
    
    if no.count(1) >= 4:
        if g == 0:
          if y == ym:
              s.add((x, y+10))
              g += 1
          elif x == xm:
              s.add((x+10, y))
              g += 1
          
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
    if y == ym or (x, y+20) in s:
        no[2] = 1
    if x == xm or (x+20, y) in s:
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
        if y == ym or (x, y+20) in s:
            no[2] = 1
        if x == xm or (x+20, y) in s:
            no[3] = 1
            
        if (x-20, y) not in s and n != 1:
            s.add((x-10,y))
            s.add((x-20,y))
            s = Maze(x-20,y,s)

        if y == 0 or (x, y-20) in s:
            no[0] = 1
        if x == 0 or (x-20, y) in s:
            no[1] = 1
        if y == ym or (x, y+20) in s:
            no[2] = 1
        if x == xm or (x+20, y) in s:
            no[3] = 1
            
        if (x, y+20) not in s and n != 2:
            s.add((x,y+10))
            s.add((x,y+20))
            s = Maze(x,y+20,s)

        if y == 0 or (x, y-20) in s:
            no[0] = 1
        if x == 0 or (x-20, y) in s:
            no[1] = 1
        if y == ym or (x, y+20) in s:
            no[2] = 1
        if x == xm or (x+20, y) in s:
            no[3] = 1
            
        if (x+20, y) not in s and n != 3:
            s.add((x+10,y))
            s.add((x+20,y))
            s = Maze(x+20,y,s)

    return s

def drawMaze(l):
    for i in range(int(ym / 10) + 2):
        for j in range(int(xm / 10) + 2):
            if (j*10,i*10) not in l:
                screen.blit(wall_image, (j*10 + 50, i*10 + 50))

    for k in range(int(ym / 10) + 1):
      screen.blit(wall_image, (k * 10 + 60, 40))
      screen.blit(wall_image, (40, k * 10 + 60))

xy = set()
xy.add((0,0))
a = Maze(0,0,xy)
l = []
l = list(a)

while True:
    clock.tick(30)
    screen.fill(color)

    drawMaze(l)
    pygame.display.update()

    break

#pygame.quit()
