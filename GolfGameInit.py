# ball collider
import pygame
import sys
import time
from pygame.constants import MOUSEBUTTONUP


def checkIfScored(playerRect, holeRect):
    if playerRect.colliderect(holeRect):
        return True
    return False


def checkCollision(rect): 
    if rect.left <= 0:
        return "left"
    elif rect.right >= 600:
        return "right"
    elif rect.top <= 0:
        return "top"
    elif rect.bottom >= 600:
        return "bottom"
    
    return "none"


def getBaseAndHeight(x, y):
    base = x[0] - y[0]
    height = x[1] - y[1]   

    
    return (base, height)
    

def checkMousePos(mousePos, rect): 
    if mousePos[0] in range(rect.left, rect.right) and mousePos[1] in range(rect.top, rect.bottom):
        return True
    
    return False


pygame.init()
screen = pygame.display.set_mode((600,600))
black = pygame.Color(0,0,0)
clock = pygame.time.Clock()


ballPic = pygame.image.load('Assets/images/ball.png').convert_alpha()
ballPic = pygame.transform.scale(ballPic, (32,32))
ballPic_rect = ballPic.get_rect(center=(500,300))
backgroundPic = pygame.image.load('Assets/images/golf-background.jpg').convert_alpha()
backgroundPic = pygame.transform.scale(backgroundPic, (600,600))
golfHole = pygame.image.load('Assets/images/golf-hole.jpeg').convert_alpha()
golfHole = pygame.transform.scale(golfHole, (32,32))
golfHole_rect = golfHole.get_rect(center=(300,300))

ball_movement_x = 0
ball_movement_y = 0
friction = 0.98

mouse_state = "none"


while True:
    mouse_pos = pygame.mouse.get_pos()
    screen.fill(black)
    screen.blit(backgroundPic, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT and checkMousePos(mouse_pos, ballPic_rect) == True:
                print("Mouse Pressed at: ", pygame.mouse.get_pos())
                pos1 = event.pos
                mouse_state = "pressed"


        elif event.type == MOUSEBUTTONUP:
            if event.button == pygame.BUTTON_LEFT and checkMousePos(mouse_pos, ballPic_rect) == False: 
                print("mouse released at: ", pygame.mouse.get_pos())
                pos2 = event.pos
                if mouse_state == "pressed":
                    mouse_state = "pressed and released"
            
    

    if mouse_state == "pressed and released":
        baseHeight = getBaseAndHeight(pos1, pos2)
        mouse_state = "none"
        ball_movement_x = (baseHeight[0])/5
        ball_movement_y = (baseHeight[1])/5


    # collision check ifs
    collisionCheck = checkCollision(ballPic_rect)
    if collisionCheck == "right" or collisionCheck == "left": 
        ball_movement_x = -ball_movement_x
    elif collisionCheck == "top" or collisionCheck == "bottom":
        ball_movement_y = -ball_movement_y


    # movement
    ballPic_rect.centerx += ball_movement_x
    ballPic_rect.centery += ball_movement_y
    ball_movement_x *= friction
    ball_movement_y *= friction

    # friction lower cutoff
    if abs(ball_movement_x) <= 0.5 and abs(ball_movement_y) <= 0.5:
        ball_movement_x = 0
        ball_movement_y = 0
   
    if (ballPic_rect.left < 0 or ballPic_rect.right > 600) and (ball_movement_x == 0):
        ballPic_rect.centerx = 20
    
    if (ballPic_rect.top < 0 or ballPic_rect.bottom > 600) and (ball_movement_y == 0): 
        ballPic_rect.centery = 20

    print("movement speeds: ", ball_movement_x, ball_movement_y)
    
    if checkIfScored(ballPic_rect, golfHole_rect):
        print("Yay U scored!!!!!!!!!!!!")
        break

    screen.blit(ballPic, ballPic_rect)
    screen.blit(golfHole, golfHole_rect)
    pygame.display.update()
    clock.tick(60)