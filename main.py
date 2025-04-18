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


# Example usage
if __name__ == "__main__":
    gout = SimpleGraphics(800, 600)
    gout.color((255, 0, 0))  # Red
    gout.move_to(10, 10)
    gout.dot()
    gout.line_to(200, 200)
    gout.color((0, 255, 0))  # Green
    gout.move_to(50, 50)
    gout.box(100, 50)
    # gout.refresh()
    # Create and use a canvas
    canvas = Canvas(200, 150)
    canvas.set_pixel(10, 10, (0, 0, 255))  # Blue pixel on canvas
    canvas.draw_line((0, 0), (200, 150), (255, 255, 0))  # Yellow line on canvas
    canvas.draw_box(pygame.Rect(10, 10, 50, 50), (0, 255, 255))  # Cyan box
    canvas.draw_to(gout.buffer, 300, 300)  # Draw canvas onto the main buffer

    while gout.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gout.running = False
            elif event.type == pygame.KEYDOWN:
                print(f"Key pressed: {pygame.key.name(event.key)}")
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                print(f"Mouse button pressed at ({x}, {y})")

        gout.refresh()
        gout.clock.tick(60)

    pygame.quit()