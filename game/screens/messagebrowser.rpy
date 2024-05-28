screen history():

    tag menu
    modal True
    add "gui/bgdark.png" at center
    add "gui/backlog/background.png" at center
    text _("MessageBrowser") outlines [ (absolute(4), "#00000094", absolute(1), absolute(1)) ] size 90 font "fonts/Georgia.ttf" xalign 0.5 yalign 0.03
    imagebutton auto "images/system/back2_%s.png" action [ShowMenu("game_menu"), Hide("history")] activate_sound "audio/sys/sysse_cancel.wav" hover_sound "audio/sys/sysse_move.wav" yalign 0.02 xalign 0.97
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
                ## I simply love to give these kind of prefixes ridiculous names
                for hurensohn in _history_list:

                    window:

                        ## This lays things out properly if history_height is None.
                        has fixed:
                            yfit True

                        if hurensohn.who:

                            label hurensohn.who:
                                style "history_name"
                                substitute False at dialogue_gradient

                        ## Take the color of the who text from the Character, if
                        ## set.
                                if "color" in hurensohn.who_args:
                                    text_color hurensohn.who_args["color"]

                        $ what = renpy.filter_text_tags(hurensohn.what, allow=gui.history_allow_tags)
                        text what:
                            substitute False at dialogue_gradient

                if not _history_list:
                    label _("Keine Nachrichten vorhanden")

## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art", "red_truth", "blue_truth", "gold_truth"}