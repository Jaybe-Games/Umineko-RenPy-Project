style charheader:
    color "#ffffff"
    outlines [ (absolute(2), "#000000ff", absolute(1), absolute(1)) ] 
    size 55 
    font "fonts/newrodin.otf" 
    yalign 0.0 
    xalign 0.0 
    xpos 610 
    ypos 254

style chardesc:
    outlines [ (absolute(2), "#000000ff", absolute(1), absolute(1)) ] 
    size 30 
    font "fonts/newrodin.otf" 
    yalign 0.0 
    xalign 0.0 
    xpos 612 
    ypos 337



screen characters():
    tag menu
    modal True
    if main_menu:
        add "images/system/mm_clouds.png" at mmclouds
        add "images/system/mm_bg.png" at mm_bg
        add "rainbackscroll"
        add "rainfrontscroll"
    text _("Charaktere") outlines [ (absolute(4), "#00000094", absolute(1), absolute(1)) ] size 90 font "fonts/Georgia.ttf" xalign 0.5 yalign 0.03 
    add "gui/charbox/background.png" at center
    add partObj
    imagebutton auto "images/system/back2_%s.png" action Return() activate_sound "audio/sys/sysse_cancel.wav" hover_sound "audio/sys/sysse_move.wav" yalign 0.02 xalign 0.97
    hbox:

        xpos 110
        ypos 240

        if persistent.kinzo == True:
            imagebutton auto "gui/charbox/icons/char01_%s.png" action ShowMenu("char01") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav"
        else:
            imagebutton auto "gui/charbox/icons/char00_%s.png" action NullAction() activate_sound "audio/sys/sysse_error.wav" hover_sound "audio/sys/sysse_move.wav"

        if persistent.krauss == True:
            imagebutton auto "gui/charbox/icons/char02_%s.png" action ShowMenu("char02") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav"
        else:
            imagebutton auto "gui/charbox/icons/char00_%s.png" action NullAction() activate_sound "audio/sys/sysse_error.wav" hover_sound "audio/sys/sysse_move.wav"

        if persistent.natsuhi == True:
            imagebutton auto "gui/charbox/icons/char03_%s.png" action ShowMenu("char03") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav"
        else:
            imagebutton auto "gui/charbox/icons/char00_%s.png" action NullAction() activate_sound "audio/sys/sysse_error.wav" hover_sound "audio/sys/sysse_move.wav"

        if persistent.jessica == True:
            imagebutton auto "gui/charbox/icons/char05_%s.png" action ShowMenu("char05") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav"
        else:
            imagebutton auto "gui/charbox/icons/char00_%s.png" action NullAction() activate_sound "audio/sys/sysse_error.wav" hover_sound "audio/sys/sysse_move.wav"

    hbox:

        xpos 110
        ypos 340

        if persistent.nanjo == True:
            imagebutton auto "gui/charbox/icons/char15_%s.png" action ShowMenu("char15") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav"
        else:
            imagebutton auto "gui/charbox/icons/char00_%s.png" action NullAction() activate_sound "audio/sys/sysse_error.wav" hover_sound "audio/sys/sysse_move.wav"

        if persistent.eva == True:
            imagebutton auto "gui/charbox/icons/char06_%s.png" action ShowMenu("char06") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav"
        else:
            imagebutton auto "gui/charbox/icons/char00_%s.png" action NullAction() activate_sound "audio/sys/sysse_error.wav" hover_sound "audio/sys/sysse_move.wav"

        if persistent.hideyoshi == True:    
            imagebutton auto "gui/charbox/icons/char07_%s.png" action ShowMenu("char07") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav"
        else:
            imagebutton auto "gui/charbox/icons/char00_%s.png" action NullAction() activate_sound "audio/sys/sysse_error.wav" hover_sound "audio/sys/sysse_move.wav"

        if persistent.george == True:
            imagebutton auto "gui/charbox/icons/char08_%s.png" action ShowMenu("char08") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav"
        else:
            imagebutton auto "gui/charbox/icons/char00_%s.png" action NullAction() activate_sound "audio/sys/sysse_error.wav" hover_sound "audio/sys/sysse_move.wav"
    hbox:

        xpos 110
        ypos 440

        if persistent.beatrice == True:
            imagebutton auto "gui/charbox/icons/char21_%s.png" action ShowMenu("char21") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav"
        else:
            imagebutton auto "gui/charbox/icons/char00_%s.png" action NullAction() activate_sound "audio/sys/sysse_error.wav" hover_sound "audio/sys/sysse_move.wav"

        if persistent.rudolf == True:
            imagebutton auto "gui/charbox/icons/char09_%s.png" action ShowMenu("char09") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav"
        else:
            imagebutton auto "gui/charbox/icons/char00_%s.png" action NullAction() activate_sound "audio/sys/sysse_error.wav" hover_sound "audio/sys/sysse_move.wav"

        if persistent.kyrie == True:
            imagebutton auto "gui/charbox/icons/char10_%s.png" action ShowMenu("char10") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav"
        else:
            imagebutton auto "gui/charbox/icons/char00_%s.png" action NullAction() activate_sound "audio/sys/sysse_error.wav" hover_sound "audio/sys/sysse_move.wav"

        if persistent.battler == True:
            imagebutton auto "gui/charbox/icons/char11_%s.png" action ShowMenu("char11") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav"
        else:
            imagebutton auto "gui/charbox/icons/char00_%s.png" action NullAction() activate_sound "audio/sys/sysse_error.wav" hover_sound "audio/sys/sysse_move.wav"
    hbox:

        xpos 110
        ypos 540

        if persistent.genji == True:
            imagebutton auto "gui/charbox/icons/char16_%s.png" action ShowMenu("char16") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav"
        else:
            imagebutton auto "gui/charbox/icons/char00_%s.png" action NullAction() activate_sound "audio/sys/sysse_error.wav" hover_sound "audio/sys/sysse_move.wav"

        if persistent.rosa == True:
            imagebutton auto "gui/charbox/icons/char13_%s.png" action ShowMenu("char13") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav"
        else:
            imagebutton auto "gui/charbox/icons/char00_%s.png" action NullAction() activate_sound "audio/sys/sysse_error.wav" hover_sound "audio/sys/sysse_move.wav"

        add "gui/charbox/icons/emptyspace.png"

        if persistent.maria == True:
            imagebutton auto "gui/charbox/icons/char14_%s.png" action ShowMenu("char14") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav"
        else:
            imagebutton auto "gui/charbox/icons/char00_%s.png" action NullAction() activate_sound "audio/sys/sysse_error.wav" hover_sound "audio/sys/sysse_move.wav"

    hbox:

        xpos 110
        ypos 640

        if persistent.shannon == True:
            imagebutton auto "gui/charbox/icons/char19_%s.png" action ShowMenu("char19") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav"
        else:
            imagebutton auto "gui/charbox/icons/char00_%s.png" action NullAction() activate_sound "audio/sys/sysse_error.wav" hover_sound "audio/sys/sysse_move.wav"

        if persistent.kanon == True:
            imagebutton auto "gui/charbox/icons/char20_%s.png" action ShowMenu("char20") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav"
        else:
            imagebutton auto "gui/charbox/icons/char00_%s.png" action NullAction() activate_sound "audio/sys/sysse_error.wav" hover_sound "audio/sys/sysse_move.wav"

        if persistent.gohda == True:
            imagebutton auto "gui/charbox/icons/char18_%s.png" action ShowMenu("char18") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav"
        else:
            imagebutton auto "gui/charbox/icons/char00_%s.png" action NullAction() activate_sound "audio/sys/sysse_error.wav" hover_sound "audio/sys/sysse_move.wav"

        if persistent.kumasawa == True:
            imagebutton auto "gui/charbox/icons/char17_%s.png" action ShowMenu("char17") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav"
        else:
            imagebutton auto "gui/charbox/icons/char00_%s.png" action NullAction() activate_sound "audio/sys/sysse_error.wav" hover_sound "audio/sys/sysse_move.wav"


## Diese ganzen Sachen sind entweder nicht implementiert oder müssen ausgetauscht werden
screen witches():
    imagemap:
        ground "gui/title/hovermenu2.png"


screen hina():

    imagemap:
        ground "gui/title/hovermenu2.png"

screen char01():
    tag menu
    use characters
    add "gui/scenario/sub.png" yalign 0.27 xalign 0.86
    text _("Ushiromiya Kinzo (右代宮 金蔵)") style "charheader"
    viewport:
        draggable True
        mousewheel True
        xpos 612 
        ypos 337
        ysize 550
        xsize 900
        scrollbars "vertical"
        text _("""Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, 
sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, 
sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. 
At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, 
consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, 
sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, 
sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, 
sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. 
At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, 
consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, 
sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet.""") style "chardesc"

screen char05():
    tag menu
    use characters
    add "gui/scenario/sub.png" yalign 0.27 xalign 0.86
    text _("Ushiromiya Jessica (右代宮 朱志香)") style "charheader"
    viewport:
        draggable True
        mousewheel True
        xpos 612 
        ypos 337
        ysize 550
        xsize 900
        scrollbars "vertical"
        text _("""Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, 
sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, 
sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. 
At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, 
consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, 
sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, 
sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, 
sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. 
At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, 
consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, 
sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet.""") style "chardesc"

screen char06():
    tag menu
    use characters
    add "gui/scenario/sub.png" yalign 0.27 xalign 0.86
    text _("Ushiromiya Eva (右代宮 絵羽)") style "charheader"
    viewport:
        draggable True
        mousewheel True
        xpos 612 
        ypos 337
        ysize 550
        xsize 900
        scrollbars "vertical"
        text _("""Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, 
sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, 
sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. 
At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, 
consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, 
sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, 
sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, 
sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. 
At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, 
consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, 
sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet.""") style "chardesc"

screen char07():
    tag menu
    use characters
    add "gui/scenario/sub.png" yalign 0.27 xalign 0.86
    text _("Ushiromiya Hideyoshi (右代宮 秀吉)") style "charheader"
    viewport:
        draggable True
        mousewheel True
        xpos 612 
        ypos 337
        ysize 550
        xsize 900
        scrollbars "vertical"
        text _("""Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, 
sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, 
sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. 
At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, 
consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, 
sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, 
sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, 
sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. 
At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, 
consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, 
sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet.""") style "chardesc"

screen char08():
    tag menu
    use characters
    add "gui/scenario/sub.png" yalign 0.27 xalign 0.86
    text _("Ushiromiya George (右代宮 譲治)") style "charheader"
    viewport:
        draggable True
        mousewheel True
        xpos 612 
        ypos 337
        ysize 550
        xsize 900
        scrollbars "vertical"
        text _("""Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, 
sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, 
sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. 
At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, 
consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, 
sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, 
sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, 
sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. 
At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, 
consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, 
sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet.""") style "chardesc"

screen char09():
    tag menu
    use characters
    add "gui/scenario/sub.png" yalign 0.27 xalign 0.86
    text _("Ushiromiya Rudolf (右代宮 留弗夫)") style "charheader"
    viewport:
        draggable True
        mousewheel True
        xpos 612 
        ypos 337
        ysize 550
        xsize 900
        scrollbars "vertical"
        text _("""Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, 
sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, 
sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. 
At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, 
consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, 
sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, 
sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, 
sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. 
At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, 
consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, 
sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet.""") style "chardesc"

screen char10():
    tag menu
    use characters
    add "gui/scenario/sub.png" yalign 0.27 xalign 0.86
    text _("Ushiromiya Kyrie (右代宮 霧江)") style "charheader"
    viewport:
        draggable True
        mousewheel True
        xpos 612 
        ypos 337
        ysize 550
        xsize 900
        scrollbars "vertical"
        text _("""Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, 
sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, 
sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. 
At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, 
consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, 
sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, 
sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, 
sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. 
At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, 
consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, 
sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet.""") style "chardesc"

screen char11(scroll="viewport"):
    tag menu
    use characters()
    add "sprites/but/a11/defo1/0.png" zoom 0.5 xalign 0.995 ypos 315
    add "gui/scenario/sub.png" yalign 0.27 xalign 0.86
    text _("Ushiromiya Battler (右代宮 戦人)") style "charheader"
    viewport:
        draggable True
        mousewheel True
        xpos 612 
        ypos 337
        ysize 550
        xsize 900
        scrollbars "vertical"
        text _("""Sohn von Asumu und Rudolf.

Er ist ein sehr lebhafter und fröhlicher Mensch, dem seine Freunde und seine Familie alles bedeuten, der aber auch sehr unangenehm werden kann, wenn man ihm diese wegnehmen will. 
Von seinem Vater hat er ein wenig die Womanizer-Gene geerbt, denn er flirtet sehr gerne mit Frauen. 
Vor sechs Jahren ist er allerdings aus dem Familienregister ausgetreten, denn nach dem Tod seiner Mutter Asumu hat sein Vater Rudolf bereits eine neue Frau geheiratet, seine jetzige Stiefmutter Kyrie. 
Es kam zum Streit und er zog zu seinen Großeltern mütterlicherseits.
Im Jahr 1986, also genau sechs Jahre später, sind seine Großeltern leider verstorben und er ist wieder in das Familienregister aufgenommen worden, d.h. er nimmt dieses Jahr wieder an der Familienkonferenz teil. 
Er liebt Kriminalromane und ist sehr intelligent.""") style "chardesc"


screen char13():
    tag menu
    use characters
    add "sprites/ros/a11/ikari1/0.png" zoom 0.5 xalign 0.95 ypos 385
    add "gui/scenario/sub.png" yalign 0.27 xalign 0.86
    text _("Ushiromiya Rosa (右代宮 楼座)") style "charheader"
    viewport:
        draggable True
        mousewheel True
        xpos 612 
        ypos 337
        ysize 550
        xsize 900
        scrollbars "vertical"
        text _("""Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, 
sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, 
sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. 
At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, 
consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, 
sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, 
sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, 
sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. 
At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, 
consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, 
sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet.""") style "chardesc"

screen char14():
    tag menu
    use characters
    add "gui/scenario/sub.png" yalign 0.27 xalign 0.86
    text _("Ushiromiya Maria (右代宮 真里亞)") style "charheader"
    viewport:
        draggable True
        mousewheel True
        xpos 612 
        ypos 337
        ysize 550
        xsize 900
        scrollbars "vertical"
        text _("""Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, 
sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, 
sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. 
At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, 
consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, 
sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, 
sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, 
sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. 
At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, 
consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, 
sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet.""") style "chardesc"

screen char15():
    tag menu
    use characters
    add "gui/scenario/sub.png" yalign 0.27 xalign 0.86
    text _("Nanjo Terumasa (南條 輝正)") style "charheader"
    viewport:
        draggable True
        mousewheel True
        xpos 612 
        ypos 337
        ysize 550
        xsize 900
        scrollbars "vertical"
        text _("""Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, 
sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, 
sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. 
At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, 
consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, 
sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, 
sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, 
sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. 
At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, 
consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, 
sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet.""") style "chardesc"

screen char16():
    tag menu
    use characters
    add "gui/scenario/sub.png" yalign 0.27 xalign 0.86
    text _("Ronoue Genji (呂ノ上 源次)") style "charheader"
    viewport:
        draggable True
        mousewheel True
        xpos 612 
        ypos 337
        ysize 550
        xsize 900
        scrollbars "vertical"
        text _("""Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, 
sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, 
sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. 
At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, 
consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, 
sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, 
sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, 
sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. 
At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, 
consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, 
sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet.""") style "chardesc"

screen char17():
    tag menu
    use characters
    add "gui/scenario/sub.png" yalign 0.27 xalign 0.86
    text _("Chiyo Kumasawa (熊沢 チヨ)") style "charheader"
    viewport:
        draggable True
        mousewheel True
        xpos 612 
        ypos 337
        ysize 550
        xsize 900
        scrollbars "vertical"
        text _("""Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, 
sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, 
sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. 
At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, 
consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, 
sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, 
sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, 
sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. 
At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, 
consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, 
sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet.""") style "chardesc"

screen char18():
    tag menu
    use characters
    add "gui/scenario/sub.png" yalign 0.27 xalign 0.86
    text _("Toshiro Gohda (郷田 俊朗)") style "charheader"
    viewport:
        draggable True
        mousewheel True
        xpos 612 
        ypos 337
        ysize 550
        xsize 900
        scrollbars "vertical"
        text _("""Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, 
sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, 
sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. 
At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, 
consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, 
sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, 
sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, 
sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. 
At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, 
consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, 
sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet.""") style "chardesc"

screen char19():
    tag menu
    use characters
    add "gui/scenario/sub.png" yalign 0.27 xalign 0.86
    text _("Shannon (紗音)") style "charheader"
    viewport:
        draggable True
        mousewheel True
        xpos 612 
        ypos 337
        ysize 550
        xsize 900
        scrollbars "vertical"
        text _("""Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, 
sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, 
sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. 
At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, 
consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, 
sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, 
sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, 
sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. 
At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, 
consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, 
sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet.""") style "chardesc"

screen char21():
    tag menu
    use characters
    add "gui/scenario/sub.png" yalign 0.27 xalign 0.86
    text _("BEATRICE (ベアトリーチェ)") style "charheader"
    viewport:
        draggable True
        mousewheel True
        xpos 612 
        ypos 337
        ysize 550
        xsize 900
        scrollbars "vertical"
        text _("""Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, 
sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, 
sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. 
At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, 
consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, 
sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, 
sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, 
sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. 
At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, 
consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, 
sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
no sea takimata sanctus est Lorem ipsum dolor sit amet.""") style "chardesc"