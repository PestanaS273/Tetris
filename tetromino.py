from settings import *
import random



class Block(pg.sprite.Sprite):
    def __init__(self, tetromino, position, image):
        self.tetromino = tetromino
        self.position = vec(position) + INIT_OFFSET
        self.active = True
        self.image = image
        self.next_postion = vec(position) + NEXT_TETROMINO_POSITION
        

        super().__init__(tetromino.tetris.sprite_group)
        self.rect = self.image.get_rect()

    def set_rectangle_position(self):
        position = [self.next_postion, self.position][self.tetromino.current]
        self.rect.topleft = position * TILE_SIZE
    

    def rotation(self, pivot):
        #3 steps calculation to rotate a tetromino
        first = self.position - pivot
        second = first.rotate(90)
        return second + pivot
    
    #check if the block is active, if not remove from the Sprite group
    def is_active(self):
        if not self.active:
            self.kill()


    def update(self):
        self.is_active()
        self.set_rectangle_position()

    #limits
    def collision(self, position):
        x, y = int(position.x), int(position.y)
        #check if the block is inside the field 
        if 0 <= x < FIELD_WIDTH and y < FIELD_HEIGHT and (
            #check if there is other blocks in the Array and not take it into account if there are above it
            y < 0 or not self.tetromino.tetris.field_array[y][x]):
            #There is no colission
            return False
        #There is collision
        return True



class Tetromino:
    def __init__(self, tetris, current=True):
        self.tetris = tetris
        self.shape = random.choice(list(TETROMINOES.keys()))
        self.blocks = [Block(self, position, self.tetris.app.images[self.shape]) for position in TETROMINOES[self.shape]]
        self.bottom = False
        self.current = current


    def rotation(self):
        pivot = self.blocks[0].position
        #calculate the new block position after rotation
        block_rotated = [block.rotation(pivot) for block in self.blocks]

        if not self.collision(block_rotated):
            for i, block in enumerate(self.blocks):
                block.position = block_rotated[i]

    
    def collision(self, block_position):
        #call colission check for each block
        return any(map(Block.collision, self.blocks, block_position))

    def move(self, direction):
        move_direction = MOVE_DIRECTIONS[direction]
        #def of new positions for blocks taking in consideration movement
        new_block_position = [block.position + move_direction for block in self.blocks]

        #check collision in the new position
        collision = self.collision(new_block_position)
        if not collision:
            for block in self.blocks:
                block.position += move_direction
        elif direction == 'down':
            self.bottom = True
    
    def update(self):

        self.move(direction='down')

