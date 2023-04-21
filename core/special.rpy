default menuquit = False
image confirmblack = Solid("#0000005a")

label quit_scene:
    $ menuquit = True
    hide window
    stop music fadeout 1.0
    play sound "audio/sfx/umise_018.ogg"
    scene black zorder 99
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
    with kanon_rev
    $ renpy.pause(4, hard=True)
    return
init -3 python:
    class titurnd(Action):
        def __call__(self):
            renpy.call_in_new_context("title_return")
            return

init python: 
    renpy.game.preferences.pad_enabled = False