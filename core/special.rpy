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

image ctc_blink:
    "GUI/arrow.png"
    linear 0.75 alpha 1.0
    linear 0.75 alpha 0.0
    repeat

image copyright = "gui/title/copyright.png"
image titlehana = "gui/title/title_hana.png"
image menu_bg = "images/backgrounds/mmbg.png"
image clouds = "images/backgrounds/mmbackground.png"