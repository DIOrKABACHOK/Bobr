import pygame
from pygame.draw import *
from random import randint
import time

pygame.init()

FPS = 144
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700
BLACK = (0, 0, 0)
COLORS = [(255, 0, 0), (0, 0, 255), (255, 255, 0), (0, 255, 0), (255, 0, 255), (0, 255, 255)]
BALL_DURATION = 2
BALL_SPEED = 10


def new_ball():
    x = randint(100, SCREEN_WIDTH - 100)
    y = randint(100, SCREEN_HEIGHT - 100)
    r = randint(30, 50)
    color = COLORS[randint(0, 5)]
    return {'x': x, 'y': y, 'r': r, 'color': color, 'creation_time': time.time()}


# Функция для отображения шарика
def draw_ball(ball):
    circle(screen, ball['color'], (ball['x'], ball['y']), ball['r'])


# Функция для проверки времени жизни шарика
def is_ball_alive(ball):
    return time.time() - ball['creation_time'] <= BALL_DURATION


# Создание окна
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Поймай шарик")

# Переменные
balls = []
score = 0

font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()
finished = False
while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for ball in balls:
                if (ball['x'] - event.pos[0]) ** 2 + (ball['y'] - event.pos[1]) ** 2 <= ball['r'] ** 2:
                    balls.remove(ball)
                    score += 1
                    break

    if len(balls) < 5 and randint(0, 100) < 10:
        balls.append(new_ball())

    balls = [ball for ball in balls if is_ball_alive(ball)]

    screen.fill(BLACK)
    for ball in balls:
        draw_ball(ball)
        ball['x'] += randint(-BALL_SPEED, BALL_SPEED)
        ball['y'] += randint(-BALL_SPEED, BALL_SPEED)
        if ball['x'] - ball['r'] < 0 or ball['x'] + ball['r'] > SCREEN_WIDTH:
            ball['x'] = min(max(ball['x'], ball['r']), SCREEN_WIDTH - ball['r'])
        if ball['y'] - ball['r'] < 0 or ball['y'] + ball['r'] > SCREEN_HEIGHT:
            ball['y'] = min(max(ball['y'], ball['r']), SCREEN_HEIGHT - ball['r'])

    text = font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(text, (10, 10))

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()