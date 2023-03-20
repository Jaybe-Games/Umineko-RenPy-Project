
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
        "tipshunter": [_("Bronze: Tippsjäger"), _("Erhalte deinen ersten Tipp"), 'gui/bronze.png', 'hidden'],
        "charhunter": [_("Bronze: Charakterjäger"), _("Schalte den ersten Charakter frei."), 'gui/bronze.png', 'hidden'],
        "chapter1": [_("Bronze: Runter vom Boot"), _("Du hast Rokkenjima erreicht."), 'gui/bronze.png', 'hidden'],
        "malocher": [_("Bronze: Ein guter Tüftler"), _("Öffne die Einstellungen."), 'gui/bronze.png', None],
        "tip": [_("Bronze: Ratschlag gefällig?"), _("Öffne die Tipps."), 'gui/bronze.png', None],
        "char": [_("Bronze: Wer war das nochmal?"), _("Öffne das Charaktermenü."), 'gui/bronze.png', None],
        "help": [_("Bronze: Gibt's Probleme?"), _("Öffne das Hilfemenü."), 'gui/bronze.png', None],
        "konami": [_("Silber: Konami Code"), _("War das etwa ein Nipah?"), 'gui/silver.png', 'hidden'],
        "musicbox": [_("Silber: Musikbox"), _("Du hast die Musikbox geöffnet."), 'gui/silver.png', 'hidden'],
        "mainclear": [_("Silber: Eine andere Beatrice?"), _("Der Täter hat sich gezeigt."), 'gui/silver.png', 'hidden'],
        "teaclear": [_("Silber: Ayato und Yuria"), _("Du hast das Geheimnis des Urfragments erfahren."), 'gui/silver.png', 'hidden'],
        "gameclear": [_("Gold: Resurrection of the Golden Witch"), _("Du hast Umineko Zero abgeschlossen."), 'gui/gold.png', None],
        "secret": [_("Silber: Streng geheim"), _("Du hast das Geheimnis im Hauptmenü gefunden."), 'gui/silver.png', 'hidden'],
        ## The None, means that the achievement will be displayed greyed-out before it is granted (or achieved).
        ## I use these words to describe the type of achievement it is;
        ##            None = default (greyed out and can see the name and description of the achievement.)
        ##        'hidden' = Achievements with this label will be displayed as hidden.
        ##      'platinum' = The final achievement to be granted once all other achievements have been granted.

        "gamemaster": [_("Platin: Gamemaster LV0"), _("Erhalte alle Trophäen!"), 'gui/platinum.png', 'platinum']

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
default achievement_bronze3 = Achievement(name=achievement_name['char'][0], message=achievement_name['char'][1], image=achievement_name['char'][2])
default achievement_bronze4 = Achievement(name=achievement_name['tip'][0], message=achievement_name['tip'][1], image=achievement_name['tip'][2])
default achievement_bronze5 = Achievement(name=achievement_name['malocher'][0], message=achievement_name['malocher'][1], image=achievement_name['malocher'][2])
default achievement_bronze6 = Achievement(name=achievement_name['help'][0], message=achievement_name['help'][1], image=achievement_name['help'][2])
default achievement_bronze10 = Achievement(name=achievement_name['chapter1'][0], message=achievement_name['chapter1'][1], image=achievement_name['chapter1'][2])
default achievement_silver1 = Achievement(name=achievement_name['konami'][0], message=achievement_name['konami'][1], image=achievement_name['konami'][2])
default achievement_silver2 = Achievement(name=achievement_name['mainclear'][0], message=achievement_name['mainclear'][1], image=achievement_name['mainclear'][2])
default achievement_silver3 = Achievement(name=achievement_name['teaclear'][0], message=achievement_name['teaclear'][1], image=achievement_name['teaclear'][2])
default achievement_silver4 = Achievement(name=achievement_name['musicbox'][0], message=achievement_name['musicbox'][1], image=achievement_name['musicbox'][2])
default achievement_silver5 = Achievement(name=achievement_name['secret'][0], message=achievement_name['secret'][1], image=achievement_name['secret'][2])
default achievement_gold1 = Achievement(name=achievement_name['gameclear'][0], message=achievement_name['gameclear'][1], image=achievement_name['gameclear'][2])
default achievement_platinum = Achievement(name=achievement_name['gamemaster'][0], message=achievement_name['gamemaster'][1], image=achievement_name['gamemaster'][2])