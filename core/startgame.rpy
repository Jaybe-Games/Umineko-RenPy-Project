label startgame:
    $ chapternumber = "Prolog"
    $ chaptername = "\"Ich schreibe an dich in einer Quadrillion Jahren\""
    $ songname = "-"
    $ _game_menu_screen = None
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
    $ _game_menu_screen = None
    $ chapternumber = "Tee Party"
    $ chaptername = "\"Eins zu einer Quadrillion\""
    $ songname = "-"
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
    $ _game_menu_screen = None
    $ chapternumber = "????"
    $ chaptername = "\"Die Illusionen der Falschen Hexe\""
    $ songname = "-"
    stop music fadeout 1.0
    stop sound fadeout 1.0
    play sound "audio/sfx/umise_017.ogg"
    scene white zorder 80
    with kanon_r
    $ renpy.pause(4, hard=True)
    scene black with dissolve
    jump startura
    return