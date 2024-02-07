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

default menuquit = False
image confirmblack = Solid("#0000005a")

label quit_scene:
    $ menuquit = True
    hide window
    stop music fadeout 1.0
    play sound "audio/sfx/umise_018.ogg"
    scene black zorder 99
    camera
    with kanon_rev
    $ renpy.pause(4, hard=True)
    $ Quit(confirm=False)()
    return
init -3 python:
    class QuitWithScene(Action):
        def __call__(self):
            renpy.call_in_new_context("quit_scene")
            renpy.quit()
            return

label title_return:
    hide window
    stop music fadeout 2.0
    play sound "audio/sfx/umise_018.ogg"
    scene black zorder 99
    camera
    with kanon_rev
    $ renpy.pause(4, hard=True)
    return
init -3 python:
    class titurnd(Action):
        def __call__(self):
            renpy.call_in_new_context("title_return")
            return

label splashscreen:

#jump beatricechess
#jump schule
jump debug

if not renpy.seen_label("start"):
    show text "Select a Language / Wähle eine Sprache" at texttop
    menu:
        "English":
            $ renpy.change_language("English")
            hide text
            return
            

        "Deutsch":
            hide text
            return

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
    #$ renpy.movie_cutscene("videos/opening.mov")
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
    hide screen tipupdate
    hide screen charupdate
    play sound "audio/sfx/umise_1006.ogg"

label before_main_menu:
    if persistent.newelement1 == True:
        $ persistent.newelement1 = False
        play effect "audio/sfx/umise_022.ogg"
        show unlocked1 with gradientcirclefade
        pause(5)
    show clouds at mmclouds
    show menu_bg
    show rainbackscroll
    show rainfrontscroll
    show copyright at left
    show titlehana at topright
    with gradientwipedown
    hide clouds
    hide menu_bg
    hide rainbackscroll
    hide rainfrontscroll
    hide titlehana
    hide copyright
    hide unlocked1
    return

label credits:
    $ renpy.pause(3, hard=True)
    $ songname = "Golden Sneers - Lovely Banquet"
    $ _skipping = False
    $ play_music(ending)
    show credits at credits_scroll
    $ renpy.pause(293, hard=True)   
    stop music
    $ renpy.pause(5, hard=True)   
    scene black with kanon_rev
    $ renpy.pause(5, hard=True)   
    $ _skipping = True 
    return

label endroll:
    $ renpy.pause(3, hard=True)
    $ songname = "Bring the Fate"
    $ _skipping = False
    $ play_music(endroll)
    show endroll at end_scroll
    $ renpy.pause(224, hard=True)   
    stop music
    $ renpy.pause(5, hard=True)   
    scene black with kanon_rev
    $ renpy.pause(5, hard=True)   
    $ _skipping = True 
    return

label gameresult:

    $ _skipping = False
    show gameresult at gameresult_scroll
    $ renpy.pause(105, hard=True)   
    $ renpy.pause(5, hard=True)   
    scene black with kanon_r
    stop music fadeout 5.0
    $ renpy.pause(5, hard=True)   
    $ _skipping = True 
    return