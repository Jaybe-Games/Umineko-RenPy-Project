init python:
    chapter = "-"
    show_chapter = ""


screen showch():

    zorder 999999
    
    text chapter size 40 xalign 0.0 yalign 1.0 font "fonts/AOTFShinGoProMedium.otf" outlines [ (absolute(2.5), "#000", absolute(0), absolute(0)) ] at chapterdissolve

    timer 8 action Hide('showch')

screen charupdate():

    zorder 999

    text _("Characters has been updated!") size 40 xalign 0.95 yalign 0.5 font "fonts/ArnoPro.otf" outlines [ (absolute(2.5), "#000", absolute(0), absolute(0)) ] at updatemessagetransform

    timer 8 action Hide('charupdate')

screen tipupdate():

    zorder 999

    text _("Tips has been updated!") size 40 xalign 0.95 yalign 0.5 font "fonts/ArnoPro.otf" outlines [ (absolute(2.5), "#000", absolute(0), absolute(0)) ] at updatemessagetransform

    timer 8 action Hide('tipupdate')

transform chapterfade1:
    subpixel True
    parallel:
        alpha 0.0
        xalign 0.1
        yalign 0.3
        ease 2 alpha 1.0
        pause 4
        ease 2 alpha 0.0
    parallel:
        xoffset -50
        ease 2 xoffset 0
        pause 4
        ease 2 xoffset 50

screen show_chapter():

    zorder 999

    text show_chapter style "chaptertext" at chapterfade1, dialogue_gradient

    timer 10 action Hide('show_chapter')

screen disclaimer():

    zorder 999
    add "images/system/disclaimer.png"
    text _("""This story is undoubtly nothing more than fantasy.
It could not possibly have any relation to real persons, 
organizations, places or events.""") style "disclaimer" at dialogue_gradient
