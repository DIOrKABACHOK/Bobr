import pygame

from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 700))

polygon(screen, (30, 30, 30), [(0, 0), (800, 0), (800, 200), (0, 200)], 200)
circle(screen, (150, 150, 150), (700, 100), 50)

rect(screen, (50, 50, 0), (90, 200, 300, 300))
rect(screen, (150, 150, 0), (300, 375, 75, 75))
rect(screen, (30, 30, 10), (200, 375, 75, 75))
rect(screen, (30, 30, 10), (100, 375, 75, 75))
rect(screen, (170, 150, 150), (180, 220, 40, 100))
rect(screen, (170, 150, 150), (110, 220, 40, 100))
rect(screen, (170, 150, 150), (250, 220, 40, 100))
rect(screen, (170, 150, 150), (320, 220, 40, 100))
polygon(screen, (10, 10, 10), [(50, 340), (420, 340), (420, 360), (50, 360)])
polygon(screen, (10, 10, 10), [(75, 320), (400, 320), (400, 330), (75, 330)])
polygon(screen, (5, 5, 10), [(80, 190), (400, 190), (420, 210), (60, 210)])

ellipse(screen, (45, 45, 45), (450, 75, 250, 25), 50)
ellipse(screen, (60, 60, 60), (275, 90, 280, 35), 50)
ellipse(screen, (75, 75, 75), (450, 100, 360, 50), 50)

circle(screen, (200, 200, 200), (600, 500), 25)
polygon(screen, (200, 200, 200), [(580, 485), (620, 485), (670, 545), (560, 545), (520, 555)])
ellipse(screen, (200, 200, 200), (580, 520, 90, 50), 25)
#ellipse(screen, (200, 200, 200), (530, 510, 80, 30), 25)
ellipse(screen, (200, 200, 200), (530, 540, 100, 30), 25)
circle(screen, (100, 100, 250), (585, 490), 5)
circle(screen, (0, 0, 0), (585, 490), 2)
circle(screen, (100, 100, 250), (605, 490), 5)
circle(screen, (0, 0, 0), (605, 490), 2)
ellipse(screen, (0, 0, 0), (585, 565, 30, 10), 25)
ellipse(screen, (0, 0, 0), (545, 565, 30, 10), 25)
ellipse(screen, (0, 0, 0), (525, 545, 10, 40), 25)
ellipse(screen, (0, 0, 0), (625, 565, 30, 10), 25)
ellipse(screen, (0, 0, 0), (660, 530, 10, 50), 100)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True


pygame.quit()