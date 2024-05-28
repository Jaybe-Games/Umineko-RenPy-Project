init offset = -1


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

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue


style say_window:
    xalign 0.5
    xfill True
    yalign 1.0
    left_margin 20
    right_margin 20
    top_margin 10
    bottom_margin 10
    left_padding 80
    right_padding 80
    top_padding 30
    bottom_padding 50
    xminimum 1420
    xmaximum 1800
    yminimum 400
    clipping True
    background Frame("gui/frame_[persistent.textbox]c.png", 25, 25)

style say_label:
    bold False
    text_align 0.5
    xalign 0.5
    yalign 0.5
    outlines [(2.5,"#181818e8",0,0)]

style say_dialogue:
    #properties gui.text_properties("dialogue")
    #xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    line_leading 5.5
    line_spacing 3.0
    kerning 1
    #ypos gui.dialogue_ypos
    outlines [(2.5,"#181818e8",0,0)]

style say_who_window:
    left_margin 20
    right_margin 20
    top_margin 5
    bottom_margin 30
    left_padding 80
    right_padding 80
    top_padding 10
    bottom_padding 5
    xalign 0.0
    yalign 0.5
    clipping True
    background Frame("gui/frame_[persistent.textbox]n.png", 100, 100)


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

#### HIER DU BLINDE NUSS!
style slider_slider:
    xsize 1500

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 675
    spacing 30

style optionname:
    outlines [ (absolute(2), "#00000094", absolute(1), absolute(1)) ]

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


style history_window:
    xfill True
    ysize gui.history_height

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign
    outlines [ (absolute(2), "#00000094", absolute(0), absolute(0)) ]
    size 50

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("tex" if gui.history_text_xalign else "tex")
    outlines [ (absolute(2), "#00000094", absolute(0), absolute(0)) ]
    size 50
    line_spacing 7

style history_label:
    xfill True

style history_label_text:
    xalign 0.5

style caption:
    bold False
    outlines [ (absolute(4), "#00000094", absolute(1), absolute(1)) ] 
    size 90 
    font "fonts/Georgia.ttf" 
    xalign 0.5 yalign 0.03

style header:
    color "#ffffff"
    outlines [ (absolute(2), "#000000ff", absolute(1), absolute(1)) ] 
    size 55 
    font "fonts/Montio-Regular.otf" 
    yalign 0.0 
    xalign 0.0 
    xpos 610 
    ypos 254

style headerlocked:
    color "#cc0000"
    outlines [ (absolute(2.5), "#000000ff", absolute(0), absolute(0)) ] 
    size 55 
    font "fonts/Montio-Regular.otf" 
    yalign 0.0 
    xalign 0.0 
    xpos 610 
    ypos 254

style desc:
    outlines [ (absolute(2.5), "#000000ff", absolute(0), absolute(0)) ] 
    size 30 
    font "fonts/Georgia.ttf" 
    yalign 0.0 
    xalign 0.0 
    xpos 610 
    ypos 335
    xmaximum 800

style victory_message_text:
    color "#ffffff"
    size 20

transform achievement_appear:
    subpixel True
    on show:
        yoffset -160.0 alpha 1.0
        easein 0.2 yoffset 5.0
        easeout 0.1 yoffset 0.0

    on hide:
        yoffset 0.0
        easein 0.2 yoffset 5.0
        easeout 0.1 yoffset -160.0
        alpha 0.0


style achievements_vbox is vbox
style achievements_text is text
style achievements_frame is frame

style achievements_vbox:
    minimum (300, 100)
    maximum (330, 100)
    spacing 2
    yfill False

style achievements_label:
    size 30
    outlines [(1, '#ffffff22', 0, 1)]
    yalign 0.5
    antialias True

style achievements_text:
    size 20
    yalign 0.5
    antialias True

style achievements_locked_text:
    antialias True
    color "#ffffff"
    size 20

style achievements_frame:
    background Solid('#444444')
    minimum (500, 140)
    align (0.5, 0.5)
    padding (15, 15, 15, 15)

style charheader:
    color "#ffffff"
    outlines [ (absolute(2), "#000000ff", absolute(1), absolute(1)) ] 
    size 55 
    font "fonts/newrodin.otf" 
    yalign 0.0 
    xalign 0.0 
    xpos 610 
    ypos 254

style chardesc:
    outlines [ (absolute(2), "#000000ff", absolute(1), absolute(1)) ] 
    size 30 
    font "fonts/newrodin.otf" 
    yalign 0.0 
    xalign 0.0 
    xpos 612 
    ypos 337

style hoverhead:
    outlines [ (absolute(2), "#000000ff", absolute(1), absolute(1)) ] 
    size 50 
    font "fonts/Georgia.ttf" 
    yalign 0.0 
    xalign 0.0 
    xpos 210 
    ypos 505

style hovertext:
    size 30 
    font "fonts/Georgia.ttf" 
    yalign 0.0 
    xalign 0.0 
    xpos 170 
    ypos 580

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

style controltext:
    outlines [ (absolute(2), "#000000ff", absolute(1), absolute(1)) ] 
    size 40
    spacing 5 
    font "fonts/Georgia.ttf" 
    yalign 0.6
    xalign 0.5 

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

style chaptertext:
    outlines [ (absolute(4), "#000000", absolute(0), absolute(0)) ]
    font "fonts/ArnoPro.otf"
    size 50
    line_spacing 7
    kerning 1

style disclaimer:
    outlines [ (absolute(2.5), "#000000", absolute(0), absolute(0)) ]
    font "fonts/ArnoPro.otf"
    xalign 0.8
    yalign 0.5
    size 50
    line_spacing 7
    kerning 1