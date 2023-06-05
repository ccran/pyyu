import pygame
import sys

'''
事件统一处理
'''


class EventBus:
    event_sub_dict = {pygame.QUIT: []}

    # 对象obj注册event_type事件
    @classmethod
    def sub(cls, event_type, obj):
        if event_type not in EventBus.event_sub_dict:
            EventBus.event_sub_dict[event_type] = []
        EventBus.event_sub_dict[event_type].append(obj)

    # 对象obj取消订阅event_type事件
    @classmethod
    def unsub(cls, even_type, obj):
        if even_type in EventBus.event_sub_dict:
            EventBus.event_sub_dict[even_type].remove(obj)

    @classmethod
    def run(cls):
        for event in pygame.event.get():
            if event.type not in EventBus.event_sub_dict:
                continue
            for obj in EventBus.event_sub_dict[event.type]:
                obj.notify(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
