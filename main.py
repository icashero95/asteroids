# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
import player
import asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group() 
    drawable = pygame.sprite.Group()
    rocks = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()
    player.Player.containers = (updatable, drawable)
    asteroid.Asteroid.containers = (rocks, updatable, drawable)
    AsteroidField.containers = (updatable)
    player.Shot.containers = (shots_group, updatable, drawable)
    ship = player.Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2), shots_group)
    asteroid_field = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        updatable.update(dt)
        for entity in drawable:
            entity.draw(screen)
        for rock in rocks:
            if ship.collision(rock) is True:
                print("Game Over")
                sys.exit()
        for rock in rocks:
            for bullet in shots_group:
                if bullet.collision(rock) is True:
                    bullet.kill()
                    rock.split()
        pygame.display.flip()
        time_passed = clock.tick(60)
        dt = time_passed / 1000


if __name__ == "__main__":
    main()