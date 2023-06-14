from settings import *
from tetromino import Tetromino
import math

class Tetris:
    def __init__(self, app):
        self.app = app
        self.sprite_group = pg.sprite.Group()
        self.tetromino = Tetromino(self)

    def grid(self):
        for x in range(Field_Width):
            for y in range(Field_Height):
                pg.draw.rect(self.app.screen, 'black',
                             (x * Tile_Size, y * Tile_Size, Tile_Size, Tile_Size), 1)



    def update(self):
        self.tetromino.update()
        self.sprite_group.update()

    def draw(self):
        self.grid()
        self.sprite_group.draw(self.app.screen)