import pygame
from constants import *
from player import Player
from asteroidfield import *
from shot import *

def main():
    pygame.get_init()
    clock = pygame.time.Clock()
    dt = 0

    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()

    Player.containers = (updatable_group, drawable_group)
    Asteroid.containers = (asteroids_group, updatable_group, drawable_group)
    AsteroidField.containers = (updatable_group)
    Shot.containers = (updatable_group, drawable_group, shots_group)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(000000)

        for obj in updatable_group:
            obj.update(dt)

        for obj in drawable_group:
            obj.draw(screen)
        
        for obj in asteroids_group:
            if obj.collision(player) == True:
                print('Game over!')
                exit()
        
        for obj in asteroids_group:
            for bullet in shots_group:
                if obj.collision(bullet) == True:
                    bullet.kill()
                    obj.kill()


        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
