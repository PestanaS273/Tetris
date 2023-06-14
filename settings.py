import pygame as pg

FPS = 60

Field_Color = (51,51,51)

Tile_Size = 50

Field_Size = Field_Height, Field_Width = 24, 10

Field_Resolution = Field_Width * Tile_Size, Field_Height * Tile_Size

Tetrominoes = {
    'T' : [(0, 0), (-1, 0), (0, 1), (1, 0)],
    'I' : [(0, 0), (0, 1), (0, 2), (0, -1)],
    'L' : [(0, 0), (0, 1), (0, 2), (1, 0)],
    'O' : [(0, 0), (-1, 1), (0, 1), (-1, 0)],
    'J' : [(0, 0), (-1, 0), (0, 1), (0, 2)],
    'Z' : [(0, 0), (-1, 1), (0, 1), (1, 0)],
    'S' : [(0, 0), (-1, 0), (0, 1), (1, 1)]
}