"""Alien Pursuit
Try to stop an alien ship before it gets away.
Created by: Jason Nestmann
Date: April 19, 2017
Last Modified: April 22, 2017
"""

# import statements
import datetime
import logging
import SpaceObjects

import pygame

# beginning initializers and configuration settings
pygame.init()
logging.basicConfig(filename="logs/space_pursuit.log", level=logging.DEBUG)

program_start = datetime.datetime.now()

# global variables and constants
WHITE = (0xFF, 0xFF, 0xFF)
BLACK = (0x00, 0x00, 0x00)
ALIEN_GREEN = (29, 213, 18)  # [#1dd512]

# load background images
bg_filenames = [
    'assets/images/space_title_background.jpg',
    'assets/images/space_game_background.jpg',
    'assets/images/credits_background.jpg'
]

# setup game window
screen_size = (960, 540)
screen_width, screen_height = screen_size
screen = pygame.display.set_mode(screen_size)

# window title and icon
pygame.display.set_caption("Alien Pursuit")
game_icon = pygame.image.load('assets/images/game_icon.png')
pygame.display.set_icon(game_icon)

# add sound effects
crash_sound = pygame.mixer.Sound('assets/sounds/crash.wav')

# load sprites
player_img = pygame.image.load('assets/images/player_img.png').convert_alpha()
alien_img = pygame.image.load('assets/images/alien_img.png').convert_alpha()

player = SpaceObjects.PlayerShip(10, 10, 10, 10, player_img)
alien = SpaceObjects.AlienShip(250, 50, 10, 10, alien_img)


# top level functions
def pquit():
    """Bundles cleanup/shutdown of application"""
    program_end = datetime.datetime.now()
    logging.info("Program ended at: " + str(program_end))
    pygame.quit()
    exit()


def draw_background(mode):
    title_background = pygame.image.load(bg_filenames[mode]).convert()
    screen.blit(title_background, [0, 0])


def draw_player(player):
    screen.blit(player.img, [player.x, player.y])


def display_screen(screen_mode, player, alien):
    bg_mode = 0
    if screen_mode == 'splash':
        bg_mode = 0
    elif screen_mode == 'game':
        bg_mode = 1
    elif screen_mode == 'credits':
        bg_mode = 2
    else:
        logging.error("Invalid screen mode passed to display_screen function")
        pquit()
    draw_background(bg_mode)

    if screen_mode == 'game':
        screen.blit(player.img, [player.x, player.y])
        screen.blit(alien.img, [alien.x, alien.y])


def game_loop():
    game_play = True
    logging.info("Game started at: " + str(program_start))
    screen_mode = 'splash'

    # starting player position
    player_x, player_y = (10, 10)
    py_change = 0

    pygame.mixer.music.load('assets/sounds/gamemusic.wav')
    pygame.mixer.music.play(-1)  # -1 means repeat continuously, a number would be
    # the number of times the file plays

    while game_play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pquit()
            elif event.type == pygame.KEYDOWN:
                if event.key == 27:
                    pquit()
                elif screen_mode == 'splash':
                    if (event.key == pygame.K_p or
                                event.key == pygame.K_SPACE or
                                event.key == pygame.K_RETURN):
                        screen_mode = 'game'
                    elif event.key == pygame.K_q:
                        pquit()
                elif screen_mode == 'game':
                    if event.key == pygame.K_UP:
                        py_change = -5
                    elif event.key == pygame.K_DOWN:
                        py_change = 5
                    if event.key == pygame.K_SPACE:
                        screen_mode = 'credits'
                elif screen_mode == 'credits':
                    pquit()
            elif event.type == pygame.KEYUP:
                if screen_mode == 'game':
                    py_change = 0
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mousex, mousey = event.pos
                if 200 <= mousex <= 430 and 230 <= mousey <= 280:
                    screen_mode = 'game'
                if 520 <= mousex <= 760 and 230 <= mousey <= 280:
                    pquit()

        # update player location
        player.y += py_change
        # advance alien
        alien.x += 5
        # update screen
        screen.fill(WHITE)
        display_screen(screen_mode, player, alien)
        pygame.display.flip()

    clock.tick(60)


game_loop()
