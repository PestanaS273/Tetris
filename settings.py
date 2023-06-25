import pygame as pg
import math

vec = pg.math.Vector2

FPS = 60

FIELD_COLOR = (105,13,210)
INTERFACE_COLOR = (25, 7, 118)
NEXT_TETROMINO_COLOR = (105,13,210)

ANIMATION_TIME = 250

TILE_SIZE = 40

FIELD_SIZE = FIELD_WIDTH, FIELD_HEIGHT = 10, 20

FIELD_RESOLUTION = FIELD_WIDTH * TILE_SIZE, FIELD_HEIGHT * TILE_SIZE

FIELD_SCALE_WIDTH, FIELD_SCALE_HEIGHT = 1.7, 1.0
WINDOW_RESOLUTION = FIELD_SCALE_WIDTH, FIELD_SCALE_HEIGHT = FIELD_RESOLUTION[0] * FIELD_SCALE_WIDTH, FIELD_RESOLUTION[1] * FIELD_SCALE_HEIGHT

INIT_OFFSET = vec(FIELD_WIDTH // 2 -1, 0)

MOVE_DIRECTIONS = {
    'right' : vec(1, 0),
    'left' : vec(-1, 0),
    'down' : vec(0, 1)
}

TETROMINOES = {
    'T' : [(0, 0), (-1, 0), (0, 1), (1, 0)],
    'I' : [(0, 0), (0, 1), (0, 2), (0, -1)],
    'J' : [(0, 0), (0, 1), (0, 2), (1, 0)],
    'O' : [(0, 0), (0, 1), (-1, 0), (-1, 1)],
    'L' : [(0, 0), (-1, 0), (0, 1), (0, 2)],
    'Z' : [(0, 0), (-1, 1), (0, 1), (1, 0)],
    'S' : [(0, 0), (-1, 0), (0, 1), (1, 1)]
}

SPRITE_PATH = 'assets/sprites'


NEXT_TETROMINO_POSITION = vec(FIELD_WIDTH * 1.3, FIELD_HEIGHT * 0.15)
NEXT_TETROMINO_BACKGROUND = NEXT_WIDTH, NEXT_HEIGHT = 4, 5