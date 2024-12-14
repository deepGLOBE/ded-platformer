import pygame
from script import  load_image
player_image = load_image('image/players')
earth_image  = pygame.image.load('image/blocks/earth.png').convert_alpha()
center_image = pygame.image.load('image/blocks/center.png').convert_alpha()
box_image = pygame.image.load('image/blocks/box.png').convert_alpha()
water_image = pygame.image.load('image/blocks/water.png').convert_alpha()
players_image = pygame.image.load('image/players/player.png').convert_alpha()

players_image = pygame.transform.rotozoom(players_image, 0,0.9)

stop_image = pygame.image.load('image/blocks/stop (1).png').convert_alpha()
enemy_1_image = pygame.image.load('image/enemy/1/1.png').convert_alpha()
enemy_2_image = pygame.image.load('image/enemy/2/1.png').convert_alpha()
enemy_3_image = pygame.image.load('image/enemy/3/1.png').convert_alpha()
enemy_4_image = pygame.image.load('image/enemy/4/1.png').convert_alpha()
portal_image = pygame.image.load('image/portal/Portal_100x100px1.png')
monetka_image =pygame.image.load('image/item/monetka.png').convert_alpha()
skala_image = pygame.transform.scale(pygame.image.load('image/backgrund/2.jpg').convert_alpha(), (1200,800))











