from email.header import Header

import pygame
import  os
import sys
import random

from pygame.examples.moveit import WIDTH, HEIGHT

pygame.init()
current_path = os.path.dirname(__file__)
os.chdir(current_path)
WIDTH = 1200
HEIGHT = 800
FPS = 60
sc = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
from load import*

def restart():
    global players_group, earth_group,box_group,center_group,water_group,camera_group,player
    players_group = pygame.sprite.Group()
    earth_group = pygame.sprite.Group()
    box_group = pygame.sprite.Group()
    center_group = pygame.sprite.Group()
    water_group = pygame.sprite.Group()
    camera_group = pygame.sprite.Group()
    player = Player(players_image, (300,300))
    players_group.add(player)




def gamelvl():
    sc.fill('black')
    players_group.update()
    players_group.draw(sc)
    earth_group.update(0)
    earth_group.draw(sc)
    box_group.update(0)
    box_group.draw(sc)
    water_group.update(0)
    water_group.draw(sc)
    center_group.update(0)
    center_group.draw(sc)
    pygame.display.update()






def drawMaps(nameFile,):
    maps = []
    source = "game_lvl/" + str(nameFile)
    with open(source,"r") as file:
        for i in range(0, 10):
            maps.append(file.readline().replace("\n", "").split(",")[0:-1])
    pos = [0,0]
    for i in range(0, len(maps)):
        pos[1] = i * 80
        for j in range(0,len(maps[0])):
            pos[0] = 80 * j
            if maps[i][j] == "3":
                earth = Earth(earth_image,pos)
                earth_group.add(earth)
                camera_group.add(earth)

            elif maps[i][j] == "1":
                box = Box(box_image,pos)
                box_group.add(box)
                camera_group.add(box)

            elif maps[i][j] == "4":
                water = Water(water_image,pos)
                water_group.add(water)
                camera_group.add(water)

            elif maps[i][j] == "2":
                center = Center(center_image,pos)
                center_group.add(center)
                camera_group.add(center)














































class Earth(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self,step):
        self.rect.x += step
        if pygame.sprite.spritecollide(self, players_group , False):
            if abs(self.rect.top - player.rect.bottom) < 15:
                player.rect.bottom = self.rect.top - 5
                player.on_ground = True

            if abs(self.rect.bottom - player.rect.top) <15:
                player.rect.top = self.rect.bottom + 5
                player.velocity = 0

            if (abs(self.rect.left - player.rect.right) <15
                     and abs(self.rect.centery - player.rect.centery) <50):
                player.rect.right = self.rect.left

            if (abs(self.rect.right - player.rect.left) <15
                     and abs(self.rect.centery - player.rect.centery) <50):
                player.rect.left = self.rect.right


class Water(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self,step):
        self.rect.x += step
        if pygame.sprite.spritecollide(self, players_group, False):
            if abs(self.rect.top - player.rect.bottom) < 15:
                player.rect.bottom = self.rect.top - 5
                player.on_ground = True

            if abs(self.rect.bottom - player.rect.top) < 15:
                player.rect.top = self.rect.bottom + 5
                player.velocity = 0

            if (abs(self.rect.left - player.rect.right) < 15
                    and abs(self.rect.centery - player.rect.centery) < 50):
                player.rect.right = self.rect.left

            if (abs(self.rect.right - player.rect.left) < 15
                    and abs(self.rect.centery - player.rect.centery) < 50):
                player.rect.left = self.rect.right


class Box(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self,step):
        self.rect.x += step
        if pygame.sprite.spritecollide(self, players_group, False):
            if abs(self.rect.top - player.rect.bottom) < 15:
                player.rect.bottom = self.rect.top - 5
                player.on_ground = True

            if abs(self.rect.bottom - player.rect.top) < 15:
                player.rect.top = self.rect.bottom + 5
                player.velocity = 0

            if (abs(self.rect.left - player.rect.right) < 15
                    and abs(self.rect.centery - player.rect.centery) < 50):
                player.rect.right = self.rect.left

            if (abs(self.rect.right - player.rect.left) < 15
                    and abs(self.rect.centery - player.rect.centery) < 50):
                player.rect.left = self.rect.right

class Center(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self,step):
        self.rect.x += step
        if pygame.sprite.spritecollide(self, players_group, False):
            if abs(self.rect.top - player.rect.bottom) < 15:
                player.rect.bottom = self.rect.top - 5
                player.on_ground = True

            if abs(self.rect.bottom - player.rect.top) < 15:
                player.rect.top = self.rect.bottom + 5
                player.velocity = 0

            if (abs(self.rect.left - player.rect.right) < 15
                    and abs(self.rect.centery - player.rect.centery) < 50):
                player.rect.right = self.rect.left

            if (abs(self.rect.right - player.rect.left) < 15
                    and abs(self.rect.centery - player.rect.centery) < 50):
                player.rect.left = self.rect.right


class Player(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.speed = 5
        self.velocity_y = 0
        self.on_ground = True

    def update(self, *args, **kwargs):
        key = pygame.key.get_pressed()
        if key[pygame.K_d]:
            self.rect.x += self.speed
            if self.rect.right > WIDTH/2 + 500:
                self.rect.right = WIDTH/2 + 500
                camera_group.update(-self.speed)
        elif key[pygame.K_a]:
            self.rect.x -= self.speed
            if self.rect.left < WIDTH/2 - 500:
                self.rect.left = WIDTH/2 - 500
                camera_group.update(self.speed)
        if key[pygame.K_SPACE] and self.on_ground:
            self.velocity_y = -17
            self.on_ground = False
        self.rect.y += self.velocity_y
        self.velocity_y += 1
        if self.velocity_y > 10:
            self.velocity_y = 10










restart()
drawMaps('1.txt')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    gamelvl()
    clock.tick(FPS)
































