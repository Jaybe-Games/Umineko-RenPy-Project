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
    hide rain
    hide rain2
    hide rain3
    stop music
    stop ship
    stop wind
    stop rain
    play sound "audio/sfx/umise_1006.ogg"
    show ware
    pause 2
    show screen cinemalogo
    pause 4
    show blackpic behind cinemalogo with dissolve
    return

label chapterendsecret:

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
    pause 2.0
    hide screen cinemalogo with dissolve
    pause 1
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
    scene blackpic with dissolve
    hide screen clocktimu_break1 with dissolve
    pause 1
    hide screen cinemalogo with dissolve
    return

label rainlayer:
    
    show rain
    show rain2
    show rain3
    show rain4
    return

label hiderain:
    hide rain with dissolve
    pause 0.5
    hide rain2 with dissolve
    pause 0.5
    hide rain3 with dissolve
    pause 0.5
    hide rain4 with dissolve
    stop rain fadeout 1.0
    return