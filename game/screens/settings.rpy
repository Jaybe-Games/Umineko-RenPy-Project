screen preferences():

    tag menu
    modal True
    if main_menu:
        add "gui/settings/bg.png" at bgani
    add "gui/bgdark.png" at center  
    add "gui/settings/background.png" at center
    text _("Settings") outlines [ (absolute(4), "#00000094", absolute(1), absolute(1)) ] size 90 font "fonts/Georgia.ttf" xalign 0.5 yalign 0.03
    if main_menu:
        imagebutton auto "images/system/back2_%s.png" action Return() activate_sound "audio/sys/sysse_cancel.wav" hover_sound "audio/sys/sysse_move.wav" yalign 0.02 xalign 0.97
    else:
        imagebutton auto "images/system/back2_%s.png" action [ShowMenu("game_menu"), Hide("preferences")] activate_sound "audio/sys/sysse_cancel.wav" hover_sound "audio/sys/sysse_move.wav" yalign 0.02 xalign 0.97
    add partObj

    hbox:
        xalign 0.5
        yalign 0.155

        imagebutton idle "gui/settings/buttons/message_hover.png" action NullAction() activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav"
        imagebutton auto "gui/settings/buttons/sound_%s.png" action ShowMenu("sound") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav"
        imagebutton auto "gui/settings/buttons/misc_%s.png" action ShowMenu("misc") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav"

    hbox:
        xalign 0.5
        yalign 0.63
        spacing 30
        imagebutton auto "gui/settings/buttons/config_button_%s.png" action Preference("skip", "Toggle") activate_sound "audio/sys/sysse_son.wav" hover_sound "audio/sys/sysse_move.wav"
        imagebutton idle "gui/settings/buttons/none.png"
        imagebutton idle "gui/settings/buttons/none.png"

    hbox:
        xalign 0.35
        yalign 0.635
        spacing 222
        text _("ON") size 70 antialias True outlines [ (absolute(2.5), "#000", absolute(0), absolute(0)) ]

    hbox:
        xalign 0.5
        yalign 0.74
        spacing 30
        imagebutton auto "gui/settings/buttons/config_button_%s.png" action [SelectedIf(SetVariable("persistent.textbox","65")), SetVariable("persistent.textbox","65")]  activate_sound "audio/sys/sysse_soff.wav" hover_sound "audio/sys/sysse_move.wav"
        imagebutton auto "gui/settings/buttons/config_button_%s.png" action [SelectedIf(SetVariable("persistent.textbox","66")), SetVariable("persistent.textbox","66")] activate_sound "audio/sys/sysse_soff.wav" hover_sound "audio/sys/sysse_move.wav"
        imagebutton auto "gui/settings/buttons/config_button_%s.png" action [SelectedIf(SetVariable("persistent.textbox","67")), SetVariable("persistent.textbox","67")] activate_sound "audio/sys/sysse_soff.wav" hover_sound "audio/sys/sysse_move.wav"
    

    hbox:
        xalign 0.5
        yalign 0.745
        spacing 222
        text _("A") size 70 antialias True outlines [ (absolute(2.5), "#000", absolute(0), absolute(0)) ]
        text _("B") size 70 antialias True outlines [ (absolute(2.5), "#000", absolute(0), absolute(0)) ]
        text _("C") size 70 antialias True outlines [ (absolute(2.5), "#000", absolute(0), absolute(0)) ]

    # hbox:
    #     xalign 0.5
    #     yalign 0.85
    #     spacing 30
    #     imagebutton auto "gui/settings/buttons/config_button_%s.png" action Language(None)  activate_sound "audio/sys/sysse_soff.wav" hover_sound "audio/sys/sysse_move.wav"
    #     imagebutton auto "gui/settings/buttons/config_button_%s.png" action Language("German")  activate_sound "audio/sys/sysse_soff.wav" hover_sound "audio/sys/sysse_move.wav"
    #     imagebutton idle "gui/settings/buttons/none.png"

    

    # hbox:
    #     xalign 0.415
    #     yalign 0.855
    #     spacing 180
    #     text _("EN") size 70 antialias True outlines [ (absolute(2.5), "#000", absolute(0), absolute(0)) ]
    #     text _("DE") size 70 antialias True outlines [ (absolute(2.5), "#000", absolute(0), absolute(0)) ]



    vbox:

        xalign 0.15
        yalign 0.69
        spacing 68
        
        text _("Enable Skip") outlines [ (absolute(2), "#00000094", absolute(1), absolute(1)) ] size 40 yoffset 20
        text _("Textbox") outlines [ (absolute(2), "#00000094", absolute(1), absolute(1)) ] size 40 yoffset 20
        #text _("UI & Text") outlines [ (absolute(2), "#00000094", absolute(1), absolute(1)) ] size 40 yoffset 20

    vbox:
        xalign 0.5
        yalign 0.3
        yoffset 50
        style_prefix "slider"
        box_wrap True

        vbox:
                    
            text _("- Textspeed +") outlines [ (absolute(2), "#00000094", absolute(1), absolute(1)) ] size 40

            bar value Preference("text speed")

            text _("{color=#fff}+ Automodespeed -") outlines [ (absolute(2), "#00000094", absolute(1), absolute(1)) ] size 40

            bar value Preference("auto-forward time")
        

screen sound():

    tag menu
    modal True
    if main_menu:
        add "gui/settings/bg.png" at bgani
    add "gui/bgdark.png" at center
    add "gui/settings/background.png" at center
    text _("Settings") outlines [ (absolute(4), "#00000094", absolute(1), absolute(1)) ] size 90 font "fonts/Georgia.ttf" xalign 0.5 yalign 0.03   
    if main_menu:
        imagebutton auto "images/system/back2_%s.png" action Return() activate_sound "audio/sys/sysse_cancel.wav" hover_sound "audio/sys/sysse_move.wav" yalign 0.02 xalign 0.97
    else:
        imagebutton auto "images/system/back2_%s.png" action [ShowMenu("game_menu"), Hide("sound")] activate_sound "audio/sys/sysse_cancel.wav" hover_sound "audio/sys/sysse_move.wav" yalign 0.02 xalign 0.97
    add partObj

    hbox:
        xalign 0.5
        yalign 0.155

        imagebutton auto "gui/settings/buttons/message_%s.png" action ShowMenu("preferences") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav"
        imagebutton idle "gui/settings/buttons/sound_hover.png" action NullAction() activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav"
        imagebutton auto "gui/settings/buttons/misc_%s.png" action ShowMenu("misc") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav"

    vbox:

        style_prefix "slider"
        box_wrap True

        xalign 0.5
        yalign 0.5

        text _("- Musicvolume +") outlines [ (absolute(2), "#00000094", absolute(1), absolute(1)) ] size 40

        vbox:
            bar value Preference("music volume")



        text _("- Soundvolume +") outlines [ (absolute(2), "#00000094", absolute(1), absolute(1)) ] size 40

        vbox:
            bar value Preference("sound volume")

        text _(" - Voicevolume +") outlines [ (absolute(2), "#00000094", absolute(1), absolute(1)) ] size 40

        vbox:
            bar value Preference("voice volume")

    # vbox:

    #     xalign 0.15
    #     yalign 0.77
        
    #     text _("Voices") outlines [ (absolute(2), "#00000094", absolute(1), absolute(1)) ] size 40 yoffset 20

    # hbox:
    #     xalign 0.5
    #     yalign 0.80
    #     spacing 30
    #     imagebutton auto "gui/settings/buttons/config_button_%s.png" action [SelectedIf(SetVariable("persistent.voices","")), SetVariable("persistent.voices",""), SetVariable("persistent.voicedir", "audio/voice/")]  activate_sound "audio/sys/sysse_soff.wav" hover_sound "audio/sys/sysse_move.wav"
    #     imagebutton auto "gui/settings/buttons/config_button_%s.png" action [SelectedIf(SetVariable("persistent.voices","de_")), SetVariable("persistent.voices","de_"), SetVariable("persistent.voicedir", "tl/German/voice/")]  activate_sound "audio/sys/sysse_soff.wav" hover_sound "audio/sys/sysse_move.wav"

    

    # hbox:
    #     xalign 0.5
    #     yalign 0.805
    #     spacing 180
    #     text _("EN") size 70 antialias True outlines [ (absolute(2.5), "#000", absolute(0), absolute(0)) ]
    #     text _("DE") size 70 antialias True outlines [ (absolute(2.5), "#000", absolute(0), absolute(0)) ]


screen misc():

    tag menu
    modal True
    if main_menu:
        add "gui/settings/bg.png" at bgani
    add "gui/bgdark.png" at center
    add "gui/settings/background.png" at center
    text _("Settings") outlines [ (absolute(4), "#00000094", absolute(1), absolute(1)) ] size 90 font "fonts/Georgia.ttf" xalign 0.5 yalign 0.03  
    if main_menu:
        imagebutton auto "images/system/back2_%s.png" action Return() activate_sound "audio/sys/sysse_cancel.wav" hover_sound "audio/sys/sysse_move.wav" yalign 0.02 xalign 0.97
    else:
        imagebutton auto "images/system/back2_%s.png" action [ShowMenu("game_menu"), Hide("misc")] activate_sound "audio/sys/sysse_cancel.wav" hover_sound "audio/sys/sysse_move.wav" yalign 0.02 xalign 0.97
    add partObj

    hbox:
        xalign 0.5
        yalign 0.155

        imagebutton auto "gui/settings/buttons/message_%s.png" action ShowMenu("preferences") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav"
        imagebutton auto "gui/settings/buttons/sound_%s.png" action ShowMenu("sound") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav"
        imagebutton idle "gui/settings/buttons/misc_hover.png" action NullAction() activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav"


    vbox:

        xalign 0.1
        yalign 0.485
        spacing 75
        
        text _("Fullscreen") outlines [ (absolute(2), "#00000094", absolute(1), absolute(1)) ] size 40 yoffset 20
        text _("API") outlines [ (absolute(2), "#00000094", absolute(1), absolute(1)) ] size 40 yoffset 20

    vbox:

        xalign 0.5
        yalign 0.5
        spacing 30
        

        hbox:

            style_prefix "radio"

            imagebutton auto "gui/settings/buttons/off_%s.png" action Preference("display", "window") activate_sound "audio/sys/sysse_son.wav" hover_sound "audio/sys/sysse_move.wav"
            imagebutton auto "gui/settings/buttons/on_%s.png" action Preference("display", "fullscreen") activate_sound "audio/sys/sysse_son.wav" hover_sound "audio/sys/sysse_move.wav"

        hbox:
            style_prefix "radio"

            imagebutton auto "gui/settings/buttons/gl_%s.png" action [_SetRenderer("gl2"), SelectedIf(SetVariable("persistent.renderer", 0)), SetVariable("persistent.renderer", 0)] activate_sound "audio/sys/sysse_son.wav" hover_sound "audio/sys/sysse_move.wav"
            imagebutton auto "gui/settings/buttons/angle2_%s.png" action [_SetRenderer("angle2"), SelectedIf(SetVariable("persistent.renderer", 1)), SetVariable("persistent.renderer", 1)] activate_sound "audio/sys/sysse_son.wav" hover_sound "audio/sys/sysse_move.wav"

    vbox:

        xalign 0.5
        yalign 0.7

        text ("Made with Ren'Py [renpy.version_only]") outlines [ (absolute(2), "#00000094", absolute(1), absolute(1)) ] size 40 yoffset 20 xalign 0.5
        text ("07th Expansion & Entergram (All Rights reserved)") outlines [ (absolute(2), "#00000094", absolute(1), absolute(1)) ] size 40 yoffset 20 xalign 0.5
        text ("Developed by Jaybe Games") outlines [ (absolute(2), "#00000094", absolute(1), absolute(1)) ] size 40 yoffset 20 xalign 0.5

    hbox:
        xalign 0.5
        yalign 0.85
        imagebutton auto "gui/settings/buttons/controls_%s.png" action ShowMenu("help") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav"

screen help():
    modal True
    tag menu
    if main_menu:
        add "gui/settings/bg.png" at bgani
    add "gui/bgdark.png" at center
    text _("Settings") outlines [ (absolute(4), "#00000094", absolute(1), absolute(1)) ] size 90 font "fonts/Georgia.ttf" xalign 0.5 yalign 0.03 
    add "gui/controls/background.png" at center
    if main_menu:
        imagebutton auto "images/system/back2_%s.png" action Return() activate_sound "audio/sys/sysse_cancel.wav" hover_sound "audio/sys/sysse_move.wav" yalign 0.02 xalign 0.97
    else:
        imagebutton auto "images/system/back2_%s.png" action [ShowMenu("game_menu"), Hide("help")] activate_sound "audio/sys/sysse_cancel.wav" hover_sound "audio/sys/sysse_move.wav" yalign 0.02 xalign 0.97
    add partObj

    hbox:
        xalign 0.5
        yalign 0.155

        imagebutton auto "gui/settings/buttons/message_%s.png" action ShowMenu("preferences") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav"
        imagebutton auto "gui/settings/buttons/sound_%s.png" action ShowMenu("sound") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav"
        imagebutton auto "gui/settings/buttons/misc_%s.png" action ShowMenu("misc") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav"

    add "gui/controls/controls.png" at center
    text _("""Toggle Automode

Hide UI

Open Menu

Toggle Skipmode

Continue

Skip chapter""") style "controltext"