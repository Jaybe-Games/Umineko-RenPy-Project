
label splashscreen:

scene black with dissolve
pause (1)
queue sound "audio/sfx/umise_051.ogg" noloop
show splash1 with dissolve
pause (1.5)
hide splash1 with dissolve
pause (1)
show splash2 with dissolve
pause (1.5)
hide splash2 with dissolve
pause (1)
show splash3 with dissolve
pause (1.5)
hide splash3 with dissolve
pause (1)

if persistent.alreadystarted == True:
    $ renpy.movie_cutscene("videos/opening.webm")
    play sound "audio/sfx/umilse_002.ogg" noloop
    $ renpy.movie_cutscene("videos/mmani.webm")
    stop sound fadeout 3
    return
else:
    play sound "audio/sfx/umilse_002.ogg" noloop
    $ renpy.movie_cutscene("videos/mmani.webm")
    stop sound fadeout 3
    return
