image blackpic:
    "images/system/black.png"

label butterfly1:
play effect "audio/sfx/umise_022.ogg"
show butterfly1
pause 2
return


label hidebf1:
play effect "audio/sfx/umise_022.ogg"
hide butterfly1
show butterfly1_0
pause 3
return

label chapterenda:

    pause 1
    show hana2 with kanon_r
    pause 1
    show screen cinemalogo
    pause 4
    show blackpic behind cinemalogo with dissolve
    stop ship fadeout 2.0
    stop wind fadeout 2.0
    stop rain fadeout 2.0
    stop music fadeout 2.0
    return

label chapterendb:

    pause 1
    stop music
    stop ship
    stop wind
    stop rain
    play sound "audio/sfx/umise_1006.ogg"
    hide rainbackscroll
    hide rainfrontscroll
    show rainbackstatic with instant
    show rainfrontstatic with instant
    show ware with instant
    pause 2
    show screen cinemalogo
    pause 4
    show blackpic behind cinemalogo with dissolve
    pause 2.0
    hide screen cinemalogo with dissolve
    return

label clockch2:

    stop music fadeout 2.0
    stop rain fadeout 2.0
    stop ship fadeout 2.0
    stop wind fadeout 2.0
    pause 3
    play sound "<from 0 to 2>/audio/sfx/umilse_1050.ogg"
    pause 7
    scene black with dissolve
    hide screen cinemalogo
    with dissolve
    return