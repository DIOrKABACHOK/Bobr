import pygame

from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1000, 800))

polygon(screen, (30, 30, 30), [(0, 0), (1000, 0), (1000, 200), (0, 200)], 200)
circle(screen, (150, 150, 150), (900, 100), 50)

def home(x, y):
    rect(screen, (50, 50, 0), (90+x, 200+y, 300, 300))
    rect(screen, (150, 150, 0), (300+x, 375+y, 75, 75))
    rect(screen, (30, 30, 10), (200+x, 375+y, 75, 75))
    rect(screen, (30, 30, 10), (100+x, 375+y, 75, 75))
    rect(screen, (170, 150, 150), (180+x, 220+y, 40, 100))
    rect(screen, (170, 150, 150), (110+x, 220+y, 40, 100))
    rect(screen, (170, 150, 150), (250+x, 220+y, 40, 100))
    rect(screen, (170, 150, 150), (320+x, 220+y, 40, 100))
    polygon(screen, (10, 10, 10), [(50+x, 340+y), (420+x, 340+y), (420+x, 360+y), (50+x, 360+y)])
    polygon(screen, (10, 10, 10), [(75+x, 320+y), (400+x, 320+y), (400+x, 330+y), (75+x, 330+y)])
    polygon(screen, (5, 5, 10), [(80+x, 190+y), (400+x, 190+y), (420+x, 210+y), (60+x, 210+y)])


def oblaka(x, y):
    ellipse(screen, (45, 45, 45), (450+x, 75+y, 250, 25), 50)
    ellipse(screen, (60, 60, 60), (275+x, 90+y, 280, 35), 50)
    ellipse(screen, (75, 75, 75), (450+x, 100+y, 360, 50), 50)


def ghost(x, y):
    circle(screen, (200, 200, 200), (600+x, 500+y), 25)
    polygon(screen, (200, 200, 200), [(580+x, 485+y), (620+x, 485+y), (670+x, 545+y), (560+x, 545+y), (520+x, 555+y)])
    ellipse(screen, (200, 200, 200), (580+x, 520+y, 90, 50), 25)
    ellipse(screen, (200, 200, 200), (530+x, 540+y, 100, 30), 25)
    circle(screen, (100, 100, 250), (585+x, 490+y), 5)
    circle(screen, (0, 0, 0), (585+x, 490+y), 2)
    circle(screen, (100, 100, 250), (605+x, 490+y), 5)
    circle(screen, (0, 0, 0), (605+x, 490+y), 2)
    ellipse(screen, (0, 0, 0), (585+x, 565+y, 30, 10), 25)
    ellipse(screen, (0, 0, 0), (545+x, 565+y, 30, 10), 25)
    ellipse(screen, (0, 0, 0), (525+x, 545+y, 10, 40), 25)
    ellipse(screen, (0, 0, 0), (625+x, 565+y, 30, 10), 25)
    ellipse(screen, (0, 0, 0), (660+x, 530+y, 10, 50), 100)


home(600, -50)
home(275, 50)
home(-70, 200)

ghost(0, 100)
ghost(-300, 200)
ghost(-350, 220)
ghost(300, -50)

oblaka(120, 0)
oblaka(-25, 50)
oblaka(-100, 250)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True


pygame.quit()