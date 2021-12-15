import pygame as pg

CELL_SIZE = 30
SIZE = (CELL_SIZE,) * 2
WALL = pg.Surface(SIZE)
WALL.fill("brown")
PLAYER = pg.Surface(SIZE)
PLAYER.fill("red")
VOID = pg.Surface(SIZE)
VOID.fill("black")

d = {
    '@': PLAYER,
    '#': WALL
}


def get_surface_from_char(char):
    return d.get(char, VOID)


def main():
    pg.init()
    size_x, size_y = None, None

    with open("level.txt") as file:
        size_x = int(file.readline().split()[-1])
        size_y = int(file.readline().split()[-1])
        screen = pg.display.set_mode((CELL_SIZE * size_x, CELL_SIZE * size_y))
        for y in range(size_y):
            row = file.readline().strip()
            for x in range(size_x):
                screen.blit(get_surface_from_char(row[x]), (x * CELL_SIZE, y * CELL_SIZE))

    pg.display.update()
    running = True
    while running:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                running = False




main()