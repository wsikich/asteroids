import pygame
import random

from circleshape import *
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = radius
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position), self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        
        vector1 = self.velocity.rotate(random_angle)
        vector2 = self.velocity.rotate(-random_angle)
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        self.radius = new_radius
        
        new_asteroid1 = Asteroid(0, 0, new_radius)
        new_asteroid2 = Asteroid(0, 0, new_radius)

        new_asteroid1.position += self.position
        new_asteroid2.position += self.position

        new_asteroid1.velocity = vector1 * 1.2
        new_asteroid2.velocity = vector2 * 1.2
