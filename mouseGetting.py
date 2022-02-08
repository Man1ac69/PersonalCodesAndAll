import pygame
import sys


global pos1, pos2

from pygame.constants import MOUSEBUTTONUP

def distanceFromPythagoras(baseHeightTuple): 
    distance = int(((baseHeightTuple[0]**2) + (baseHeightTuple[1]**2)**0.5))
    return distance

def getBaseAndHeight(x, y):
    base = abs(x[0] - y[0])
    height = abs(x[1]- y[1])  

    
    return (base, height)
    

pygame.init() 
screen = pygame.display.set_mode((600,600))

mouse_state = "none"
while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT:
                print("Mouse Pressed at: ", pygame.mouse.get_pos())
                pos1 = event.pos
                mouse_state = "pressed"

        elif event.type == MOUSEBUTTONUP:
            if event.button == pygame.BUTTON_LEFT: 
                print("mouse released at: ", pygame.mouse.get_pos())
                pos2 = event.pos
                mouse_state = "pressed and released"


    
    # pos1[1] and pos2[1] are x coordinates. 
    # pos1[2] and pos2[2] are y coordinates
    # assume right angled triangle
    # base will be pos2[1] - pos1[1], if pos2[1] > pos1[1], vice versa.
    # height will be pos1[2] - pos2[2], if pos1[2] > pos2[2], vice versa.
    if mouse_state == "pressed and released":
        baseHeight = getBaseAndHeight(pos1, pos2)
        clickDistance = distanceFromPythagoras(baseHeight)
        print("Distance from click and release: ", clickDistance)
        mouse_state = "none"




    pygame.display.update()