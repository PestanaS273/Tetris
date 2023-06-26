import pygame as pg
import sys
from tetris import Tetris, Text
from settings import *
import pathlib
from Data.database_handler import database_handler

    

class App:

    def __init__(self):
        pg.init()
        pg.display.set_caption('Tetris')
        self.screen = pg.display.set_mode(WINDOW_RESOLUTION)
        self.clock = pg.time.Clock()

        self.mode = 0
        self.start_time = None
        # self.set_timer()
        
        self.images = self.load_images()
        self.tetris = Tetris(self)
        pg.mixer.music.load('assets/music_and_sounds/Original-Tetris-theme-Tetris-Soundtrack-.mp3')
        pg.mixer.music.play(-1)
        pg.mixer.music.set_volume(0.2)
        self.text = Text(self)
        
        db_handler = database_handler("database.db")


        self.paused = False
        self.over = False
        self.start = False
        self.level = 0
        self.set_timer(ANIMATION_TIME)

        

        
        


    #Set animation time original
    # def set_timer(self):
    #     self.user_event = pg.USEREVENT + 0
    #     self.anim_trigger= False
    #     pg.time.set_timer(self.user_event, ANIMATION_TIME)

    def set_timer(self, time):
        self.user_event = pg.USEREVENT + 0
        self.anim_trigger= False
        pg.time.set_timer(self.user_event, time)

        
        

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
        

    def game_start(self):
        start = True
        
        pg.mixer.music.stop()
        game_start_screen_fade = pg.Surface(WINDOW_RESOLUTION)
        game_start_screen_fade.fill((105,13,210))
        self.screen.blit(game_start_screen_fade, (0, 0))



        self.text.font.render_to(self.screen, (FIELD_WIDTH* 5, FIELD_HEIGHT* 5),
                            text="T", fgcolor='red',
                            size=TILE_SIZE * 3)
        self.text.font.render_to(self.screen, (FIELD_WIDTH* 15, FIELD_HEIGHT* 5),
                            text="E", fgcolor='orange',
                            size=TILE_SIZE * 3)
        self.text.font.render_to(self.screen, (FIELD_WIDTH* 25, FIELD_HEIGHT* 5),
                            text="T", fgcolor='yellow',
                            size=TILE_SIZE * 3)
        self.text.font.render_to(self.screen, (FIELD_WIDTH* 35, FIELD_HEIGHT* 5),
                            text="R", fgcolor='green',
                            size=TILE_SIZE * 3)
        self.text.font.render_to(self.screen, (FIELD_WIDTH* 45, FIELD_HEIGHT* 5),
                            text="I", fgcolor='cyan',
                            size=TILE_SIZE * 3)
        self.text.font.render_to(self.screen, (FIELD_WIDTH* 55, FIELD_HEIGHT* 5),
                            text="S", fgcolor='violet',
                            size=TILE_SIZE * 3)
        
        self.text.font.render_to(self.screen, (FIELD_WIDTH* 10, FIELD_HEIGHT* 20),
                            text="Classic: Press 1", fgcolor='white',
                            size=TILE_SIZE * 0.90, bgcolor=(25, 7, 118))
        
        self.text.font.render_to(self.screen, (FIELD_WIDTH* 10, FIELD_HEIGHT* 25),
                            text="No rotation: Press 2", fgcolor='white',
                            size=TILE_SIZE * 0.90, bgcolor=(25, 7, 118))
        self.text.font.render_to(self.screen, (FIELD_WIDTH* 10, FIELD_HEIGHT* 30),
                            text="2 Minutes Rush!: Press 3", fgcolor='white',
                            size=TILE_SIZE * 0.90, bgcolor=(25, 7, 118))
        
        pg.display.update()
        
        while start:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_1:
                        start = False
                        self.start = True
                        self.mode = 1
                        pg.mixer.music.play(-1)
                        pg.mixer.music.set_volume(0.2)
                    if event.key == pg.K_2:
                        start = False
                        self.start = True
                        self.mode = 2
                        pg.mixer.music.play(-1)
                        pg.mixer.music.set_volume(0.2)
                    elif event.key == pg.K_3:
                        start = False
                        self.start = True
                        self.mode = 3
                        pg.mixer.music.play(-1)
                        pg.mixer.music.set_volume(0.2)
                    
            self.clock.tick(5)
        if not self.start_time:
            self.start_time = pg.time.get_ticks()



    def game_paused(self):
        
        paused = True
        
        pg.mixer.music.stop()
        game_over_screen_fade = pg.Surface(WINDOW_RESOLUTION)
        game_over_screen_fade.fill((0, 0, 0))
        game_over_screen_fade.set_alpha(90)
        self.screen.blit(game_over_screen_fade, (0, 0))

        self.text.font.render_to(self.screen, (FIELD_WIDTH* 5, FIELD_HEIGHT* 5),
                            text="GAME PAUSED", fgcolor='white',
                            size=TILE_SIZE * 2, bgcolor=(0,0,0))
        
        self.text.font.render_to(self.screen, (FIELD_WIDTH* 12, FIELD_HEIGHT* 30),
                            text="Press esc to continue", fgcolor='white',
                            size=TILE_SIZE * 0.70, bgcolor=(0,0,0))
        pg.display.update()
        
        
        while paused:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        paused = False
                        pg.mixer.music.play(-1)
                        pg.mixer.music.set_volume(0.2)
                        
            self.clock.tick(5)
            

        

    def game_over(self):

        over = True

        self.start_time = None
        
        pg.mixer.music.stop()
        game_over_screen_fade = pg.Surface(WINDOW_RESOLUTION)
        game_over_screen_fade.fill((0, 0, 0))
        game_over_screen_fade.set_alpha(90)
        self.screen.blit(game_over_screen_fade, (0, 0))


        self.text.font.render_to(self.screen, (FIELD_WIDTH* 10, FIELD_HEIGHT* 10),
                            text="GAMEOVER", fgcolor='white',
                            size=TILE_SIZE * 2, bgcolor=(0,0,0))
        
        

        self.text.font.render_to(self.screen, (FIELD_WIDTH* 6, FIELD_HEIGHT* 30),
                            text="Press space to start a new game", fgcolor='white',
                            size=TILE_SIZE * 0.70, bgcolor=(0,0,0))
        pg.display.update()
        
        while over:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        over = False
                        
                        pg.mixer.music.play(-1)
                        pg.mixer.music.set_volume(0.2)
                        
                        self.tetris.reset()
                        
            self.clock.tick(5)

            
            
    def check_events(self):
        self.anim_trigger = False
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                self.tetris.controls(pressed_arrows=event.key)
                # if self.over and event.key == pg.K_ESCAPE:
                #     self.over = False
                #     self.tetris.reset()
                # elif not self.over:
                    


            elif event.type == self.user_event:
                self.anim_trigger = True
                
        

#def run original 
    # def run(self):
    #     while True:
    #         self.check_events()
            
    #         if not self.over:
    #             self.update()
    #             self.draw()
                
    #         else: 
    #             self.game_over()

    def run(self):
        while True:
            self.check_events()
            
            if not self.start:
                self.game_start()
            
            elif not self.over:
                self.update()
                self.draw()
                if self.mode == 3 and pg.time.get_ticks() - self.start_time >= 3 * 60 * 1000: 
                    self.game_over()
                
            else: 
                self.game_over()
            pg.display.flip()
            

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


