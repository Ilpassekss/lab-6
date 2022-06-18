from settings import *
import pygame
import math
import time 


class Bullet:
    def __init__(self, bullet_angle, start_pos):
        self.coords = start_pos
        self.angle = bullet_angle
        self.image = pygame.image.load("e4b.png").convert_alpha()
        self.rect = self.image.get_rect(center = self.coords)

    def update(self):
        self.coords[0] += bullet_speed * math.cos(self.angle)
        self.coords[1] += bullet_speed * math.sin(self.angle)
        self.rect.centerx = self.coords[0]
        self.rect.centery = self.coords[1]

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Zombie:
    def __init__(self, posx, posy, speed):
        self.pos = [posx, posy]
        self.zomb_surf = pygame.image.load("zombie.png")
        self.zomb_rect = self.zomb_surf.get_rect(center=[self.pos[0], self.pos[1]])
        self.health = 100
        self.speed = speed
        self.angle = 0

    def zomb_update(self, sold_pos):
        self.angle = math.atan2(self.pos[0] - sold_pos[0], self.pos[1] - sold_pos[1]) + math.pi/2

        self.pos[0] += math.cos(self.angle) * self.speed
        self.pos[1] -= math.sin(self.angle) * self.speed

        self.zomb_rect.centerx = self.pos[0]
        self.zomb_rect.centery = self.pos[1]

        return self.pos


class Player:
    def __init__(self):
        self.x = player_x
        self.y = player_y

        self.angle = player_angle
        self.sold_angle = sol_angle

        self.counter = 0

        self.delay = player_delay

    @property
    def pos(self):
        return self.x, self.y

    def movement(self, bullets):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.y -= player_speed
            if self.y < 0:
                self.y = 0
        if keys[pygame.K_s]:
            self.y += player_speed
            if self.y > 768:
                self.y = 768
        if keys[pygame.K_a]:
            self.x -= player_speed
            if self.x < 0:
                self.x = 0
        if keys[pygame.K_d]:
            self.x += player_speed
            if self.x > 1366:
                self.x = 1366
        if keys[pygame.K_LEFT]:
            self.sold_angle += 4
            self.angle -= 0.06981317008
        if keys[pygame.K_RIGHT]:
            self.sold_angle -= 4
            self.angle += 0.06981317008
        if keys[pygame.K_SPACE]:
            self.shoot(bullets)

    def shoot(self, bullets):
        if self.counter % self.delay == 0:
            bullets.append(Bullet(self.angle, [self.x + height * math.cos(self.angle),
                                               self.y + height * math.sin(self.angle)]))
        self.counter += 1
        self.counter %= FPS

