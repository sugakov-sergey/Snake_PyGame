import pygame
import random

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Snake")

active = True
snake_len = 1
x1, y1 = 300, 400
snake_set = [(x1, y1)]
x1_change, y1_change = 0, 0

clock = pygame.time.Clock()
bg = pygame.image.load('bground.jpg')

# Создаем клубнички и рассыпаем по экрану
berry = pygame.image.load('berry.png')
berry_set = []
for i in range(30):
    berry_set += [(random.randint(10, 780), random.randint(10, 480))]

while active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -10
            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = 10

    # Проверка на пройгрыш
    if x1 >= 800 or x1 < 0 or y1 >= 600 or y1 < 0:
        my_font = pygame.font.SysFont('Verdana', 30)
        msg = 'Game Over!'
        text_surface = my_font.render(msg, True, (0, 0, 0))
        screen.blit(text_surface, (310, 200))
        pygame.display.update()
        pygame.time.wait(1000)
        active = False

    x1 += x1_change
    y1 += y1_change
    screen.blit(bg, (0, 0))

    # Проверка на столкновение и обновление малинки:
    for x_y in berry_set.copy():
        if x_y[0] - 10 <= x1 <= x_y[0] + 15 and x_y[1] - 10 <= y1 <= x_y[1] + 18:
            berry_set.remove(x_y)
            snake_len += 1
        screen.blit(berry, x_y)

    # регистрация координат каждого элемента хвоста:
    if x1_change != 0 or y1_change != 0:
        snake_set += [(x1, y1)]
        if len(snake_set) > snake_len:
            del snake_set[0]

    for i in range(len(snake_set) - 1):
        pygame.draw.rect(screen, 'yellow', [snake_set[i][0], snake_set[i][1], 10, 10])
    pygame.draw.rect(screen, 'brown', [snake_set[-1][0], snake_set[-1][1], 10, 10])

    # Выводим счет:
    my_font = pygame.font.SysFont('Verdana', 16)
    msg = 'Score: '
    text_surface = my_font.render(f'{msg}{snake_len*100}', True, (0, 0, 0))
    screen.blit(text_surface, (10, 0))
    pygame.display.update()

    clock.tick(5)

pygame = quit()
quit()
