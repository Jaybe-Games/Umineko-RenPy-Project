init python:
    songname = "-"
    chapter = "-"


screen showch():

    zorder 999
    
    text chapter size 40 xalign 0.0 yalign 1.0 font "fonts/AOTFShinGoProMedium.otf" outlines [ (absolute(3), "#000", absolute(0), absolute(0)) ] at chapterdissolve

    timer 8 action Hide('showch')

screen showsong():

    zorder 999999

    text "{bgm}♪" + songname size 40 xalign 0.05 yalign 0.01 font "fonts/AOTFShinGoProMedium.otf" outlines [ (absolute(3), "#000", absolute(0), absolute(0)) ] at songflyin

    timer 8 action Hide('showsong')

screen charupdate():

    zorder 999

    text _("Die Charaktere wurden geupdated!") size 40 xalign 0.95 yalign 0.5 font "fonts/ArnoPro.otf" outlines [ (absolute(3), "#000", absolute(0), absolute(0)) ] at updatemessagetransform

    timer 8 action Hide('charupdate')

screen tipupdate():

    zorder 999

    text _("Die Tipps wurden geupdated!") size 40 xalign 0.95 yalign 0.5 font "fonts/ArnoPro.otf" outlines [ (absolute(3), "#000", absolute(0), absolute(0)) ] at updatemessagetransform

    timer 8 action Hide('tipupdate')