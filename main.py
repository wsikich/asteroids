import pygame
import sys

from constants import *
from player import *
from asteroid import *
from asteroidfield import *


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatables = pygame.sprite.Group()

    drawables = pygame.sprite.Group()

    asteroids = pygame.sprite.Group()

    shots = pygame.sprite.Group()
    
    Player.containers = (updatables, drawables)

    Asteroid.containers = (updatables, drawables, asteroids)

    AsteroidField.containers = (updatables,)

    Shot.containers = (updatables, drawables, shots)
    
    avatar = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    asteroid_field = AsteroidField()

    clock = pygame.time.Clock()

    dt = 0

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for drawable in drawables:
            drawable.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        updatables.update(dt)
        for asteroid_object in asteroids:
            if asteroid_object.check_collision(avatar):
                print("Game over!")
                sys.exit()
        for asteroid_object in asteroids:
            for shot in shots:
                if asteroid_object.check_collision(shot):
                    asteroid_object.split()
                    shot.kill()


if __name__ == "__main__":
    main()
