import pygame
import random
from circleshape import CircleShape
from constants import *



class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0

    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, width = 2)

    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        angle = random.uniform(20,50)
        new_asteroid_plus_angle_velocity = self.velocity.rotate(angle)
        new_asteroid_minus_angle_velocity = self.velocity.rotate(-angle)

        new_asteroids_radius = self.radius
        new_asteroids_radius -= ASTEROID_MIN_RADIUS

        new_asteroid_plus_angle = Asteroid(self.position.x, self.position.y, new_asteroids_radius)
        new_asteroid_minus_angle = Asteroid(self.position.x, self.position.y, new_asteroids_radius)

        new_asteroid_plus_angle.velocity = new_asteroid_plus_angle_velocity * 1.2
        new_asteroid_minus_angle.velocity = new_asteroid_minus_angle_velocity * 1.2

