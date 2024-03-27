screen tipps():

    tag menu
    modal True
    if main_menu:
        add "images/backgrounds/mmbackground.png" at mmclouds
        add "images/backgrounds/mmbg.png"
        add "rainbackscroll"
        add "rainfrontscroll"
    text _("Tipps") outlines [ (absolute(4), "#00000094", absolute(1), absolute(1)) ] size 90 font "fonts/Georgia.ttf" xalign 0.5 yalign 0.03
    add "gui/tipps/background.png" at center
    add partObj
    imagebutton auto "images/system/back2_%s.png" action Return() activate_sound "audio/sys/sysse_cancel.wav" hover_sound "audio/sys/sysse_move.wav" yalign 0.02 xalign 0.97

    vbox:
        xpos 1373
        yalign 0.5


        imagebutton auto "gui/tipps/tip01_%s.png" action ShowMenu("tip01") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav"

        if persistent.tip2 == True:
            imagebutton auto "gui/tipps/tip02_%s.png" action ShowMenu("tip02") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav"

        if persistent.tip3 == True:
            imagebutton auto "gui/tipps/tip03_%s.png" action ShowMenu("tip03") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav"

## DIe Tipps sind kompletter bullshit und tragen nichts zur Story bei und werden sich höchstens auf relevantes beschreiben
## To Do: Raus damit!
screen tip01():

    tag menu
    modal True
    use tipps

    add "gui/tipps/tip01_details.png" at center

screen tip02():

    tag menu
    modal True
    use tipps

    add "gui/tipps/tip02_details.png" at center

screen tip03():

    tag menu
    modal True
    use tipps

    add "gui/tipps/tip03_details.png" at center