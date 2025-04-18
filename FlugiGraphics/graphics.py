# simplegraphics/graphics.py

import pygame

class SimpleGraphics:
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.running = True
        self.current_pos = (0, 0)
        self.current_color = (255, 255, 255)
        self.buffer = pygame.Surface((width, height))

    def move(self, x, y):
        self.current_pos = (self.current_pos[0] + x, self.current_pos[1] + y)

    def move_to(self, x, y):
        self.current_pos = (x, y)

    def color(self, color):
        self.current_color = color

    def dot(self):
        self.buffer.set_at(self.current_pos, self.current_color)

    def draw_line(self, start_pos, end_pos, color, width=1):
        pygame.draw.line(self.buffer, color, start_pos, end_pos, width)

    def line_to(self, x, y):
        self.draw_line(self.current_pos, (x, y), self.current_color)
        self.move_to(x, y)

    def draw_box(self, rect, color):
        pygame.draw.rect(self.buffer, color, rect)

    def box(self, width, height):
        rect = pygame.Rect(self.current_pos, (width, height))
        pygame.draw.rect(self.buffer, self.current_color, rect)

    def box_to(self, x, y):
        width = x - self.current_pos[0]
        height = y - self.current_pos[1]
        self.box(width, height)
        self.move_to(x, y)

    def draw_text(self, x, y, text, font_name='Arial', size=24, color=(255, 255, 255)):
        font = pygame.font.SysFont(font_name, size)
        text_surface = font.render(text, True, color)
        self.buffer.blit(text_surface, (x, y))

    def refresh(self):
        self.screen.blit(self.buffer, (0, 0))
        pygame.display.flip()

    def show_mouse(self, show):
        pygame.mouse.set_visible(show)

    def move_mouse(self, x, y):
        pygame.mouse.set_pos(x, y)

class Canvas:
    def __init__(self, width, height):
        self.buffer = pygame.Surface((width, height), pygame.SRCALPHA)

    def draw_to(self, target_surface, x, y):
        target_surface.blit(self.buffer, (x, y))

    def move(self, x, y):
        self.current_pos = (self.current_pos[0] + x, self.current_pos[1] + y)

    def set_pixel(self, x, y, color):
        self.buffer.set_at((x, y), color)

    def draw_line(self, start_pos, end_pos, color, width=1):
        pygame.draw.line(self.buffer, color, start_pos, end_pos, width)

    def draw_box(self, rect, color):
        pygame.draw.rect(self.buffer, color, rect)