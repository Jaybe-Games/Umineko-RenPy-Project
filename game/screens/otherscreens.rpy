init offset = -1


style bigtext:
    bold False
    font "fonts/Georgia.ttf"
    size 35

style button_back:
    activate_sound "audio/sfx/umise_1001.ogg"
    hover_sound "audio/sys/sysse_move.wav"
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

screen say(who, what, slow_effect = slow_fade, slow_effect_delay = 0, always_effect = None):
    style_prefix "say"

    window:
        id "window"

        if who is not None:
                    window:
                        id "namebox"
                        style "namebox"
                        text who id "who" at charname

        
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
    yminimum gui.textbox_height
    background Transform("gui/[persistent.textbox].png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/[persistent.namebox].png", gui.namebox_borders, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5
    outlines [ (absolute(2), "#000000ff", absolute(1), absolute(1)) ]
    kerning -1.7
    antialias True
    shaper "hardbuzz"

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos
    outlines [ (absolute(2), "#000000ff", absolute(1), absolute(1)) ]
    line_spacing 15
    language "western"
    kerning -1.0
    antialias True
    ### Ich versuche nicht mal so zu tun, als wüsste ich, was der shaper macht, es ist neu, also habe ich es eingefügt.
    shaper "hardbuzz"
    ### Dieser overlay_split Kasper soll die Artefakte in der Font minimieren.
    line_overlap_split -5


### Dieser Screen wird nur benutzt, damit man die Sprache vor Spielbeginn wählen kann

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
    ypos 0.5
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")



## Dieser Screen ist wirklich stark, ich habe dem nichts zuzufügen

screen confirm(message, yes_action, no_action):
    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    if message == layout.ARE_YOU_SURE:
        add "gui/confirmblack.png" at center
        imagebutton auto "images/system/accept_%s.png" action yes_action:
            yalign 0.7
            xalign 0.5
            activate_sound "audio/sys/sysse_decide.wav" 
            hover_sound "audio/sys/sysse_move.wav"
        imagebutton auto "images/system/refuse_%s.png" action no_action:
            yalign 0.8
            activate_sound "audio/sys/sysse_cancel.wav" 
            hover_sound "audio/sys/sysse_move.wav"
        add "images/system/sure.png":
            xalign 0.5
            yalign 0.5
    elif message == layout.OVERWRITE_SAVE:
        add "gui/confirmblack.png" at center
        imagebutton auto "images/system/accept_%s.png" action [Play("sound", "audio/sfx/umise_056.ogg"), yes_action]:
            yalign 0.7
            activate_sound "audio/sys/sysse_decide.wav" 
            hover_sound "audio/sys/sysse_move.wav"
        imagebutton auto "images/system/refuse_%s.png" action no_action:
            yalign 0.8
            activate_sound "audio/sys/sysse_cancel.wav" 
            hover_sound "audio/sys/sysse_move.wav"
        add "images/system/save.png":
            xalign 0.5
            yalign 0.5
    elif message == layout.LOADING:
        add "gui/confirmblack.png" at center
        imagebutton auto "images/system/accept_%s.png" action [Play("sound", "audio/sfx/umise_058.ogg"), yes_action]:
            yalign 0.7
            xalign 0.5
            activate_sound "audio/sys/sysse_decide.wav" 
            hover_sound "audio/sys/sysse_move.wav"
        imagebutton auto "images/system/refuse_%s.png" action no_action:
            yalign 0.8
            xalign 0.5
            activate_sound "audio/sys/sysse_cancel.wav" 
            hover_sound "audio/sys/sysse_move.wav"
        add "images/system/load.png":
            xalign 0.5
            yalign 0.5
    elif message == layout.QUIT:
        add "gui/confirmblack.png" at center
        imagebutton auto "images/system/accept_%s.png" action [QuitWithScene(), yes_action]:
            yalign 0.7
            xalign 0.5
            activate_sound "audio/sys/sysse_decide.wav" 
            hover_sound "audio/sys/sysse_move.wav"
        imagebutton auto "images/system/refuse_%s.png" action no_action:
            yalign 0.8
            xalign 0.5
            activate_sound "audio/sys/sysse_cancel.wav" 
            hover_sound "audio/sys/sysse_move.wav"
        add "images/system/quit.png":
            xalign 0.5
            yalign 0.5
    elif message == layout.MAIN_MENU:
        add "gui/confirmblack.png" at center
        imagebutton auto "images/system/accept_%s.png" action [titurnd(), yes_action]: 
            yalign 0.7
            xalign 0.5
            activate_sound "audio/sys/sysse_decide.wav" 
            hover_sound "audio/sys/sysse_move.wav"
        imagebutton auto "images/system/refuse_%s.png" action no_action:
            yalign 0.8
            xalign 0.5
            activate_sound "audio/sys/sysse_cancel.wav" 
            hover_sound "audio/sys/sysse_move.wav"
        add "images/system/quit.png":
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


## Wird irgendwann auch mal besser aussehen

screen skip_indicator():

    zorder 100

    imagebutton idle "images/system/skip.png" action NullAction at topleft

## Ich hoffe ich muss mich um diesen kleinen Schlingel nicht mehr kümmern, es hat mich alle nerven gekostet,
## dass FancyText hier funktioniert.

screen nvl(dialogue, slow_effect = slow_fade, slow_effect_delay = 0, always_effect = None, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue, slow_effect = slow_effect, slow_effect_delay = slow_effect_delay, always_effect = always_effect)

        else:

            use nvl_dialogue(dialogue, slow_effect = slow_effect, slow_effect_delay = slow_effect_delay, always_effect = always_effect)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True.

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue, slow_effect = slow_fade, slow_effect_delay = 0, always_effect = None):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                fancytext d.what id d.what_id slow_effect slow_effect slow_effect_delay slow_effect_delay always_effect always_effect


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = 6

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
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.text_properties("nvl_button")

screen Debugscreen():
    
    $ director.button = True
    vbox:
        yalign 0.4
        xalign 0.01
        text "Toggle Directormode = D" outlines [ (absolute(3), "#000", absolute(0), absolute(0)) ] size 25
        text "Toggle FPS = F3" outlines [ (absolute(3), "#000", absolute(0), absolute(0)) ] size 25
        text "Toggle Imagelog = F4" outlines [ (absolute(3), "#000", absolute(0), absolute(0)) ] size 25
        text "Reload Game = Shift + R" outlines [ (absolute(3), "#000", absolute(0), absolute(0)) ] size 25
        text "Menustate = " + str(persistent.menustate) outlines [ (absolute(3), "#000", absolute(0), absolute(0)) ] size 25
        text "Current Chapter = " + str(chapter) outlines [ (absolute(3), "#000", absolute(0), absolute(0)) ] size 25
        text "Current Soundtrack = " + songname outlines [ (absolute(3), "#000", absolute(0), absolute(0)) ] size 25
        text "Current Playtime = " + getPlayTime() outlines [ (absolute(3), "#000", absolute(0), absolute(0)) ] size 25
        text "Current Speaker = " + str(speaking) outlines [ (absolute(3), "#000", absolute(0), absolute(0)) ] size 25
