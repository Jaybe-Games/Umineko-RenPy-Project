transform butterflies:
    xalign 0.5
    yalign 0.9320

screen say(who, what, slow_effect = slow_typewriter, slow_effect_delay = 0, always_effect = None):

    default two_window = True
    default sx = 0.5
    default sy = 0.975
    default sr = 0.0

    vbox:
        xalign sx
        yalign sy
        style "say_two_window_vbox"
        if who:
            window:
                xalign sr
                yoffset 40
                style "say_who_window"
                text who:
                    id "who" at dialogue_gradient
        window:
            xalign sx
            yalign sy
            id "window"
            has vbox:
                style "say_vbox"
            fancytext what id "what" slow_effect slow_effect slow_effect_delay slow_effect_delay always_effect always_effect at dialogue_gradient
    #add "gui/butterflies.png" at butterflies


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')