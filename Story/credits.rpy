transform end_scroll:
    subpixel True
    yoffset 0
    xalign 0.5
    linear 222 yoffset -17280

transform gameresult_scroll:
    subpixel True
    yoffset 0
    xalign 0.5
    linear 100 yoffset -21420

transform credits_scroll:
    subpixel True
    yoffset 0
    xalign 0.5
    linear 280 yoffset -17280

label credits:
    $ renpy.pause(3, hard=True)
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

label creditsmenu:
    $ discord.update(state = "In Main Menu")
    $ discord.update(details = "watching Credits")
    $ chaptername = "\"Credits\""
    $ chapternumber = "Main Menu"
    $ songname = "Black Lilliana Orchestra"
    $ _skipping = True
    scene white zorder 80
    with kanon_r
    scene black with dissolve
    show credits at credits_scroll
    $ renpy.pause(293, hard=False)    
    scene black with kanon_rev
    $ renpy.pause(5, hard=False)   
    return

label endroll:
    $ renpy.pause(3, hard=True)
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

label gameresult:

    $ _skipping = False
    show gameresult at gameresult_scroll
    $ renpy.pause(105, hard=True)   
    $ renpy.pause(5, hard=True)   
    scene black with kanon_rev
    stop music fadeout 5.0
    $ renpy.pause(5, hard=True)   
    $ _skipping = True 
    return

