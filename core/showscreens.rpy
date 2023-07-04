init python:
    songname = "SongName"


screen showch():

    if chapter == 0:
        text _("Ich schreibe an dich in einer Quadrillion Jahren") size 40 xalign 0.0 yalign 1.0 font "fonts/AOTFShinGoProMedium.otf" outlines [ (absolute(3), "#000", absolute(0), absolute(0)) ] at chapterdissolve
    if chapter == 1:
        text _("Bootsfahrt nach Rokkenjima") size 40 xalign 0.0 yalign 1.0 font "fonts/AOTFShinGoProMedium.otf" outlines [ (absolute(3), "#000", absolute(0), absolute(0)) ] at chapterdissolve

screen showsong():

    text "♪"+ songname size 40 xalign 0.05 yalign 0.01 font "fonts/AOTFShinGoProMedium.otf" outlines [ (absolute(3), "#000", absolute(0), absolute(0)) ] at songflyin

screen charupdate():

    text _("Die Charaktere wurden geupdated!") size 40 xalign 0.95 yalign 0.5 font "fonts/ArnoPro.otf" outlines [ (absolute(3), "#000", absolute(0), absolute(0)) ] at updatemessagetransform

screen tipupdate():

    text _("Die Tipps wurden geupdated!") size 40 xalign 0.95 yalign 0.5 font "fonts/ArnoPro.otf" outlines [ (absolute(3), "#000", absolute(0), absolute(0)) ] at updatemessagetransform

label showch0:

    show chaptertext _("Ich schreibe an dich in einer Quadrillion Jahren") at chapterdissolve
    pause 4
    return

label showch1:

    show chaptertext _("Bootsfahrt nach Rokkenjima") at chapterdissolve
    pause 4
    return

label showch2:

    show chaptertext _("Die Hexe auf dem Balkon") at chapterdissolve
    
    return

label showch3:

    show chaptertext _("Der Überlebende") at chapterdissolve
    pause 4
    return

label showch4:

    show chaptertext _("Das Rätsel um die Inschrift der Hexe") at chapterdissolve
    pause 4
    return

label showch5:

    show chaptertext _("Treffen im Rosengarten") at chapterdissolve
    pause 4
    return

label showch6:

    show chaptertext _("Die Familienkonferenz") at chapterdissolve
    pause 4
    return

label showch7:

    show chaptertext _("Brief und Schlüssel") at chapterdissolve
    pause 4
    return

label showch8:

    show chaptertext _("Auf ewig Vereint und für immer getrennt") at chapterdissolve
    pause 4
    return

label showch9:

    show chaptertext _("Vertrauen und Misstrauen") at chapterdissolve
    pause 4
    return

label showch10:

    show chaptertext _("Aufteilung") at chapterdissolve
    pause 4
    return

label showch11:

    show chaptertext _("Narrenmatt") at chapterdissolve
    pause 4
    return

label showch12:

    show chaptertext _("Vorhang auf für das Göttliche Gericht") at chapterdissolve
    pause 4
    return

label showch13:

    show chaptertext _("Der Sieger des Spiels ist...") at chapterdissolve
    pause 4
    return

label showtea01:

    show chaptertext _("Eins zu einer Quadrillion") at chapterdissolve
    pause 4
    return

label showtea02:

    show chaptertext _("Ayato & Yuria") at chapterdissolve
    pause 4
    return

label showtea03:

    show chaptertext _("Auferstehung der Goldenen Hexe") at chapterdissolve
    pause 4
    return

label showtea04:

    show chaptertext _("Die Rokkenjima Massenmorde") at chapterdissolve
    pause 4
    return

label showtea05:

    show chaptertext _("ZERO") at chapterdissolve
    pause 4
    return

label showura01:

    show chaptertext _("Die Illusionen der Falschen Hexe") at chapterdissolve
    pause 4
    return

label showura02:

    show chaptertext _("Bis zum Zentrum des Universums") at chapterdissolve
    pause 4
    return


label showura03:

    show chaptertext _("Geschrieben von dir, von vor einer Quadrillion Jahren") at chapterdissolve
    pause 4
    return