
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


## DO NOT TOUCH/REUSE/CHANGE THIS AT ANY TIME!
## To clear this list use ::  achievements.purge()
default persistent.my_achievements = []
default achievements = Achievement()

init python:

    achievement.steam_position = "bottom right"

    achievement_name = {

        ## How to set up achievements
        # "achievement_key": [_("Name of Achievement"), _("Description"), '<image_path_here>', '<type>'],

        ## Note: If you decide to add/amend any achievement's data long after the game has started or
        ##       an achievement has been granted you will have to do a full reset of the game for those
        ##       changes to be reflected.

        ## Example
        "tipshunter": [_("Tippsjäger"), _("Erhalte deinen ersten Tipp."), 'gui/trophys/bronze1.png', None],
        "charhunter": [_("Charakterjäger"), _("Schalte den ersten Charakter frei."), 'gui/trophys/bronze2.png', None],
        "musichunter": [_("Musikboxjäger"), _("Schalte die Musikbox frei."), 'gui/trophys/bronze3.png', None],
        "chapter1": [_("Runter vom Boot"), _("Du hast Rokkenjima erreicht."), 'gui/trophys/bronze4.png', 'hidden'],
        "konami": [_("Konami Code"), _("War das etwa ein Nipah?"), 'gui/trophys/silver1.png', 'hidden'],
        "secret": [_("Autorentreffen"), _("Du hast den Autor gefunden."), 'gui/trophys/silver2.png', 'hidden'],
        "mainclear": [_("Eine andere Beatrice?"), _("Schließe die Hauptstory ab."), 'gui/trophys/silver3.png', 'hidden'],
        "teaclear": [_("Ayato und Yuria"), _("Schließe die Tee Party ab."), 'gui/trophys/silver4.png', 'hidden'],
        "gameclear": [_("Auferstehung der Goldenen Hexe"), _("Schließe ???? ab."), 'gui/trophys/gold1.png', 'hidden'],
        ## The None, means that the achievement will be displayed greyed-out before it is granted (or achieved).
        ## I use these words to describe the type of achievement it is;
        ##            None = default (greyed out and can see the name and description of the achievement.)
        ##        'hidden' = Achievements with this label will be displayed as hidden.
        ##      'platinum' = The final achievement to be granted once all other achievements have been granted.

        "gamemaster": [_("Platin: Gamemaster LV0"), _("Erhalte alle Trophäen!"), 'gui/trophys/platinum.png', 'platinum']

        ## More of this is explained in 'achievement_screen.rpy'.

    }

    ## Here we are simply registering the achievements.
    ## This is solely for backend use.
    for k, v in achievement_name.items():
        achievement.register(v[0])


## Here are the instances of the achievements.
## These are what will be added to the persistent
## list we made earlier.
default achievement_bronze1 = Achievement(name=achievement_name['tipshunter'][0], message=achievement_name['tipshunter'][1], image=achievement_name['tipshunter'][2])
default achievement_bronze2 = Achievement(name=achievement_name['charhunter'][0], message=achievement_name['charhunter'][1], image=achievement_name['charhunter'][2])
default achievement_bronze3 = Achievement(name=achievement_name['musichunter'][0], message=achievement_name['musichunter'][1], image=achievement_name['musichunter'][2])
default achievement_bronze4 = Achievement(name=achievement_name['chapter1'][0], message=achievement_name['chapter1'][1], image=achievement_name['chapter1'][2])
default achievement_silver1 = Achievement(name=achievement_name['konami'][0], message=achievement_name['konami'][1], image=achievement_name['konami'][2])
default achievement_silver2 = Achievement(name=achievement_name['secret'][0], message=achievement_name['secret'][1], image=achievement_name['secret'][2])
default achievement_silver3 = Achievement(name=achievement_name['mainclear'][0], message=achievement_name['mainclear'][1], image=achievement_name['mainclear'][2])
default achievement_silver4 = Achievement(name=achievement_name['teaclear'][0], message=achievement_name['teaclear'][1], image=achievement_name['teaclear'][2])
default achievement_gold1 = Achievement(name=achievement_name['gameclear'][0], message=achievement_name['gameclear'][1], image=achievement_name['gameclear'][2])
default achievement_platinum = Achievement(name=achievement_name['gamemaster'][0], message=achievement_name['gamemaster'][1], image=achievement_name['gamemaster'][2])