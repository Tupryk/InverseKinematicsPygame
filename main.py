import pygame
import numpy as np
from segment import Segment

pygame.init()
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

arm = []
seg_count = 7
for i in range(seg_count):
    width = i+1
    seg = Segment(300, 200, 50, 0, width=width)
    arm.append(seg)

base = np.array([SCREEN_WIDTH//2, SCREEN_HEIGHT])

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0))

    arm[0].follow(np.asarray( pygame.mouse.get_pos() ))
    arm[0].update()

    for i in range(1, len(arm)):
        arm[i].follow(arm[i-1].a)
        arm[i].update()

    arm[-1].set_a(base)

    for i in range(len(arm)-2, -1, -1):
        arm[i].set_a(arm[i+1].b)

    for seg in arm:
        seg.draw(screen)

    pygame.display.update()

pygame.quit()
