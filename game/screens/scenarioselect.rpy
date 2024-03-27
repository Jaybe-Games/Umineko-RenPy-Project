style caption:
    bold False
    outlines [ (absolute(4), "#00000094", absolute(1), absolute(1)) ] 
    size 90 
    font "fonts/Georgia.ttf" 
    xalign 0.5 yalign 0.03

style header:
    color "#ffffff"
    outlines [ (absolute(2), "#000000ff", absolute(1), absolute(1)) ] 
    size 55 
    font "fonts/Montio-Regular.otf" 
    yalign 0.0 
    xalign 0.0 
    xpos 610 
    ypos 254

style headerlocked:
    color "#cc0000"
    outlines [ (absolute(2), "#000000ff", absolute(1), absolute(1)) ] 
    size 55 
    font "fonts/Montio-Regular.otf" 
    yalign 0.0 
    xalign 0.0 
    xpos 610 
    ypos 254

style desc:
    outlines [ (absolute(2), "#000000ff", absolute(1), absolute(1)) ] 
    size 30 
    font "fonts/Georgia.ttf" 
    yalign 0.0 
    xalign 0.0 
    xpos 612 
    ypos 337

screen story_select():

    tag menu
    add "images/backgrounds/mmbackground.png" at mmclouds
    add "images/backgrounds/mmbg.png"
    add "rainbackscroll"
    add "rainfrontscroll"
    add "gui/scenario/background.png" at center
    text _("Szenarios") style "caption"
    add partObj

    imagebutton auto "images/system/back2_%s.png" action ShowMenu("main_menu") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav" yalign 0.01 xalign 0.98

    hbox:

        yalign 0.1
        xpos 10


        imagebutton idle "gui/scenario/buttons/main2_selected_idle.png" action NullAction()

        if persistent.gamecleared == True:

            imagebutton auto "gui/scenario/buttons/bonus2_%s.png" action ShowMenu("story_select_bonus") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav"

        else:

            imagebutton auto "gui/scenario/buttons/bonuslocked_%s.png" action NullAction() activate_sound "audio/sys/sysse_error.wav" hovered Show('locked') unhovered Hide('locked') hover_sound "audio/sys/sysse_move.wav"
    vbox:
        
        xpos 73
        yalign 0.5


        imagebutton auto "gui/scenario/buttons/main_%s.png" action Start("startgame") hovered Show('mainstory') unhovered Hide('mainstory') hover_sound "audio/sys/sysse_move.wav"

        if persistent.mainstorycleared == True:

            imagebutton auto "gui/scenario/buttons/teaparty_%s.png" action Start("teaparty") hovered Show('teaparty') unhovered Hide('teaparty') hover_sound "audio/sys/sysse_move.wav"

        else:

            imagebutton auto "gui/scenario/buttons/tealocked_%s.png" action NullAction() activate_sound "audio/sys/sysse_error.wav" hovered Show('locked') unhovered Hide('locked') hover_sound "audio/sys/sysse_move.wav"


        if persistent.teapartycleared == True:

            imagebutton auto "gui/scenario/buttons/hidden_%s.png" action Start("urateaparty") hovered Show('urateaparty') unhovered Hide('urateaparty') hover_sound "audio/sys/sysse_move.wav"
        else:

            imagebutton auto "gui/scenario/buttons/uralocked_%s.png" action NullAction() activate_sound "audio/sys/sysse_error.wav" hovered Show('locked') unhovered Hide('locked') hover_sound "audio/sys/sysse_move.wav"

screen story_select_bonus():

    tag menu
    add "gui/game_menu.png" at center
    add "gui/scenario/background.png" at center
    text _("Szenarios") style "caption"
    add partObj

    imagebutton auto "gui/scenario/buttons/back2_%s.png" action ShowMenu("main_menu") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav" yalign 0.01 xalign 0.98

    hbox:

        yalign 0.1
        xpos 10


        imagebutton auto "gui/scenario/buttons/main2_%s.png" action ShowMenu("story_select") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav"

        imagebutton idle "gui/scenario/buttons/bonus2_selected_idle.png" action NullAction()

screen mainstory():
    tag hover
    add "gui/scenario/sprite.png" yalign 0.64 xalign 0.86
    add "gui/scenario/sub.png" yalign 0.27 xalign 0.86
    text _("Episode0 Resurrection of the golden witch") style "header"
    text _("""Guten Morgen.
Willkommen auf Rokkenjima. Ich hoffe, du hattest eine angenehme Reise.\n
Die Goldene Hexe begrüßt dich persönlich zu einem neuen Spiel.
Von dir wird nicht erwartet, dass du die Spielregeln kennst.
Aber das absolute Minimum wird von dir verlangt.\n
Also lehn dich zurück und genieße die Erzählung.
Aber ich muss dich warnen, dass es vielleicht nicht so kommt, wie du es erwartest.
Lass uns nun erst einmal ankommen und dem Schrei der Möwen lauschen.\n\n
Der Schwierigkeitsgrad ist viel zu leicht.
Das klingt doch fair, oder?""") style "desc"

screen teaparty():
    tag hover
    add "gui/scenario/sub.png" yalign 0.27 xalign 0.86
    text _("Teeparty") style "header"
    text _("""Die Goldene Hexe lädt dich herzlich zu ihrer Teeparty ein.
Wirst du daran teilnehmen?""") style "desc"

screen urateaparty():
    tag hover
    add "gui/scenario/sub.png" yalign 0.27 xalign 0.86
    text _("????") style "header"
    text _("""Die Teeparty der Dämonen und Hexen.""") style "desc"

screen bonushover():
    tag hover
    add "gui/scenario/sub.png" yalign 0.27 xalign 0.86
    text _("Bonuskapitel") style "header"
    text _("""Nicht genug von Rokkenjima?
Die Goldene Hexe hat noch einige zusätzliche Kapitel für dich vorbereitet.""") style "desc"

screen locked():
    tag hover
    add "gui/scenario/sub.png" yalign 0.27 xalign 0.86
    text _("Warnung!") style "headerlocked"
    text _("""Dieser Inhalt ist gesperrt!\n
Bitte spiele erst verfügbare Inhalte durch, um diesen Inhalt freizuschalten.""") style "desc"