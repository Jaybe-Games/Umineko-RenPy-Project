
label splashscreen:

#jump beatricechess
#jump test2
#jump debug

if not renpy.seen_label("start"):
    show text "Select a Language / Wähle eine Sprache" at texttop
    menu:
        "English":
            $ renpy.change_language("English")
            hide text
            jump start

        "Deutsch":
            hide text
            jump start

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
    pause 0.1

    if persistent.newelement1 == False:
        show menu_bg at bganistart
        show copyright at left
        show titlehana at topright
        with gradientwipedown
        hide titlehana
        hide copyright

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
    pause 0.1

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
    hide screen tipupdate
    hide screen charupdate
    play sound "audio/sfx/umise_1006.ogg"

label before_main_menu:
    if persistent.newelement1 == True:
        $ persistent.newelement1 = False
        play effect "audio/sfx/umise_022.ogg"
        show unlocked1 with gradientcirclefade
        pause(5)
    show menu_bg at bganistart
    show copyright at left
    show titlehana at topright
    with gradientwipedown
    hide titlehana
    hide copyright
    hide unlocked1
    return
