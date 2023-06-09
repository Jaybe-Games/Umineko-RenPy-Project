
label splashscreen:

jump test
scene black with dissolve
pause (1)
show splash1 with dissolve
pause (1.5)
hide splash1 with dissolve
pause (1)
show splash2 with dissolve
pause (1.5)
hide splash2 with dissolve
pause (1)
show splash3 with dissolve
pause (1.5)
hide splash3 with dissolve
pause (1)

if persistent.openingplayed == True:
    $ renpy.movie_cutscene("videos/opening.mov")
    pause (1)
    show load1 at right
    pause 0.1

    hide load1
    show load2 at right
    pause 0.1

    hide load2
    show load3 at right
    pause 0.1

    hide load3
    show load4 at right
    pause 0.1

    hide load4
    show load1 at right
    pause 0.1

    hide load1
    show load2 at right
    pause 0.1

    hide load2
    show load3 at right
    pause 0.1

    hide load3
    show load4 at right
    pause 0.1

    hide load4
    return
else:
    pause (1)
    show load1 at right
    pause 0.1

    hide load1
    show load2 at right
    pause 0.1

    hide load2
    show load3 at right
    pause 0.1

    hide load3
    show load4 at right
    pause 0.1

    hide load4
    show load1 at right
    pause 0.1

    hide load1
    show load2 at right
    pause 0.1

    hide load2
    show load3 at right
    pause 0.1

    hide load3
    show load4 at right
    pause 0.1

    hide load4
    return

label quit:
    if menuquit == True:
        hide window
        $ menuquit = False
        return
    hide window
    stop music fadeout 1.0
    stop rain fadeout 1.0
    stop ship fadeout 1.0
    stop wind fadeout 1.0
    play sound "audio/sfx/umise_018.ogg"
    scene black zorder 99
    with kanon_rev
    $ renpy.pause(1, hard=True)
    return

label after_load:
    play sound "audio/sfx/umise_1006.ogg"