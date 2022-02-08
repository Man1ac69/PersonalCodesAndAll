import pygame
import sys

clock = pygame.time.Clock()
pic_x_pos = 0

# gravity and all
NewPic_movement = 0
gravity = 0.125


def drawingFloorAgain():
    screen.blit(thePic, (pic_x_pos, 400))
    screen.blit(thePic, (pic_x_pos + 288, 400))
    screen.blit(thePic, (pic_x_pos + 512, 400))


pygame.init()
screen = pygame.display.set_mode((512, 512))

blue = pygame.Color(0, 0, 255)
black = pygame.Color(0, 0, 0)
thePic = pygame.image.load('/home/hw814745/spotiAds.png')
NewPic = pygame.image.load('/home/hw814745/Programs/game/Flappy_bird/Assets/images/redbird-midflap.png')
NewPic_rect = NewPic.get_rect(center=(50, 288))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("lol")
                NewPic_movement = 0
                NewPic_movement -= 3

    NewPic_movement += gravity
    NewPic_rect.centery += NewPic_movement
    pic_x_pos -= 1
    screen.fill(black)
    screen.blit(NewPic, NewPic_rect)



    pygame.display.update()
    clock.tick(120)
