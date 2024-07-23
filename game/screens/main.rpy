transform buttondissolvetitle:
    alpha 0.0
    pause 0.2
    ease 0.5 alpha 1.0

transform buttondissolve1:
    subpixel True
    alpha 0.0
    pause 0.2
    ease 0.5 alpha 1.0

transform buttondissolve2:
    subpixel True
    alpha 0.0
    pause 0.3
    ease 0.5 alpha 1.0

transform buttondissolve3:
    subpixel True
    alpha 0.0
    pause 0.4
    ease 0.5 alpha 1.0
transform buttondissolve4:
    subpixel True
    alpha 0.0
    pause 0.5
    ease 0.5 alpha 1.0

transform buttondissolve5:
    subpixel True
    alpha 0.0
    pause 0.6
    ease 0.5 alpha 1.0

transform buttondissolve6:
    subpixel True
    alpha 0.0
    pause 0.7
    ease 0.5 alpha 1.0

transform buttondissolve7:
    subpixel True
    alpha 0.0
    pause 0.8
    ease 0.5 alpha 1.0

transform buttondissolve8:
    subpixel True
    alpha 0.0
    pause 0.9
    ease 0.5 alpha 1.0

screen main_menu():

    tag menu
    add "gui/title/bg.png" at bgani
    #add "gui/title/title_hana.png" at topright
    add "gui/title/copyright.png" at left
    add "gui/title/titlelogo.png" at topleft,buttondissolvetitle,mm_logo
    text "V[config.version!t]" at topleft size 30 antialias True outlines [ (absolute(3), "#000", absolute(0), absolute(0)) ]
    on "show" action Play("seagulls", "audio/sfx/umilse_002.ogg")
    on "hide" action Stop("seagulls")

    fixed:
        ### This is my special way to make imagebuttons translatable by simply having 3 vboxes overlapping in a certain order
        vbox:
            yalign 0.5
            xalign 0.9
            spacing 20
            add "gui/title/buttons/button.png" at buttondissolve1
            add "gui/title/buttons/button.png" at buttondissolve2
            add "gui/title/buttons/button.png" at buttondissolve3
            add "gui/title/buttons/button.png" at buttondissolve4
            if persistent.tipunlocked == True:
                add "gui/title/buttons/button.png" at buttondissolve5
            if persistent.charsunlocked == True:
                add "gui/title/buttons/button.png" at buttondissolve6
            add "gui/title/buttons/button.png" at buttondissolve7

        vbox:
            yalign 0.5
            xalign 0.850
            spacing 45


            text _("Start") size 70 antialias True outlines [ (absolute(2.5), "#000", absolute(0), absolute(0)) ] at buttondissolve1
            if renpy.seen_label("umi1_1"):

                text _("Continue") size 70 antialias True outlines [ (absolute(2.5), "#000", absolute(0), absolute(0)) ] at buttondissolve2
            text _("Load") size 70 antialias True outlines [ (absolute(2.5), "#000", absolute(0), absolute(0)) ] at buttondissolve3
            text _("Trophys") size 70 antialias True outlines [ (absolute(2.5), "#000", absolute(0), absolute(0)) ] at buttondissolve4
            if persistent.tipunlocked == True:
                text _("Tips") size 70 antialias True outlines [ (absolute(2.5), "#000", absolute(0), absolute(0)) ] at buttondissolve5
            if persistent.charsunlocked == True:
                text _("Characters") size 70 antialias True outlines [ (absolute(2.5), "#000", absolute(0), absolute(0)) ] at buttondissolve6
            text _("Quit") size 70 antialias True outlines [ (absolute(2.5), "#000", absolute(0), absolute(0)) ] at buttondissolve7

        vbox:
            yalign 0.5
            xalign 0.9
            spacing 20
            imagebutton auto "gui/title/buttons/button_highlight_%s.png" action [Play("sound", "/audio/sfx/umise_051.ogg"), ShowMenu("story_select"), Hide('starthover')] hovered Show('starthover') unhovered Hide('starthover') hover_sound "audio/sys/sysse_move.wav" activate_sound "audio/sys/sysse_decide.wav" at buttondissolve1
            imagebutton auto "gui/title/buttons/button_highlight_%s.png" action Continue() hovered Show('continuehover') unhovered Hide('continuehover') hover_sound "audio/sys/sysse_move.wav" activate_sound "audio/sys/sysse_decide.wav" at buttondissolve2
            imagebutton auto "gui/title/buttons/button_highlight_%s.png" action [ShowMenu("load"), Hide('loadhover')] activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav" hovered Show('loadhover') unhovered Hide('loadhover') at buttondissolve3
            imagebutton auto "gui/title/buttons/button_highlight_%s.png" action [ShowMenu("achievement_menu"), Hide('trophyhover')] activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav" hovered Show('trophyhover') unhovered Hide('trophyhover') at buttondissolve4
            if persistent.tipunlocked == True:
                imagebutton auto "gui/title/buttons/button_highlight_%s.png" action [ShowMenu("tipps"), Hide('tiphover')] activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav" hovered Show('tiphover') unhovered Hide('tiphover') at buttondissolve5
            if persistent.charsunlocked == True:
                imagebutton auto "gui/title/buttons/button_highlight_%s.png" action [ShowMenu("characters"), Hide('characterhover')] activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav" hovered Show('characterhover') unhovered Hide('characterhover') at buttondissolve6
            imagebutton auto "gui/title/buttons/button_highlight_%s.png" action [QuitWithScene(), Hide('quithover')] activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav" hovered Show('quithover') unhovered Hide('quithover') at buttondissolve7
        

        vbox:
            yalign 0.5
            xalign 0.9
            spacing 20

            if persistent.new == True:
                add "gui/title/buttons/new.png" at buttondissolve1
                add "gui/title/buttons/button_highlight_idle.png"
                add "gui/title/buttons/button_highlight_idle.png"
                add "gui/title/buttons/button_highlight_idle.png"
                if persistent.tipunlocked == True:
                    add "gui/title/buttons/button_highlight_idle.png"
                if persistent.charsunlocked == True:
                    add "gui/title/buttons/button_highlight_idle.png"
                add "gui/title/buttons/button_highlight_idle.png"

        vbox:
            yalign 0.5
            xalign 0.9
            spacing 20

            if persistent.tsubasacompleted == True:
                add "gui/title/buttons/star.png" at buttondissolve1
                add "gui/title/buttons/button_highlight_idle.png"
                add "gui/title/buttons/button_highlight_idle.png"
                add "gui/title/buttons/button_highlight_idle.png"
                if persistent.tipunlocked == True:
                    add "gui/title/buttons/button_highlight_idle.png"
                if persistent.charsunlocked == True:
                    add "gui/title/buttons/button_highlight_idle.png"
                add "gui/title/buttons/button_highlight_idle.png"

        vbox:
            yalign 0.95
            xalign 0.98
    
            imagebutton auto "gui/title/buttons/settings_%s.png" action [ShowMenu("preferences"), Hide('settingshover')] activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav" hovered Show('settingshover') unhovered Hide('settingshover') at buttondissolve8

screen starthover():
    tag hover
    imagemap:
        ground "gui/title/hover.png"
    text _("Start") style "hoverhead"
    text _("""Welcome to Rokkenjima.
Would you like your stay today to be more pleasant?
The Golden Witch would be happy to help you.
She has made her narrations a little more crisp for you.

Start a new game.""") style "hovertext"

screen loadhover():
    tag hover
    imagemap:
        ground "gui/title/hover.png"
    text _("Load") style "hoverhead"
    text _("""So you're back again?
The Golden Witch is looking forward 
to facing you again.

Load a previous saved game.""") style "hovertext"

screen settingshover():
    tag hover
    imagemap:
        ground "gui/title/hover.png"
    text _("Settings") style "hoverhead"
    text _("""Need some customisation?
Nobody wants your stay not to be to your taste.

Change settings to your liking.""") style "hovertext"

screen quithover():
    tag hover
    imagemap:
        ground "gui/title/hover.png"
    text _("Quit") style "hoverhead"
    text _("""Would you like to leave Rokkenjima?
The Golden Witch awaits your swift return.

Exit the game.""") style "hovertext"

screen trophyhover():
    tag hover
    imagemap:
        ground "gui/title/hover.png"
    text _("Trophies") style "hoverhead"
    text _("""Achievements during your stay on Rokkenjima.
The Golden Witch is impressed by your trophies.

Look at your precious trophies.""") style "hovertext"

screen characterhover():
    tag hover
    imagemap:
        ground "gui/title/hover.png"
    text _("Characters") style "hoverhead"
    text _("""The characters you met on Rokkenjima.
The Golden Witch provides you 
with additional information 
that could be useful during your stay.

Show the characters.""") style "hovertext"

screen tiphover():
    tag hover
    imagemap:
        ground "gui/title/hover.png"
    text _("Tips") style "hoverhead"
    text _("""The tips you acquired on Rokkenjima.
The Golden Witch provides you 
with additional information 
that could be useful during your stay.

Show tips.""") style "hovertext"

screen continuehover():
    tag hover
    imagemap:
        ground "gui/title/hover.png"
    text _("Continue") style "hoverhead"
    text _("""Welcome back!
Would you like to continue enjoying your stay quickly?

Continue reading from the last line you read.""") style "hovertext"

transform blink:
    linear 1.0 alpha 0.2
    linear 1.0 alpha 1.0
    repeat

transform press_start_logo:
    xalign 0.5
    yalign 0.5

transform mm_bg:
    xalign 0.5
    yalign 0.3
    zoom 0.8

transform mm_buttonzoom:
    zoom 1.00

transform mm_fadeout:
    alpha 1.0
    linear 1.0 alpha 0.0

transform mm_logofadeout:
    zoom 1.0
    ease 1.0 zoom 0.5

transform mm_logo:
    zoom 0.8
    xalign 0.1
    yalign 0.1
    yoffset -50

transform mm_settings:
    yoffset -50
    xoffset -50