import pygame
from segment import Segment

pygame.init()
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

arm = []
for i in range(20):
    seg = Segment(300, 200, 10, 0, width=(i+1))
    arm.append(seg)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0))

    for i in range(len(arm)):
        if i == 0: arm[0].follow(pygame.mouse.get_pos())
        else: arm[i].follow(arm[i-1].a)
        arm[i].update()
        arm[i].draw(screen)

    pygame.display.update()

pygame.quit()
