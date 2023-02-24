define sprite_focus = {}

default speaking_char = None

transform autosprite(sprite_name):
    function SpriteFocus(sprite_name)

init -10 python:
    import math

    def name_callback(event, interact=True, name=None, **kwargs):
        global speaking_char
        if event == "begin":
            speaking_char = name

    class SpriteFocus(object):

        def __init__(self, char_name):
            self.char_name = char_name

        def __call__(self, trans, start_time, anim_time):

            def get_ease(t):
                return .5 - math.cos(math.pi * t) / 2.0

            global sprite_focus, speaking_char
            char_name = self.char_name

            if char_name not in sprite_focus:
                sprite_focus[char_name] = False
            anim_length = 0.2
            bright_change = 0.18
            sat_change = 0.0
            zoom_change = 0.0025

            y_change = 1

            is_talking = speaking_char == char_name

            if isinstance(sprite_focus[char_name], (int, float)) and anim_time < sprite_focus[char_name]:
                sprite_focus[char_name] = is_talking

            if sprite_focus[char_name] != is_talking and isinstance(sprite_focus[char_name], bool):
                sprite_focus[char_name] = anim_time

                if renpy.is_skipping() or renpy.in_rollback():
                    sprite_focus[char_name] = is_talking

            curr_time = max(anim_time - sprite_focus[char_name],0)

            curr_ease = 1.0

            if curr_time < anim_length and not isinstance(sprite_focus[char_name], bool):
                curr_ease = get_ease(curr_time/anim_length)
            else:
                sprite_focus[char_name] = is_talking

            if is_talking:
                trans.matrixcolor = SaturationMatrix((1.0-sat_change) + curr_ease * sat_change) * BrightnessMatrix(-bright_change + curr_ease * bright_change)
                trans.zoom = min(curr_ease * zoom_change + (1.0-zoom_change), 1.0)
                trans.yoffset = y_change - curr_ease * y_change
            else:
                trans.matrixcolor = SaturationMatrix(1.0 - curr_ease * sat_change) * BrightnessMatrix(curr_ease * -bright_change)
                trans.zoom = max(1.0 - curr_ease * zoom_change, (1.0-zoom_change))
                trans.yoffset = y_change * curr_ease

            return 0
