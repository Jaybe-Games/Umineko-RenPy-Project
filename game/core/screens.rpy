init offset = -1


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
    font "fonts/Georgia.otf"
    size 25

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
    yminimum gui.textbox_height
    background Transform("gui/[textbox].png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/[namebox].png", gui.namebox_borders, xalign=gui.name_xalign)
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

### Der Screen der mehr generalüberholungen hatte, als ein 10 fach retouriertes Appleprodukt.

screen navigation():

    add "images/backgrounds/mmbackground.png" at mmclouds
    add "images/backgrounds/mmbg.png"
    add "rainbackscroll"
    add "rainfrontscroll"
    add "gui/title/title_hana.png" at topright
    add "gui/title/copyright.png" at left
    add "gui/title/titlelogo.png" at topright,buttondissolvetitle
    add partObj
    text "V[config.version!t]" at topleft size 30 antialias True outlines [ (absolute(3), "#000", absolute(0), absolute(0)) ]
    on "show" action Play("rain", "audio/sfx/umilse_012.ogg")
    on "hide" action Stop("rain")

    fixed:

        vbox:

            xalign 0.98
            yalign 0.9
            spacing 3
                 
            if persistent.new == True:
                imagebutton auto "gui/title/buttons/startnew_%s.png" action [Play("sound", "/audio/sfx/umise_051.ogg"), ShowMenu("story_select"), Hide('starthover'), SetVariable("ismain", True)] hover_sound "audio/sys/sysse_move.wav" hovered Show('starthover') unhovered Hide('starthover') at buttondissolve1
            else:
                imagebutton auto "gui/title/buttons/start_%s.png" action [Play("sound", "/audio/sfx/umise_051.ogg"), ShowMenu("story_select"), Hide('starthover'), SetVariable("ismain", True)] hover_sound "audio/sys/sysse_move.wav" hovered Show('starthover') unhovered Hide('starthover') at buttondissolve1

            if renpy.seen_label("start"):

                imagebutton auto "gui/title/buttons/continue_%s.png" action Continue(confirm=True) hovered Show('continuehover') unhovered Hide('continuehover') hover_sound "audio/sys/sysse_move.wav" at buttondissolve1
                
            if persistent.menustate == 0:
                imagebutton auto "gui/title/buttons/load2_%s.png" action [ShowMenu("load"), Hide('loadhover')] activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav" hovered Show('loadhover') unhovered Hide('loadhover') at buttondissolve1
            if persistent.menustate == 1:
                imagebutton auto "gui/title/buttons/load_%s.png" action [ShowMenu("load"), Hide('loadhover')] activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav" hovered Show('loadhover') unhovered Hide('loadhover') at buttondissolve2
            if persistent.menustate == 2:
                imagebutton auto "gui/title/buttons/load_%s.png" action [ShowMenu("load"), Hide('loadhover')] activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav" hovered Show('loadhover') unhovered Hide('loadhover') at buttondissolve2
            if persistent.menustate == 3:
                imagebutton auto "gui/title/buttons/load_%s.png" action [ShowMenu("load"), Hide('loadhover')] activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav" hovered Show('loadhover') unhovered Hide('loadhover') at buttondissolve2

            if persistent.menustate == 0:
                imagebutton auto "gui/title/buttons/settings2_%s.png" action [ShowMenu("preferences"), Hide('settingshover')] activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav" hovered Show('settingshover') unhovered Hide('settingshover') at buttondissolve2
            if persistent.menustate == 1:
                imagebutton auto "gui/title/buttons/settings_%s.png" action [ShowMenu("preferences"), Hide('settingshover')] activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav" hovered Show('settingshover') unhovered Hide('settingshover') at buttondissolve2
            if persistent.menustate == 2:
                imagebutton auto "gui/title/buttons/settings_%s.png" action [ShowMenu("preferences"), Hide('settingshover')] activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav" hovered Show('settingshover') unhovered Hide('settingshover') at buttondissolve2
            if persistent.menustate == 3:
                imagebutton auto "gui/title/buttons/settings_%s.png" action [ShowMenu("preferences"), Hide('settingshover')] activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav" hovered Show('settingshover') unhovered Hide('settingshover') at buttondissolve2

            if persistent.menustate == 0:
                imagebutton auto "gui/title/buttons/achieve2_%s.png" action [ShowMenu("achievement_menu"), Hide('trophyhover')] activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav" hovered Show('trophyhover') unhovered Hide('trophyhover') at buttondissolve2
            if persistent.menustate == 1:
                imagebutton auto "gui/title/buttons/achieve_%s.png" action [ShowMenu("achievement_menu"), Hide('trophyhover')] activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav" hovered Show('trophyhover') unhovered Hide('trophyhover') at buttondissolve3
            if persistent.menustate == 2:
                imagebutton auto "gui/title/buttons/achieve_%s.png" action [ShowMenu("achievement_menu"), Hide('trophyhover')] activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav" hovered Show('trophyhover') unhovered Hide('trophyhover') at buttondissolve3
            if persistent.menustate == 3:
                imagebutton auto "gui/title/buttons/achieve_%s.png" action [ShowMenu("achievement_menu"), Hide('trophyhover')] activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav" hovered Show('trophyhover') unhovered Hide('trophyhover') at buttondissolve3

            if persistent.tipunlocked == True:
                imagebutton auto "gui/title/buttons/tip_%s.png" action [ShowMenu("tipps"), Hide('tiphover')] activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav" hovered Show('tiphover') unhovered Hide('tiphover') at buttondissolve3
            else:
                pass

            if persistent.battler == True:
                imagebutton auto "gui/title/buttons/chars_%s.png" action [ShowMenu("characters"), Hide('characterhover')] activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav" hovered Show('characterhover') unhovered Hide('characterhover') at buttondissolve4
            else:
                pass
            
            if persistent.menustate == 0:
                imagebutton auto "gui/title/buttons/quit2_%s.png" action [QuitWithScene(), Hide('quithover')] activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav" hovered Show('quithover') unhovered Hide('quithover') at buttondissolve3
            if persistent.menustate == 1:
                imagebutton auto "gui/title/buttons/quit0_%s.png" action [QuitWithScene(), Hide('quithover')] activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav" hovered Show('quithover') unhovered Hide('quithover') at buttondissolve4
            if persistent.menustate == 2:
                imagebutton auto "gui/title/buttons/quit3_%s.png" action [QuitWithScene(), Hide('quithover')] activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav" hovered Show('quithover') unhovered Hide('quithover') at buttondissolve4
            if persistent.menustate == 3:
                imagebutton auto "gui/title/buttons/quit4_%s.png" action [QuitWithScene(), Hide('quithover')] activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav" hovered Show('quithover') unhovered Hide('quithover') at buttondissolve5


## Bei Gott ich habe gar keine Ahnung warum das hier existiert.
## Ohne diesen Mist funktioniert das Hauptmenü nicht

screen main_menu():

    tag menu
    use navigation



## Ein wenig Mathematik für einen Spielzeitzähler und das Pausenmenü

init python:
    def getPlayTime():

        pt = renpy.get_game_runtime()

        pth = int(pt // 3600)

        ptm = int(pt - pth * 3600) // 60

        pts = int(pt - (pth * 3600) - (ptm * 60))

        return "{:02d}:{:02d}:{:02d}".format(pth, ptm, pts)

screen game_menu(scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    add "gui/gamemenu/hanabottom.png" at hanabottomtransform
    add "gui/gamemenu/hanatop.png" at hanatoptransform
    add "gui/gamemenu/darken.png" at center
    imagebutton auto "images/system/back2_%s.png" action Return() activate_sound "audio/sys/sysse_cancel.wav" hover_sound "audio/sys/sysse_move.wav" yalign 0.02 xalign 0.97
    add partObj

    ### Wieder ein If der überflüssiger nicht sein kann, wird mal Zeit für ein wenig Code aufräumen

    vbox:

        yalign 0.5
        xalign 0.98

        imagebutton auto "gui/gamemenu/save_%s.png" action ShowMenu("save") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav" at gamemenubuttontransform

        imagebutton auto "gui/gamemenu/load_%s.png" action ShowMenu("load") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav" at gamemenubuttontransform

        imagebutton auto "gui/gamemenu/backlog_%s.png" action ShowMenu("history") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav" at gamemenubuttontransform

        imagebutton auto "gui/gamemenu/settings_%s.png" action [ShowMenu("preferences")] activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav" at gamemenubuttontransform

        imagebutton auto "gui/gamemenu/control_%s.png" action [ShowMenu("help")] activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav" at gamemenubuttontransform

        imagebutton auto "gui/gamemenu/trophy_%s.png" action [ShowMenu("achievement_menu"), Hide('trophyhover')] activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav" at gamemenubuttontransform

        if persistent.battler == True:
            imagebutton auto "gui/gamemenu/chars_%s.png" action [ShowMenu("characters"), Hide('characterhover')] activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav" at gamemenubuttontransform
        else:
            pass

        if persistent.tipunlocked == True:
            imagebutton auto "gui/gamemenu/tip_%s.png" action [ShowMenu("tipps"), Hide('tiphover')] activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav" at gamemenubuttontransform

        imagebutton auto "gui/gamemenu/backtomain_%s.png" action MainMenu() activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav" at gamemenubuttontransform

    text "♪" + songname ypos 1005 xpos 1900 xalign 1.0 size 30 font "fonts/AOTFShinGoProMedium.otf" outlines [ (absolute(3), "#000", absolute(0), absolute(0)) ]

    text _("Spielzeit: ") + getPlayTime() ypos 1040 xpos 1900 xalign 1.0 size 30 font "fonts/AOTFShinGoProMedium.otf" outlines [ (absolute(3), "#000", absolute(0), absolute(0)) ]


## Dieser Screen hatte mal irgend einen Sinn für einen Workaround
## Ich erinnere mich, ohne den scheiß, kann man das Menü nicht öffnen.
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

## Der Grund warum ich mit Visual Novel Maker auf Steam abgebrochen habe

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

## Ich neige dazu diesen Screen gerne voll zu müllen
screen preferences():

    tag menu
    modal True
    if main_menu:
        add "images/backgrounds/mmbackground.png" at mmclouds
        add "images/backgrounds/mmbg.png"
        add "rainbackscroll"
        add "rainfrontscroll"
    add "gui/settings/background.png" at center
    add "gui/settings/caption.png" at top
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
            imagebutton auto "gui/settings/buttons/a_%s.png" action [SelectedIf(gui.SetPreference("font", "newrodin.otf")), gui.SetPreference("font", "newrodin.otf")]  activate_sound "audio/sys/sysse_soff.wav" hover_sound "audio/sys/sysse_move.wav"
            imagebutton auto "gui/settings/buttons/b_%s.png" action [SelectedIf(gui.SetPreference("font", "ArnoPro.otf")), gui.SetPreference("font", "ArnoPro.otf"), gui.SetPreference("size", 45)] activate_sound "audio/sys/sysse_soff.wav" hover_sound "audio/sys/sysse_move.wav"

        hbox:
            #TODO: Buttons auswechseln
            style_prefix "radio"
            text _("Textboxstil") outlines [ (absolute(2), "#00000094", absolute(1), absolute(1)) ] size 40 yoffset 20
            imagebutton auto "gui/settings/buttons/a_%s.png" action [SelectedIf(SetVariable("textbox", "textboxa")), SetVariable("textbox", "textboxa"), SetVariable("namebox", "nameboxa"), SetVariable("narratorbox", "narratorboxa") ]  activate_sound "audio/sys/sysse_soff.wav" hover_sound "audio/sys/sysse_move.wav"
            imagebutton auto "gui/settings/buttons/b_%s.png" action [SelectedIf(SetVariable("textbox", "textboxb")), SetVariable("textbox", "textboxb"), SetVariable("namebox", "nameboxb"), SetVariable("narratorbox", "narratorboxb") ] activate_sound "audio/sys/sysse_soff.wav" hover_sound "audio/sys/sysse_move.wav"
            imagebutton auto "gui/settings/buttons/c_%s.png" action [SelectedIf(SetVariable("textbox", "textboxc")), SetVariable("textbox", "textboxc"), SetVariable("namebox", "nameboxc"), SetVariable("narratorbox", "narratorboxc") ] activate_sound "audio/sys/sysse_soff.wav" hover_sound "audio/sys/sysse_move.wav"
        
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

                    ### Eines Tages hat diese Config Voice... Eines Tages
                    #if config.has_voice:
                        #label _("Sprachlautstärke")

                        #hbox:
                            #bar value Preference("voice volume")

                            #if config.sample_voice:
                                #textbutton _("Test") action Play("voice", config.sample_voice)

                    #if config.has_music or config.has_sound or config.has_voice:
                        #null height gui.pref_spacing
                        #imagebutton auto "gui/button/mute_%s.png" action Preference("all mute", "toggle") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav"
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
    add "gui/settings/caption.png" at top
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

screen misc():

    tag menu
    modal True
    if main_menu:
        add "images/backgrounds/mmbackground.png" at mmclouds
        add "images/backgrounds/mmbg.png"
        add "rainbackscroll"
        add "rainfrontscroll"
    add "gui/settings/background.png" at center
    add "gui/settings/caption.png" at top
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

        


## Wer sich diesen Screen vorgenommen hat, ist heute Internationaler Geschäftsmann (Ich)

screen history():

    tag menu
    modal True
    add "gui/backlog/background.png" at center
    imagebutton auto "images/system/back2_%s.png" action Return() activate_sound "audio/sys/sysse_cancel.wav" hover_sound "audio/sys/sysse_move.wav" yalign 0.02 xalign 0.97
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


## Dieser Screen, wird irgendwann in die Preferences landen, also mach dich darauf gefasst die Macht von STRG C und STRG V zu spüren

screen help():
    modal True
    tag menu
    if main_menu:
        add "images/backgrounds/mmbackground.png" at mmclouds
        add "images/backgrounds/mmbg.png"
        add "rainbackscroll"
        add "rainfrontscroll"
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



################################################################################
## Additional screens
################################################################################


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


## Ein gutes 100% Custom Screen

screen story_select():

    tag menu
    add "images/backgrounds/mmbackground.png" at mmclouds
    add "images/backgrounds/mmbg.png"
    add "rainbackscroll"
    add "rainfrontscroll"
    add "gui/scenario/background.png" at center
    add partObj

    imagebutton auto "images/system/back2_%s.png" action ShowMenu("main_menu") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav" yalign 0.01 xalign 0.98

    hbox:

        yalign 0.1
        xpos 10


        imagebutton idle "gui/scenario/buttons/main2_selected_idle.png" action NullAction()

        if persistent.gamecleared == True:

            imagebutton auto "gui/scenario/buttons/bonus2_%s.png" action ShowMenu("story_select_bonus") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav"

        else:

            imagebutton auto "gui/scenario/buttons/bonuslocked_%s.png" action NullAction() activate_sound "audio/sys/sysse_error.wav" hovered Show('locked') unhovered Hide('locked') hover_sound "audio/sys/sysse_move.wav"
    vbox:
        
        xpos 73
        yalign 0.5


        imagebutton auto "gui/scenario/buttons/main_%s.png" action Start("startgame") hovered Show('mainstory') unhovered Hide('mainstory') hover_sound "audio/sys/sysse_move.wav"

        if persistent.mainstorycleared == True:

            imagebutton auto "gui/scenario/buttons/teaparty_%s.png" action Start("teaparty") hovered Show('teaparty') unhovered Hide('teaparty') hover_sound "audio/sys/sysse_move.wav"

        else:

            imagebutton auto "gui/scenario/buttons/tealocked_%s.png" action NullAction() activate_sound "audio/sys/sysse_error.wav" hovered Show('locked') unhovered Hide('locked') hover_sound "audio/sys/sysse_move.wav"


        if persistent.teapartycleared == True:

            imagebutton auto "gui/scenario/buttons/hidden_%s.png" action Start("urateaparty") hovered Show('urateaparty') unhovered Hide('urateaparty') hover_sound "audio/sys/sysse_move.wav"
        else:

            imagebutton auto "gui/scenario/buttons/uralocked_%s.png" action NullAction() activate_sound "audio/sys/sysse_error.wav" hovered Show('locked') unhovered Hide('locked') hover_sound "audio/sys/sysse_move.wav"

screen story_select_bonus():

    tag menu
    add "gui/game_menu.png" at center
    add "gui/scenario/background.png" at center
    add partObj

    imagebutton auto "gui/scenario/buttons/back2_%s.png" action ShowMenu("main_menu") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav" yalign 0.01 xalign 0.98

    hbox:

        yalign 0.1
        xpos 10


        imagebutton auto "gui/scenario/buttons/main2_%s.png" action ShowMenu("story_select") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav"

        imagebutton idle "gui/scenario/buttons/bonus2_selected_idle.png" action NullAction()

screen mainstory():
    tag hover
    ## TO DO: Durch Text ersetzen, der nichts mit einer PSD zutun hat
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


## Was zu machen = Durch Ingametext ersetzen für bessere Übersetzbarkeit
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


## Dieser Screen wird noch große Schmerzen verursachen
## To Do: Charakterbeschreibungen durch Ingametext ersetzen.

screen characters():
    tag menu
    modal True
    if main_menu:
        add "images/backgrounds/mmbackground.png" at mmclouds
        add "images/backgrounds/mmbg.png"
        add "rainbackscroll"
        add "rainfrontscroll"
    add "gui/charbox/background.png" at center
    add partObj
    imagebutton auto "images/system/back2_%s.png" action Return() activate_sound "audio/sys/sysse_cancel.wav" hover_sound "audio/sys/sysse_move.wav" yalign 0.02 xalign 0.97
    hbox:

        xpos 110
        ypos 200

        if persistent.kinzo == True:
            imagebutton auto "gui/charbox/icons/char01_%s.png" action ShowMenu("char01") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav"
        else:
            imagebutton auto "gui/charbox/icons/char00_%s.png" action NullAction() activate_sound "audio/sys/sysse_error.wav" hover_sound "audio/sys/sysse_move.wav"

        if persistent.krauss == True:
            imagebutton auto "gui/charbox/icons/char02_%s.png" action ShowMenu("char02") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav"
        else:
            imagebutton auto "gui/charbox/icons/char00_%s.png" action NullAction() activate_sound "audio/sys/sysse_error.wav" hover_sound "audio/sys/sysse_move.wav"

        if persistent.natsuhi == True:
            imagebutton auto "gui/charbox/icons/char03_%s.png" action ShowMenu("char03") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav"
        else:
            imagebutton auto "gui/charbox/icons/char00_%s.png" action NullAction() activate_sound "audio/sys/sysse_error.wav" hover_sound "audio/sys/sysse_move.wav"

        if persistent.jessica == True:
            imagebutton auto "gui/charbox/icons/char05_%s.png" action ShowMenu("char05") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav"
        else:
            imagebutton auto "gui/charbox/icons/char00_%s.png" action NullAction() activate_sound "audio/sys/sysse_error.wav" hover_sound "audio/sys/sysse_move.wav"

    hbox:

        xpos 110
        ypos 300

        if persistent.nanjo == True:
            imagebutton auto "gui/charbox/icons/char15_%s.png" action ShowMenu("char15") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav"
        else:
            imagebutton auto "gui/charbox/icons/char00_%s.png" action NullAction() activate_sound "audio/sys/sysse_error.wav" hover_sound "audio/sys/sysse_move.wav"

        if persistent.eva == True:
            imagebutton auto "gui/charbox/icons/char06_%s.png" action ShowMenu("char06") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav"
        else:
            imagebutton auto "gui/charbox/icons/char00_%s.png" action NullAction() activate_sound "audio/sys/sysse_error.wav" hover_sound "audio/sys/sysse_move.wav"

        if persistent.hideyoshi == True:    
            imagebutton auto "gui/charbox/icons/char07_%s.png" action ShowMenu("char07") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav"
        else:
            imagebutton auto "gui/charbox/icons/char00_%s.png" action NullAction() activate_sound "audio/sys/sysse_error.wav" hover_sound "audio/sys/sysse_move.wav"

        if persistent.george == True:
            imagebutton auto "gui/charbox/icons/char08_%s.png" action ShowMenu("char08") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav"
        else:
            imagebutton auto "gui/charbox/icons/char00_%s.png" action NullAction() activate_sound "audio/sys/sysse_error.wav" hover_sound "audio/sys/sysse_move.wav"
    hbox:

        xpos 110
        ypos 400

        if persistent.beatrice == True:
            imagebutton auto "gui/charbox/icons/char21_%s.png" action ShowMenu("char21") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav"
        else:
            imagebutton auto "gui/charbox/icons/char00_%s.png" action NullAction() activate_sound "audio/sys/sysse_error.wav" hover_sound "audio/sys/sysse_move.wav"

        if persistent.rudolf == True:
            imagebutton auto "gui/charbox/icons/char09_%s.png" action ShowMenu("char09") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav"
        else:
            imagebutton auto "gui/charbox/icons/char00_%s.png" action NullAction() activate_sound "audio/sys/sysse_error.wav" hover_sound "audio/sys/sysse_move.wav"

        if persistent.kyrie == True:
            imagebutton auto "gui/charbox/icons/char10_%s.png" action ShowMenu("char10") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav"
        else:
            imagebutton auto "gui/charbox/icons/char00_%s.png" action NullAction() activate_sound "audio/sys/sysse_error.wav" hover_sound "audio/sys/sysse_move.wav"

        if persistent.battler == True:
            imagebutton auto "gui/charbox/icons/char11_%s.png" action ShowMenu("char11") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav"
        else:
            imagebutton auto "gui/charbox/icons/char00_%s.png" action NullAction() activate_sound "audio/sys/sysse_error.wav" hover_sound "audio/sys/sysse_move.wav"
    hbox:

        xpos 110
        ypos 500

        if persistent.genji == True:
            imagebutton auto "gui/charbox/icons/char16_%s.png" action ShowMenu("char16") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav"
        else:
            imagebutton auto "gui/charbox/icons/char00_%s.png" action NullAction() activate_sound "audio/sys/sysse_error.wav" hover_sound "audio/sys/sysse_move.wav"

        if persistent.rosa == True:
            imagebutton auto "gui/charbox/icons/char13_%s.png" action ShowMenu("char13") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav"
        else:
            imagebutton auto "gui/charbox/icons/char00_%s.png" action NullAction() activate_sound "audio/sys/sysse_error.wav" hover_sound "audio/sys/sysse_move.wav"

        add "gui/charbox/icons/emptyspace.png"

        if persistent.maria == True:
            imagebutton auto "gui/charbox/icons/char14_%s.png" action ShowMenu("char14") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav"
        else:
            imagebutton auto "gui/charbox/icons/char00_%s.png" action NullAction() activate_sound "audio/sys/sysse_error.wav" hover_sound "audio/sys/sysse_move.wav"

    hbox:

        xpos 110
        ypos 600

        if persistent.shannon == True:
            imagebutton auto "gui/charbox/icons/char19_%s.png" action ShowMenu("char19") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav"
        else:
            imagebutton auto "gui/charbox/icons/char00_%s.png" action NullAction() activate_sound "audio/sys/sysse_error.wav" hover_sound "audio/sys/sysse_move.wav"

        if persistent.kanon == True:
            imagebutton auto "gui/charbox/icons/char20_%s.png" action ShowMenu("char20") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav"
        else:
            imagebutton auto "gui/charbox/icons/char00_%s.png" action NullAction() activate_sound "audio/sys/sysse_error.wav" hover_sound "audio/sys/sysse_move.wav"

        if persistent.gohda == True:
            imagebutton auto "gui/charbox/icons/char18_%s.png" action ShowMenu("char18") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav"
        else:
            imagebutton auto "gui/charbox/icons/char00_%s.png" action NullAction() activate_sound "audio/sys/sysse_error.wav" hover_sound "audio/sys/sysse_move.wav"

        if persistent.kumasawa == True:
            imagebutton auto "gui/charbox/icons/char17_%s.png" action ShowMenu("char17") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav"
        else:
            imagebutton auto "gui/charbox/icons/char00_%s.png" action NullAction() activate_sound "audio/sys/sysse_error.wav" hover_sound "audio/sys/sysse_move.wav"


## Diese ganzen Sachen sind entweder nicht implementiert oder müssen ausgetauscht werden
screen witches():
    imagemap:
        ground "gui/title/hovermenu2.png"


screen hina():

    imagemap:
        ground "gui/title/hovermenu2.png"

screen char01():
    tag menu
    use characters
    imagemap:
        ground "gui/charbox/kindesc.png"

screen char05():
    tag menu
    use characters
    imagemap:
        ground "gui/charbox/jesdesc.png"

screen char06():
    tag menu
    use characters
    imagemap:
        ground "gui/charbox/evadesc.png"

screen char07():
    tag menu
    use characters
    imagemap:
        ground "gui/charbox/hiddesc.png"

screen char08():
    tag menu
    use characters
    imagemap:
        ground "gui/charbox/geodesc.png"

screen char09():
    tag menu
    use characters
    imagemap:
        ground "gui/charbox/ruddesc.png"

screen char10():
    tag menu
    use characters
    imagemap:
        ground "gui/charbox/kirdesc.png"

screen char11():
    tag menu
    use characters
    imagemap:
        ground "gui/charbox/butdesc.png"

screen char11dead():
    tag menu
    use characters
    imagemap:
        ground "gui/charbox/buttest.png"

        vbox:
            xpos 100
            ypos 700

            imagebutton auto "gui/button/resurrect_%s.png" action Show("char11") activate_sound "audio/sfx/umise_1021.ogg" hover_sound "audio/sys/sysse_move.wav"

    

screen char13():
    tag menu
    use characters
    imagemap:
        ground "gui/charbox/rosdesc.png"

screen char14():
    tag menu
    use characters
    imagemap:
        ground "gui/charbox/mardesc.png"

screen char15():
    tag menu
    use characters
    imagemap:
        ground "gui/charbox/nandesc.png"

screen char16():
    tag menu
    use characters
    imagemap:
        ground "gui/charbox/gendesc.png"

screen char17():
    tag menu
    use characters
    imagemap:
        ground "gui/charbox/kumdesc.png"

screen char18():
    tag menu
    use characters
    imagemap:
        ground "gui/charbox/gohdesc.png"

screen char19():
    tag menu
    use characters
    imagemap:
        ground "gui/charbox/shadesc.png"

screen char21():
    tag menu
    use characters
    imagemap:
        ground "gui/title/hovermenu2.png"
    image bea_char at r3
    text "Beatrice die Goldene" style 'charnametext' at Position(xpos = 75, ypos = 500)
    text """Hier sollten Infos über Beatrice stehen.""" style 'chartext' at Position (xpos = 60, ypos = 550)

screen tipps():

    tag menu
    modal True
    if main_menu:
        add "images/backgrounds/mmbackground.png" at mmclouds
        add "images/backgrounds/mmbg.png"
        add "rainbackscroll"
        add "rainfrontscroll"
    add "gui/tipps/background1.png" at center
    add partObj
    imagebutton auto "images/system/back2_%s.png" action Return() activate_sound "audio/sys/sysse_cancel.wav" hover_sound "audio/sys/sysse_move.wav" yalign 0.02 xalign 0.97

    vbox:
        xpos 1373
        yalign 0.5


        imagebutton auto "gui/tipps/tip01_%s.png" action ShowMenu("tip01") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav"

        if persistent.tip2 == True:
            imagebutton auto "gui/tipps/tip02_%s.png" action ShowMenu("tip02") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav"

        if persistent.tip3 == True:
            imagebutton auto "gui/tipps/tip03_%s.png" action ShowMenu("tip03") activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav"

## DIe Tipps sind kompletter bullshit und tragen nichts zur Story bei und werden sich höchstens auf relevantes beschreiben
## To Do: Raus damit!
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

screen tip03():

    tag menu
    modal True
    use tipps

    add "gui/tipps/tip03_details.png" at center

## Ich habe das nur eingefügt, weil es cool ist Debugfunktionen sehen zu können.
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
