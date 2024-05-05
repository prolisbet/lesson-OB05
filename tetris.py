import pygame
import sys
import random
import time
pygame.init()

screen_width = 450
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('ТЕТРИС')

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (171, 205, 239)  # tetronimo T
RED = (246, 74, 70)  # tetronimo S
GREEN = (140, 203, 94)  # tetronimo Z
YELLOW = (255, 220, 51)  # tetronimo J
VIOLET = (116, 66, 200)  # tetronimo L
ROSE = (224, 176, 255)  # tetronimo O
ORANGE = (255, 185, 97)  # tetronimo I
COLORS = [BLUE, RED, GREEN, YELLOW, VIOLET, ROSE, ORANGE]

tetronimo_shapes = [
    [[1, 1, 1],
     [0, 1, 0]],

    [[0, 2, 2],
     [2, 2, 0]],

    [[3, 3, 0],
     [0, 3, 3]],

    [[4, 0, 0],
     [4, 4, 4]],

    [[0, 0, 5],
     [5, 5, 5]],

    [[6, 6],
     [6, 6]],

    [[7, 7, 7, 7]]
]

once_rotated_shapes = [
    [[1, 0],
     [1, 1],
     [1, 0]],

    [[2, 0],
     [2, 2],
     [0, 2]],

    [[0, 3],
     [3, 3],
     [3, 0]],

    [[0, 4],
     [0, 4],
     [4, 4]],

    [[5, 5],
     [0, 5],
     [0, 5]],

    [[6, 6],
     [6, 6]],

    [[7],
     [7],
     [7],
     [7]]
]

twice_rotated_shapes = [
    [[0, 1, 0],
     [1, 1, 1]],

    [[0, 2, 2],
     [2, 2, 0]],

    [[3, 3, 0],
     [0, 3, 3]],

    [[4, 4, 4],
     [0, 0, 4]],

    [[5, 5, 5],
     [5, 0, 0]],

    [[6, 6],
     [6, 6]],

    [[7, 7, 7, 7]]
]


thrice_rotated_shapes = [
    [[0, 1],
     [1, 1],
     [0, 1]],

    [[2, 0],
     [2, 2],
     [0, 2]],

    [[0, 3],
     [3, 3],
     [3, 0]],

    [[4, 4],
     [4, 0],
     [4, 0]],

    [[5, 0],
     [5, 0],
     [5, 5]],

    [[6, 6],
     [6, 6]],

    [[7],
     [7],
     [7],
     [7]]
]


class Piece(object):
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.index = tetronimo_shapes.index(shape)
        self.color = COLORS[self.index]
        self.rotation = 0

    # Логика поворота фигуры
    def rotate(self):
        self.rotation += 1
        print(self.rotation)
        if self.rotation % 4 == 1:
            self.shape = once_rotated_shapes[self.index]
        elif self.rotation % 4 == 2:
            self.shape = twice_rotated_shapes[self.index]
        elif self.rotation % 4 == 3:
            self.shape = thrice_rotated_shapes[self.index]
        else:
            self.shape = tetronimo_shapes[self.index]


# Логика движения фигуры вниз, влево, вправо
def check_collision(piece, grid, adj_x=0, adj_y=0):
    # Проверка столкновений фигур с границами и друг с другом
    for y, row in enumerate(piece.shape):
        for x, cell in enumerate(row):
            if cell:
                try:
                    if grid[y + piece.y + adj_y][x + piece.x + adj_x]:
                        return True
                except IndexError:
                    return True
    return False


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[0 for _ in range(width)] for _ in range(height)]

    def add_piece(self, piece):
        for y, row in enumerate(piece.shape):
            for x, cell in enumerate(row):
                if cell:
                    self.grid[y + piece.y][x + piece.x] = cell

    def check_lines(self):
        for y in range(self.height):
            if 0 not in self.grid[y]:
                del self.grid[y]
                self.grid.insert(0, [0 for _ in range(self.width)])


def draw_piece(screen, piece):
    for i, row in enumerate(piece.shape):
        for j, cell in enumerate(row):
            if cell:
                pygame.draw.rect(screen, COLORS[piece.index],
                                 ((piece.x + j) * 30, (piece.y + i) * 30, 30, 30))
                pygame.draw.rect(screen, BLACK, ((piece.x + j) * 30, (piece.y + i) * 30, 30, 30), 1)


# Кнопки
game_over_button = pygame.Rect(125, 200, 180, 50)
new_game_button = pygame.Rect(125, 375, 180, 50)

font = pygame.font.Font(None, 36)


def draw_button(button, text, color=WHITE):
    pygame.draw.rect(screen, color, button)
    pygame.draw.rect(screen, BLACK, button, 1)
    text_render = font.render(text, True, BLACK)
    text_rect = text_render.get_rect(center=button.center)
    screen.blit(text_render, text_rect)


def game_over():
    draw_button(game_over_button, "Game Over", WHITE)
    draw_button(new_game_button, "New Game", WHITE)
    pygame.display.flip()
    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if new_game_button.collidepoint(event.pos):
                    waiting_for_input = False
                    return True
    return False


run = True
clock = pygame.time.Clock()
fps = 30
board = Board(screen_width // 30, screen_height // 30)
current_piece = Piece(5, 1, random.choice(tetronimo_shapes))
fall_speed = 30
fall_time = 0

while run:
    fall_time += clock.get_rawtime()
    clock.tick(fps)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Управление фигуры клавишами:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        current_piece.x -= 1
        if current_piece.x < 0 or check_collision(current_piece, board.grid):
            current_piece.x += 1
        time.sleep(0.1)
    if keys[pygame.K_RIGHT]:
        current_piece.x += 1
        if check_collision(current_piece, board.grid):
            current_piece.x -= 1
        time.sleep(0.1)
    if keys[pygame.K_UP]:
        current_piece.rotate()
        if check_collision(current_piece, board.grid):
            for _ in range(3):  # Вращаем обратно
                current_piece.rotate()
        time.sleep(0.1)
    if keys[pygame.K_DOWN] and not check_collision(current_piece, board.grid, adj_y=1):
        current_piece.y += 1

    if fall_time > fall_speed:
        fall_time = 0
        if not check_collision(current_piece, board.grid, adj_y=1):
            current_piece.y += 1
        else:
            board.add_piece(current_piece)
            board.check_lines()
            current_piece = Piece(5, 0, random.choice(tetronimo_shapes))
            if check_collision(current_piece, board.grid):
                if game_over():
                    # Сброс игры
                    board = Board(screen_width // 30, screen_height // 30)
                    current_piece = Piece(5, 1, random.choice(tetronimo_shapes))
                    continue
                else:
                    run = False

    screen.fill(BLACK)
    for y, row in enumerate(board.grid):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(screen, COLORS[cell-1], (x*30, y*30, 30, 30))
                pygame.draw.rect(screen, BLACK, (x*30, y*30, 30, 30), 1)

    draw_piece(screen, current_piece)
    pygame.display.flip()  # команда для изменения событий на экране

pygame.quit()
sys.exit()
