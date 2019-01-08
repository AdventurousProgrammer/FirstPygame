import pygame
pygame.init()
win = pygame.display.set_mode((500,480))
pygame.display.set_caption("First Pygame Game")

walk_right = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walk_left = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png') 

x = 50
y = 400
width = 64
height = 64
vel = 5

screen_width = 500
screen_height = 480

is_jump = False
jump_count = 10
run = True

left = False
right = False
walk_count = 0

clock = pygame.time.Clock()

print(3//4)
def redraw_game_window():
    #update game window every frame, 27 frames per second
    #each entry in the arrays is 3 frames
    global walk_count #will be changing outside
    #27 frames per second
    win.blit(bg,(0,0)) 
    
    if walk_count + 1 >= 27:
        walk_count = 0
    
    if left:
        win.blit(walk_left[walk_count//3],(x,y))
        walk_count+=1
        
    elif right:
        win.blit(walk_right[walk_count//3],(x,y))
        walk_count+=1
    
    else:
        win.blit(char,(x,y))
        
        
    #final argument is dimensions, starting point top left corner
    pygame.display.update() #to update the screen

while run:
    clock.tick(27)   
     
    for event in pygame.event.get():
        #go through all the events
        if event.type == pygame.QUIT:
            run = False
    #movement hold down the arrow key
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x >= vel:
        left = True
        right = False
        x -= vel
    
    elif keys[pygame.K_RIGHT] and x + width + vel <= screen_width:
        left = False
        right = True
        x += vel
    else:
        right = False
        left = False;
        walk_count = 0
    if not(is_jump):
        if keys[pygame.K_SPACE]:
            is_jump = True
            right = False
            left = False
            walk_count = 0
    else:
        #for jumping think 2D motion from physics parabola
        #cant allow upward or downward movement
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            y -= (jump_count**2)*0.5*neg
            print('Jump Count: ' + str(jump_count) + 'y = ' + str(y))
            jump_count -= 1
        else:
            jump_count = 10
            is_jump = False
    redraw_game_window()
pygame.quit()