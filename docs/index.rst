Welcome to FlugiGraphics's documentation!
==========================================

FlugiGraphics is a minimal Pygame-based graphics framework designed for educational use, lightweight graphics prototyping, and simple 2D drawing. It provides an event abstraction layer, buffered drawing, mouse/keyboard input handling, and image export capabilities.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   modules

Examples
--------

Demo Program
^^^^^^^^^^^^
A basic interactive drawing demo using `FlugiGraphics` and `Canvas`:

.. code-block:: python

    from FlugiGraphics import *

    def run_demo():
        graphics = FlugiGraphics(800, 600)
        graphics.color((0, 0, 0))
        canvas = Canvas(200, 200)
        canvas.color((255, 0, 0))
        canvas.box_to(100, 100)
        canvas.color((0, 255, 0))
        canvas.move_to(50, 50)
        canvas.box(50, 50)

        running = True
        while running:
            for event in graphics.get_events():
                if graphics.is_quit_event(event) or (event.type == 'ev_key' and event.keycode == KEY_ESCAPE):
                    running = False
                if event.type == 'ev_mouse':
                    graphics.color((0, 0, 255))
                    graphics.move_to(event.pos_x, event.pos_y)
                    graphics.dot()

            graphics.color((255, 255, 0))
            graphics.move_to(400, 300)
            graphics.line(100, 100)
            graphics.text(10, 10, "FlugiGraphics", "Arial", 36)
            canvas.draw_to(graphics.screen, 600, 400)
            graphics.refresh()
            graphics.tick(60)

        graphics.quit()

    if __name__ == '__main__':
        run_demo()

Pathfinding Example
^^^^^^^^^^^^^^^^^^^
A terrain/pathfinding visualizer with event control and graphics:

.. code-block:: python

    from FlugiGraphics import *
    import numpy as np
    import random

    class Terkep:
        def __init__(self):
            self.XX, self.YY = self.beolvas()
            self.graphics = FlugiGraphics(self.XX, self.YY)
            self.graphics.refresh()
            self.terkep = np.array(self.terkep)
            self.sziget = np.zeros_like(self.terkep)
            self.tavolsag = np.zeros_like(self.terkep)
            self.tav = 2

        def beolvas(self):
            try:
                with open("terkep.txt", "r") as bf:
                    XX, YY = map(int, bf.readline().split())
                    self.terkep = [list(map(int, bf.readline().split())) for _ in range(YY)]
                    print("Sikeres beolvasas!")
                    return XX, YY
            except FileNotFoundError:
                print("Nem sikerult megnyitni a fajlt.")

        def kirajzol(self):
            for j in range(self.YY):
                for i in range(self.XX):
                    m = self.terkep[j][i]
                    if m > 0:
                        self.graphics.color((0, min(255, 120 + m), 0))
                    else:
                        self.graphics.color((0, 0, min(255, 220 + m)))
                    self.graphics.move_to(i, j)
                    self.graphics.dot()

        def utvonal_keres(self, px1, px2, py1, py2):
            self.sziget.fill(0)
            self.tavolsag.fill(0)
            if self.terkep[py1][px1] < 0 or self.terkep[py2][px2] < 0:
                print("Nem lehet ilyen utat megjeleniteni.")
                return

            self.sziget[py1][px1] = 1
            elozo_pontok = [(px1, py1)]

            while elozo_pontok:
                uj_pontok = []
                for x, y in elozo_pontok:
                    if x == px2 and y == py2:
                        self.ut_keres(px2, py2)
                        return

                    for j in range(max(0, y - 1), min(self.YY - 1, y + 1) + 1):
                        for i in range(max(0, x - 1), min(self.XX - 1, x + 1) + 1):
                            if self.terkep[j][i] > 0 and self.sziget[j][i] == 0 and not (i == x and j == y):
                                self.sziget[j][i] = self.tav
                                uj_pontok.append((i, j))

                elozo_pontok = uj_pontok
                self.tav += 1

            print("Nincs ut")

        def ut_keres(self, px2, py2):
            counter = 0
            while self.sziget[py2][px2] != 1:
                for j in range(max(0, py2 - 1), min(self.YY - 1, py2 + 1) + 1):
                    for i in range(max(0, px2 - 1), min(self.XX - 1, px2 + 1) + 1):
                        if self.sziget[j][i] < self.sziget[py2][px2] and self.sziget[j][i] != 0:
                            px2, py2 = i, j
                            self.tavolsag[j][i] = 1
                            counter += 1
            print("Ut hossza:", counter)

        def utvonal_rajzol(self):
            for j in range(self.YY):
                for i in range(self.XX):
                    if self.tavolsag[j][i]:
                        self.graphics.color((255, 0, 0))
                        self.graphics.move_to(i, j)
                        self.graphics.dot()

    def main():
        terkep = Terkep()
        terkep.kirajzol()
        terkep.graphics.refresh()
        elozo_x = 0
        elozo_y = 0
        jel = 0

        while terkep.graphics.running:
            events = terkep.graphics.get_events()
            for ev in events:
                if ev.type == 'ev_key' and ev.keycode == -KEY_ESCAPE:
                    terkep.graphics.running = False

                if ev.type == 'ev_mouse':
                    if ev.button == -BTN_LEFT and jel == 1:
                        elozo_x, elozo_y = ev.pos_x, ev.pos_y
                        jel = 0

                    if ev.button == BTN_LEFT:
                        terkep.kirajzol()
                        uj_x, uj_y = ev.pos_x, ev.pos_y
                        jel = 1

                        if elozo_x and elozo_y:
                            terkep.utvonal_keres(elozo_x, uj_x, elozo_y, uj_y)
                            terkep.utvonal_rajzol()
                            elozo_x, elozo_y = 0, 0
                            jel = 0

                        terkep.graphics.refresh()
            terkep.graphics.refresh()
            terkep.graphics.tick(60)

        terkep.graphics.quit()

    if __name__ == "__main__":
        main()
