"""Here we have the menu screen to display all the locked
and unlocked achievements."""
screen achievement_menu():

    tag menu

    ## If you'd like to display a number and total of achievements you can use this.
    use game_menu(_("Trophäen | {:01d}/{}".format(len(persistent.my_achievements), len(achievement_name) if len(persistent.my_achievements) == len(achievement_name) else len(achievement_name) - 1)), scroll="viewport"):
    ## Else, use this.
    ## Else, use this.
    #use game_menu(_("Achievements"), scroll="viewport"):

        style_prefix "achievements"

        frame:
            background None
            padding (20, 20, 20, 20)
            align (0.0, 0.0)
            ysize 1080
            
            

            vpgrid:
                cols 2
                spacing 10
                xoffset 300

                ## Granted achievements
                for t in persistent.my_achievements:
                    if achievement.has(t.name):
                        frame:
                            background Solid('#00000067')

                            hbox:
                                yalign 0.5
                                xysize (50, 100)
                                add t.image size (100, 100) yalign 0.5

                                null width 20

                                vbox:
                                    spacing 0
                                    yfill False
                                    text t.name style 'achievements_label' color '#ffffff'
                                    text t.message color '#ffffff'

                ## Locked achievements
                for v in achievement_name.values():
                    ## Index '0' is the name of the achievement.
                    if not achievement.has(v[0]):

                        ## We're doing a check for all achievements
                        ## that is not a 'platinum'.
                        ## The platinum achievement will not appear
                        ## in the list.
                        ## Index '3' is the type of achievement.
                        #if v[3] != 'platinum':
                            frame:
                                hbox:
                                    yalign 0.5
                                    xysize (100, 100)
                                    ## This will display a locked icon.
                                    add 'gui/trophys/locked.png' size (100, 100) yalign 0.5

                                    null width 20

                                    vbox:
                                        spacing 0
                                        yfill False

                                        ## We're setting the data feedback to represent
                                        ## the None and 'hidden' achievements.
                                        if v[3] is None:
                                            ## Index '1' is the description of the achievemnt.
                                            text str(v[0]) style 'achievements_label' color '#FFF3'
                                            text str(v[1]) color '#FFF3'
                                        else:
                                            text _('Versteckte Trophäe') style 'achievements_label' color '#FFF3'


init python:

    ## These two functions are the ones that will be used
    ## to handle the list as achievements are added to it.

    def achievement_notification_show():
        ## This is to force the notification to show if
        ## the list is not empty.
        store.achievement_is_done = False
        if achievement_notification_list:
            store.achievement_notification_list.pop(0)


    def achievement_notification_done():
        ## This is to tell RenPy that the notification list
        ## is now empty and sets the variable to True.
        if not achievement_notification_list:
            store.achievement_is_done = True

    config.overlay_screens.append("achievement_notification_catcher")


    ## Here we have a funtion that is passive.
    def passive_function():
        ## This code here will grant the platinum achievement.
        if len(persistent.my_achievements) >= (len(achievement_name) - 1):
                Achievement.add(achievement_platinum)

define config.periodic_callback = passive_function

## The notification screen.
## By default, the notification will appear at the top of the screen.
## If you want to change this you'll have to amend the transform 'achievement_appear'.

default achievement_notification_list = []
default achievement_is_done = False

## This screen will catch any achievement that is in the list.
screen achievement_notification_catcher():

    if len(achievement_notification_list) > 0 and not renpy.get_screen('achievement_notification'):
        timer 1.0 repeat True:
            action [SetVariable('achievement_is_done', False), Show('achievement_notification')]

    if not achievement_is_done:
        timer 4.0 repeat True:
            action If(len(achievement_notification_list) > 0,
                    true =[Hide("achievement_notification"), Function(achievement_notification_show)],
                    false =[Function(achievement_notification_done)])

screen achievement_notification():

    zorder 100

    if achievement_notification_list:

        frame at achievement_appear:
            background Solid('#00000098')
            align (0.5, 0.0)
            padding (20, 20, 20, 20)

            hbox:
                xysize (100, 100)
                add achievement_notification_list[0].image

                null width 20

                vbox:
                    yalign 0.5
                    xminimum 340
                    xmaximum 440
                    yfill False
                    xfill False

                    text str(achievement_notification_list[0].name):
                        color '#ffffff'
                        size 25

                    text str(achievement_notification_list[0].message):
                        style 'victory_message_text'
                        size 16

style victory_message_text:
    color "#ffffff"
    size 40

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
    size 40
    outlines [(1, '#ffffff22', 0, 1)]
    yalign 0.5
    antialias True

style achievements_text:
    size 30
    yalign 0.5
    antialias True

style achievements_locked_text:
    antialias True
    color "#ffffff"
    size 25

style achievements_frame:
    background Solid('#444444')
    minimum (500, 140)
    align (0.5, 0.5)
    padding (15, 15, 15, 15)