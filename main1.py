import pygame
pygame.init()

window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Тестовый проект')

image = pygame.image.load('picPython.png')
image_rect = image.get_rect()

speed = 2

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Перемещение по клавишам:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and image_rect.x > 0:
        image_rect.x -= speed
    if keys[pygame.K_RIGHT] and image_rect.x < 700:
        image_rect.x += speed
    if keys[pygame.K_UP] and image_rect.y > 0:
        image_rect.y -= speed
    if keys[pygame.K_DOWN] and image_rect.y < 500:
        image_rect.y += speed

    screen.fill((0, 0, 0))
    screen.blit(image, image_rect)
    pygame.display.flip()  # команда для изменения событий на экране

pygame.quit()
