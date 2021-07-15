import pygame, sys, random, time
from pygame.locals import *

xm = 400
ym = 400

pygame.init()
size = [xm+100, ym + 100]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Maze")
clock = pygame.time.Clock()
color = (255,255,255)
gameover = True

big_wall_image = pygame.image.load("wall.png")
wall_image = pygame.transform.scale(big_wall_image, (10,10))
big_player_image = pygame.image.load("player.png")
player_image = pygame.transform.scale(big_player_image, (10,10))

font = pygame.font.Font(None, 40)
endfont = pygame.font.Font(None, 60)

g = 0
px = int(xm / 2) + 50
py = int(ym / 2) + 50
gxy = [0,0]
ml = []
mazechange = time.time()

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
        if y == ym and g == 0:
            s.add((x, y+10))
            gxy[0] = x
            gxy[1] = y+20
            g += 1
        if x == xm and g == 0:
            s.add((x+10, y))
            gxy[0] = x+20
            gxy[1] = y
            g += 1
        if y == 0 and g == 0:
            s.add((x, y-10))
            gxy[0] = x
            gxy[1] = y-20
            g += 1
        if x == 0 and g == 0:
            s.add((x-10, y))
            gxy[0] = x-20
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

    for k in range(int(xm / 10) + 3):
      if (k*10 - 10, -10) not in l:
          screen.blit(wall_image, (k * 10 + 40, 40))
          
    for m in range(int(ym/10) + 3):
      if (-10, m*10 - 10) not in l:
          screen.blit(wall_image, (40, m * 10 + 40))

def movePlayer():
    global px, py, gameover
    
    if (pressed_keys[K_w] or pressed_keys[K_UP]) and (px-50, py-60) in ml:
        py -= 10
    elif (pressed_keys[K_a] or pressed_keys[K_LEFT]) and (px-60, py-50) in ml:
        px -= 10
    elif (pressed_keys[K_s] or pressed_keys[K_DOWN]) and (px-50, py-40) in ml:
        py += 10
    elif (pressed_keys[K_d] or pressed_keys[K_RIGHT]) and (px-40, py-50) in ml:
        px += 10
        
    if ((gxy[0] == px-50 and gxy[1] == py-40) or (gxy[0] == px-40 and gxy[1] == py-50)) or ((gxy[0] == px-60 and gxy[1] == py-50) or (gxy[0] == px-50 and gxy[1] == py - 60)):
        gameover = False

def makeMaze():
    xy = set()
    xy.add((int(xm / 2),int(ym/2)))
    a = Maze(int(xm / 2),int(ym/2),xy)
    l = []
    l = list(a)
    l.sort()
    return l
        
def drawPlayer():
    screen.blit(player_image, (px, py))

def timec():
    global ml, mazechange, g
    t = 30 - (time.time() - mazechange)
    txt = font.render(str(int(t)), True, (255,0,0))
    tx = int(size[0] / 2 - txt.get_width() / 2)
    ty = int(size[1] * 1 / 24 - txt.get_height() / 2)

    screen.blit(txt, (tx,ty))
    
    if time.time() - mazechange > 30:
        g = 0
        ml = makeMaze()
        mazechange = time.time()

ml = makeMaze()

while gameover:
    clock.tick(10)
    screen.fill(color)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    pressed_keys = pygame.key.get_pressed()

    movePlayer()
    drawPlayer()
    drawMaze(ml)
    timec()
    pygame.display.update()

screen.fill(color)
    
txt = endfont.render("Congratulation!", True, (0,255,0))
tx = int(size[0] / 2 - txt.get_width() / 2)
ty = int(size[1] / 2 - txt.get_height() / 2)
screen.blit(txt, (tx,ty))

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()
