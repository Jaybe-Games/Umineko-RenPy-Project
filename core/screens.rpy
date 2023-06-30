################################################################################
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

style charnametext:
    bold False
    font "fonts/Georgia.ttf"
    size 32

style menutext:
    bold False
    font "fonts/ariston.ttf"
    size 32

style chartext:
    bold False
    font "fonts/ArnoPro.otf"
    size 25


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
    unscrollable "hide"
    ## Prevents Ren'Py from showing a scrollbar when there's nothing to scroll

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"



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

screen say(who, what, slow_effect = slow_typewriter, slow_effect_delay = 0, always_effect = None):
    style_prefix "say"

    window:
        id "window"

        if who is not None:
                    window:
                        id "namebox"
                        style "namebox"
                        text who id "who"

        
        fancytext what id "what" slow_effect slow_effect slow_effect_delay slow_effect_delay always_effect always_effect


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
    outlines [ (absolute(2), "#00000094", absolute(0), absolute(0)) ]
    kerning 1.5
    antialias True

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos
    outlines [ (absolute(2), "#00000094", absolute(0), absolute(0)) ]
    line_spacing 5
    kerning 1.3
    antialias True
    layout "greedy"
    line_overlap_split -8
    newline_indent True


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
    #zorder 100

    if quick_menu:

        vbox:
            style_prefix "quick"

            xalign 0.0
            yalign 0.0

            #imagebutton auto "gui/button/quickbuttonautomode_%s.png" action Preference("auto-forward", "toggle") xpos 1850 ypos 25
            #imagebutton auto "gui/button/quickbuttonskip_%s.png" action Skip() alternate Skip(fast=True, confirm=True) xpos 1825 ypos 25


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

screen navigationfake():

    add "gui/title/bg.png" at bgani
    add "gui/title/menu.png" at center
    add "gui/title/titlelogo.png" at topright
    add partObj
    text "v1.0.0A" at topleft size 30 antialias True outlines [ (absolute(3), "#000", absolute(0), absolute(0)) ]

    fixed:

        if main_menu:

            imagebutton auto "gui/button/secret_%s.png" action Start("supersecret") xpos 210 ypos 1032
            imagebutton auto "gui/button/secret_%s.png" action Start("supersecret") xpos 338 ypos 1032

        else:

            pass

        if main_menu:

            vpgrid:

                cols 2
                xpos 1280
                ypos 680
                yalign 0.5
                spacing 10 

                imagebutton auto "gui/button/start_%s.png" action [Play("sound", "/audio/sfx/umise_051.ogg"), ShowMenu("story_select"), Hide('starthover')] hover_sound "audio/sfx/click-21156.mp3" hovered Show('starthover') unhovered Hide('starthover')

                imagebutton auto "gui/button/load_%s.png" action [ShowMenu("load"), Hide('loadhover')] activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3" hovered Show('loadhover') unhovered Hide('loadhover')

                $ lastsave=renpy.newest_slot(r"\d+")
        
                if lastsave is not None:
                    $ name, page = lastsave.split("-")
                    imagebutton auto "gui/button/continue_%s.png" action FileLoad(name, page) hovered Show('continuehover') unhovered Hide('continuehover') hover_sound "audio/sfx/click-21156.mp3"

                imagebutton auto "gui/button/settings_%s.png" action [ShowMenu("preferences"), Hide('settingshover')] activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3" hovered Show('settingshover') unhovered Hide('settingshover')

                #imagebutton auto "gui/button/credits_%s.png" action [ShowMenu("about"), Hide('creditshover')] activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3" hovered Show('creditshover') unhovered Hide('creditshover')

                imagebutton auto "gui/button/achieve_%s.png" action [ShowMenu("achievement_menu"), Hide('trophyhover')] activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3" hovered Show('trophyhover') unhovered Hide('trophyhover')

                if persistent.battler == True:
                    imagebutton auto "gui/button/chars_%s.png" action [ShowMenu("characters"), Hide('characterhover')] activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3" hovered Show('characterhover') unhovered Hide('characterhover')
                else:
                    pass

                if persistent.tipunlocked == True:
                    imagebutton auto "gui/button/tip_%s.png" action [ShowMenu("tipps"), Hide('tiphover')] activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3" hovered Show('tiphover') unhovered Hide('tiphover')
                else:
                    pass

                if persistent.musicbox == True:
                    imagebutton auto "gui/button/jukebox_%s.png" action [ShowMenu("music_room"), Hide('jukeboxhover'), Function(ost.get_music_channel_info), Stop('music', fadeout=1.0), Stop('sound', fadeout=1.0), Stop('ship', fadeout=1.0), Stop('wind', fadeout=1.0), Function(ost.refresh_list)] hovered Show('jukeboxhover') unhovered Hide('jukeboxhover') activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"
                else:
                    pass

                imagebutton auto "gui/button/help_%s.png" action [ShowMenu("help"), Hide('helphover')] activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3" hovered Show('helphover') unhovered Hide('helphover')

                imagebutton auto "gui/button/quit_%s.png" action [QuitWithScene(), Hide('quithover')] activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3" hovered Show('quithover') unhovered Hide('quithover')

        else:

            pass

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

screen navigation():

    add "gui/title/bg.png" at bgani
    add "gui/title/menu.png" at center
    add "gui/title/titlelogo.png" at topright
    add partObj
    text "v1.0.0A" at topleft size 30 antialias True outlines [ (absolute(3), "#000", absolute(0), absolute(0)) ]

    fixed:

        if main_menu:

            imagebutton auto "gui/button/secret_%s.png" action Start("supersecret") xpos 210 ypos 1032
            imagebutton auto "gui/button/secret_%s.png" action Start("supersecret") xpos 338 ypos 1032

        else:

            pass

        if main_menu:

            vpgrid:

                cols 2
                xpos 1280
                ypos 680
                yalign 0.5
                spacing 10 

                imagebutton auto "gui/button/start_%s.png" action [Play("sound", "/audio/sfx/umise_051.ogg"), ShowMenu("story_select"), Hide('starthover'), SetVariable("ismain", True)] hover_sound "audio/sfx/click-21156.mp3" hovered Show('starthover') unhovered Hide('starthover')

                imagebutton auto "gui/button/load_%s.png" action [ShowMenu("load"), Hide('loadhover')] activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3" hovered Show('loadhover') unhovered Hide('loadhover')

                $ lastsave=renpy.newest_slot(r"\d+")
        
                if lastsave is not None:
                    $ name, page = lastsave.split("-")
                    imagebutton auto "gui/button/continue_%s.png" action FileLoad(name, page) hovered Show('continuehover') unhovered Hide('continuehover') hover_sound "audio/sfx/click-21156.mp3"

                imagebutton auto "gui/button/settings_%s.png" action [ShowMenu("preferences"), Hide('settingshover')] activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3" hovered Show('settingshover') unhovered Hide('settingshover')

                #imagebutton auto "gui/button/credits_%s.png" action [ShowMenu("about"), Hide('creditshover')] activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3" hovered Show('creditshover') unhovered Hide('creditshover')

                imagebutton auto "gui/button/achieve_%s.png" action [ShowMenu("achievement_menu"), Hide('trophyhover')] activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3" hovered Show('trophyhover') unhovered Hide('trophyhover')

                if persistent.battler == True:
                    imagebutton auto "gui/button/chars_%s.png" action [ShowMenu("characters"), Hide('characterhover')] activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3" hovered Show('characterhover') unhovered Hide('characterhover')
                else:
                    pass

                if persistent.tipunlocked == True:
                    imagebutton auto "gui/button/tip_%s.png" action [ShowMenu("tipps"), Hide('tiphover')] activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3" hovered Show('tiphover') unhovered Hide('tiphover')
                else:
                    pass

                if persistent.musicbox == True:
                    imagebutton auto "gui/button/jukebox_%s.png" action [ShowMenu("music_room"), Hide('jukeboxhover'), Function(ost.get_music_channel_info), Stop('music', fadeout=1.0), Stop('sound', fadeout=1.0), Stop('ship', fadeout=1.0), Stop('wind', fadeout=1.0), Function(ost.refresh_list)] hovered Show('jukeboxhover') unhovered Hide('jukeboxhover') activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"
                else:
                    pass

                imagebutton auto "gui/button/help_%s.png" action [ShowMenu("help"), Hide('helphover')] activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3" hovered Show('helphover') unhovered Hide('helphover')

                imagebutton auto "gui/button/quit_%s.png" action [QuitWithScene(), Hide('quithover')] activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3" hovered Show('quithover') unhovered Hide('quithover')

        else:

            pass

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)




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

    #if persistent.gamecleared == True:

        #add gui.main_menu3_background

    #elif persistent.teapartycleared == True:

        #add gui.main_menu2_background

    #else:

        #add gui.main_menu_background

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

## anywhere

init python:
    def getPlayTime():

        pt = renpy.get_game_runtime()

        pth = int(pt // 3600)

        ptm = int(pt - pth * 3600) // 60

        pts = int(pt - (pth * 3600) - (ptm * 60))

        return "{:02d}:{:02d}:{:02d}".format(pth, ptm, pts)

screen game_menu(scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    add "images/system/hana3.png"
    imagebutton auto "gui/button/back2_%s.png" action Return() activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3" yalign 0.02 xalign 0.97
    add partObj


    

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
                        xoffset -250

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

    if not main_menu:

        if persistent.showch == True:

            if chapter == 0:

                add "gui/chapter/ch0.png"

            elif chapter == 1: 

                add "gui/chapter/ch1.png"

            elif chapter == 404: 

                add "gui/chapter/ch404.png"
        
            else:

                pass

        vpgrid:

            cols 2
            xpos 1280
            yalign 0.5
            spacing 10

            imagebutton auto "gui/button/save_%s.png" action ShowMenu("save") activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"

            imagebutton auto "gui/button/load_%s.png" action ShowMenu("load") activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"

            imagebutton auto "gui/button/history_%s.png" action ShowMenu("history") activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"

            imagebutton auto "gui/button/settings_%s.png" action [ShowMenu("preferences")] activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"

            #imagebutton auto "gui/button/credits_%s.png" action ShowMenu("about") activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"

            imagebutton auto "gui/button/help_%s.png" action [ShowMenu("help")] activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"

            imagebutton auto "gui/button/achieve_%s.png" action [ShowMenu("achievement_menu"), Hide('trophyhover')] activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"

            if persistent.battler == True:
                imagebutton auto "gui/button/chars_%s.png" action [ShowMenu("characters"), Hide('characterhover')] activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"
            else:
                pass

            if persistent.tipunlocked == True:
                imagebutton auto "gui/button/tip_%s.png" action [ShowMenu("tipps"), Hide('tiphover')] activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"
            else:
                pass

            if persistent.musicbox == True:
                imagebutton auto "gui/button/jukebox_%s.png" action [ShowMenu("music_room"), Hide('jukeboxhover'), Function(ost.get_music_channel_info), Stop('music', fadeout=1.0), Stop('sound', fadeout=1.0), Stop('ship', fadeout=1.0), Stop('wind', fadeout=1.0), Function(ost.refresh_list)] activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"
            else:
                pass

            imagebutton auto "gui/button/mainmenu_%s.png" action MainMenu() activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"

            #imagebutton auto "gui/button/back_%s.png" activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3" action Return()
        if persistent.showbgm == True:
            text "Soundtrack: " + songname ypos 1005 xpos 1900 xalign 1.0 size 30 font "fonts/AOTFShinGoProMedium.otf" outlines [ (absolute(3), "#000", absolute(0), absolute(0)) ]
        if persistent.showplaytime == True:
            text "Spielzeit: " + getPlayTime() + "" ypos 1040 xpos 1900 xalign 1.0 size 30 font "fonts/AOTFShinGoProMedium.otf" outlines [ (absolute(3), "#000", absolute(0), absolute(0)) ]

    else:

        vpgrid:

                cols 2
                xpos 1280
                ypos 680
                yalign 0.5
                spacing 10 

                imagebutton auto "gui/button/start_%s.png" action [Play("sound", "/audio/sfx/umise_051.ogg"), ShowMenu("story_select"), Hide('starthover')] hover_sound "audio/sfx/click-21156.mp3"

                imagebutton auto "gui/button/load_%s.png" action [ShowMenu("load"), Hide('loadhover')] activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"

                $ lastsave=renpy.newest_slot(r"\d+")
        
                if lastsave is not None:
                    $ name, page = lastsave.split("-")
                    imagebutton auto "gui/button/continue_%s.png" action FileLoad(name, page), Hide('continuehover') hover_sound "audio/sfx/click-21156.mp3"

                imagebutton auto "gui/button/settings_%s.png" action [ShowMenu("preferences"), Hide('settingshover')] activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"

                #imagebutton auto "gui/button/credits_%s.png" action [ShowMenu("about"), Hide('creditshover')] activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"

                imagebutton auto "gui/button/achieve_%s.png" action [ShowMenu("achievement_menu"), Hide('trophyhover')] activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"

                if persistent.battler == True:
                    imagebutton auto "gui/button/chars_%s.png" action [ShowMenu("characters"), Hide('characterhover')] activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"
                else:
                    pass

                if persistent.tipunlocked == True:
                    imagebutton auto "gui/button/tip_%s.png" action [ShowMenu("tipps"), Hide('tiphover')] activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"
                else:
                    pass

                if persistent.musicbox == True:
                    imagebutton auto "gui/button/jukebox_%s.png" action [ShowMenu("music_room"), Hide('jukeboxhover'), Function(ost.get_music_channel_info), Stop('music', fadeout=1.0), Stop('sound', fadeout=1.0), Stop('ship', fadeout=1.0), Stop('wind', fadeout=1.0), Stop('rain', fadeout=1.0), Function(ost.refresh_list)] activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"
                else:
                    pass

                imagebutton auto "gui/button/help_%s.png" action [ShowMenu("help"), Hide('helphover')] activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"

                imagebutton auto "gui/button/quit_%s.png" action [QuitWithScene(), Hide('quithover')] activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"

    if main_menu:
        key "game_menu" action ShowMenu("main_menu") activate_sound "audio/sfx/umise_1005.ogg"

screen cleanmenu():

    tag menu
    add partObj

    use game_menu()



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

    #background "gui/game_menu1.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True
    xpos 0

style game_menu_content_frame:
    left_margin -400
    right_margin 700
    top_margin -70
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
    use game_menu(_("{color=#fff}Cre{color=#f00}d{color=#fff}its"), scroll="viewport"):

        style_prefix "about"

        vbox:
            xalign 0.5
            xoffset 270

            label "\n      Umineko When They {red_truth}C{/red_truth}ry Zero\n~Waltz of Reflections and Delusions~"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only] [renpy.license!t].")
            
            if main_menu:
                imagebutton auto "gui/button/creditswatch_%s.png" action Start("creditsmenu") activate_sound "audio/sfx/umise_017.ogg" hover_sound "audio/sfx/click-21156.mp3"


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
    modal True
    use file_slots_save


screen load():

    tag menu
    modal True
    use file_slots_load


screen file_slots_save():

    default page_name_value = FilePageNameInputValue(pattern=_("Seite {}"), auto=_("Automatische Spielstände"), quick=_("Schnell Speicherungen"))
    add "gui/game_menu.png" at center
    add "gui/saveload/savebg.png" at center
    imagebutton auto "gui/button/back2_%s.png" action Return() activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3" yalign 0.02 xalign 0.97
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
            yalign 0.8

            spacing gui.slot_spacing

            for i in range(gui.file_slot_cols * gui.file_slot_rows):

                $ slot = i + 1

                button:
                    action FileAction(slot)

                    has vbox

                    add FileScreenshot(slot) xalign 0.0
            
                    text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M "), empty=_("")):
                        style "slot_time_text"

                    text FileSaveName(slot):
                        style "slot_name_text"

                    key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
        vbox:
            style_prefix "Seite"

            xalign 0.0
            yalign 0.5
            spacing 0

            textbutton _("<") action FilePagePrevious()

            if config.has_autosave:
                textbutton _("{#auto_page}A") hover_sound "audio/sfx/click-21156.mp3" activate_sound "audio/sfx/umise_1005.ogg" action FilePage("auto")

            if config.has_quicksave:
                textbutton _("{#quick_page}Q") hover_sound "audio/sfx/click-21156.mp3" activate_sound "audio/sfx/umise_1005.ogg" action FilePage("quick")

            ## range(1, 10) gives the numbers from 1 to 9.
            for page in range(1, 6):
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

screen file_slots_load():

    default page_name_value = FilePageNameInputValue(pattern=_("Seite {}"), auto=_("Automatische Spielstände"), quick=_("Schnell Speicherungen"))
    add "gui/game_menu.png" at center
    add "gui/saveload/loadbg.png" at center
    imagebutton auto "gui/button/back2_%s.png" action Return() activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3" yalign 0.02 xalign 0.97
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
            yalign 0.8

            spacing gui.slot_spacing

            for i in range(gui.file_slot_cols * gui.file_slot_rows):

                $ slot = i + 1

                button:
                    action FileAction(slot)

                    has vbox

                    add FileScreenshot(slot) xalign 0.0
            
                    text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M "), empty=_("")):
                        style "slot_time_text"

                    text FileSaveName(slot):
                        style "slot_name_text"

                    key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
        vbox:
            style_prefix "Seite"

            yalign 0.5
            xalign 0.0
            spacing 0
            

            textbutton _("<") action FilePagePrevious()

            if config.has_autosave:
                textbutton _("{#auto_page}A") hover_sound "audio/sfx/click-21156.mp3" activate_sound "audio/sfx/umise_1005.ogg" action FilePage("auto")

            if config.has_quicksave:
                textbutton _("{#quick_page}Q") hover_sound "audio/sfx/click-21156.mp3" activate_sound "audio/sfx/umise_1005.ogg" action FilePage("quick")

            ## range(1, 10) gives the numbers from 1 to 9.
            for page in range(1, 6):
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
    modal True
    add "gui/game_menu.png" at center
    add "gui/settings/background.png" at center
    imagebutton auto "gui/button/back2_%s.png" action Return() activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3" yalign 0.02 xalign 0.97
    add partObj

    vbox:

        xalign 0.35
        yalign 0.6
        spacing 50
        

        hbox:

            style_prefix "radio"
            imagebutton auto "gui/button/window_%s.png" action Preference("display", "window") activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"
            imagebutton auto "gui/button/full_%s.png" action Preference("display", "fullscreen") activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"

        hbox:

            style_prefix "check"
            imagebutton auto "gui/button/on_%s.png" action Preference("skip", "Toggle") activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"

        hbox:

            style_prefix "check"
            imagebutton auto "gui/button/de_%s.png" action Language(None) activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"
            imagebutton auto "gui/button/en_%s.png" action Language("English") activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"

        hbox:

            style_prefix "check"
            imagebutton auto "gui/button/off_%s.png" action SetVariable("persistent.showch", False) activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"
            imagebutton auto "gui/button/on_%s.png" action SetVariable("persistent.showch", True) activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"
        
        hbox:

            style_prefix "check"
            imagebutton auto "gui/button/off_%s.png" action SetVariable("persistent.showbgm", False) activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"
            imagebutton auto "gui/button/on_%s.png" action SetVariable("persistent.showbgm", True) activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"

        hbox:

            style_prefix "check"
            imagebutton auto "gui/button/off_%s.png" action SetVariable("persistent.showplaytime", False) activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"
            imagebutton auto "gui/button/on_%s.png" action SetVariable("persistent.showplaytime", True) activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"

    vbox:
        xalign 0.1
        yalign 0.60
        spacing 75
        yoffset 2
        label _("{color=#fff}Anzei{/color}{color=#f00}g{/color}{color=#fff}e{/color}")
        label _("{color=#fff}Übers{/color}{color=#f00}p{/color}{color=#fff}ringen{/color}")
        label _("{color=#fff}Spr{/color}{color=#f00}a{/color}{color=#fff}che{/color}")
        label _("Zeige Kapite{red_truth}l{/red_truth}namen")
        label _("Zeige BGM T{red_truth}i{/red_truth}tel")
        label _("Zeige S{red_truth}p{/red_truth}ielzeit")
    vbox:
        xalign 0.85
        yalign 0.5
        yoffset 50
        style_prefix "slider"
        box_wrap True

        default text_cps_preview = PreviewSlowText("So sieht der Text aus.")

        vbox:
                    
            label _("{color=#fff}- Textgeschwindi{color=#f00}g{color=#fff}keit >>")

            bar value Preference("text speed"):
                released Function(text_cps_preview.update_cps)

            add text_cps_preview:                      #####
                ysize 38 # Same size as the bar        #####
                yoffset 3 # Slight offset down         #####

            label _("{color=#fff}+ Auto{color=#f00}m{color=#fff}odusgeschwindigkeit -")

            bar value Preference("auto-forward time")

            vbox:

                if config.has_music:
                    label _("{color=#fff}- Musiklautstär{color=#f00}k{color=#fff}e +")

                    vbox:
                        bar value Preference("music volume")

                if config.has_sound:

                    label _("{color=#fff}- Soundlautstär{color=#f00}k{color=#fff}e +")

                    vbox:
                        bar value Preference("sound volume")

                        if config.sample_sound:
                            textbutton _("Test") action Play("sound", config.sample_sound)


                    #if config.has_voice:
                        #label _("Sprachlautstärke")

                        #hbox:
                            #bar value Preference("voice volume")

                            #if config.sample_voice:
                                #textbutton _("Test") action Play("voice", config.sample_voice)

                    #if config.has_music or config.has_sound or config.has_voice:
                        #null height gui.pref_spacing
                        #imagebutton auto "gui/button/mute_%s.png" action Preference("all mute", "toggle") activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"
                        #textbutton _("Alles Stummschal{color=#f00}t{/color}en"):
                            #action Preference("all mute", "toggle")
                            #style "mute_all_button"


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
    xsize 800

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
    modal True
    add "gui/game_menu.png" at center
    add "gui/backlog/background.png" at center
    imagebutton auto "gui/button/back2_%s.png" action Return() activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3" yalign 0.02 xalign 0.97
    #add partObj
    predict False

    frame:

        style_prefix "history"

        xmargin 100
        ymargin 5
        xpadding 50
        ypadding 150
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

                        if h.what:

                            label h.what:
                                style "history_new"
                                substitute False

                                ## Take the color of the who text from the Character, if
                                ## set.
                                if "color" in h.what_args:
                                    text_color h.what_args["color"]


                    ## This puts some space between entries so it's easier to read
                    null height 5

                if not _history_list:

                    text "Keine Nachrichten vorhanden." line_spacing 10
                    ## Adding line_spacing prevents the bottom of the text
                    ## from getting cut off. Adjust when replacing the
                    ## default fonts.


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


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

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("tex" if gui.history_text_xalign else "tex")

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
    modal True
    tag menu
    add "gui/game_menu.png" at center
    add "gui/controls/background.png" at center
    imagebutton auto "gui/button/back2_%s.png" action Return() activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3" yalign 0.02 xalign 0.97
    add partObj

    default device = "keyboard"

    style_prefix "help"

    vbox:
        xalign 0.5
        yalign 0.2

        hbox:
            yalign 0.5
            imagebutton auto "gui/button/keyboard_%s.png" action SetScreenVariable("device", "keyboard") activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"

            if GamepadExists():
                imagebutton auto "gui/button/gamepad_%s.png" action SetScreenVariable("device", "gamepad") activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"

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

    if message == layout.ARE_YOU_SURE:
        add "gui/confirmblack.png" at center
        imagebutton auto "gui/button/accept_%s.png" action yes_action:
            xpos 450
            ypos 650
            activate_sound "audio/sfx/umise_1005.ogg" 
            hover_sound "audio/sfx/click-21156.mp3"
        imagebutton auto "gui/button/refuse_%s.png" action no_action:
            xpos 950
            ypos 650
            activate_sound "audio/sfx/umise_1005.ogg" 
            hover_sound "audio/sfx/click-21156.mp3"
        add "gui/button/sure.png":
            xalign 0.5
            yalign 0.5
    elif message == layout.OVERWRITE_SAVE:
        add "gui/confirmblack.png" at center
        imagebutton auto "gui/button/accept_%s.png" action [Play("sound", "audio/sfx/umise_056.ogg"), yes_action]:
            xpos 450
            ypos 650
            activate_sound "audio/sfx/umise_1005.ogg" 
            hover_sound "audio/sfx/click-21156.mp3"
        imagebutton auto "gui/button/refuse_%s.png" action no_action:
            xpos 950
            ypos 650
            activate_sound "audio/sfx/umise_1005.ogg" 
            hover_sound "audio/sfx/click-21156.mp3"
        add "gui/button/save.png":
            xalign 0.5
            yalign 0.5
    elif message == layout.LOADING:
        add "gui/confirmblack.png" at center
        imagebutton auto "gui/button/accept_%s.png" action [Play("sound", "audio/sfx/umise_058.ogg"), yes_action]:
            xpos 450
            ypos 650
            activate_sound "audio/sfx/umise_1005.ogg" 
            hover_sound "audio/sfx/click-21156.mp3"
        imagebutton auto "gui/button/refuse_%s.png" action no_action:
            xpos 950
            ypos 650
            activate_sound "audio/sfx/umise_1005.ogg" 
            hover_sound "audio/sfx/click-21156.mp3"
        add "gui/button/load.png":
            xalign 0.5
            yalign 0.5
    elif message == layout.QUIT:
        add "gui/confirmblack.png" at center
        imagebutton auto "gui/button/accept_%s.png" action [QuitWithScene(), yes_action]:
            xpos 450
            ypos 650
            activate_sound "audio/sfx/umise_1005.ogg" 
            hover_sound "audio/sfx/click-21156.mp3"
        imagebutton auto "gui/button/refuse_%s.png" action no_action:
            xpos 950
            ypos 650
            activate_sound "audio/sfx/umise_1005.ogg" 
            hover_sound "audio/sfx/click-21156.mp3"
        add "gui/button/quit.png":
            xalign 0.5
            yalign 0.5
    elif message == layout.MAIN_MENU:
        add "gui/confirmblack.png" at center
        imagebutton auto "gui/button/accept_%s.png" action [titurnd(), yes_action]: 
            xpos 450
            ypos 650
            activate_sound "audio/sfx/umise_1005.ogg" 
            hover_sound "audio/sfx/click-21156.mp3"
        imagebutton auto "gui/button/refuse_%s.png" action no_action:
            xpos 950
            ypos 650
            activate_sound "audio/sfx/umise_1005.ogg" 
            hover_sound "audio/sfx/click-21156.mp3"
        add "gui/button/quit.png":
            xalign 0.5
            yalign 0.5

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

    #add SideImage() xalign 0.0 yalign 1.0


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
    layout "greedy"
    line_overlap_split -8
    newline_indent True

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
    add "gui/game_menu.png" at center
    add "gui/scenario/background.png" at center
    add partObj

    imagebutton auto "gui/button/back2_%s.png" action ShowMenu("main_menu") activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3" yalign 0.01 xalign 0.98

    hbox:

        yalign 0.1
        xpos 10


        imagebutton idle "gui/button/main2_selected_idle.png" action NullAction()

        if persistent.gamecleared == True:

            imagebutton auto "gui/button/bonus2_%s.png" action ShowMenu("story_select_bonus") activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"

        else:

            imagebutton auto "gui/button/bonuslocked_%s.png" action NullAction() hovered Show('locked') unhovered Hide('locked') hover_sound "audio/sfx/click-21156.mp3"
    vbox:
        
        xpos 73
        yalign 0.5


        imagebutton auto "gui/button/main_%s.png" action Start("startgame") hovered Show('mainstory') unhovered Hide('mainstory') hover_sound "audio/sfx/click-21156.mp3"

        if persistent.mainstorycleared == True:

            imagebutton auto "gui/button/teaparty_%s.png" action Start("teaparty") hovered Show('teaparty') unhovered Hide('teaparty') hover_sound "audio/sfx/click-21156.mp3"

        else:

            imagebutton auto "gui/button/tealocked_%s.png" action NullAction() hovered Show('locked') unhovered Hide('locked') hover_sound "audio/sfx/click-21156.mp3"


        if persistent.teapartycleared == True:

            imagebutton auto "gui/button/hidden_%s.png" action Start("urateaparty") hovered Show('urateaparty') unhovered Hide('urateaparty') hover_sound "audio/sfx/click-21156.mp3"
        else:

            imagebutton auto "gui/button/uralocked_%s.png" action NullAction() hovered Show('locked') unhovered Hide('locked') hover_sound "audio/sfx/click-21156.mp3"

        if persistent.gamecleared == True:

            imagebutton auto "gui/button/bonus_%s.png" action NullAction() hovered Show('bonushover') unhovered Hide('bonushover') hover_sound "audio/sfx/click-21156.mp3"

        else:

            pass

screen story_select_bonus():

    tag menu
    add "gui/game_menu.png" at center
    add "gui/scenario/background.png" at center
    add partObj

    imagebutton auto "gui/button/back2_%s.png" action ShowMenu("main_menu") activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3" yalign 0.01 xalign 0.98

    hbox:

        yalign 0.1
        xpos 10


        imagebutton auto "gui/button/main2_%s.png" action ShowMenu("story_select") activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"

        imagebutton idle "gui/button/bonus2_selected_idle.png" action NullAction()

screen mainstory():
    tag hover
    imagemap:
        ground "gui/scenario/details_00.png"

screen teaparty():
    tag hover
    imagemap:
        ground "gui/scenario/details_01.png"

screen urateaparty():
    tag hover
    imagemap:
        ground "gui/scenario/details_02.png"

screen bonushover():
    tag hover
    imagemap:
        ground "gui/title/hover/bonus.png"

screen continuehover():
    tag hover
    imagemap:
        ground "gui/title/hover/continue.png"


## hover textboxen ##
screen starthover():
    tag hover
    imagemap:
        ground "gui/title/hover/start.png"

screen loadhover():
    tag hover
    imagemap:
        ground "gui/title/hover/load.png"

screen creditshover():
    tag hover
    imagemap:
        ground "gui/title/hover/credits.png"

screen settingshover():
    tag hover
    imagemap:
        ground "gui/title/hover/settings.png"

screen helphover():
    tag hover
    imagemap:
        ground "gui/title/hover/controls.png"

screen quithover():
    tag hover
    imagemap:
        ground "gui/title/hover/quit.png"

screen trophyhover():
    tag hover
    imagemap:
        ground "gui/title/hover/trophy.png"

screen characterhover():
    tag hover
    imagemap:
        ground "gui/title/hover/characterbox.png"


screen jukeboxhover():
    tag hover
    imagemap:
        ground "gui/title/hover/musicbox.png"

screen tiphover():
    tag hover
    imagemap:
        ground "gui/title/hover/tips.png"

screen locked():
    tag hover
    imagemap:
        ground "gui/scenario/details_404.png"

screen characters():
    tag menu
    modal True
    add "gui/game_menu.png" at center
    add "gui/charbox/background.png" at center
    add partObj
    imagebutton auto "gui/button/back2_%s.png" action Return() activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3" yalign 0.02 xalign 0.97
    hbox:

        xpos 110
        ypos 200

        if persistent.kinzo == True:
            imagebutton auto "gui/chars/char01_%s.png" action ShowMenu("char01") activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"
        else:
            imagebutton auto "gui/chars/char00_%s.png" action NullAction()

        if persistent.krauss == True:
            imagebutton auto "gui/chars/char02_%s.png" action ShowMenu("char02") activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"
        else:
            imagebutton auto "gui/chars/char00_%s.png" action NullAction()

        if persistent.natsuhi == True:
            imagebutton auto "gui/chars/char03_%s.png" action ShowMenu("char03") activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"
        else:
            imagebutton auto "gui/chars/char00_%s.png" action NullAction()

        if persistent.jessica == True:
            imagebutton auto "gui/chars/char05_%s.png" action ShowMenu("char05") activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"
        else:
            imagebutton auto "gui/chars/char00_%s.png" action NullAction()

    hbox:

        xpos 110
        ypos 300

        if persistent.nanjo == True:
            imagebutton auto "gui/chars/char15_%s.png" action ShowMenu("char15") activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"
        else:
            imagebutton auto "gui/chars/char00_%s.png" action NullAction()

        if persistent.eva == True:
            imagebutton auto "gui/chars/char06_%s.png" action ShowMenu("char06") activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"
        else:
            imagebutton auto "gui/chars/char00_%s.png" action NullAction()

        if persistent.hideyoshi == True:    
            imagebutton auto "gui/chars/char07_%s.png" action ShowMenu("char07") activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"
        else:
            imagebutton auto "gui/chars/char00_%s.png" action NullAction()

        if persistent.george == True:
            imagebutton auto "gui/chars/char08_%s.png" action ShowMenu("char08") activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"
        else:
            imagebutton auto "gui/chars/char00_%s.png" action NullAction()
    hbox:

        xpos 110
        ypos 400

        if persistent.beatrice == True:
            imagebutton auto "gui/chars/char21_%s.png" action ShowMenu("char21") activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"
        else:
            imagebutton auto "gui/chars/char00_%s.png" action NullAction()

        if persistent.rudolf == True:
            imagebutton auto "gui/chars/char09_%s.png" action ShowMenu("char09") activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"
        else:
            imagebutton auto "gui/chars/char00_%s.png" action NullAction()

        if persistent.kyrie == True:
            imagebutton auto "gui/chars/char10_%s.png" action ShowMenu("char10") activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"
        else:
            imagebutton auto "gui/chars/char00_%s.png" action NullAction()

        if persistent.battlerdead == True:
            imagebutton auto "gui/chars/char11_%s.png" action [ShowMenu("char11dead"), SelectedIf(SetVariable("battlerexe", True)), SetVariable("battlerexe", True)] activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"
        elif persistent.battler == True:
            imagebutton auto "gui/chars/char11_%s.png" action ShowMenu("char11") activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"
        else:
            imagebutton auto "gui/chars/char00_%s.png" action NullAction()
    hbox:

        xpos 110
        ypos 500

        if persistent.genji == True:
            imagebutton auto "gui/chars/char16_%s.png" action ShowMenu("char16") activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"
        else:
            imagebutton auto "gui/chars/char00_%s.png" action NullAction()

        if persistent.rosa == True:
            imagebutton auto "gui/chars/char13_%s.png" action ShowMenu("char13") activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"
        else:
            imagebutton auto "gui/chars/char00_%s.png" action NullAction()

        add "gui/chars/emptyspace.png"

        if persistent.maria == True:
            imagebutton auto "gui/chars/char14_%s.png" action ShowMenu("char14") activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"
        else:
            imagebutton auto "gui/chars/char00_%s.png" action NullAction()

    hbox:

        xpos 110
        ypos 600

        if persistent.shannon == True:
            imagebutton auto "gui/chars/char19_%s.png" action ShowMenu("char19") activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"
        else:
            imagebutton auto "gui/chars/char00_%s.png" action NullAction()

        if persistent.kanon == True:
            imagebutton auto "gui/chars/char20_%s.png" action ShowMenu("char20") activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"
        else:
            imagebutton auto "gui/chars/char00_%s.png" action NullAction()

        if persistent.gohda == True:
            imagebutton auto "gui/chars/char18_%s.png" action ShowMenu("char18") activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"
        else:
            imagebutton auto "gui/chars/char00_%s.png" action NullAction()

        if persistent.kumasawa == True:
            imagebutton auto "gui/chars/char17_%s.png" action ShowMenu("char17") activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"
        else:
            imagebutton auto "gui/chars/char00_%s.png" action NullAction()


screen witches():
    imagemap:
        ground "gui/title/hovermenu2.png"


screen hina():

    imagemap:
        ground "gui/title/hovermenu2.png"

screen char05():
    tag menu
    use characters
    imagemap:
        ground "gui/title/hovermenu2.png"
    image jes_char at r3
    text "Ushiromiya Jessica" style 'charnametext' at Position(xpos = 75, ypos = 500)
    text "Hier sollten Infos über Jessica stehen." style 'chartext' at Position (xpos = 60, ypos = 550)

screen char06():
    tag menu
    use characters
    imagemap:
        ground "gui/title/hovermenu2.png"
    image eva_char at r3
    text "Ushiromiya Eva" style 'charnametext' at Position(xpos = 75, ypos = 500)
    text "Hier sollten Infos über Eva stehen." style 'chartext' at Position (xpos = 60, ypos = 550)

screen char07():
    tag menu
    use characters
    imagemap:
        ground "gui/title/hovermenu2.png"
    image hid_char at r3
    text "Ushiromiya Hideyoshi" style 'charnametext' at Position(xpos = 75, ypos = 500)
    text "Hier sollten Infos über Hideyoshi stehen." style 'chartext' at Position (xpos = 60, ypos = 550)

screen char08():
    tag menu
    use characters
    imagemap:
        ground "gui/title/hovermenu2.png"
    image geo_char at r3
    text "Ushiromiya George" style 'charnametext' at Position(xpos = 75, ypos = 500)
    text "Hier sollten Infos über George stehen." style 'chartext' at Position (xpos = 60, ypos = 550)

screen char09():
    tag menu
    use characters
    imagemap:
        ground "gui/title/hovermenu2.png"
    image rud_char at r3
    text "Ushiromiya Rudolf" style 'charnametext' at Position(xpos = 75, ypos = 500)
    text "Hier sollten Infos über Rudolf stehen." style 'chartext' at Position (xpos = 60, ypos = 550)

screen char10():
    tag menu
    use characters
    imagemap:
        ground "gui/charbox/hovermenu2.png"
    image kyr_char at r3
    text "Ushiromiya Kyrie" style 'charnametext' at Position(xpos = 75, ypos = 500)
    text "Hier sollten Infos über Kyrie stehen." style 'chartext' at Position (xpos = 60, ypos = 550)

screen char11():
    tag menu
    use characters
    imagemap:
        ground "gui/charbox/butdesc.png"

    vbox:
        xpos 100
        ypos 700

        if persistent.battlerdead == True:
            imagebutton auto "gui/button/execute_%s.png" action Show("char11dead") activate_sound "audio/sfx/umise_1006.ogg" hover_sound "audio/sfx/click-21156.mp3"
        else: 
            pass

screen char11dead():
    tag menu
    use characters
    imagemap:
        ground "gui/charbox/buttest.png"

        vbox:
            xpos 100
            ypos 700

            imagebutton auto "gui/button/resurrect_%s.png" action Show("char11") activate_sound "audio/sfx/umise_1021.ogg" hover_sound "audio/sfx/click-21156.mp3"

    

screen char13():
    tag menu
    use characters
    imagemap:
        ground "gui/title/hovermenu2.png"
    image ros_char at r3
    text "Ushiromiya Rosa" style 'charnametext' at Position(xpos = 75, ypos = 500)
    text "Hier sollten Infos über Rosa stehen." style 'chartext' at Position (xpos = 60, ypos = 550)

screen char14():
    tag menu
    use characters
    imagemap:
        ground "gui/title/hovermenu2.png"
    image mar_char at r3
    text "Ushiromiya Maria" style 'charnametext' at Position(xpos = 75, ypos = 500)
    text "Hier sollten Infos über Maria stehen." style 'chartext' at Position (xpos = 60, ypos = 550)

screen char17():
    tag menu
    use characters
    imagemap:
        ground "gui/title/hovermenu2.png"
    image kum_char at r3
    text "Kumasawa Chiyo" style 'charnametext' at Position(xpos = 75, ypos = 500)
    text "Hier sollten Infos über Kumasawa stehen." style 'chartext' at Position (xpos = 60, ypos = 550)

screen char18():
    tag menu
    use characters
    imagemap:
        ground "gui/title/hovermenu2.png"
    image goh_char at r3
    text "Gohda Toshiro" style 'charnametext' at Position(xpos = 75, ypos = 500)
    text "Hier sollten Infos über Gohda stehen." style 'chartext' at Position (xpos = 60, ypos = 550)

screen char19():
    tag menu
    use characters
    imagemap:
        ground "gui/title/hovermenu2.png"
    image sha_char at r3
    text "Shannon" style 'charnametext' at Position(xpos = 75, ypos = 500)
    text "Hier sollten Infos über Shannon stehen." style 'chartext' at Position (xpos = 60, ypos = 550)

screen char21():
    tag menu
    use characters
    imagemap:
        ground "gui/title/hovermenu2.png"
    image bea_char at r3
    text "Beatrice die Goldene" style 'charnametext' at Position(xpos = 75, ypos = 500)
    text "Hier sollten Infos über Beatrice stehen." style 'chartext' at Position (xpos = 60, ypos = 550)

define config.hyperlink_protocol = "showmenu"

screen tipps():

    tag menu
    modal True
    add "gui/game_menu.png" at center
    add "gui/tipps/background1.png" at center
    add partObj
    imagebutton auto "gui/button/back2_%s.png" action Return() activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3" yalign 0.02 xalign 0.97

    vbox:
        xpos 1373
        yalign 0.5


        imagebutton auto "gui/tipps/tip01_%s.png" action ShowMenu("tip01") activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"

        if persistent.tip2 == True:
            imagebutton auto "gui/tipps/tip02_%s.png" action ShowMenu("tip02") activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3"

screen grimoire():
    tag menu
    modal True
    add "gui/game_menu.png" at center
    add "gui/tipps/background2.png" at center
    add partObj
    imagebutton auto "gui/button/back2_%s.png" action Return() activate_sound "audio/sfx/umise_1005.ogg" hover_sound "audio/sfx/click-21156.mp3" yalign 0.02 xalign 0.97

screen tip01():

    tag menu
    modal True
    use tipps

    add "gui/tipps/tip01_details.png" at center

screen tip02():

    tag menu
    modal True
    use tipps

    add "gui/tipps/tip02_details.png" at center


screen confirmrestart():

    modal True

    window:
        style "gm_root"

    frame:
        style_prefix "confirm"

        xfill True
        xmargin 50
        ypadding 25
        yalign .25

        vbox:
            xfill True
            spacing 25

            text(""" 
Das ändern der Textbox erfordert einen sofortigen Neustart.
            """) text_align 0.5 xalign 0.5

            hbox:
                spacing 100
                xalign .5
                textbutton _("Bestätigen") action QuitWithScene()
################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger button that are easier to touch.
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
    #background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin -80
    bottom_margin 0

style pref_vbox:
    variant "small"
    xsize 650

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
