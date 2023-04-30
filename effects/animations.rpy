label butterfly1:

play sound "audio/sfx/umise_022.ogg"
show butterfly1
pause(2.495)
show no83_0051
return


label hidebf1:

play sound "audio/sfx/umise_022.ogg"
show butterfly1_0
pause(0.05)
hide no83_0051
return

label chapterenda:

    pause 1
    stop ship fadeout 2.0
    stop wind fadeout 2.0
    stop rain fadeout 2.0
    show hana2 with kanon_r
    pause 1
    show screen cinemalogo
    pause 4
    show black behind cinemalogo with dissolve
    return

label chapterendb:

    pause 1
    hide rain
    stop music
    stop ship
    stop wind
    stop rain
    play sound "audio/sfx/umise_1006.ogg"
    show ware
    pause 2
    show screen cinemalogo
    pause 4
    show black behind cinemalogo with dissolve
    return

label clockch2:

    stop music fadeout 2.0
    stop rain fadeout 2.0
    stop ship fadeout 2.0
    stop wind fadeout 2.0
    pause 3
    show screen clocktimu_break1
    play sound "<from 0 to 2>/audio/sfx/umilse_1050.ogg"
    pause 7
    scene black with dissolve
    hide screen clocktimu_break1 with dissolve
    pause 1
    hide screen cinemalogo with dissolve
    return