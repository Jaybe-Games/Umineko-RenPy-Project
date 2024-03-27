screen history():

    tag menu
    modal True
    add "gui/backlog/background.png" at center
    text _("Nachrichten Browser") outlines [ (absolute(4), "#00000094", absolute(1), absolute(1)) ] size 90 font "fonts/Georgia.ttf" xalign 0.5 yalign 0.03
    imagebutton auto "images/system/back2_%s.png" action Return() activate_sound "audio/sys/sysse_cancel.wav" hover_sound "audio/sys/sysse_move.wav" yalign 0.02 xalign 0.97
    #add partObj
    predict False

    frame:

        style_prefix "history"

        xmargin 100
        ymargin 5
        xpadding 50
        ypadding 190
        yoffset 70

        vpgrid:

            cols 1
            yinitial 1.0

            draggable True
            mousewheel True
            scrollbars "vertical"

            vbox:

                for h in _history_list:

                    window:

                        ## This lays things out properly if history_height is None.
                        has fixed:
                            yfit True

                        if h.who:

                            label h.who:
                                style "history_name"
                                substitute False

                        ## Take the color of the who text from the Character, if
                        ## set.
                                if "color" in h.who_args:
                                    text_color h.who_args["color"]

                        $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                        text what:
                            substitute False

                if not _history_list:
                    label _("Keine Nachrichten vorhanden")

## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art", "note_green", "red_truth", "blue_truth", "dialogue" }



style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label:
    xfill True
    top_margin -100

style history_label_text:
    xalign 0.5
    ## Note: When altering the size of the label, you may need to increase the
    ## ypadding of the Frame, or separate it again into top_padding and bottom_padding

style history_return_button:
    align(1.0,1.0)
    yoffset 100

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width
    outlines [ (absolute(2), "#00000094", absolute(0), absolute(0)) ]

style history_new:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("tex" if gui.history_text_xalign else "tex")

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign
    outlines [ (absolute(2), "#00000094", absolute(0), absolute(0)) ]

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("tex" if gui.history_text_xalign else "tex")
    outlines [ (absolute(2), "#00000094", absolute(0), absolute(0)) ]
    size 40

style history_label:
    xfill True

style history_label_text:
    xalign 0.5