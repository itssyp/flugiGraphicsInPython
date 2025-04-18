# simplegraphics/graphics.py

import pygame

KEY_ESCAPE = pygame.K_ESCAPE
KEY_SPACE = pygame.K_SPACE
KEY_ENTER = pygame.K_RETURN
KEY_BACKSPACE = pygame.K_BACKSPACE
KEY_UP = pygame.K_UP
KEY_DOWN = pygame.K_DOWN
KEY_LEFT = pygame.K_LEFT
KEY_RIGHT = pygame.K_RIGHT
# Add other keys as needed...

BTN_LEFT = 1
BTN_RIGHT = 3
BTN_MIDDLE = 2

class Event:
    def __init__(self, event):
        self.type = None
        self.keycode = None
        self.button = None
        self.pos_x = None
        self.pos_y = None

        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            self.type = 'ev_key'
            self.keycode = event.key if event.type == pygame.KEYDOWN else -event.key
        elif event.type in (pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP):
            self.type = 'ev_mouse'
            self.button = event.button if event.type == pygame.MOUSEBUTTONDOWN else -event.button
            self.pos_x, self.pos_y = event.pos


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

    def get_events(self):
        return [Event(event) for event in pygame.event.get()]

    def get_custom_event(self):
        for event in pygame.event.get():
            yield Event(event)

    def is_quit_event(self, event):
        return event.type == pygame.QUIT

    def is_keydown_event(self, event):
        return event.type == pygame.KEYDOWN

    def handle_keydown(self, event):
        print(f"Key pressed: {pygame.key.name(event.key)}")

    def is_mouse_event(self, event):
        return event.type == pygame.MOUSEBUTTONDOWN

    def handle_mouse_event(self, event):
        x, y = event.pos
        print(f"Mouse button pressed at ({x}, {y})")

    def tick(self, fps):
        self.clock.tick(fps)

    def quit(self):
        pygame.quit()

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

    def set_pixel(self, x, y, color):
        self.buffer.set_at((x, y), color)

    def draw_line(self, start_pos, end_pos, color, width=1):
        pygame.draw.line(self.buffer, color, start_pos, end_pos, width)

    def draw_box(self, rect, color):
        pygame.draw.rect(self.buffer, color, rect)