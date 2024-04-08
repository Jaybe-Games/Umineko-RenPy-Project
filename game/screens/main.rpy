screen navigation():

    add "images/system/mm_clouds.png" at mmclouds
    add "images/system/mm_bg.png" at mm_bg
    add "rainbackscroll"
    add "rainfrontscroll"
    add "gui/title/title_hana.png" at topright
    add "gui/title/copyright.png" at left
    add "gui/title/titlelogo.png" at topright,buttondissolvetitle
    add partObj
    text "V[config.version!t]" at topleft size 30 antialias True outlines [ (absolute(3), "#000", absolute(0), absolute(0)) ]
    on "show" action Play("rain", "audio/sfx/umilse_012.ogg")
    on "hide" action Stop("rain")
    on "show" action Play("wind", "audio/sfx/umilse_005.ogg")
    on "hide" action Stop("wind")

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

## Was zu machen = Durch Ingametext ersetzen für bessere Übersetzbarkeit
screen starthover():
    tag hover
    imagemap:
        ground "gui/title/hover/start.png"

screen loadhover():
    tag hover
    imagemap:
        ground "gui/title/hover/load.png"

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

screen tiphover():
    tag hover
    imagemap:
        ground "gui/title/hover/tips.png"

screen continuehover():
    tag hover
    imagemap:
        ground "gui/title/hover/continue.png"

transform blink:
    linear 1.0 alpha 0.2
    linear 1.0 alpha 1.0
    repeat

transform press_start_logo:
    xalign 0.5
    yalign 0.5

transform mm_bg:
    xalign 0.5
    yalign 0.3
    zoom 0.8

transform mm_fadeout:
    alpha 1.0
    linear 1.0 alpha 0.0

transform mm_logofadeout:
    zoom 1.0
    ease 1.0 zoom 0.5

style press_start_text:
    outlines [ (absolute(2), "#000000ff", absolute(1), absolute(1)) ] 
    size 50
    xalign 0.5
    yalign 0.8 

screen press_to_start():
    tag menu
    add "images/system/mm_clouds.png" at mmclouds
    add "images/system/pre_bg.png" at top
    add "rainbackscroll"
    add "rainfrontscroll"
    add "gui/title/copyright.png" at left
    add "gui/title/titlelogo.png" at press_start_logo

    
    text _("Klicke zum Starten") style "press_start_text" at blink
    
    imagemap:
        ground "images/system/transparent.png"
        hotspot (0, 0,1920, 1080) focus_mask None action Return()  activate_sound "audio/sys/sysse_decide.wav"

    on "show" action Play("rain", "audio/sfx/umilse_012.ogg")
    on "hide" action Stop("rain")
    on "show" action Play("wind", "audio/sfx/umilse_005.ogg")
    on "hide" action Stop("wind")