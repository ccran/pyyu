# Example file showing a basic pygame "game loop"
import sys

import pygame
from event import EventBus
from dialog import Dialog

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 768))

clock = pygame.time.Clock()

# load background
bg = pygame.image.load("../assets/pic/sakura.png").convert_alpha()

dialog = Dialog(['1111', '2222'])

# load music
# bgm = pygame.mixer.Sound('../assets/music/bgm.wav')
# bgm.play()
pygame.mixer.music.load('../assets/music/bgm.wav')
pygame.mixer.music.play(-1)

while True:
    # 事件循环
    EventBus.run()

    # RENDER YOUR GAME HERE
    # bgm.play()
    screen.blit(bg, (0, 0))
    dialog.show(screen)

    # update screen
    pygame.display.update()
    # limits FPS to 60
    clock.tick(60)
