screen navigationnew():

    fixed:
        style_prefix "navigation"

        #if main_menu:
            #xalign 1.0
            #yalign 0.5
            #xoffset -30
        #else:
            #xoffset 60
            #yalign 0.5

        #spacing gui.navigation_spacing

        if main_menu:

            imagebutton auto "gui/button/start_%s.png" action ShowMenu("story_select") xpos 1292 ypos 200



        else:

            textbutton _("Lo{color=#f00}g{/color}") action ShowMenu("history")

            textbutton _("Speic{color=#f00}h{/color}ern") action ShowMenu("save")


        imagebutton auto "gui/button/load_%s.png" action ShowMenu("load") xpos 1291 ypos 315


        imagebutton auto "gui/button/settings_%s.png" action ShowMenu("preferences") xpos 1292 ypos 435

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Hauptm{color=#f00}e{/color}nü") action MainMenu()

        imagebutton auto "gui/button/credits_%s.png" action ShowMenu("about") xpos 1292 ypos 553

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Help isn't necessary or relevant to mobile devices.
            #textbutton _("Hilfe") action ShowMenu("help")
            imagebutton auto "gui/button/help_%s.png" action ShowMenu("help") xpos 1292 ypos 670

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            imagebutton auto "gui/button/quit_%s.png" action Quit(confirm=not main_menu) xpos 1292 ypos 787

style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")
    outlines [ (absolute(4), "#000000", absolute(0), absolute(0)) ]
    xalign 1.0
