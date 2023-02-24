label test:

    scene sea_1c with dissolve
    $ play_music(ride_on)
    $ quick_menu = True
    show mar_a11_defo1 at zero_right
    show but_b22_nayamu1 at zero_left
    but "\"Dieser Text ist absichtlich viel zu lang um die oprimalen Textbox Einstellungen zu finden, also ich bin der Autor dieser Geschichte und niemand kann sich mir widersetzen, es ist absolut unmöglich für einen Charakter der Handlung nicht zu folgen.\""
    but "Das kann nicht richtig sein!"
    mar "Weiß ich auch nicht.. uu..."
    but "Schöne Sauce hier haha."
    $ renpy.movie_cutscene("videos/intro.mov")
    stop music fadeout 3
    pause (3)
    jump test
