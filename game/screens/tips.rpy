screen tipps():

    tag menu
    modal True
    if main_menu:
        add "gui/title/bg.png"
    add "gui/bgdark.png" at center
    text _("Tips") outlines [ (absolute(4), "#00000094", absolute(1), absolute(1)) ] size 90 font "fonts/Georgia.ttf" xalign 0.5 yalign 0.03
    add "gui/tipps/background.png" at center
    add partObj
    if main_menu:
        imagebutton auto "images/system/back2_%s.png" action Return() activate_sound "audio/sys/sysse_cancel.wav" hover_sound "audio/sys/sysse_move.wav" yalign 0.02 xalign 0.97
    else:
        imagebutton auto "images/system/back2_%s.png" action [ShowMenu("game_menu"), Hide("tipps")] activate_sound "audio/sys/sysse_cancel.wav" hover_sound "audio/sys/sysse_move.wav" yalign 0.02 xalign 0.97

## To do: Adding a screen to select episode specific tips
screen tip01():

    tag menu
    modal True
    use tipps


screen tip02():

    tag menu
    modal True
    use tipps


screen tip03():

    tag menu
    modal True
    use tipps
