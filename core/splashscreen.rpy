
label splashscreen:

scene black with dissolve
pause (1)
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
    $ renpy.movie_cutscene("videos/opening.mov")
    pause (1)
else:
    pause (1)
