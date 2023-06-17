import pygame as pg
import math

vec = pg.math.Vector2

FPS = 60

FIELD_COLOR = (51,51,51)

TILE_SIZE = 50

FIELD_SIZE = FIELD_WIDTH, FIELD_HEIGHT = 10, 20

FIELD_RESOLUTION = FIELD_WIDTH * TILE_SIZE, FIELD_HEIGHT * TILE_SIZE

INIT_OFFSET = vec(FIELD_WIDTH // 2 -1, 0)

MOVE_DIRECTIONS = {
    'right' : vec(1, 0),
    'left' : vec(-1, 0),
    'down' : vec(0, 1)
}

TETROMINOES = {
    'T' : [(0, 0), (-1, 0), (0, 1), (1, 0)],
    'I' : [(0, 0), (0, 1), (0, 2), (0, -1)],
    'L' : [(0, 0), (0, 1), (0, 2), (1, 0)],
    'O' : [(0, 0), (-1, 1), (0, 1), (-1, 0)],
    'J' : [(0, 0), (-1, 0), (0, 1), (0, 2)],
    'Z' : [(0, 0), (-1, 1), (0, 1), (1, 0)],
    'S' : [(0, 0), (-1, 0), (0, 1), (1, 1)]
}