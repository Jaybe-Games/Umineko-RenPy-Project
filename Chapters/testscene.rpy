label test:

    scene sea_1c with dissolve
    $ play_music(ride_on)
    $ quick_menu = True
    show mar_a11_defo1 at zero_right
    show but_b22_nayamu1 at zero_left
    but "Warum wird der der nicht spricht dunkler gemacht?"
    but "Das kann nicht richtig sein!"
    mar "Weiß ich auch nicht.. uu..."
    but "Schöne Sauce hier haha."
    $ renpy.movie_cutscene("videos/intro.mov")
    stop music fadeout 3
    pause (3)
    jump test
