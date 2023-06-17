from settings import *
import random


class Block(pg.sprite.Sprite):
    def __init__(self, tetromino, position):
        self.tetromino = tetromino
        self.position = vec(position) + INIT_OFFSET

        super().__init__(tetromino.tetris.sprite_group)
        self.image = pg.Surface([TILE_SIZE, TILE_SIZE])
        self.image.fill('cyan')
        self.rect = self.image.get_rect()

    def set_rectangle_position(self):
        self.rect.topleft = self.position * TILE_SIZE

    def update(self):
        self.set_rectangle_position()

class Tetromino:
    def __init__(self, tetris):
        self.tetris = tetris
        self.shape = random.choice(list(TETROMINOES.keys()))
        self.blocks = [Block(self, position) for position in TETROMINOES[self.shape]]

    def move(self, direction):
        move_direction = MOVE_DIRECTIONS[direction]
        for block in self.blocks:
            block.position += move_direction
    
    def update(self):
        self.move(direction='down')