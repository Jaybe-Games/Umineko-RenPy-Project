init python:
    def getPlayTime():

        pt = renpy.get_game_runtime()

        pth = int(pt // 3600)

        ptm = int(pt - pth * 3600) // 60

        pts = int(pt - (pth * 3600) - (ptm * 60))

        return "{:02d}:{:02d}:{:02d}".format(pth, ptm, pts)

screen game_menu(scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    add "gui/gamemenu/hanabottom.png" at hanabottomtransform
    add "gui/gamemenu/hanatop.png" at hanatoptransform
    add "gui/gamemenu/darken.png" at center
    imagebutton auto "images/system/back2_%s.png" action Return() activate_sound "audio/sys/sysse_cancel.wav" hover_sound "audio/sys/sysse_move.wav" yalign 0.02 xalign 0.97
    add partObj

    ### Wieder ein If der überflüssiger nicht sein kann, wird mal Zeit für ein wenig Code aufräumen

    vbox:

        yalign 0.5
        xalign 0.98

        imagebutton auto "gui/gamemenu/save_%s.png" action ShowMenu("save") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav" at gamemenubuttontransform

        imagebutton auto "gui/gamemenu/load_%s.png" action ShowMenu("load") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav" at gamemenubuttontransform

        imagebutton auto "gui/gamemenu/backlog_%s.png" action ShowMenu("history") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav" at gamemenubuttontransform

        imagebutton auto "gui/gamemenu/settings_%s.png" action [ShowMenu("preferences")] activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav" at gamemenubuttontransform

        imagebutton auto "gui/gamemenu/control_%s.png" action [ShowMenu("help")] activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav" at gamemenubuttontransform

        imagebutton auto "gui/gamemenu/trophy_%s.png" action [ShowMenu("achievement_menu"), Hide('trophyhover')] activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav" at gamemenubuttontransform

        if persistent.battler == True:
            imagebutton auto "gui/gamemenu/chars_%s.png" action [ShowMenu("characters"), Hide('characterhover')] activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav" at gamemenubuttontransform
        else:
            pass

        if persistent.tipunlocked == True:
            imagebutton auto "gui/gamemenu/tip_%s.png" action [ShowMenu("tipps"), Hide('tiphover')] activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav" at gamemenubuttontransform

        imagebutton auto "gui/gamemenu/backtomain_%s.png" action MainMenu() activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav" at gamemenubuttontransform

    text "♪" + songname ypos 1005 xpos 1900 xalign 1.0 size 30 font "fonts/AOTFShinGoProMedium.otf" outlines [ (absolute(3), "#000", absolute(0), absolute(0)) ]

    text _("Spielzeit: ") + getPlayTime() ypos 1040 xpos 1900 xalign 1.0 size 30 font "fonts/AOTFShinGoProMedium.otf" outlines [ (absolute(3), "#000", absolute(0), absolute(0)) ]


## Dieser Screen hatte mal irgend einen Sinn für einen Workaround
## Ich erinnere mich, ohne den scheiß, kann man das Menü nicht öffnen.
screen cleanmenu():

    tag menu
    add partObj

    use game_menu()



style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    #background "gui/game_menu1.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True
    xpos 0

style game_menu_content_frame:
    left_margin -400
    right_margin 700
    top_margin -70
    bottom_margin 150

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 100

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45