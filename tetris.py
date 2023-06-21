from settings import *
from tetromino import Tetromino

class Tetris:
    def __init__(self, app):
        self.app = app
        self.field_array = self.set_field_array()
        self.sprite_group = pg.sprite.Group()
        self.tetromino = Tetromino(self)

    #set blocs occuped in the field by tetrominoes
    def set_tetrominoes_in_array(self):
        for block in self.tetromino.blocks:
            x, y = int(block.position.x), int(block.position.y)
            self.field_array[y][x] = block

    def set_field_array(self):
        return [[0 for x in range(FIELD_WIDTH)] for y in range(FIELD_HEIGHT)]

    def controls(self, pressed_arrows):
        if pressed_arrows == pg.K_LEFT:
            self.tetromino.move(direction='left')
        elif pressed_arrows == pg.K_RIGHT:
            self.tetromino.move(direction='right')
        elif pressed_arrows == pg.K_DOWN:
            self.tetromino.move(direction='down')
        elif pressed_arrows == pg.K_UP:
            self.tetromino.rotation()

    def check_reach_bottom(self):
        #create new tetromino is bottom is reached
        if self.tetromino.bottom:
            self.set_tetrominoes_in_array()
            self.tetromino = Tetromino(self)
        

    def grid(self):
        for x in range(FIELD_WIDTH):
            for y in range(FIELD_HEIGHT):
                pg.draw.rect(self.app.screen, 'black',
                             (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)



    def update(self):
        if self.app.anim_trigger == True:
            self.tetromino.update()
            self.check_reach_bottom()
        self.sprite_group.update()

    def draw(self):
        self.grid()
        self.sprite_group.draw(self.app.screen)