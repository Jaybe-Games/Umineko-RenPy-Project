init python hide:

    class KonamiListener(renpy.Displayable):

        def __init__(self, target):

            renpy.Displayable.__init__(self)

            import pygame
            
            self.target = target

            self.state = 0

            self.code = [
                pygame.K_UP,
                pygame.K_UP,
                pygame.K_DOWN,
                pygame.K_DOWN,
                pygame.K_LEFT,
                pygame.K_RIGHT,
                pygame.K_LEFT,
                pygame.K_RIGHT,
                pygame.K_b,
                pygame.K_a,
                ]

        def event(self, ev, x, y, st):
            import pygame

            if ev.type != pygame.KEYDOWN:
                return

            if ev.key != self.code[self.state]:
                self.state = 0
                return

            self.state += 1

            if self.state == len(self.code):
                self.state = 0
                renpy.call_in_new_context(self.target)

            return

        def render(self, width, height, st, at):
            return renpy.Render(1, 1)


    store.konami_listener = KonamiListener('konami_code')

    def konami_overlay():
        ui.add(store.konami_listener)

    config.overlay_functions.append(konami_overlay)


label konami_code:
    window hide
    play sound "audio/sfx/umise_1021.ogg"
    play sound "audio/sfx/nipah.mp3"
    show nipah at truecenter with quickergradientwiperight
    pause 2.2
    hide nipah with quickergradientwiperight
    window show

    return