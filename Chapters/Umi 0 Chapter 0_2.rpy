label chapter2:

    $ renpy.notify("Kapitel 2 - Unerwartete Tragödie")
    pause (2)
    show text "Der erste Tag\n04. Oktober 1986\n10:25 Uhr" with dissolve
    pause (2)
    play sound "audio/sfx/umilse_1050.ogg"
    show text "Der erste Tag\n04. Oktober 1986\n10:26 Uhr"
    pause (0.8)
    show text "Der erste Tag\n04. Oktober 1986\n10:27 Uhr"
    pause (0.8)
    show text "Der erste Tag\n04. Oktober 1986\n10:28 Uhr"
    pause (0.8)
    show text "Der erste Tag\n04. Oktober 1986\n10:29 Uhr"
    pause (0.8)
    show text "Der erste Tag\n04. Oktober 1986\n10:30 Uhr"
    stop sound
    pause (5)
    hide text with dissolve
    pause (2)
    camera:
        anchor (0.5, 0.5)
        pos (960, 540)
        matrixcolor IdentityMatrix()
