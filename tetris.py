import pygame
pygame.init()

window_size = (400, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('ТЕТРИС')

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (171, 205, 239)
RED = (246, 74, 70)
GREEN = (140, 203, 94)
YELLOW = (255, 220, 51)
VIOLET = (116, 66, 200)
ROSE = (224, 176, 255)
ORANGE = (255, 185, 97)

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


class Piece(object):
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = colors[shapes.index(shape)]
        self.rotation = 0

    # Логика поворота фигуры
    def rotate(shape):
        return [list(row) for row in zip(*shape[::-1])]

    # Логика движения фигуры вниз, влево, вправо
    def check_collision():
        # Проверка столкновений фигур с границами и друг с другом
        pass


run = True
clock = pygame.time.Clock()
fps = 60

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Перемещение по клавишам:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        pass
        # image_rect.x -= speed
    if keys[pygame.K_RIGHT]:
        pass
        # image_rect.x += speed
    if keys[pygame.K_UP]:
        pass
        # image_rect.y -= speed
    if keys[pygame.K_DOWN]:
        pass
        # image_rect.y += speed

    screen.fill(BLACK)
    # screen.blit(image, image_rect)
    pygame.display.flip()  # команда для изменения событий на экране

clock.tick(fps)
pygame.quit()
