﻿################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Styles
################################################################################

style bigtext:
    bold False
    font "fonts/Georgia.ttf"
    size 35

style menutext:
    bold False
    font "fonts/ariston.ttf"
    size 32

style button_story:
    activate_sound "audio/sfx/umise_1005.ogg"
    background Frame("gui/button/FrmBlood.png", left=280, top=20, right=240, bottom=None, tile=False)
    xminimum 1300
    yminimum 140

style button_story_text:
    color "#000"
    align (0.5, 0.5)


style button_back:
    activate_sound "audio/sfx/umise_1001.ogg"
    hover_sound "audio/sfx/click-21156.mp3"
    idle_background "gui/button/BtnBackBlank.png"
    hover_background "gui/button/BtnBackBlankOn.png"
    xpos 40
    ypos 1000

style button_back_text:
    size 45
    xoffset 90
    yoffset 8
    outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]


style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")
    size 30


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)

################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5
    outlines [ (absolute(1), "#000", absolute(2), absolute(1)) ]

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos
    outlines [ (absolute(1), "#000", absolute(2), absolute(1)) ]
    line_spacing 15
    adjust_spacing True

## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        vbox:
            style_prefix "quick"

            xalign 0.0
            yalign 0.0

            imagebutton auto "gui/button/quickbuttonlog_%s.png" action ShowMenu("history") xpos 0 ypos 750 activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"
            imagebutton auto "gui/button/quickbuttonload_%s.png" action ShowMenu("load") xpos 0 ypos 750 activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"
            imagebutton auto "gui/button/quickbuttonsave_%s.png" action ShowMenu("save") xpos 0 ypos 750 activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"
            imagebutton auto "gui/button/quickbuttonautomode_%s.png" action Preference("auto-forward", "toggle") xpos 0 ypos 750 activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"
            imagebutton auto "gui/button/quickbuttonskip_%s.png" action Skip() alternate Skip(fast=True, confirm=True) xpos 0 ypos 750 activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"
            imagebutton auto "gui/button/quickbuttonmenu_%s.png" action ShowMenu('preferences') xpos 0 ypos 750 activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")



################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():

    fixed:
        #style_prefix "navigation"

        #if main_menu:
            #xalign 1.0
            #yalign 0.5
            #xoffset -30
        #else:
            #xoffset 60
            #yalign 0.5

        #spacing gui.navigation_spacing

        if main_menu:

            imagebutton auto "gui/button/start_%s.png" action Play("sound", "/audio/sfx/umise_051.ogg"), ShowMenu("story_select") xpos 1350 ypos 200 hover_sound "audio/sfx/click-21156.mp3"

        else:

            imagebutton auto "gui/button/history_%s.png" action ShowMenu("history") xpos 1350 ypos 80 activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"

            imagebutton auto "gui/button/save_%s.png" action ShowMenu("save") xpos 1350 ypos 200 activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"

        imagebutton auto "gui/button/load_%s.png" action ShowMenu("load") xpos 1350 ypos 315 activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"

        imagebutton auto "gui/button/settings_%s.png" action ShowMenu("preferences") xpos 1350 ypos 435 activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            text "{i}Episode 0 " + chapternumber ypos 875 xpos 10 xalign 0.0 size 70 font "fonts/ariston.ttf" outlines [ (absolute(3), "#000", absolute(0), absolute(0)) ]

            text "{i}" + chaptername ypos 955 xpos 10 xalign 0.0 size 50 font "fonts/ariston.ttf" outlines [ (absolute(3), "#000", absolute(0), absolute(0)) ]

            text "Aktueller Soundtrack: " + songname ypos 1030 xpos 1900 xalign 1.0 size 30 font "fonts/AOTFShinGoProMedium.otf" outlines [ (absolute(3), "#000", absolute(0), absolute(0)) ]

            imagebutton auto "gui/button/mainmenu_%s.png" action MainMenu() xpos 1350 ypos 787 activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"

        imagebutton auto "gui/button/credits_%s.png" action ShowMenu("about") xpos 1350 ypos 553 activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Help isn't necessary or relevant to mobile devices.
            #textbutton _("Hilfe") action ShowMenu("help")
            imagebutton auto "gui/button/help_%s.png" action ShowMenu("help") xpos 1350 ypos 670 activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"

        if main_menu and renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            imagebutton auto "gui/button/quit_%s.png" action Quit(confirm=not main_menu) xpos 1350 ypos 787 activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"

        #if renpy.variant("mobile") and not main_menu:

            #imagebutton auto "gui/button/mainmenu_%s.png" action MainMenu() xpos 1292 ypos 787 activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"

            #imagebutton auto "gui/button/history_%s.png" action ShowMenu("history") xpos 1292 ypos 670 activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"



style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")
    xalign 1.0


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    if persistent.gamecleared == True:

        add gui.main_menu3_background

    elif persistent.teapartycleared == True:

        add gui.main_menu2_background

    else:

        add gui.main_menu_background

    ## This empty frame darkens the main menu.
    frame:
        style "main_menu_frame"

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation

    #if gui.show_name:

        #vbox:
            #style "main_menu_vbox"

            #text "[config.name!t]":
                #style "main_menu_title"

            #text "[config.version]":
                #style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    #background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.game_menu1_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    #imagebutton auto "gui/button/back_%s.png" style "return_button" activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3" xpos 800 action Return()


    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu") activate_sound "audio/sfx/umise_1005.ogg"


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True
    xpos 0

style game_menu_content_frame:
    left_margin -100
    right_margin 630
    top_margin -100
    bottom_margin 150

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 100

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("{color=#fff}Üb{color=#f00}e{color=#fff}r"), scroll="viewport"):

        style_prefix "about"

        vbox:
            xalign 0.0

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only] [renpy.license!t].")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text


style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("{color=#fff}Speic{color=#f00}h{color=#fff}ern"))


screen load():

    tag menu

    use file_slots(_("{color=#fff}Spiel La{color=#f00}d{color=#fff}en"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatische Spielstände"), quick=_("Schnell Speicherungen"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.0
                xpos -300
                ypos 130
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.0
                yalign 0.5
                xpos -300
                ypos 500

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.0

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("Freier Speicherplatz")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0
                ypos 120
                xpos 350

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") hover_sound "audio/sfx/click-21156.mp3" activate_sound "audio/sfx/umise_1005.ogg" action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") hover_sound "audio/sfx/click-21156.mp3" activate_sound "audio/sfx/umise_1005.ogg" action FilePage("quick")

                ## range(1, 10) gives the numbers from 1 to 9.
                for page in range(1, 10):
                    textbutton "[page]" hover_sound "audio/sfx/click-21156.mp3" activate_sound "audio/sfx/umise_1005.ogg" action FilePage(page)

                textbutton _(">") hover_sound "audio/sfx/click-21156.mp3" activate_sound "audio/sfx/umise_1005.ogg" action FilePageNext()


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


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("{color=#fff}Einstell{/color}{color=#f00}u{/color}{color=#fff}ngen{/color}"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("{color=#fff}Anzei{/color}{color=#f00}g{/color}{color=#fff}e{/color}")
                        textbutton _("Fen{color=#f00}s{/color}ter") action Preference("display", "window") activate_sound "audio/sfx/umise_1005.ogg"
                        textbutton _("Voll{color=#f00}b{/color}ild") action Preference("display", "fullscreen") activate_sound "audio/sfx/umise_1005.ogg"

                vbox:
                    style_prefix "check"
                    label _("{color=#fff}Übers{/color}{color=#f00}p{/color}{color=#fff}ringen{/color}")
                    textbutton _("Unge{color=#f00}l{/color}esen") action Preference("skip", "toggle") activate_sound "audio/sfx/umise_1005.ogg"
                    #textbutton _("Nach Auswahl") action Preference("after choices", "toggle")
                    #textbutton _("Über{color=#f00}g{/color}änge") action InvertSelected(Preference("transitions", "toggle")) activate_sound "audio/sfx/umise_1005.ogg"

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:


                    label _("{color=#fff}> Textgeschwindi{color=#f00}g{color=#fff}keit >>") ypos 15

                    bar value Preference("text speed")

                    label _("{color=#fff}>> Auto{color=#f00}m{color=#fff}odusgeschwindigkeit >") ypos 15

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("{color=#fff}> Musiklautstär{color=#f00}k{color=#fff}e >>") ypos 15

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("{color=#fff}> Soundlautstär{color=#f00}k{color=#fff}e >>") ypos 20

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    #if config.has_voice:
                        #label _("Sprachlautstärke")

                        #hbox:
                            #bar value Preference("voice volume")

                            #if config.sample_voice:
                                #textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Alles Stummschal{color=#f00}t{/color}en"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


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
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 675
    spacing 15


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("{color=#fff}Vergangene Dia{color=#f00}l{color=#fff}oge"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

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
            label _("{color=#fff}Es hat noch kein Charakter gesprochen.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("{color=#fff}Hi{color=#f00}l{color=#fff}fe"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Tastatur") action SetScreenVariable("device", "keyboard") activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"
                textbutton _("Maus") action SetScreenVariable("device", "mouse") activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad") activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Fährt den Text fort und bestätigt\nMenü Buttons")

    hbox:
        label _("Leertaste")
        text _("Fährt den Text fort.")

    hbox:
        label _("Pfeiltasten")
        text _("Navigiere durch die Menüs.")

    hbox:
        label _("Escape")
        text _("Öffnet das Menü.")

    hbox:
        label _("Ctrl")
        text _("Überspringt Text beim gedrückthalten.")

    hbox:
        label _("Tab")
        text _("Schaltet auf Textüberspringen um.")

    hbox:
        label _("Bild Hoch")
        text _("Springt zurück zu früherem Dialog.")

    hbox:
        label _("Bild Runter")
        text _("Springt zu späterem Dialog.")

    hbox:
        label "H"
        text _("Versteckt das Interface.")

    hbox:
        label "S"
        text _("Macht einen Screenshot.")

    hbox:
        label "V"
        text _("Schaltet auf Sprachausgabe um aber willst du das echt? {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    hbox:
        label "Shift+A"
        text _("Öffnet Menü für erleichterten Zugang.")


screen mouse_help():

    hbox:
        label _("Linksklick")
        text _("Fährt den Text fort und betätigt\nMenü Buttons.")

    hbox:
        label _("Mausrad klicken")
        text _("Versteckt das Interface.")

    hbox:
        label _("Rechtsklick")
        text _("Öffnet das Menü.")

    hbox:
        label _("Mausrad hochdrehen")
        text _("Springt zurück zu früherem Dialog.")

    hbox:
        label _("Mausrad runterdrehen")
        text _("Springt zu späterem Dialog.")


screen gamepad_help():

    hbox:
        label _("Rechter Trigger RT / A")
        text _("Fährt den Text fort und betätigt\nMenü Buttons.")

    hbox:
        label _("Linker Trigger LT / Linker Bumper LB")
        text _("Springt zurück zu früherem Dialog.")

    hbox:
        label _("Rechter Bumper")
        text _("Springt zu späterem Dialog.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigiere durch die Menüs.")

    hbox:
        label _("Start")
        text _("Öffnet das Menü.")

    hbox:
        label _("Y")
        text _("Versteckt das Interface.")

    textbutton _("Kalibrieren") action GamepadCalibrate() activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"


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



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Ja") action yes_action activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"
                textbutton _("Nein") action no_action activate_sound "audio/sfx/umise_1001.ogg" hover_sound "audio/sfx/click-21156.mp3"

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "{font=fonts/AOTFShinGoProMedium.otf}{size=35}[message!tq]{/size}"

    timer 5.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")

## Story Select Screen ##############

screen story_select():

    tag menu

    add "images/menu/scenario.png" at center

    textbutton "Zum Hauptm{color=#f00}e{color=#fff}nü" style "button_back" action ShowMenu("main_menu")

    vbox:
        xpos 985
        yalign 0.5
        spacing -20

        imagebutton idle "gui/button/mainidle.png" action Start("startde") hover "gui/button/mainhover.png" hovered Show('mainstory') unhovered Hide('mainstory') activate_sound "audio/sfx/umise_017.ogg" hover_sound "audio/sfx/click-21156.mp3"

        hbox:
            if persistent.gamecleared == True:

                xpos 5
                spacing 10

            else:

                xpos 30
                spacing 250


            if persistent.mainstorycleared == False:

                imagebutton idle "gui/button/teapartyidle.png" at grayscale hovered Show('teaparty') unhovered Hide('teaparty') action NullAction() hover_sound "audio/sfx/click-21156.mp3"

            else:

                imagebutton idle "gui/button/teapartyidle.png" hover "gui/button/teapartyhover.png" hovered Show('teaparty') unhovered Hide('teaparty') action Start("teapartyde") hover_sound "audio/sfx/click-21156.mp3" activate_sound "audio/sfx/umise_017.ogg"

            if persistent.gamecleared == True:

                imagebutton idle "gui/button/bonusidle.png" hover "gui/button/bonushover.png" action Start("urateapartyde") hovered Show('bonushover') unhovered Hide('bonushover') hover_sound "audio/sfx/click-21156.mp3" activate_sound "audio/sfx/umise_017.ogg"

            else:

                pass

            if persistent.teapartycleared == False:

                imagebutton idle "gui/button/hiddenidle.png" at grayscale action NullAction() hovered Show('urateaparty') unhovered Hide('urateaparty') hover_sound "audio/sfx/click-21156.mp3"

            else:

                imagebutton idle "gui/button/hiddenidle.png" hover "gui/button/hiddenhover.png" action Start("urateapartyde") hovered Show('urateaparty') unhovered Hide('urateaparty') hover_sound "audio/sfx/click-21156.mp3" activate_sound "audio/sfx/umise_017.ogg"

screen mainstory():
    tag hover
    imagemap:
        ground "gui/hovermenu.png"
    text "Episode 0\nResurrection of the golden witch" style 'bigtext' at Position(xpos = 75, ypos = 330)
    text "Willkommen auf Rokkenjima.\nDie Goldene Hexe heißt dich zu einem neuen Spiel willkommen.\nWie amüsant, dich erwartet die Ehre gegen eine Hexe zu spielen.\n\nDie Hexe von Rokkenjima erwartet nicht, dass du bereits\nmit den Spielregeln vertraut bist, also lasse es ruhig angehen\nund geniesse das Narrativ solange du es noch kannst.\n\nDer Schwierigkeitsgrad ist viel zu einfach.\nDas klingt doch fair oder nicht?" style 'menutext' at Position (xpos = 60, ypos = 420)

screen teaparty():
    tag hover
    imagemap:
        ground "gui/hovermenu.png"
    text "Tee Party" style 'bigtext' at Position(xpos = 75, ypos = 330)

    if persistent.mainstorycleared == False:

        text "Dieser Teil wurde noch nicht geschrieben.\nDieses Kapitel wird erst nach der Hauptstory spielbar sein." style 'menutext' at Position (xpos = 60, ypos = 420)

    else:

        text "Bitte nimm Platz und entspanne dich.\nWar dein Aufenthalt auf Rokkenjima angenehm?\n\nDie Goldene Hexe hat dir eine Einladung\nzu ihrer Teeparty geschenkt.\nIch hoffe, dass du daran teilnehmen wirst." style 'menutext' at Position (xpos = 60, ypos = 420)

screen urateaparty():
    tag hover
    imagemap:
        ground "gui/hovermenu.png"
    text "????" style 'bigtext' at Position(xpos = 75, ypos = 330)

    if persistent.teapartycleared == False:

        text "Dieser Teil wurde noch nicht geschrieben.\nDieses Kapitel wird erst nach der Tee Party spielbar sein." style 'menutext' at Position (xpos = 60, ypos = 420)

    else:

        text "Willkommen zur Tee Party der Nichtmenschen." style 'menutext' at Position (xpos = 60, ypos = 420)

screen bonushover():
    tag hover
    imagemap:
        ground "gui/hovermenu.png"
    text "Bonuskapitel" style 'bigtext' at Position(xpos = 75, ypos = 330)
    text "Noch nicht genug?\n\nNun gut, die Goldene Hexe hat noch ein wenig\nvom Kuchen übrig gelassen.\nNimm dir gerne so viel du willst." style 'menutext' at Position (xpos = 60, ypos = 420)

################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0
            ypos 1050


            textbutton _("Zur{color=#f00}ü{/color}ck") action Rollback() activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"
            textbutton _("Übersp{color=#f00}r{/color}ingen") action Skip() alternate Skip(fast=True, confirm=True) activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"
            textbutton _("Autom{color=#f00}o{/color}dus") action Preference("auto-forward", "toggle") activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"
            textbutton _("Men{color=#f00}ü{/color}") action ShowMenu() activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"


style window:
    variant "small"
    background "gui/phone/textbox.png"



style quick_button_text:
    properties gui.button_text_properties("quick_button")
    size 21


style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin -80
    bottom_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 800
