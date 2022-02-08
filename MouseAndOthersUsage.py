import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()
pic1 = pygame.transform.scale(pygame.image.load('Assets/images/Ankit.png'), (600,600))
pic1Rect = pic1.get_rect(center=(300,300))
pic2 = pygame.transform.scale(pygame.image.load('Assets/images/mayookh_passport_photo.jpeg'), (600,600))
pic2Rect = pic2.get_rect(center=(300, -400))
black = pygame.Color(0,0,0)
white = pygame.Color(255, 255, 255)


while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit() 
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT:
                print("left button on mouse pressed")
                print(event.pos)
                screen.fill(black)
                screen.blit(pic1, event.pos)


            elif event.button == pygame.BUTTON_RIGHT:
                print("right button on mouse pressed")
                print(event.pos)
                screen.fill(black)
                screen.blit(pic2, (event.pos))
                

            elif event.button == pygame.BUTTON_WHEELDOWN:
                print("Wheel down at", event.pos)
                screen.fill(black)
                screen.blit(pic1, pic1Rect)
                screen.blit(pic2, pic2Rect)
                pic1Rect.centery += 20
                pic2Rect.centery += 20
                
                if pic1Rect.centery > 900:
                    pic1Rect.centery = -400
                elif pic2Rect.centery > 900:
                    pic2Rect.centery = -400
                
            
            elif event.button == pygame.BUTTON_WHEELUP: 
                print("Wheel up at ", event.pos)
                screen.fill(black)
                screen.blit(pic1, pic1Rect)
                screen.blit(pic2, pic2Rect)
                pic1Rect.centery -= 20
                pic2Rect.centery -= 20
                
                if pic1Rect.centery <= -400:
                    pic1Rect.centery = 1000
                elif pic2Rect.centery <= -400:
                    pic2Rect.centery = 1000
                
                





    pygame.display.update()
    clock.tick(120)