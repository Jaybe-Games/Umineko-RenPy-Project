transform end_scroll:
    subpixel True
    yoffset 0
    xalign 0.5
    linear 217 yoffset -17280

transform credits_scroll:
    subpixel True
    yoffset 0
    xalign 0.5
    linear 280 yoffset -17280

label credits:

    $ songname = "Golden Sneers - Lovely Banquet"
    $ _skipping = False
    $ play_music(credits)
    show credits at credits_scroll
    $ renpy.pause(293, hard=True)   
    stop music
    $ renpy.pause(5, hard=True)   
    scene black with kanon_rev
    $ renpy.pause(5, hard=True)   
    $ _skipping = True 
    return

label endroll:

    $ songname = "Bring the Fate"
    $ _skipping = False
    $ play_music(endroll)
    show endroll at end_scroll
    $ renpy.pause(224, hard=True)   
    stop music
    $ renpy.pause(5, hard=True)   
    scene black with kanon_rev
    $ renpy.pause(5, hard=True)   
    $ _skipping = True 
    return

