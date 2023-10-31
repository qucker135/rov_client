import pygame
from .model import Model


class View:
    def __init__(self, screen: pygame.Surface) -> None:
        self.screen = screen
        self.empty_image = pygame.image.load('imgs/empty.png')
        self.submarine_image = pygame.image.load('imgs/submarine.png')
        self.mine_image = pygame.image.load('imgs/mine.png')
        self.x_image = pygame.image.load('imgs/x.png')

    def draw(self, model: Model, path: list[tuple[int, int]]) -> None:
        self.screen.fill("black")

        screen_width = self.screen.get_width()
        screen_height = self.screen.get_height()

        m = model.get_data()

        if len(path) > 1:
            self._draw_path(path)

        for i_row, row in enumerate(m):
            for i_col, col in enumerate(row):
                img_to_draw = self.empty_image
                if m[i_row][i_col] == "r":
                    img_to_draw = self.submarine_image
                elif m[i_row][i_col] == "o":
                    img_to_draw = self.mine_image
                elif m[i_row][i_col] == "x":
                    img_to_draw = self.x_image
                pygame.Surface.blit(
                    self.screen,
                    img_to_draw,
                    (
                        i_col * 50 + screen_width / 2 - 250,
                        i_row * 50 + screen_height / 2 - 300
                    )
                )
        pygame.display.flip()

    def _draw_path(self, path: list[tuple[int, int]]):
        for p, k in zip(path[:-1], path[1:]):
            rect = pygame.Rect(
                min(p[1], k[1]) * 50 + self.screen.get_width() / 2 - 250 + 13,
                min(p[0], k[0]) * 50 + self.screen.get_height() / 2 - 300 + 13,
                6 + abs(p[1] - k[1]) * 44,
                6 + abs(p[0] - k[0]) * 44
            )
            pygame.draw.rect(
                self.screen,
                (0, 255, 255),
                rect
            )
