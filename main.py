import pygame
import random
import sys
import os

pageme.init()
width,height= 900, 400
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("diono run adventure")
clock = pygame.time.clock()
Font = pygame.font.Sysfont("arial",24)

#colors 
BG_COLOR = (135,206,235)
brown= (120,80,40)
red = (220,60,60)
white = (255,255,255)

# load sprites
flor_normal_img= pygame.image.load(os.path.join("sprits","flor normal.png")).convert_alpha()
agachada_img= pygame.image.load(os.path.join("sprits","agachada.png")).convert_alpha()
dino_normal_img= pygame.image.load(os.path.join("sprits","fuego.png")).convert_alpha()
dino_normal_img= pygame.image.load(os.path.join("sprits","roca.png")).convert_alpha()
dino_normal_img= pygame.image.load(os.path.join("sprits","pajaro.png")).convert_alpha()

# scale sprites to expected sizes
flor normal_img=pygame.transform.scale(dimo_normal_img,(60,80))
agachada img=pygame.transform.scale(dimo_normal_img,(60,40))
fuego_img=pygame.transform.scale(dimo_normal_img,(30,60))
roca_img=pygame.transform.scale(dimo_normal_img,(40,40))
pajaro_img=pygame.transform.scale(dimo_normal_img,(50,30))


def run_game():
# dino settings
dino_img = dino_normal_img
dino= pygame.rect(80,height - 120,60,80)
dino_vel_y= 0
gravity= 0.8
jump_strenght = -15
on_ground = true 
is_ducking=False

# graund
ground_y=height-40

#obstacles and birts 
obstacles = []  #list of (rect,image)
birds =[]       #list of rects
spaw_timer=0
spaw_delay =90
