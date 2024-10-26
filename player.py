import pygame
from circleshape import CircleShape
from constants import *

#Fuck you, I won't do what you tell me

import math

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        
    
    def move(self, dt):
        unit_vector = (0, 1)
        pointing_vector_adjusted_for_speed = []
        angle_radians = math.radians(self.rotation)
        cos_angle = math.cos(angle_radians)
        sin_angle = math.sin(angle_radians)
        rotated_vector = (
            unit_vector[0] * cos_angle - unit_vector[1] * sin_angle,
            unit_vector[0] * sin_angle + unit_vector[1] * cos_angle
        )
        pointing_vector_adjusted_for_speed.append(PLAYER_SPEED * dt * rotated_vector[0])
        pointing_vector_adjusted_for_speed.append(PLAYER_SPEED * dt * rotated_vector[1])
        x_element = pointing_vector_adjusted_for_speed[0]
        y_element = pointing_vector_adjusted_for_speed[1]
        self.position += (x_element, y_element)