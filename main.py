import pygame
from src.utils import Direction
from src.model import Model
from src.controller import Controller
from src.view import View
from src.finder import Finder

running = True
key_pressed = False
SERVER_ADDR = "http://localhost:8000/"

if __name__ == "__main__":
    pygame.init()

    clock = pygame.time.Clock()
    m = Model([[" ", " ", " "], [" ", "r", " "], [" ", " ", " "]])
    c = Controller()
    c.get_data(m, SERVER_ADDR)
    screen = pygame.display.set_mode((1000, 1000))
    v = View(screen)
    f = Finder()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                key_pressed = True
            if event.type == pygame.KEYUP:
                key_pressed = False

        if key_pressed:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                c.post_command(SERVER_ADDR, Direction.UP)
            if keys[pygame.K_DOWN]:
                c.post_command(SERVER_ADDR, Direction.DOWN)
            if keys[pygame.K_LEFT]:
                c.post_command(SERVER_ADDR, Direction.LEFT)
            if keys[pygame.K_RIGHT]:
                c.post_command(SERVER_ADDR, Direction.RIGHT)
            c.get_data(m, SERVER_ADDR)
            key_pressed = False

        path = f.find_path(m)
        v.draw(m, path)
        clock.tick(60)

    pygame.quit()
