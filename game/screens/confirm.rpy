screen confirm(message, yes_action, no_action):
    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    if message == layout.ARE_YOU_SURE:
        add "gui/confirmblack.png" at center
        vbox:
            yalign 0.8
            xalign 0.5
            spacing 20

            add "gui/title/buttons/button.png" at buttondissolve4
            add "gui/title/buttons/button.png" at buttondissolve5
        vbox:
            yalign 0.8
            xalign 0.468
            spacing 45


            text _("Confirm") size 70 antialias True outlines [ (absolute(2.5), "#000", absolute(0), absolute(0)) ] at buttondissolve4
            text _("Cancel") size 70 antialias True outlines [ (absolute(2.5), "#000", absolute(0), absolute(0)) ] at buttondissolve5

        vbox:
            yalign 0.8
            xalign 0.5
            spacing 20
            imagebutton auto "gui/title/buttons/button_highlight_%s.png" action yes_action activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav" at buttondissolve4
            imagebutton auto "gui/title/buttons/button_highlight_%s.png" action no_action activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav" at buttondissolve5
        add "images/system/sure.png":
            xalign 0.5
            yalign 0.5
    elif message == layout.DELETE_SAVE:
        add "gui/confirmblack.png" at center
        vbox:
            yalign 0.8
            xalign 0.5
            spacing 20

            add "gui/title/buttons/button.png" at buttondissolve4
            add "gui/title/buttons/button.png" at buttondissolve5
        vbox:
            yalign 0.8
            xalign 0.468
            spacing 45


            text _("Confirm") size 70 antialias True outlines [ (absolute(2.5), "#000", absolute(0), absolute(0)) ] at buttondissolve4
            text _("Cancel") size 70 antialias True outlines [ (absolute(2.5), "#000", absolute(0), absolute(0)) ] at buttondissolve5

        vbox:
            yalign 0.8
            xalign 0.5
            spacing 20
            imagebutton auto "gui/title/buttons/button_highlight_%s.png" action yes_action activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav" at buttondissolve4
            imagebutton auto "gui/title/buttons/button_highlight_%s.png" action no_action activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav" at buttondissolve5
        add "images/system/sure.png":
            xalign 0.5
            yalign 0.5
    elif message == layout.OVERWRITE_SAVE:
        add "gui/confirmblack.png" at center
        vbox:
            yalign 0.8
            xalign 0.5
            spacing 20

            add "gui/title/buttons/button.png" at buttondissolve4
            add "gui/title/buttons/button.png" at buttondissolve5
        vbox:
            yalign 0.8
            xalign 0.468
            spacing 45


            text _("Confirm") size 70 antialias True outlines [ (absolute(2.5), "#000", absolute(0), absolute(0)) ] at buttondissolve4
            text _("Cancel") size 70 antialias True outlines [ (absolute(2.5), "#000", absolute(0), absolute(0)) ] at buttondissolve5

        vbox:
            yalign 0.8
            xalign 0.5
            spacing 20
            imagebutton auto "gui/title/buttons/button_highlight_%s.png" action yes_action activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav" at buttondissolve4
            imagebutton auto "gui/title/buttons/button_highlight_%s.png" action no_action activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav" at buttondissolve5
        add "images/system/save.png":
            xalign 0.5
            yalign 0.5
    elif message == layout.LOADING:
        add "gui/confirmblack.png" at center
        vbox:
            yalign 0.8
            xalign 0.5
            spacing 20

            add "gui/title/buttons/button.png" at buttondissolve4
            add "gui/title/buttons/button.png" at buttondissolve5
        vbox:
            yalign 0.8
            xalign 0.468
            spacing 45


            text _("Confirm") size 70 antialias True outlines [ (absolute(2.5), "#000", absolute(0), absolute(0)) ] at buttondissolve4
            text _("Cancel") size 70 antialias True outlines [ (absolute(2.5), "#000", absolute(0), absolute(0)) ] at buttondissolve5

        vbox:
            yalign 0.8
            xalign 0.5
            spacing 20
            imagebutton auto "gui/title/buttons/button_highlight_%s.png" action yes_action activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav" at buttondissolve4
            imagebutton auto "gui/title/buttons/button_highlight_%s.png" action no_action activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav" at buttondissolve5
        add "images/system/load.png":
            xalign 0.5
            yalign 0.5
    elif message == layout.QUIT:
        add "gui/confirmblack.png" at center
        vbox:
            yalign 0.8
            xalign 0.5
            spacing 20

            add "gui/title/buttons/button.png" at buttondissolve4
            add "gui/title/buttons/button.png" at buttondissolve5
        vbox:
            yalign 0.8
            xalign 0.468
            spacing 45


            text _("Confirm") size 70 antialias True outlines [ (absolute(2.5), "#000", absolute(0), absolute(0)) ] at buttondissolve4
            text _("Cancel") size 70 antialias True outlines [ (absolute(2.5), "#000", absolute(0), absolute(0)) ] at buttondissolve5

        vbox:
            yalign 0.8
            xalign 0.5
            spacing 20
            imagebutton auto "gui/title/buttons/button_highlight_%s.png" action yes_action activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav" at buttondissolve4
            imagebutton auto "gui/title/buttons/button_highlight_%s.png" action no_action activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav" at buttondissolve5
        add "images/system/quit.png":
            xalign 0.5
            yalign 0.5
    elif message == layout.MAIN_MENU:
        add "gui/confirmblack.png" at center
        vbox:
            yalign 0.8
            xalign 0.5
            spacing 20

            add "gui/title/buttons/button.png" at buttondissolve4
            add "gui/title/buttons/button.png" at buttondissolve5
        vbox:
            yalign 0.8
            xalign 0.468
            spacing 45


            text _("Confirm") size 70 antialias True outlines [ (absolute(2.5), "#000", absolute(0), absolute(0)) ] at buttondissolve4
            text _("Cancel") size 70 antialias True outlines [ (absolute(2.5), "#000", absolute(0), absolute(0)) ] at buttondissolve5

        vbox:
            yalign 0.8
            xalign 0.5
            spacing 20
            imagebutton auto "gui/title/buttons/button_highlight_%s.png" action yes_action activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav" at buttondissolve4
            imagebutton auto "gui/title/buttons/button_highlight_%s.png" action no_action activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav" at buttondissolve5

        add "images/system/quit.png":
            xalign 0.5
            yalign 0.5

    ## Right-click and escape answer "no".
    key "game_menu" action no_action