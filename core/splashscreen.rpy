
label splashscreen:

#jump beatricechess
#jump test2
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
        show title_menu
        with gradientwipedown
        hide title_menu
        hide menu_bg

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

    if not renpy.seen_label("start"):
        play wind "audio/sfx/umilse_005.ogg"
        show different_space_1a at bgani
        show expression(CustomParticles("images/system/particle.png", 10))
        with gradientcirclefade
        show but b11warai3 at rightedge with dissolve
        window show
        but "Willkommen zu Umineko When They Cry Zero ~Waltz of Reflections and Delusions~ Sieht mir nach deinem ersten Spielstart aus, also wähle bitte eine Sprache!"
        window hide
        call butterfly1 from _call_butterfly1_2
        play sound "audio/sfx/umise_052.ogg"
        show bea a11defo2 at leftedge with witchfadein
        window show
        bea a11akuwarai4 "*Cackle*Cackle*"
        extend " ....Don't forget those who don't know German and only understand English, Battlerrrrrrr!" 
        bea a11defo2 " ....A warm Welcome to Umineko When They Cry Zero ~Waltz of Reflections and Delusions~ Please choose a language aswell."
        window hide
        menu:
            "EN-English":
                pause 1
                call hidebf1 from _call_hidebf1_2
                stop wind fadeout 1.0
                play sound "audio/sfx/umise_056.ogg"
                scene black with gradientcirclefade
                $ renpy.change_language("English")

            "DE-German":
                pause 1
                call hidebf1 from _call_hidebf1_3
                stop wind fadeout 1.0
                play sound "audio/sfx/umise_056.ogg"
                scene black with gradientcirclefade
                return

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
    show title_menu
    with gradientwipedown
    hide title_menu
    hide menu_bg
    hide unlocked1
    return
