# demo.py

from FlugiGraphics import *

def run_demo():
    # Initialize SimpleGraphics
    graphics = FlugiGraphics(800, 600)
    graphics.color((0, 0, 0))  # Set background color

    # Create a Canvas
    canvas = Canvas(200, 200)
    canvas.color((255, 0, 0))  # Red
    canvas.box_to(100, 100)
    canvas.color((0, 255, 0))  # Green
    canvas.move_to(50, 50)
    canvas.box(50, 50)

    running = True
    while running:
        for event in graphics.get_events():
            if graphics.is_quit_event(event) or (event.type == 'ev_key' and event.keycode == KEY_ESCAPE):
                running = False
            if event.type == 'ev_mouse':
                graphics.color((0, 0, 255))  # Blue
                graphics.move_to(event.pos_x, event.pos_y)
                graphics.dot()

        # Draw a line
        graphics.color((255, 255, 0))  # Yellow
        graphics.move_to(400, 300)
        graphics.line(100, 100)

        # Draw text
        graphics.text(10, 10, "FlugiGraphics", "Arial", 36)

        # Draw the canvas onto the main screen
        canvas.draw_to(graphics.screen, 600, 400)

        # Refresh the screen
        graphics.refresh()
        graphics.tick(60)

    graphics.quit()

if __name__ == '__main__':
    run_demo()