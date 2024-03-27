screen preferences():

    tag menu
    modal True
    if main_menu:
        add "images/backgrounds/mmbackground.png" at mmclouds
        add "images/backgrounds/mmbg.png"
        add "rainbackscroll"
        add "rainfrontscroll"
    add "gui/settings/background.png" at center
    text _("Einstellungen") outlines [ (absolute(4), "#00000094", absolute(1), absolute(1)) ] size 90 font "fonts/Georgia.ttf" xalign 0.5 yalign 0.03  
    imagebutton auto "images/system/back2_%s.png" action Return() activate_sound "audio/sys/sysse_cancel.wav" hover_sound "audio/sys/sysse_move.wav" yalign 0.02 xalign 0.97
    add partObj

    hbox:
        xalign 0.5
        yalign 0.155

        imagebutton idle "gui/settings/buttons/message_hover.png" action NullAction() activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav"
        imagebutton auto "gui/settings/buttons/sound_%s.png" action ShowMenu("sound") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav"
        imagebutton auto "gui/settings/buttons/misc_%s.png" action ShowMenu("misc") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav"

    vbox:

        #xalign 0.0
        xalign 0.5
        yalign 0.8
        spacing 30

        hbox:

            style_prefix "check"
            text _("Ungel. Überspringbar") outlines [ (absolute(2), "#00000094", absolute(1), absolute(1)) ] size 40 yoffset 20
            imagebutton auto "gui/settings/buttons/on_%s.png" action Preference("skip", "Toggle") activate_sound "audio/sys/sysse_son.wav" hover_sound "audio/sys/sysse_move.wav"

        hbox:
            #TODO: Buttons auswechseln
            style_prefix "radio"
            text _("Schriftart") outlines [ (absolute(2), "#00000094", absolute(1), absolute(1)) ] size 40 yoffset 20
            imagebutton auto "gui/settings/buttons/a_%s.png" action [SelectedIf(gui.SetPreference("font", "newrodin.otf")), gui.SetPreference("font", "newrodin.otf"), SetVariable("persistent.fontborder", 15), SetVariable("prefix", "\""), SetVariable("suffix", "\""), gui.SetPreference("size", 40)]  activate_sound "audio/sys/sysse_soff.wav" hover_sound "audio/sys/sysse_move.wav"
            imagebutton auto "gui/settings/buttons/b_%s.png" action [SelectedIf(gui.SetPreference("font", "ArnoPro.otf")), gui.SetPreference("font", "ArnoPro.otf"), SetVariable("persistent.fontborder", 5), SetVariable("prefix", "“"), SetVariable("suffix", "”"), gui.SetPreference("size", 50)] activate_sound "audio/sys/sysse_soff.wav" hover_sound "audio/sys/sysse_move.wav"

        hbox:
            #TODO: Buttons auswechseln
            style_prefix "radio"
            text _("Textboxstil") outlines [ (absolute(2), "#00000094", absolute(1), absolute(1)) ] size 40 yoffset 20
            imagebutton auto "gui/settings/buttons/a_%s.png" action [SelectedIf(SetVariable("persistent.textbox", "textboxa")), SetVariable("persistent.textbox", "textboxa"), SetVariable("persistent.namebox", "nameboxa"), SetVariable("persistent.narratorbox", "narratorboxa") ]  activate_sound "audio/sys/sysse_soff.wav" hover_sound "audio/sys/sysse_move.wav"
            imagebutton auto "gui/settings/buttons/b_%s.png" action [SelectedIf(SetVariable("persistent.textbox", "textboxb")), SetVariable("persistent.textbox", "textboxb"), SetVariable("persistent.namebox", "nameboxb"), SetVariable("persistent.narratorbox", "narratorboxb") ] activate_sound "audio/sys/sysse_soff.wav" hover_sound "audio/sys/sysse_move.wav"
            imagebutton auto "gui/settings/buttons/c_%s.png" action [SelectedIf(SetVariable("persistent.textbox", "textboxc")), SetVariable("persistent.textbox", "textboxc"), SetVariable("persistent.namebox", "nameboxc"), SetVariable("persistent.narratorbox", "narratorboxc") ] activate_sound "audio/sys/sysse_soff.wav" hover_sound "audio/sys/sysse_move.wav"
        
    vbox:
        xalign 0.5
        yalign 0.3
        yoffset 50
        style_prefix "slider"
        box_wrap True

        vbox:
                    
            text _("- Textgeschwindigkeit +") outlines [ (absolute(2), "#00000094", absolute(1), absolute(1)) ] size 35

            bar value Preference("text speed")

            text _("{color=#fff}+ Automodusgeschwindigkeit -") outlines [ (absolute(2), "#00000094", absolute(1), absolute(1)) ] size 35

            bar value Preference("auto-forward time")


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 1000

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 675
    spacing 15

style optionname:
    outlines [ (absolute(2), "#00000094", absolute(1), absolute(1)) ]

screen sound():

    tag menu
    modal True
    if main_menu:
        add "images/backgrounds/mmbackground.png" at mmclouds
        add "images/backgrounds/mmbg.png"
        add "rainbackscroll"
        add "rainfrontscroll"
    add "gui/settings/background.png" at center
    text _("Einstellungen") outlines [ (absolute(4), "#00000094", absolute(1), absolute(1)) ] size 90 font "fonts/Georgia.ttf" xalign 0.5 yalign 0.03   
    imagebutton auto "images/system/back2_%s.png" action Return() activate_sound "audio/sys/sysse_cancel.wav" hover_sound "audio/sys/sysse_move.wav" yalign 0.02 xalign 0.97
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

        text _("- Musiklautstärke +") outlines [ (absolute(2), "#00000094", absolute(1), absolute(1)) ] size 35

        vbox:
            bar value Preference("music volume")



        text _("- Soundlautstärke +") outlines [ (absolute(2), "#00000094", absolute(1), absolute(1)) ] size 35

        vbox:
            bar value Preference("sound volume")

        if config.has_voice:
            label _("Sprachlautstärke")

            vbox:
                bar value Preference("voice volume")

screen misc():

    tag menu
    modal True
    if main_menu:
        add "images/backgrounds/mmbackground.png" at mmclouds
        add "images/backgrounds/mmbg.png"
        add "rainbackscroll"
        add "rainfrontscroll"
    add "gui/settings/background.png" at center
    text _("Einstellungen") outlines [ (absolute(4), "#00000094", absolute(1), absolute(1)) ] size 90 font "fonts/Georgia.ttf" xalign 0.5 yalign 0.03  
    imagebutton auto "images/system/back2_%s.png" action Return() activate_sound "audio/sys/sysse_cancel.wav" hover_sound "audio/sys/sysse_move.wav" yalign 0.02 xalign 0.97
    add partObj

    hbox:
        xalign 0.5
        yalign 0.155

        imagebutton auto "gui/settings/buttons/message_%s.png" action ShowMenu("preferences") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav"
        imagebutton auto "gui/settings/buttons/sound_%s.png" action ShowMenu("sound") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav"
        imagebutton idle "gui/settings/buttons/misc_hover.png" action NullAction() activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav"

    vbox:

        #xalign 0.0
        xalign 0.5
        yalign 0.5
        spacing 10
        

        hbox:

            style_prefix "radio"
            text _("Vollbildmodus") outlines [ (absolute(2), "#00000094", absolute(1), absolute(1)) ] size 40 yoffset 20
            imagebutton auto "gui/settings/buttons/off_%s.png" action Preference("display", "window") activate_sound "audio/sys/sysse_son.wav" hover_sound "audio/sys/sysse_move.wav"
            imagebutton auto "gui/settings/buttons/on_%s.png" action Preference("display", "fullscreen") activate_sound "audio/sys/sysse_son.wav" hover_sound "audio/sys/sysse_move.wav"
        hbox:
            style_prefix "radio"
            text _("Grafik-API") outlines [ (absolute(2), "#00000094", absolute(1), absolute(1)) ] size 40 yoffset 20
            imagebutton auto "gui/settings/buttons/gl_%s.png" action [_SetRenderer("gl2"), SelectedIf(SetVariable("persistent.renderer", 0)), SetVariable("persistent.renderer", 0)] activate_sound "audio/sys/sysse_son.wav" hover_sound "audio/sys/sysse_move.wav"
            imagebutton auto "gui/settings/buttons/angle2_%s.png" action [_SetRenderer("angle2"), SelectedIf(SetVariable("persistent.renderer", 1)), SetVariable("persistent.renderer", 1)] activate_sound "audio/sys/sysse_son.wav" hover_sound "audio/sys/sysse_move.wav"
    vbox:

        xalign 0.5
        yalign 0.7

        text ("Made with Ren'Py [renpy.version_only]") outlines [ (absolute(2), "#00000094", absolute(1), absolute(1)) ] size 40 yoffset 20 xalign 0.5
        text ("07th Expansion & Entergram (All Rights reserved)") outlines [ (absolute(2), "#00000094", absolute(1), absolute(1)) ] size 40 yoffset 20 xalign 0.5
        text ("Developed by Jaybe Games") outlines [ (absolute(2), "#00000094", absolute(1), absolute(1)) ] size 40 yoffset 20 xalign 0.5

screen help():
    modal True
    tag menu
    if main_menu:
        add "images/backgrounds/mmbackground.png" at mmclouds
        add "images/backgrounds/mmbg.png"
        add "rainbackscroll"
        add "rainfrontscroll"
    text _("Einstellungen") outlines [ (absolute(4), "#00000094", absolute(1), absolute(1)) ] size 90 font "fonts/Georgia.ttf" xalign 0.5 yalign 0.03    
    add "gui/controls/background.png" at center
    imagebutton auto "images/system/back2_%s.png" action Return() activate_sound "audio/sys/sysse_cancel.wav" hover_sound "audio/sys/sysse_move.wav" yalign 0.02 xalign 0.97
    add partObj

    default device = "keyboard"

    style_prefix "help"

    vbox:
        xalign 0.5
        yalign 0.2

        hbox:
            yalign 0.5
            imagebutton auto "gui/controls/buttons/keyboard_%s.png" action SetScreenVariable("device", "keyboard") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav"

            if GamepadExists():
                imagebutton auto "gui/controls/buttons/gamepad_%s.png" action SetScreenVariable("device", "gamepad") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav"

    if device == "keyboard":
        use keyboard_help
    elif device == "gamepad":
        use gamepad_help


screen keyboard_help():

    add "gui/controls/keyboard.png" yalign 0.7 xalign 0.55

screen gamepad_help():

    add "gui/controls/gamepad.png" yalign 0.7 xalign 0.55


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 375
    right_padding 10

style help_label_text:
    size gui.text_size
    xalign 0.0
    text_align 0.0