import pygame as pg
import sys
from tetris import Tetris
from settings import *


class App:
    def __init__(self):
        pg.init()
        pg.display.set_caption('Tetris')
        self.screen = pg.display.set_mode(FIELD_RESOLUTION)
        self.clock = pg.time.Clock()
        self.set_timer()
        self.tetris = Tetris(self)


    #Set animation time
    def set_timer(self):
        self.user_event = pg.USEREVENT + 0
        self.anim_trigger= False
        pg.time.set_timer(self.user_event, ANIMATION_TIME)

    def update(self):
        self.tetris.update()
        self.clock.tick(FPS)

    def draw(self):
        self.screen.fill(color=FIELD_COLOR)
        self.tetris.draw()
        pg.display.flip()

    def check_events(self):
        self.anim_trigger = False
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                self.tetris.controls(pressed_arrows=event.key)
            elif event.type == self.user_event:
                self.anim_trigger = True
        


    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == '__main__':
    app = App()
    app.run()


