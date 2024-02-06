init python:
    songname = "SongName"


screen showch():

    if chapter == 0:
        text _("Ich schreibe an dich in einer Quadrillion Jahren") size 40 xalign 0.0 yalign 1.0 font "fonts/AOTFShinGoProMedium.otf" outlines [ (absolute(3), "#000", absolute(0), absolute(0)) ] at chapterdissolve
    if chapter == 1:
        text _("Bootsfahrt nach Rokkenjima") size 40 xalign 0.0 yalign 1.0 font "fonts/AOTFShinGoProMedium.otf" outlines [ (absolute(3), "#000", absolute(0), absolute(0)) ] at chapterdissolve
    if chapter == 2:
        text _("Die Hexe auf dem Balkon") size 40 xalign 0.0 yalign 1.0 font "fonts/AOTFShinGoProMedium.otf" outlines [ (absolute(3), "#000", absolute(0), absolute(0)) ] at chapterdissolve
    
    timer 5.25 action Hide('showch')

screen showsong():

    text "♪"+ songname size 40 xalign 0.05 yalign 0.01 font "fonts/AOTFShinGoProMedium.otf" outlines [ (absolute(3), "#000", absolute(0), absolute(0)) ] at songflyin

    timer 8 action Hide('showsong')

screen charupdate():

    text _("Die Charaktere wurden geupdated!") size 40 xalign 0.95 yalign 0.5 font "fonts/ArnoPro.otf" outlines [ (absolute(3), "#000", absolute(0), absolute(0)) ] at updatemessagetransform

    timer 8 action Hide('charupdate')

screen tipupdate():

    text _("Die Tipps wurden geupdated!") size 40 xalign 0.95 yalign 0.5 font "fonts/ArnoPro.otf" outlines [ (absolute(3), "#000", absolute(0), absolute(0)) ] at updatemessagetransform

    timer 8 action Hide('tipupdate')