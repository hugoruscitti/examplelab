# -*- encoding: utf-8 -*-
import pygame


class Control:
    "Gestiona todos los movimientos del joystick."

    def __init__(self):
        pygame.display.init()
        pygame.joystick.init()
        print "Iniciando el programa."
        
        self.quit = False
        self.joysticks = []
        self._create_joysticks()

    def _create_joysticks(self):
        "Verifica si se ha conectado un joystics."

        count = pygame.joystick.get_count()

        if count > len(self.joysticks):
            # Atiene la conexión de un Joystick

            new = pygame.joystick.Joystick(count - 1)
            new.init()
            print "Se ha conectado el Joystick:", new.get_name()
            self.joysticks.append(new)

    def loop(self):
        "Atiende los eventos de la aplicacion."

        while not self.quit:

            for e in pygame.event.get():
                print e

                if e.type == pygame.QUIT:
                    quit = True

            pygame.time.wait(10)


if __name__ == '__main__':
    control = Control()
    control.loop()

