import pygame
import numpy as np
from arm import Arm

pygame.init()
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

seg_len = 30
arm0 = Arm(base=np.array([0, SCREEN_HEIGHT]), seg_len=seg_len*2)
arm1 = Arm(base=np.array([SCREEN_WIDTH//2, SCREEN_HEIGHT]), seg_len=seg_len)
arm2 = Arm(base=np.array([SCREEN_WIDTH, SCREEN_HEIGHT]), seg_len=seg_len*2)
arm3 = Arm(base=np.array([0, 0]), seg_len=seg_len*2)
arm4 = Arm(base=np.array([SCREEN_WIDTH//2, 0]), seg_len=seg_len)
arm5 = Arm(base=np.array([SCREEN_WIDTH, 0]), seg_len=seg_len*2)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0))

    arm0.update(np.asarray( pygame.mouse.get_pos() ))
    arm0.draw(screen)

    arm1.update(np.asarray( pygame.mouse.get_pos() ))
    arm1.draw(screen)

    arm2.update(np.asarray( pygame.mouse.get_pos() ))
    arm2.draw(screen)

    arm3.update(np.asarray( pygame.mouse.get_pos() ))
    arm3.draw(screen)

    arm4.update(np.asarray( pygame.mouse.get_pos() ))
    arm4.draw(screen)

    arm5.update(np.asarray( pygame.mouse.get_pos() ))
    arm5.draw(screen)

    pygame.display.update()

pygame.quit()
