default menuchapter = ""

init python:
    def getPlayTime():

        pt = renpy.get_game_runtime()

        pth = int(pt // 3600)

        ptm = int(pt - pth * 3600) // 60

        pts = int(pt - (pth * 3600) - (ptm * 60))

        return "{:02d}:{:02d}:{:02d}".format(pth, ptm, pts)

screen game_menu(scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    add "gui/gamemenu/hanabottom.png" at hanabottomtransform
    add "gui/gamemenu/hanatop.png" at hanatoptransform
    add "gui/bgdark.png" at center
    imagebutton auto "images/system/back2_%s.png" action Return() activate_sound "audio/sys/sysse_cancel.wav" hover_sound "audio/sys/sysse_move.wav" yalign 0.02 xalign 0.97
    add partObj

    fixed:
        ### This is my special way to make imagebuttons translatable by simply having 3 vboxes overlapping in a certain order
        vbox:
            yalign 0.5
            xalign 0.9
            spacing 20
            add "gui/title/buttons/button.png" at gamemenubuttontransform
            add "gui/title/buttons/button.png" at gamemenubuttontransform
            add "gui/title/buttons/button.png" at gamemenubuttontransform
            add "gui/title/buttons/button.png" at gamemenubuttontransform
            if persistent.tipunlocked == True:
                add "gui/title/buttons/button.png" at gamemenubuttontransform
            if persistent.charsunlocked == True:
                add "gui/title/buttons/button.png" at gamemenubuttontransform
            add "gui/title/buttons/button.png" at gamemenubuttontransform

        vbox:
            yalign 0.5
            xalign 0.861
            spacing 45


            text _("Save") size 70 antialias True outlines [ (absolute(2.5), "#000", absolute(0), absolute(0)) ] at gamemenubuttontransform
            text _("Load") size 70 antialias True outlines [ (absolute(2.5), "#000", absolute(0), absolute(0)) ] at gamemenubuttontransform
            text _("Logview") size 70 antialias True outlines [ (absolute(2.5), "#000", absolute(0), absolute(0)) ] at gamemenubuttontransform
            text _("Trophys") size 70 antialias True outlines [ (absolute(2.5), "#000", absolute(0), absolute(0)) ] at gamemenubuttontransform
            if persistent.tipunlocked == True:
                text _("Tips") size 70 antialias True outlines [ (absolute(2.5), "#000", absolute(0), absolute(0)) ] at gamemenubuttontransform
            if persistent.charsunlocked == True:
                text _("Characters") size 70 antialias True outlines [ (absolute(2.5), "#000", absolute(0), absolute(0)) ] at gamemenubuttontransform
            text _("Main Menu") size 70 antialias True outlines [ (absolute(2.5), "#000", absolute(0), absolute(0)) ] at gamemenubuttontransform

        vbox:
            yalign 0.5
            xalign 0.9
            spacing 20
            imagebutton auto "gui/title/buttons/button_highlight_%s.png" action ShowMenu("save") hover_sound "audio/sys/sysse_move.wav" activate_sound "audio/sys/sysse_decide.wav" at gamemenubuttontransform
            imagebutton auto "gui/title/buttons/button_highlight_%s.png" action ShowMenu("load") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav" at gamemenubuttontransform
            imagebutton auto "gui/title/buttons/button_highlight_%s.png" action ShowMenu("history") hover_sound "audio/sys/sysse_move.wav" activate_sound "audio/sys/sysse_decide.wav" at gamemenubuttontransform
            imagebutton auto "gui/title/buttons/button_highlight_%s.png" action ShowMenu("achievement_menu") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav"at gamemenubuttontransform
            if persistent.tipunlocked == True:
                imagebutton auto "gui/title/buttons/button_highlight_%s.png" action ShowMenu("tipps") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav"at gamemenubuttontransform
            if persistent.charsunlocked == True:
                imagebutton auto "gui/title/buttons/button_highlight_%s.png" action ShowMenu("characters") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav"at gamemenubuttontransform
            imagebutton auto "gui/title/buttons/button_highlight_%s.png" action MainMenu() activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav" at gamemenubuttontransform
    
        vbox:
            yalign 0.15
            xalign 0.05
    
            imagebutton auto "gui/title/buttons/settings_%s.png" action ShowMenu("preferences") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav" at gamemenubuttontransform2
        
    if renpy.music.get_playing('music') is not None:

        text "♪" + music_dictionary[renpy.music.get_playing('music')] ypos 1005 xalign 0.99 size 30 font "fonts/AOTFShinGoProMedium.otf" outlines [ (absolute(3), "#000", absolute(0), absolute(0)) ] at gamemenubuttontransform

    else:
        text "♪-" ypos 1005 xalign 0.99 size 30 font "fonts/AOTFShinGoProMedium.otf" outlines [ (absolute(3), "#000", absolute(0), absolute(0)) ] at gamemenubuttontransform

    text _("Playtime: ") + getPlayTime() ypos 1040 xalign 0.99 size 30 font "fonts/AOTFShinGoProMedium.otf" outlines [ (absolute(3), "#000", absolute(0), absolute(0)) ] at gamemenubuttontransform

    text menuchapter yalign 0.99 xalign 0.01 size 80 font "fonts/ariston.ttf" outlines [ (absolute(4), "#000", absolute(0), absolute(0)) ] at gamemenubuttontransform2


## Dieser Screen hatte mal irgend einen Sinn für einen Workaround
## Ich erinnere mich, ohne den scheiß, kann man das Menü nicht öffnen.
screen cleanmenu():

    tag menu
    add particles

    use game_menu()