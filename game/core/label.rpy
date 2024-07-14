label start:
    $ songname = "-"
    $ _game_menu_screen = None
    stop music fadeout 1.0
    stop sound fadeout 1.0
    play sound "audio/sfx/umise_017.ogg"
    scene white zorder 80
    with kanon_r
    $ renpy.pause(2, hard=True)
    scene black with dissolve
    pause 3
    play sound umise_028
    show screen disclaimer
    pause 10
    hide screen disclaimer
    scene black
    with dissolve
    pause 3
    if ep1_start == True:
        $ ep1_start = False
        jump umi1_1
    elif ep2_start == True:
        $ ep2_start = False
        jump umi2_1
    elif ep3_start == True:
        $ ep3_start = False
        jump umi3_1
    elif ep4_start == True:
        $ ep4_start = False
        jump umi4_1
    elif ep5_start == True:
        $ ep5_start = False
        jump umi5_1
    elif ep6_start == True:
        $ ep6_start = False
        jump umi6_1
    elif ep7_start == True:
        $ ep7_start = False
        jump umi7_1
    elif ep8_start == True:
        $ ep8_start = False
        jump umi8_1
    else:
        return


default menuquit = False
image confirmblack = Solid("#0000005a")

label quit_scene:
    $ menuquit = True
    stop music fadeout 1.0
    play sound "audio/sfx/umise_018.ogg"
    scene black zorder 99
    camera
    with kanon_rev
    $ renpy.pause(4, hard=True)
    $ Quit()
    return
init -3 python:
    class QuitWithScene(Action):
        def __call__(self):
            renpy.call_in_new_context("quit_scene")
            renpy.quit()
            return

label title_return:
    window hide
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


image splash:
    "images/system/splash1.png" with dissolve
    1.5
    "images/system/black.png" with dissolve
    1
    "images/system/splash2.png" with dissolve
    1.5
    "images/system/black.png" with dissolve
    1
    "images/system/splash3.png" with dissolve
    1.5
    "images/system/black.png" with dissolve

image loadbutterfly:
    "images/system/load1.png"
    .15
    "images/system/load2.png"
    .15
    "images/system/load3.png"
    .15
    "images/system/load4.png"
    .15
    repeat

label splashscreen:
    pause 1
    show splash at center
    pause 8
    hide splash
    if persistent.gamemode == "rondo":
        $ renpy.movie_cutscene("videos/op1.mkv")
    else:
        $ renpy.movie_cutscene("videos/op2.mkv")
    pause 1
    show loadbutterfly at right
    pause 2
    hide loadbutterfly with dissolve
    return

label switch_game_mode:
    play sound "audio/sfx/umise_1006.ogg"
    show ware
    pause 2.0
    hide ware
    if persistent.gamemode == "rondo":
        $ persistent.gamemode = "nocturne"
    else:
        $ persistent.gamemode = "rondo"
    jump splashscreen

label quit:
    if menuquit == True:
        window hide
        $ menuquit = False
        return
    window hide
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
    hide screen showch
    hide screen showsong
    play sound "audio/sfx/umise_1006.ogg"

label before_main_menu:
    if persistent.newelement1 == True:
        $ persistent.newelement1 = False
        play effect "audio/sfx/umise_022.ogg"
        show unlocked1 with gradientcirclefade
        pause(5)
        return
    return