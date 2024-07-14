transform coverzoom:
    zoom 0.4

image ep1_cover:
    yalign 0.60 
    xalign 0.90 
    "gui/scenario/covers/ep1_1.png" with dissolve
    5
    "gui/scenario/covers/ep1_2.png" with dissolve
    5
    "gui/scenario/covers/ep1_3.png" with dissolve
    5
    repeat


screen story_select():

    tag menu
    add "gui/scenario/bg.png"
    add "gui/bgdark.png" at center
    add "gui/scenario/background.png" at center
    text _("ScenarioSelect") style "caption"
    add partObj

    imagebutton auto "images/system/back2_%s.png" action ShowMenu("main_menu") hovered Show('fflush') unhovered Hide('fflush') activate_sound "audio/sys/sysse_decide.wav" hover_sound "audio/sys/sysse_move.wav" yalign 0.01 xalign 0.98

    vbox:
        
        xpos 73
        yalign 0.5

        ## Rondo of the Witch and Reasoning / EP1-4

        if persistent.gamemode == "rondo":
            ## Note: you have to do these if clauses in a certain order, otherwise things are getting weird
            
            # Episode1 Legend of the Golden Witch Button
            if persistent.ep1started == False:
                imagebutton auto "gui/scenario/buttons/ep1new_%s.png" action [SetVariable("ep1_start", True), Start()] hovered Show('ep1') hover_sound "audio/sys/sysse_move.wav"
            elif persistent.ep1completed == True:
                imagebutton auto "gui/scenario/buttons/ep1complete_%s.png" action [SetVariable("ep1_start", True), Start()]hovered Show('ep1') hover_sound "audio/sys/sysse_move.wav"
            else:
                imagebutton auto "gui/scenario/buttons/ep1_%s.png" action [SetVariable("ep1_start", True), Start()] hovered Show('ep1') hover_sound "audio/sys/sysse_move.wav"

            # Episode2 Turn of the Golden Witch Button
            if persistent.ep1completed == False:
                imagebutton auto "gui/scenario/buttons/ep2locked_%s.png" action NullAction() hovered Show('locked') hover_sound "audio/sys/sysse_move.wav" activate_sound "audio/sys/sysse_error.wav" 
            elif persistent.ep2started == False:
                imagebutton auto "gui/scenario/buttons/ep2new_%s.png" action [SetVariable("ep2_start", True), Start()] hovered Show('ep2') hover_sound "audio/sys/sysse_move.wav"
            elif persistent.ep2completed == True:
                imagebutton auto "gui/scenario/buttons/ep2complete_%s.png" action [SetVariable("ep2_start", True), Start()] hovered Show('ep2') hover_sound "audio/sys/sysse_move.wav"
            else:
                imagebutton auto "gui/scenario/buttons/ep2_%s.png" action [SetVariable("ep2_start", True), Start()] hovered Show('ep2') hover_sound "audio/sys/sysse_move.wav"

            # Episode3 Banquet of the Golden Witch Button
            if persistent.ep2completed == False:
                imagebutton auto "gui/scenario/buttons/ep3locked_%s.png" action NullAction() hovered Show('locked') hover_sound "audio/sys/sysse_move.wav" activate_sound "audio/sys/sysse_error.wav" 
            elif persistent.ep3started == False:
                imagebutton auto "gui/scenario/buttons/ep3new_%s.png" action [SetVariable("ep3_start", True), Start()] hovered Show('ep3') hover_sound "audio/sys/sysse_move.wav"
            elif persistent.ep3completed == True:
                imagebutton auto "gui/scenario/buttons/ep3complete_%s.png" action [SetVariable("ep3_start", True), Start()] hovered Show('ep3') hover_sound "audio/sys/sysse_move.wav"
            else:
                imagebutton auto "gui/scenario/buttons/ep3_%s.png" action [SetVariable("ep3_start", True), Start()] hovered Show('ep3') hover_sound "audio/sys/sysse_move.wav"

            # Episode4 Alliance of the Golden Witch Button
            if persistent.ep3completed == False:
                imagebutton auto "gui/scenario/buttons/ep4locked_%s.png" action NullAction() hovered Show('locked') hover_sound "audio/sys/sysse_move.wav" activate_sound "audio/sys/sysse_error.wav" 
            elif persistent.ep4started == False:
                imagebutton auto "gui/scenario/buttons/ep4new_%s.png" action [SetVariable("ep4_start", True), Start()] hovered Show('ep4') hover_sound "audio/sys/sysse_move.wav"
            elif persistent.ep4completed == True:
                imagebutton auto "gui/scenario/buttons/ep4complete_%s.png" action [SetVariable("ep4_start", True), Start()] hovered Show('ep1') hover_sound "audio/sys/sysse_move.wav"
            else:
                imagebutton auto "gui/scenario/buttons/ep4_%s.png" action [SetVariable("ep4_start", True), Start()] hovered Show('ep4') hover_sound "audio/sys/sysse_move.wav"

            # Button to go to Answer Arcs after completing EP4
            if persistent.ep4completed == False:
                imagebutton auto "gui/scenario/buttons/nocturnelocked_%s.png" action NullAction() hovered Show('locked') hover_sound "audio/sys/sysse_move.wav" activate_sound "audio/sys/sysse_error.wav" 
        else:
        ### We pass here because I haven't started with nocturne yet and you cannot even get to this statement
            pass


## This screen is literally nothing and that's why it's so brilliant
## When you have a hoverscreen displayed all the time and you go into another screen, the hoverscreen can still be seen
## We don't want that, so we have this screen we can call on the return button to force hide every hoverscreen.
## Yea I know, fflush is a really good name for this hahaha
screen fflush():
    tag hover

### Here goes every episode description and some other stuff like a locked screen

screen locked():
    tag hover
    add "gui/scenario/sub.png" yalign 0.27 xalign 0.86
    text _("WARNING! This episode is locked!") style "headerlocked"
    text _("""You cannot go here yet!
 
You should finish your current episode first,
before considering reading this one!
Reading Umineko out of the intended order
can lead to massive confusion and you may lose interest.""") style "desc"

### Let it be known that you have a certain limit how long a line can be.
### if you neglect that, your lines are colliding with the cover image.
### You can make your lines as long as the sentence with "Kinzo" at the end.
screen ep1():
    tag hover
    add "gui/scenario/sprites/ep1_sprite.png" yalign 0.64 xalign 0.60
    add "gui/scenario/sub.png" yalign 0.27 xalign 0.86
    add "ep1_cover" at coverzoom
    text _("Episode1 Legend of the Golden Witch") style "header"
    text _("""October 4th and 5th, 1986.
The Ushiromiya family has gathered 
on the private island of Rokkenjima 
for their annual family conference. 
Chief on the agenda concerns the struggle 
for the inheritance assets of the ailing family head, Kinzo. 
But as the family is trapped on the island by a typhoon, 
they receive a letter claiming to be 
from the rumored witch of the island, BEATRICE, 
and mysterious events begin to occur.""") style "desc"

screen ep2():
    tag hover
    add "gui/scenario/sprites/ep2_sprite.png" yalign 0.64 xalign 0.60
    add "gui/scenario/sub.png" yalign 0.27 xalign 0.86
    add "ep2_cover" at coverzoom
    text _("Episode2 Turn of the Golden Witch") style "header"
    text _("""October 4th and 5th, 1986.
 
This episode develops the confrontation 
between Battler and BEATRICE, 
who each try to disprove the other's position
regarding the existence of magic.
The conflict between them plays out 
in a higher-level plane, allowing them to oversee 
the events on the island, where the murders repeat once again 
under different circumstances.""") style "desc"

screen ep3():
    tag hover
    add "gui/scenario/sprites/ep3_sprite.png" yalign 0.64 xalign 0.60
    add "gui/scenario/sub.png" yalign 0.27 xalign 0.86
    add "ep3_cover" at coverzoom
    text _("Episode3 Banquet of the Golden Witch") style "header"
    text _("""October 4th and 5th, 1986.
 
The episode continues the battle 
between Battler and BEATRICE, 
with the events on the island having 
a special focus on Ushiromiya Eva. 
Battler's debate against magic is further 
complicated by the introduction 
of new witches and demons, and as the Ushiromiya adults 
make a serious attempt to solve the epitaph, Battler starts 
to learn more about BEATRICE's past 
and the state of the island.""") style "desc"

screen ep4():
    tag hover
    add "gui/scenario/sprites/ep4_sprite.png" yalign 0.64 xalign 0.60
    add "gui/scenario/sub.png" yalign 0.27 xalign 0.86
    add "ep4_cover" at coverzoom
    text _("Episode4 Alliance of the Golden Witch") style "header"
    text _("""The future in 1998.
 
This episode introduces Battler's sister Ange 
as a secondary protagonist, who was absent 
from the 1986 Ushiromiya family conference 
and was taken in by Eva, the only survivor 
of the Rokkenjima Mass Murders. 
The narrative shifts between the 
gameboard and the outside world, 
showing readers the impact of the incident on Ange's life 
and exploring her relationship with Maria and magic 
through Maria's diary.""") style "desc"