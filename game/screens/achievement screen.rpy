
python early:


    class Achievement(NoRollback):
        def __init__(self, name='', image='', message='', **kwargs):
            self.name = name
            if image == '':
                ## If image is None, we will give a default image.
                self.image = Transform('gui/trophy_icon.png', fit='contain')
            else:
                self.image = Transform(image, fit='contain')
            self.message = message


        def __eq__(self, value):
            """
            Since we are using a persistent list we need to do an equality
            check.
            Below we are simply checking 'self.name == value.name, self.message == value.message'
            """
            return all((self.name == value.name, self.message == value.message))

        def add(trophy):
            """
            Add/Grant Trophies/Achievements to the list.
            As a standard python expression  ::  Achievement.add( <trophy> )
            As a screen action  ::  Function( Achievement.add, <trophy> )
            """
            if not achievement.has(trophy.name):
                achievement.grant(trophy.name)
                store.achievement_notification_list.append(trophy)

            if trophy not in persistent.my_achievements:
                ## New acheievements will appear first in the list.
                persistent.my_achievements.insert(0, trophy)

        def purge(self):
            """
            This will clear the achievements AND persistent list.
            """
            achievement.clear_all()
            persistent.my_achievements.clear()

default persistent.my_achievements = []
default achievements = Achievement()

init python:

    achievement.steam_position = "bottom right"

    achievement_name = {
        # Legend of the Golden Witch Trophys goes here
        "tipshunterep1": [_("Legend: Tipshunter"), _("Get a tip in Episode1"), 'gui/trophys/bronze1.png', 'hidden'],
        "charhunterep1": [_("Legend: Characterhunter"), _("Unlock a character in Episode1"), 'gui/trophys/bronze2.png', 'hidden'],
        "tipshunterep2": [_("Turn: Tipshunter"), _("Get a tip in Episode2"), 'gui/trophys/bronze1.png', 'hidden'],
        "charhunterep2": [_("Turn: Characterhunter"), _("Unlock a character in Episode2"), 'gui/trophys/bronze2.png', 'hidden'],
        "tipshunterep3": [_("Banquet: Tipshunter"), _("Get a tip in Episode3"), 'gui/trophys/bronze1.png', 'hidden'],
        "charhunterep3": [_("Banquet: Characterhunter"), _("Unlock a character in Episode3"), 'gui/trophys/bronze2.png', 'hidden'],
        "tipshunterep4": [_("Alliance: Tipshunter"), _("Get a tip in Episode4"), 'gui/trophys/bronze1.png', 'hidden'],
        "charhunterep4": [_("Alliance: Characterhunter"), _("Unlock a character in Episode4"), 'gui/trophys/bronze2.png', 'hidden'],
        "gonnafall": [_("Off the boat"), _("You reached Rokkenjima!"), 'gui/trophys/bronze4.png', 'hidden'],
        "ep1": [_("Legend of the Golden Witch"), _("Complete Episode1"), 'gui/trophys/bronze1.png', None],
        "ep2": [_("Turn of the Golden Witch"), _("Complete Episode2"), 'gui/trophys/bronze1.png', None],
        "ep3": [_("Banquet of the Golden Witch"), _("Complete Episode3"), 'gui/trophys/bronze1.png', None],
        "ep4": [_("Alliance of the Golden Witch"), _("Complete Episode4"), 'gui/trophys/bronze1.png', None],
        "gamemaster": [_("Gamemaster"), _("Unlock every single trophy!"), 'gui/trophys/platinum.png', 'platinum']

    }

    for k, v in achievement_name.items():
        achievement.register(v[0])
## I'll take the chance and spam some useless trophies here you can collect by simply skipping through the entire game.
default achievement_tipep1 = Achievement(name=achievement_name['tipshunterep1'][0], message=achievement_name['tipshunterep1'][1], image=achievement_name['tipshunterep1'][2])
default achievement_charep1 = Achievement(name=achievement_name['charhunterep1'][0], message=achievement_name['charhunterep1'][1], image=achievement_name['charhunterep1'][2])
default achievement_tipep2 = Achievement(name=achievement_name['tipshunterep1'][0], message=achievement_name['tipshunterep1'][1], image=achievement_name['tipshunterep1'][2])
default achievement_charep2 = Achievement(name=achievement_name['charhunterep1'][0], message=achievement_name['charhunterep1'][1], image=achievement_name['charhunterep1'][2])
default achievement_tipep3 = Achievement(name=achievement_name['tipshunterep1'][0], message=achievement_name['tipshunterep1'][1], image=achievement_name['tipshunterep1'][2])
default achievement_charep3 = Achievement(name=achievement_name['charhunterep1'][0], message=achievement_name['charhunterep1'][1], image=achievement_name['charhunterep1'][2])
default achievement_tipep4 = Achievement(name=achievement_name['tipshunterep1'][0], message=achievement_name['tipshunterep1'][1], image=achievement_name['tipshunterep1'][2])
default achievement_charep4 = Achievement(name=achievement_name['charhunterep1'][0], message=achievement_name['charhunterep1'][1], image=achievement_name['charhunterep1'][2])
default achievement_ep1_1 = Achievement(name=achievement_name['gonnafall'][0], message=achievement_name['gonnafall'][1], image=achievement_name['gonnafall'][2])
default achievement_ep1 = Achievement(name=achievement_name['ep1'][0], message=achievement_name['ep1'][1], image=achievement_name['ep1'][2])
default achievement_ep2 = Achievement(name=achievement_name['ep1'][0], message=achievement_name['ep1'][1], image=achievement_name['ep1'][2])
default achievement_ep3 = Achievement(name=achievement_name['ep1'][0], message=achievement_name['ep1'][1], image=achievement_name['ep1'][2])
default achievement_ep4 = Achievement(name=achievement_name['ep1'][0], message=achievement_name['ep1'][1], image=achievement_name['ep1'][2])
default achievement_platinum = Achievement(name=achievement_name['gamemaster'][0], message=achievement_name['gamemaster'][1], image=achievement_name['gamemaster'][2])

screen achievement_menu(scroll="viewport"):

    tag menu
    modal True
    if main_menu:
        add "gui/trophys/bg.png"
    add "gui/bgdark.png" at center
    text _("Trophies") outlines [ (absolute(4), "#00000094", absolute(1), absolute(1)) ] size 90 font "fonts/Georgia.ttf" xalign 0.5 yalign 0.03 
    add "gui/trophys/background.png" at center
    if main_menu:
        imagebutton auto "images/system/back2_%s.png" action Return() activate_sound "audio/sys/sysse_cancel.wav" hover_sound "audio/sys/sysse_move.wav" yalign 0.02 xalign 0.97
    else:
        imagebutton auto "images/system/back2_%s.png" action [ShowMenu("game_menu"), Hide("achievement_menu")] activate_sound "audio/sys/sysse_cancel.wav" hover_sound "audio/sys/sysse_move.wav" yalign 0.02 xalign 0.97
    add partObj

    style_prefix "achievements"

    text _("Unlocked | {:01d}/{}".format(len(persistent.my_achievements), len(achievement_name) if len(persistent.my_achievements) == len(achievement_name) else len(achievement_name) - 1)) yalign 0.1 xalign 0.1 size 50 outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]
    ### Getting things right was a pain in the ass, you can suck my twig and berries before I tell you a thing here
    ### Of course the code itself has comments but what I did to make it look good is a secret :)
    frame:
        background None
        padding (20, 20, 20, 20)
        #align (0.0, 0.0)
        ysize 1000
        ymargin 150
        yalign 0.5
        yoffset 60     

        vpgrid:
            cols 3
            spacing 15
            xalign 0.5
            yalign 0.7
            scrollbars "vertical"
            mousewheel True
            draggable True

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
                                        text _('Hidden Trophy') style 'achievements_label' color '#FFF3'


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
            align (1.0, 0.0)
            padding (20, 20, 200, 20)

            hbox:
                xysize (300, 100)
                add achievement_notification_list[0].image

                null width 20

                vbox:
                    yalign 0.5
                    xminimum 700
                    xmaximum 900
                    yfill False
                    xfill False

                    text str(achievement_notification_list[0].name):
                        color '#ffffff'
                        size 50

                    text str(achievement_notification_list[0].message):
                        style 'victory_message_text'
                        size 40