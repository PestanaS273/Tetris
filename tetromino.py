from settings import *

class Block(pg.sprite.Sprite):
    def __init__(self, tetromino, position):
        self.tetromino = tetromino

        super().__init__(tetromino.tetris.sprite_group)
        self.image = pg.Surface([Tile_Size, Tile_Size])
        self.image.fill('orange')

        self.rect = self.image.get_rect()
        self.rect.topleft = position[0] * Tile_Size, position[1] * Tile_Size

    

class Tetromino:
    def __init__(self, tetris):
        self.tetris = tetris
        self.shape = 'T'
        self.blocks = [Block(self, position) for position in Tetrominoes[self.shape]]
    
    def update(self):
        pass