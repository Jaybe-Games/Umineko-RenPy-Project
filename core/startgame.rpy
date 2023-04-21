label startgame:
    stop music fadeout 1.0
    stop sound fadeout 1.0
    play sound "audio/sfx/umise_017.ogg"
    scene white zorder 80
    with kanon_r
    $ renpy.pause(4, hard=True)
    scene black with dissolve
    jump start
    return

label starttea:
    stop music fadeout 1.0
    stop sound fadeout 1.0
    play sound "audio/sfx/umise_017.ogg"
    scene white zorder 80
    with kanon_r
    $ renpy.pause(4, hard=True)
    scene black with dissolve
    jump starttea
    return

label startura:
    stop music fadeout 1.0
    stop sound fadeout 1.0
    play sound "audio/sfx/umise_017.ogg"
    scene white zorder 80
    with kanon_r
    $ renpy.pause(4, hard=True)
    scene black with dissolve
    jump startura
    return