FlugiGraphics Modules
=======================

This project contains the following components:

Event Class
-----------

Encapsulates `pygame` events for keyboard and mouse. Maps:

- `ev_key`: Key pressed/released (positive or negative keycode)
- `ev_mouse`: Mouse click, release, or motion (button info and position)
- `ev_timer`: Custom/timer events (via `pygame.USEREVENT`)

BaseGraphics Class
------------------

Provides core drawing operations on an off-screen buffer.

Methods include:
- `move(x, y)` / `move_to(x, y)`
- `color(rgb_tuple)`
- `dot()`
- `line(x, y)` / `line_to(x, y)`
- `box(width, height)` / `box_to(x, y)`
- `text(x, y, str, font='Arial', size=24, color=(255,255,255))`

FlugiGraphics Class
-------------------

Inherits `BaseGraphics`. Adds window management and runtime loop support.

Methods include:
- `refresh()` – Draw buffer to display
- `tick(fps)` – Cap FPS
- `quit()` – Close pygame
- `get_events()` – Return a list of `Event` objects
- `show_mouse(True/False)`, `move_mouse(x, y)`

Canvas Class
------------

Extends `BaseGraphics` with file and pixel-level tools.

Methods:
- `draw_to(target_surface, x, y)`
- `set_pixel(x, y, color)`
- `save(filename)` – Export canvas as an image
- `transparent(True/False)` – Enable per-pixel alpha
- `load_font(file, size)` and `antialias(True/False)`

Constants
---------

Includes keyboard/mouse constants like:
- `KEY_BACKSPACE`, `KEY_ENTER`, `KEY_F1`, ..., `KEY_UP`
- `BTN_LEFT`, `BTN_MIDDLE`, `BTN_RIGHT`