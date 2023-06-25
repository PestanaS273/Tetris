import pygame as pg
from settings import *
from tetromino import Tetromino
import pygame.freetype as ft

class Text:
    def __init__(self, app):
        self.font = ft.Font(None, 40)
        self.app = app
    
    
    def draw(self):
        #Text
        # self.next_surface = self.title_font.render("Next", True, (255, 255, 255))
        # self.screen.blit(self.next_surface, (500, 18, 1, 1))
        self.font.render_to(self.app.screen, (FIELD_WIDTH * 46, FIELD_HEIGHT * 0.6),
                            text='Next', fgcolor='white',
                            size=TILE_SIZE * 1.65, bgcolor = 'black')
        # self.font.render("Next", True, (255, 255, 255))
        self.font.render_to(self.app.screen, (FIELD_WIDTH * 48, FIELD_HEIGHT * 20),
                            text=f'{self.app.tetris.score}', fgcolor='white',
                            size=TILE_SIZE * 1.8)
        
        # self.score_surface = self.title_font.render("Score:", True, (255, 255, 255))
        # self.screen.blit(self.score_surface, (500, 300, 1, 1))
        # self.score_numbers_surface = self.title_font.render(f'{self.app.tetris.score}', True, (255, 255, 255))
        # self.screen.blit(self.score_numbers_surface, (500, 350, 1, 1))

class Tetris:
    def __init__(self, app):
        self.app = app
        self.field_array = self.set_field_array()
        self.sprite_group = pg.sprite.Group()
        self.tetromino = Tetromino(self)
        self.next_tetromino = Tetromino(self, current=False)

        self.score = 0
        self.full_lines = 0
        self.points_per_lines = {
            0: 0,
            1: 100,
            2: 100,
            3: 200,
            4: 500,
        }

    def get_score(self):
        self.score += self.points_per_lines[self.full_lines]
        self.full_lines = 0

    def check_full_lines(self):
        #start at bottom
        row = FIELD_HEIGHT -1
        for current_row in range(FIELD_HEIGHT -1, -1, -1):
            for column in range(FIELD_WIDTH):
                self.field_array[row][column] = self.field_array[current_row][column]

                if self.field_array[current_row][column]:
                    self.field_array[row][column].position = vec(column, current_row)
                    
            if sum(map(bool, self.field_array[current_row])) < FIELD_WIDTH:
                row -= 1
            
            else: 
                for column in range(FIELD_WIDTH):
                    self.field_array[row][column].active = False
                    self.field_array[row][column] = 0               
                    sound_effect = pg.mixer.Sound('assets/music_and_sounds/clear.wav')
                    sound_effect.play()
                    sound_effect.set_volume(0.2)
                self.full_lines += 1

            
                
        
       
            

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
            if self.game_over():
                self.__init__(self.app)
            else:
                self.set_tetrominoes_in_array()
                self.next_tetromino.current = True
                self.tetromino = self.next_tetromino
                self.next_tetromino = Tetromino(self, current=False)
        

    def grid(self):
        for x in range(FIELD_WIDTH):
            for y in range(FIELD_HEIGHT):
                pg.draw.rect(self.app.screen, 'black',
                             (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)

    def game_over(self):
        if self.tetromino.blocks[0].position.y == INIT_OFFSET[1]:
            pg.time.wait(300)
            return True

    def update(self):
        if self.app.anim_trigger == True:
            self.tetromino.update()
            self.check_reach_bottom()
            self.check_full_lines()
            self.get_score()
        self.sprite_group.update()

    def draw(self):
        self.grid()
        self.sprite_group.draw(self.app.screen)

