import pygame
import time

RANDOM = 1
PERMUTATION = 2
GENETIC = 3

ALGORITHM_NAMES = {
    RANDOM: 'random',
    PERMUTATION: 'permutation',
    GENETIC: 'genetic'
}


def save_screenshot(game):
    timestamp = int(time.time())
    pygame.image.save(game.screen, 'screenshots/{0}.png'.format(str(timestamp)))
