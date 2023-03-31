import numpy as np
import pygame

class Segment():

    def __init__(self, x, y, length, angle, color=(255, 255, 255), width=3):
        self.a = np.array([x, y])
        self.b = np.array([0, 0])
        self.length = length
        self.angle = angle
        self.color = color
        self.width = width
        
    def follow(self, target):
        target = np.asarray(target)
        dir = target-self.a
        self.angle = np.arctan2(dir[1], dir[0])
        dir = -(dir * self.length / np.linalg.norm(dir))
        self.a = target + dir

    def update(self):
        dx = self.length * np.cos(self.angle)
        dy = self.length * np.sin(self.angle)
        self.b = np.array([self.a[0]+dx, self.a[1]+dy])
    
    def draw(self, s):
        pygame.draw.line(s, self.color, self.a, self.b, self.width)
