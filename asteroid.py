import pygame
import circleshape
import constants
import random


class Asteroid(circleshape.CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, surface):
        pygame.draw.circle(
            surface,
            (255, 255, 255),
            (int(self.position.x), int(self.position.y)),
            self.radius,
            2
        )

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        else:
            old_radius = self.radius
            random_angle = random.uniform(20, 50)
            new_angle_1 = self.velocity.rotate(random_angle)
            new_angle_2 = self.velocity.rotate(-random_angle)
            new_radius = old_radius - constants.ASTEROID_MIN_RADIUS
            new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_1.velocity = new_angle_1 * 1.2
            new_asteroid_2.velocity = new_angle_2 * 1.2
