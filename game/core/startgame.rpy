label startgame:
    $ songname = "-"
    $ _game_menu_screen = None
    stop music fadeout 1.0
    stop sound fadeout 1.0
    play sound "audio/sfx/umise_017.ogg"
    scene white zorder 80
    with kanon_r
    $ renpy.pause(2, hard=True)
    scene black with dissolve
    jump start
    return

label starttea:
    $ _game_menu_screen = None
    $ songname = "-"
    stop music fadeout 1.0
    stop sound fadeout 1.0
    play sound "audio/sfx/umise_017.ogg"
    scene white zorder 80
    with kanon_r
    $ renpy.pause(2, hard=True)
    scene black with dissolve
    jump starttea
    return

label startura:
    $ _game_menu_screen = None
    $ songname = "-"
    stop music fadeout 1.0
    stop sound fadeout 1.0
    play sound "audio/sfx/umise_017.ogg"
    scene white zorder 80
    with kanon_r
    $ renpy.pause(2, hard=True)
    scene black with dissolve
    jump startura
    return