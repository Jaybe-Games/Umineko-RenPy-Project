init python:
    chapternumber = "ChapterNumber"
    chaptername = "ChapterName"
    songname = "SongName"

image chaptertext = ParameterizedText(xalign=0.0, yalign=1.0, font="fonts/arial.ttf")

label showch1:

    show chaptertext "Sam, 04. Oktober 1986 09:30 Uhr\nBootsfahrt nach Rokkenjima"
    pause 7.0
    hide chaptertext with dissolve
    return
