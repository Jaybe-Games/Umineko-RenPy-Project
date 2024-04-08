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
#jump school
#jump test
#jump chapter2

# if not renpy.seen_label("start"):
#     show text "Select a Language / Wähle eine Sprache" at texttop
#     menu:
#         "English":
#             $ renpy.change_language("English")
#             hide text
#             return
            

#         "Deutsch":
#             hide text
#             return

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
    call screen press_to_start with dissolve
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
    call screen press_to_start with dissolve
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
    hide screen showch
    play sound "audio/sfx/umise_1006.ogg"

label before_main_menu:
    if persistent.newelement1 == True:
        $ persistent.newelement1 = False
        play effect "audio/sfx/umise_022.ogg"
        show unlocked1 with gradientcirclefade
        pause(5)
    else:
        pass