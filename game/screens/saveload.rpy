screen save():

    tag menu
    modal True
    use file_slots_save


screen load():

    tag menu
    modal True
    use file_slots_load


screen file_slots_save():

    default page_name_value = FilePageNameInputValue(pattern=_("Seite {}"), auto=_("Automatische Spielstände"), quick=_("Schnell Speicherungen"))
    add "gui/saveload/savebg.png" at center
    text _("Speichern") outlines [ (absolute(4), "#00000094", absolute(1), absolute(1)) ] size 90 font "fonts/Georgia.ttf" xalign 0.5 yalign 0.03 
    imagebutton auto "images/system/back2_%s.png" action Return() activate_sound "audio/sys/sysse_cancel.wav" hover_sound "audio/sys/sysse_move.wav" yalign 0.02 xalign 0.97
    add partObj

    fixed:

        ## This ensures the input will get the enter event before any of the
        ## button do.
        order_reverse True

        ## The page name, which can be edited by clicking on a button.
        button:
            style "page_label"

            key_events True
            xalign 0.0
            xpos 100
            ypos 80
            action page_name_value.Toggle()

            input:
                style "page_label_text"
                value page_name_value

        ## The grid of file slots.
        grid gui.file_slot_cols gui.file_slot_rows:
            style_prefix "slot"

            xalign 0.5
            yalign 0.68

            spacing gui.slot_spacing

            for i in range(gui.file_slot_cols * gui.file_slot_rows):

                $ slot = i + 1

                button:
                    action FileAction(slot)

                    add FileScreenshot(slot) xalign 0.0

                    text FileTime(slot, format=_("{#file_time}%Y/%b/%d   %H:%M  "), empty=_("Freies Lesezeichen")):
                        style "new_slot_time_text"

                    text FileSaveName(slot):
                        style "new_slot_name_text"


                    key "save_delete" action FileDelete(slot)

                    activate_sound "audio/sys/sysse_decide.wav" 
                    
                    hover_sound "audio/sys/sysse_move.wav"

            ## Buttons to access other pages.
        vbox:
            style_prefix "Seite"

            xalign 0.0
            yalign 0.5
            spacing 0

            textbutton _("<") action FilePagePrevious()

            if config.has_autosave:
                textbutton _("{#auto_page}A") hover_sound "audio/sys/sysse_move.wav" activate_sound "audio/sys/sysse_decide.wav" action FilePage("auto")

            if config.has_quicksave:
                textbutton _("{#quick_page}Q") hover_sound "audio/sys/sysse_move.wav" activate_sound "audio/sys/sysse_decide.wav" action FilePage("quick")

            ## range(1, 10) gives the numbers from 1 to 9.
            for page in range(1, 6):
                textbutton "[page]" hover_sound "audio/sys/sysse_move.wav" activate_sound "audio/sys/sysse_decide.wav" action FilePage(page)

            textbutton _(">") hover_sound "audio/sys/sysse_move.wav" activate_sound "audio/sys/sysse_decide.wav" action FilePageNext()


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    text_align 0.0
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")
    ypos 40
    size 30
## Styles die ich mal für nen Workaround benutzt habe, den ich aber nicht mehr verwende, da mein Hirn immer schlauer wurde
style new_slot_time_text:
    size 35
    xalign 0.97
    ypos 48
    outlines [ (absolute(3), "#583131ff", absolute(0), absolute(0)) ]
    idle_color "#fff"
    hover_color "#fff"
    font "fonts/Montio-Regular.otf"

style new_slot_name_text:
    size 45
    ypos 130
    xpos 360
    font "fonts/Montio-Regular.otf"
    outlines [ (absolute(3), "#583131ff", absolute(0), absolute(0)) ]
    idle_color "#fff"
    hover_color "#fff"
    line_spacing 10

screen file_slots_load():

    default page_name_value = FilePageNameInputValue(pattern=_("Seite {}"), auto=_("Automatische Spielstände"), quick=_("Schnell Speicherungen"))
    if main_menu:
        add "images/backgrounds/mmbackground.png" at mmclouds
        add "images/backgrounds/mmbg.png"
        add "rainbackscroll"
        add "rainfrontscroll"
    add "gui/saveload/loadbg.png" at center
    text _("Laden") outlines [ (absolute(4), "#00000094", absolute(1), absolute(1)) ] size 90 font "fonts/Georgia.ttf" xalign 0.5 yalign 0.03
    imagebutton auto "images/system/back2_%s.png" action Return() activate_sound "audio/sys/sysse_cancel.wav" hover_sound "audio/sys/sysse_move.wav" yalign 0.02 xalign 0.97
    add partObj

    

    fixed:

        ## This ensures the input will get the enter event before any of the
        ## button do.
        order_reverse True

        ## The page name, which can be edited by clicking on a button.
        button:
            style "page_label"

            key_events True
            xalign 0.0
            xpos 100
            ypos 80
            action page_name_value.Toggle()

            input:
                style "page_label_text"
                value page_name_value

        ## The grid of file slots.
        grid gui.file_slot_cols gui.file_slot_rows:
            style_prefix "slot"

            xalign 0.5
            yalign 0.68

            spacing gui.slot_spacing

            for i in range(gui.file_slot_cols * gui.file_slot_rows):

                $ slot = i + 1

                button:
                    action FileAction(slot)

                    add FileScreenshot(slot) xalign 0.0

                    text FileTime(slot, format=_("{#file_time}%Y/%b/%d   %H:%M "), empty=_("Freies Lesezeichen")):
                        style "new_slot_time_text"

                    text FileSaveName(slot):
                        style "new_slot_name_text"

                    key "save_delete" action FileDelete(slot)

                    activate_sound "audio/sys/sysse_decide.wav" 
                    
                    hover_sound "audio/sys/sysse_move.wav"

            ## Buttons to access other pages.
        vbox:
            style_prefix "Seite"

            yalign 0.5
            xalign 0.0
            spacing 0
            

            textbutton _("<") action FilePagePrevious()

            if config.has_autosave:
                textbutton _("{#auto_page}A") hover_sound "audio/sys/sysse_move.wav" activate_sound "audio/sys/sysse_decide.wav" action FilePage("auto")

            if config.has_quicksave:
                textbutton _("{#quick_page}Q") hover_sound "audio/sys/sysse_move.wav" activate_sound "audio/sys/sysse_decide.wav" action FilePage("quick")

            ## range(1, 10) gives the numbers from 1 to 9.
            for page in range(1, 6):
                textbutton "[page]" hover_sound "audio/sys/sysse_move.wav" activate_sound "audio/sys/sysse_decide.wav" action FilePage(page)

            textbutton _(">") hover_sound "audio/sys/sysse_move.wav" activate_sound "audio/sys/sysse_decide.wav" action FilePageNext()


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    text_align 0.0
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")
    ypos 40
    size 30