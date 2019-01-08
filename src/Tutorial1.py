import pygame
pygame.init()
win = pygame.display.set_mode((500,480))
pygame.display.set_caption("First Pygame Game")

walk_right = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walk_left = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png') 

screen_width = 500
screen_height = 480



clock = pygame.time.Clock()

class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.is_jump = False
        self.jump_count = 10
        self.left = False
        self.right = False
        self.walk_count = 0
    
    def draw(self,win):
        if self.walk_count + 1 >= 27:
            self.walk_count = 0
    
        if self.left:
            win.blit(walk_left[walk_count//3],(self.x,self.y))
            self.walk_count+=1
        
        elif self.right:
            win.blit(walk_right[self.walk_count//3],(self.x,self.y))
            self.walk_count+=1
    
        else:
            win.blit(char,(self.x,self.y))
        
def redraw_game_window():
    #update game window every frame, 27 frames per second
    #each entry in the arrays is 3 frames
    win.blit(bg,(0,0)) 
    man.draw(win)
    pygame.display.update() #to update the screen
    
man = player(300,410,64,64)
run = True

while run:
    clock.tick(27)   
     
    for event in pygame.event.get():
        #go through all the events
        if event.type == pygame.QUIT:
            run = False
    #movement hold down the arrow key
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and man.x >= man.vel:
        man.left = True
        man.right = False
        man.x -= man.vel
    
    elif keys[pygame.K_RIGHT] and man.x + man.width + man.vel <= screen_width:
        left = False
        right = True
        man.x += man.vel
    else:
        right = False
        left = False;
        walk_count = 0
    if not(man.is_jump):
        if keys[pygame.K_SPACE]:
            is_jump = True
            right = False
            left = False
            walk_count = 0
    else:
        #for jumping think 2D motion from physics parabola
        #cant allow upward or downward movement
        if man.jump_count >= -10:
            neg = 1
            if man.jump_count < 0:
                neg = -1
            man.y -= (man.jump_count**2)*0.5*neg
            #print('Jump Count: ' + str(man.jump_count) + 'y = ' + str(y))
            man.jump_count -= 1
        else:
            jump_count = 10
            is_jump = False
    redraw_game_window()
pygame.quit()