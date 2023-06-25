import pygame as pg
import sys
from tetris import Tetris, Text
from settings import *
import pathlib

    

class App:

    def __init__(self):
        pg.init()
        pg.display.set_caption('Tetris')
        self.screen = pg.display.set_mode(WINDOW_RESOLUTION)
        self.clock = pg.time.Clock()
        self.set_timer()
        self.images = self.load_images()
        self.tetris = Tetris(self)
        pg.mixer.music.load('assets/music_and_sounds/Original-Tetris-theme-Tetris-Soundtrack-.mp3')
        pg.mixer.music.play(-1)
        pg.mixer.music.set_volume(0.2)
        self.text = Text(self)


    #Set animation time
    def set_timer(self):
        self.user_event = pg.USEREVENT + 0
        self.anim_trigger= False
        pg.time.set_timer(self.user_event, ANIMATION_TIME)

    def update(self):
        self.tetris.update()
        self.clock.tick(FPS)

    def draw(self):
        
        #Interface
        self.screen.fill(color=INTERFACE_COLOR)
        self.screen.fill(color=FIELD_COLOR, rect=(0,0, *FIELD_RESOLUTION))
        self.screen.fill(color=NEXT_TETROMINO_COLOR, rect=(450, 75, 170, 170))

        self.tetris.draw()
        self.text.draw()
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

    # def laod_images(self):
    #     files = [file for file in pathlib.Path(SPRITE_PATH).rglob('*.png') if file.is_file()]
    #     images = [pg.image.load(file).convert_alpha() for file in files]
    #     images = [pg.transform.scale(image, (TILE_SIZE, TILE_SIZE)) for image in images]
    #     return images
    def load_images(self):
        files = sorted(pathlib.Path(SPRITE_PATH).rglob('*.png'))
        images = {}
        for file in files:
            image = pg.image.load(file).convert_alpha()
            image = pg.transform.scale(image, (TILE_SIZE, TILE_SIZE))
            piece_name = file.stem 
            images[piece_name] = image
        return images



if __name__ == '__main__':
    app = App()
    app.run()


