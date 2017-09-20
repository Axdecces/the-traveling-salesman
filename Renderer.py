import pygame
import math
from util import RANDOM, PERMUTATION, ALGORITHM_NAMES


class Renderer:
    def __init__(self, game):
        self.game = game
        self.background_color = 200, 200, 200
        self.marker_size = 9
        self.loading_bar_thickness = 4
        self.padding = 32
        
        self.font = pygame.font.Font('assets/fonts/joystix monospace.ttf', 30)

    def draw(self):
        self.game.screen.fill(self.background_color)
        self.draw_shortest_path()
        self.draw_points()

        printing_distance = str(int(math.floor(self.game.calculator.shortest_distance)))
        text_distance = self.font.render(printing_distance, False, (255, 0, 0))
        self.game.screen.blit(text_distance, (self.padding, self.padding))

        self.draw_indicators()
        self.draw_algorithm_font()

    def draw_shortest_path(self):
        for index, point in enumerate(self.game.calculator.shortest_path):
            try:
                pygame.draw.line(
                    self.game.screen,
                    (100, 100, 100),
                    (
                        point.x,    # x coordinate of first point
                        point.y     # y coordinate of first point
                    ),
                    (
                        self.game.calculator.shortest_path[index+1].x,  # x coordinate of second point
                        self.game.calculator.shortest_path[index+1].y   # y coordinate of second point
                    ),
                    2
                )
            except IndexError:
                pass

    def draw_points(self):
        for point in self.game.calculator.random_points:
            draw_rect = pygame.Rect(
                point.x - math.floor(self.marker_size / 2),     # x coordinate
                point.y - math.floor(self.marker_size / 2),     # y coordinate
                self.marker_size,                               # width
                self.marker_size                                # height
        )
            pygame.draw.rect(self.game.screen, (0, 0, 0), draw_rect)

    def draw_indicators(self):
        if self.game.calculator.algorithm == RANDOM:
            self.draw_random_text()
        if self.game.calculator.algorithm == PERMUTATION:
            self.draw_permutation_text()
            self.draw_loading_bar()

    def draw_random_text(self):
        text_width, text_height = self.font.size(str(self.game.calculator.current_iteration))
        text_iterations = self.font.render(str(self.game.calculator.current_iteration), False, (255, 0, 0))
        self.game.screen.blit(
            source=text_iterations,
            dest=(
                self.game.width - text_width - self.padding,    # x coordinate of textbox
                self.game.height - text_height - self.padding   # y coordinate of textbox
            )
        )

    def draw_permutation_text(self):
        text_width, text_height = self.font.size(str(round(self.game.calculator.percentage, 2)) + "%")
        text_iterations = self.font.render(
            str(round(self.game.calculator.percentage, 2)) + "%",
            False,
            (255, 0, 0))
        self.game.screen.blit(
            source=text_iterations,
            dest=(
                self.game.width - text_width - self.padding,    # x coordinate of textbox
                self.game.height - text_height - self.padding   # y coordinate of textbox
            )
        )

    def draw_loading_bar(self):
        self.loading_bar_progress = self.game.calculator.percentage / 100 * self.game.width
        draw_rect = pygame.Rect(
            0,
            self.game.height - self.loading_bar_thickness,
            self.loading_bar_progress,
            self.loading_bar_thickness,
        )

        pygame.draw.rect(self.game.screen, (255, 0, 0), draw_rect)

    def draw_algorithm_font(self):
        text_algorithm_type = self.font.render(ALGORITHM_NAMES[self.game.calculator.algorithm], False, (255, 0, 0))
        text_type_width, text_type_height = self.font.size(ALGORITHM_NAMES[self.game.calculator.algorithm])
        self.game.screen.blit(
            source=text_algorithm_type,
            dest=(
                self.game.width - text_type_width - self.padding,   # x coordinate of textbox
                self.padding                                        # y coordinate of textbox
            )
        )
