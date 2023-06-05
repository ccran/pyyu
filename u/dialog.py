import pygame
from event import EventBus

'''
    对话框封装
'''


class Dialog:
    def __init__(self, text):
        EventBus.sub(pygame.MOUSEBUTTONDOWN, self)
        # 显示内容
        self.text = text
        self.text_idx = 0
        # 遮罩
        self.mask = pygame.image.load("../assets/pic/mask.png").convert_alpha()
        self.mask_pos = (0, 502)
        self.mask.set_alpha(100)
        # 显示文本
        self.game_font = pygame.font.SysFont(['幼圆'], 35)
        self.speaker = self.game_font.render("Sakura", True, (255, 255, 255))
        self.content = self.game_font.render(self.text[self.text_idx], True, (255, 255, 255))

    def show(self, screen):
        screen.blit(self.mask, self.mask_pos)
        screen.blit(self.speaker, (10, 502))
        screen.blit(self.content, (10, 552))

    def notify(self, event):
        x, y = event.pos
        mask_x, mask_y = self.mask_pos
        if mask_x + self.mask.get_rect().w >= x >= mask_x \
                and mask_y + self.mask.get_rect().h >= y >= mask_y:
            self.text_idx += 1
            if self.text_idx < len(self.text):
                self.content = self.game_font.render(self.text[self.text_idx], True, (255, 255, 255))

    def __del__(self):
        EventBus.unsub(pygame.MOUSEBUTTONDOWN, self)
