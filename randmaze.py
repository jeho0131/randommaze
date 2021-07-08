import pygame, sys, random
from pygame.locals import *

pygame.init()
size = [600, 600]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Maze")
clock = pygame.time.Clock()
color = (255,255,255)
gameover = True

big_wall_image = pygame.image.load("wall.png")
wall_image = pygame.transform.scale(big_wall_image, (10,10))
big_player_image = pygame.image.load("player.png")
player_image = pygame.transform.scale(big_player_image, (10,10))

g = 0
xm = 500
ym = 500
px = 50
py = 50
gxy = [0,0]

def r(l):
    n = random.randint(0,3)
    if l[n] == 1:
        n = r(l)

    return n

def noc(x, y, s):
    no = [0,0,0,0]
    
    if y == 0 or (x, y-20) in s:
        no[0] = 1
    if x == 0 or (x-20, y) in s:
        no[1] = 1
    if y == ym or (x, y+20) in s:
        no[2] = 1
    if x == xm or (x+20, y) in s:
        no[3] = 1

    return no

def Maze(x, y, s):
    global g
    no = [0,0,0,0]

    no = noc(x, y, s)
    
    if no.count(1) >= 4:
        if g == 0:
          if y == ym:
              s.add((x, y+10))
              gxy[0] = x
              gxy[1] = y+20
              g += 1
          elif x == xm:
              s.add((x+10, y))
              gxy[0] = x+20
              gxy[1] = y
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
        
    no = noc(x, y, s)
        
    if ((x, y-20) not in s and n != 0) and no[0] == 0:
        s.add((x,y-10))
        s.add((x,y-20))
        s = Maze(x,y-20,s)
        no = noc(x, y, s)
            
    if ((x-20, y) not in s and n != 1) and no[1] == 0:
        s.add((x-10,y))
        s.add((x-20,y))
        s = Maze(x-20,y,s)
        no = noc(x, y, s)
            
    if ((x, y+20) not in s and n != 2) and no[2] == 0:
        s.add((x,y+10))
        s.add((x,y+20))
        s = Maze(x,y+20,s)
        no = noc(x, y, s)
            
    if ((x+20, y) not in s and n != 3) and no[3] == 0:
        s.add((x+10,y))
        s.add((x+20,y))
        s = Maze(x+20,y,s)
        no = noc(x, y, s)

    
    return s

def drawMaze(l):
    for i in range(int(ym / 10) + 2):
        for j in range(int(xm / 10) + 2):
            if (j*10,i*10) not in l:
                screen.blit(wall_image, (j*10 + 50, i*10 + 50))

    for k in range(int(ym / 10) + 3):
      screen.blit(wall_image, (k * 10 + 40, 40))
      screen.blit(wall_image, (40, k * 10 + 40))

def movePlayer():
    global px, py, gameover
    
    if pressed_keys[K_w] and (px-50, py-60) in l:
        py -= 10
    elif pressed_keys[K_a] and (px-60, py-50) in l:
        px -= 10
    elif pressed_keys[K_a] and (px-50, py-40) in l:
        py += 10
    elif pressed_keys[K_a] and (px-40, py-50) in l:
        px += 10
        
    if gxy[0] == px-50 and gxy[1] == py-50:
        gameover = False
        
def drawPlayer():
    screen.blit(player_image, (px, py))

xy = set()
xy.add((0,0))
a = Maze(0,0,xy)
l = []
l = list(a)
l.sort()

while gameover:
    clock.tick(10)
    screen.fill(color)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    movePlayer()
    drawPlayer()
    drawMaze(l)
    pygame.display.update()
