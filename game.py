import sys
import pygame
import random
from pygame.locals import *
from Sky import Sky
from Ground import Ground
from Cactus import Cactus
from Dino import Dino

FPS = 30
SCREENWIDTH = 400
SCREENHEIGHT = 300
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

DINO_IMAGE = pygame.image.load('assets/images/dino1.png')
DINO_IMAGE_2 = pygame.image.load('assets/images/dino2.png')
SKY_IMAGE = pygame.image.load('assets/images/sky.png')
GROUND_IMAGE = pygame.image.load('assets/images/ground.png')
BACKGROUND_IMAGE = pygame.image.load('assets/images/background.png')
CACTUS_IMAGE = pygame.image.load('assets/images/cactus_small.png')
CACTUS_BIG_IMAGE = pygame.image.load('assets/images/cactus_big.png')

pygame.init()
pygame.display.init()
FPSCLOCK = pygame.time.Clock()
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption("VERY BAD google dino!!!!")


def cactus_choice(cactus_random, old_cactus_random):
    while True:
        cactus_random = random.randint(0, 3)
        if cactus_random != old_cactus_random:
            break
    return cactus_random


def hello_game(ticks=0):
    sky_h = Sky(0, 0, SKY_IMAGE)
    ground_h = Ground(0, 200, GROUND_IMAGE)
    cactus_big1_h = Cactus(400, 165, CACTUS_BIG_IMAGE, CACTUS_BIG_IMAGE.get_rect())
    cactus_big2_h = Cactus(400, 165, CACTUS_BIG_IMAGE, CACTUS_BIG_IMAGE.get_rect())
    cactus_small1_h = Cactus(400, 175, CACTUS_IMAGE, CACTUS_IMAGE.get_rect())
    cactus_small2_h = Cactus(400, 175, CACTUS_IMAGE, CACTUS_IMAGE.get_rect())

    cactus_list = [cactus_big1_h, cactus_big2_h, cactus_small1_h, cactus_small2_h]

    text = 'SPACE чтобы начать игру'
    fontObj = pygame.font.Font("freesansbold.ttf", 20)
    textsurface = fontObj.render(text, True, BLACK)

    while True:
        cactus_random1 = random.randint(0, 3)
        cactus_random2 = random.randint(0, 3)
        if cactus_random1 != cactus_random2:
            break

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN and event.key == K_SPACE:
                ticks = pygame.time.get_ticks()
                main_game(pygame.time.get_ticks())

        # Смена кактусов

        if cactus_list[cactus_random1].get_x() == 400:
            cactus_random1 = cactus_choice(cactus_random1, cactus_random2)

        if cactus_list[cactus_random2].get_x() == 400:
            cactus_random2 = cactus_choice(cactus_random2, cactus_random1)

        cactus_list[cactus_random1].move()
        if pygame.time.get_ticks() >= ticks + 1845:
            cactus_list[cactus_random2].move()

        ground_h.move()
        sky_h.move()

        SCREEN.blit(BACKGROUND_IMAGE, (0, 0))
        SCREEN.blit(sky_h.get_image(), (sky_h.get_x(), sky_h.get_y()))
        SCREEN.blit(ground_h.get_image(), (ground_h.get_x(), ground_h.get_y()))
        SCREEN.blit(cactus_list[cactus_random1].get_image(), (cactus_list[cactus_random1].get_x(),
                                                              cactus_list[cactus_random1].get_y()))
        SCREEN.blit(cactus_list[cactus_random2].get_image(), (cactus_list[cactus_random2].get_x(),
                                                              cactus_list[cactus_random2].get_y()))

        SCREEN.blit(textsurface, (80, 100))

        pygame.display.update()
        FPSCLOCK.tick(FPS)


def main_game(ticks):
    dino = Dino(30, 155, DINO_IMAGE, DINO_IMAGE_2, DINO_IMAGE.get_rect())
    sky = Sky(0, 0, SKY_IMAGE)
    ground = Ground(0, 200, GROUND_IMAGE)
    cactus_big1 = Cactus(400, 165, CACTUS_BIG_IMAGE, CACTUS_BIG_IMAGE.get_rect())
    cactus_big2 = Cactus(400, 165, CACTUS_BIG_IMAGE, CACTUS_BIG_IMAGE.get_rect())
    cactus_small1 = Cactus(400, 175, CACTUS_IMAGE, CACTUS_IMAGE.get_rect())
    cactus_small2 = Cactus(400, 175, CACTUS_IMAGE, CACTUS_IMAGE.get_rect())

    cactus_list = [cactus_big1, cactus_big2, cactus_small1, cactus_small2]

    text = '0'
    fontObj = pygame.font.Font("freesansbold.ttf", 15)

    # Выбор кактусов в начале

    while True:
        cactus_random1 = random.randint(0, 3)
        cactus_random2 = random.randint(0, 3)
        if cactus_random1 != cactus_random2:
            break

    dino_space = 0

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            if dino_space == 0 and event.type == KEYDOWN and event.key == K_SPACE:
                dino_space = 1

        # Столкновение дино с кактусом
        dino_rect = dino.get_rect()
        cactus1_rect = cactus_list[cactus_random1].get_rect()
        cactus2_rect = cactus_list[cactus_random2].get_rect()

        if ((dino_rect.right or dino_rect.left) in range(cactus1_rect.left + 2, cactus1_rect.right, 1) and
                dino_rect.bottom in range(cactus1_rect.top + 3, cactus1_rect.bottom + 1, 1)):
            hello_game(pygame.time.get_ticks())

        elif ((dino_rect.right or dino_rect.left) in range(cactus2_rect.left + 2, cactus2_rect.right, 1) and
              dino_rect.bottom in range(cactus2_rect.top + 3, cactus2_rect.bottom + 1, 1)):
            hello_game(pygame.time.get_ticks())

        # Смена кактусов

        if cactus_list[cactus_random1].get_x() == 400:
            cactus_random1 = cactus_choice(cactus_random1, cactus_random2)

        if cactus_list[cactus_random2].get_x() == 400:
            cactus_random2 = cactus_choice(cactus_random2, cactus_random1)

        # Джижение обьектов

        if dino_space == 1:
            dino.jump()
            if dino.get_y() == 155:
                dino_space = 0

        cactus_list[cactus_random1].move()
        if pygame.time.get_ticks() >= ticks + 1650:
            cactus_list[cactus_random2].move()

        ground.move()
        sky.move()

        # Счёт очков

        textsurface = fontObj.render(text, True, BLACK)
        text = str(int(text) + 1)

        # Прорисовка обьектов

        SCREEN.blit(BACKGROUND_IMAGE, (0, 0))
        SCREEN.blit(sky.get_image(), (sky.get_x(), sky.get_y()))
        SCREEN.blit(ground.get_image(), (ground.get_x(), ground.get_y()))
        SCREEN.blit(cactus_list[cactus_random1].get_image(), (cactus_list[cactus_random1].get_x(),
                                                              cactus_list[cactus_random1].get_y()))
        SCREEN.blit(cactus_list[cactus_random2].get_image(), (cactus_list[cactus_random2].get_x(),
                                                              cactus_list[cactus_random2].get_y()))
        SCREEN.blit(dino.get_image(), (dino.get_x(), dino.get_y()))

        SCREEN.blit(textsurface, (300, 0))

        pygame.display.update()
        FPSCLOCK.tick(FPS)


hello_game()
