screen save():

    tag menu
    modal True
    use file_slots_save


screen load():

    tag menu
    modal True
    use file_slots_load


screen file_slots_save():

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"))
    add "gui/bgdark.png" at center
    add "gui/saveload/savebg.png" at center
    text _("Save") outlines [ (absolute(4), "#00000094", absolute(1), absolute(1)) ] size 90 font "fonts/Georgia.ttf" xalign 0.5 yalign 0.03 
    imagebutton auto "images/system/back2_%s.png" action [ShowMenu("game_menu"), Hide("save")] activate_sound "audio/sys/sysse_cancel.wav" hover_sound "audio/sys/sysse_move.wav" yalign 0.02 xalign 0.97
    add partObj

    fixed:

        ## This ensures the input will get the enter event before any of the
        ## button do.
        order_reverse True

        button:
            style "page_label"

            key_events True
            xpos 100
            ypos 80

            input:
                style "page_label_text"
                value page_name_value
        ## The grid of file slots.
        grid gui.file_slot_cols gui.file_slot_rows:
            style_prefix "slot"

            xalign 0.5
            yalign 0.68

            spacing gui.slot_spacing

            ## People without coding knowledge are always confused what "i" means
            ## It's a placeholder variable to count stuff up
            ## it can also be called fucking_idiot and it would work correctly
            ## So I am now changing it to fucking_idiot to demonstrate that.

            for fucking_idiot in range(gui.file_slot_cols * gui.file_slot_rows):

                $ slot = fucking_idiot + 1

                button:
                    action FileAction(slot)

                    add FileScreenshot(slot) xalign 0.0

                    text FileTime(slot, format=_("{#file_time}%Y/%b/%d   %H:%M  "), empty=_("unused bookmark")):
                        style "new_slot_time_text"

                    text FileSaveName(slot):
                        style "new_slot_name_text"


                    key "save_delete" action FileDelete(slot)

                    activate_sound "audio/sys/sysse_decide.wav" 
                    
                    hover_sound "audio/sys/sysse_move.wav"

            ## Buttons to access other pages.
        hbox:
            style_prefix "Page"

            yalign 0.15
            xalign 0.5
            spacing 0

            textbutton _("<") action FilePagePrevious() hover_sound "audio/sys/sysse_move.wav" activate_sound "audio/sys/sysse_decide.wav"

            for page in range(1, 13):
                textbutton "[page]" hover_sound "audio/sys/sysse_move.wav" activate_sound "audio/sys/sysse_decide.wav" action FilePage(page)

            textbutton _(">") hover_sound "audio/sys/sysse_move.wav" activate_sound "audio/sys/sysse_decide.wav" action FilePageNext()


screen file_slots_load():

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Autosaves"))
    if main_menu:
        add "gui/saveload/bg.png" at bgani
    add "gui/bgdark.png" at center
    add "gui/saveload/loadbg.png" at center
    text _("Load") outlines [ (absolute(4), "#00000094", absolute(1), absolute(1)) ] size 90 font "fonts/Georgia.ttf" xalign 0.5 yalign 0.03
    if main_menu:
        imagebutton auto "images/system/back2_%s.png" action Return() activate_sound "audio/sys/sysse_cancel.wav" hover_sound "audio/sys/sysse_move.wav" yalign 0.02 xalign 0.97
    else:
        imagebutton auto "images/system/back2_%s.png" action [ShowMenu("game_menu"), Hide("load")] activate_sound "audio/sys/sysse_cancel.wav" hover_sound "audio/sys/sysse_move.wav" yalign 0.02 xalign 0.97
    add partObj

    

    fixed:

        ## This ensures the input will get the enter event before any of the
        ## button do.
        order_reverse True

        button:
            style "page_label"

            key_events True
            xpos 100
            ypos 80

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

                    text FileTime(slot, format=_("{#file_time}%Y/%b/%d   %H:%M "), empty=_("unused bookmark")):
                        style "new_slot_time_text"

                    text FileSaveName(slot):
                        style "new_slot_name_text"

                    key "save_delete" action FileDelete(slot)

                    activate_sound "audio/sys/sysse_decide.wav" 
                    
                    hover_sound "audio/sys/sysse_move.wav"
            ## Buttons to access other pages.
        hbox:
            style_prefix "Page"

            yalign 0.15
            xalign 0.5
            spacing 0
            
            

            textbutton _("<") action FilePagePrevious() hover_sound "audio/sys/sysse_move.wav" activate_sound "audio/sys/sysse_decide.wav"

            if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

            for page in range(1, 13):
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
    outlines [ (absolute(3), "#000000ff", absolute(0), absolute(0)) ]

style page_label_text:
    text_align 0.0
    layout "subtitle"
    hover_color gui.hover_color
    outlines [ (absolute(3), "#000000ff", absolute(0), absolute(0)) ]

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")
    outlines [ (absolute(3), "#000000ff", absolute(0), absolute(0)) ]

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")
    ypos 40
    size 30