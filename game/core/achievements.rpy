
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
        "tipshunter": [_("Tippsjäger"), _("Erhalte deinen ersten Tipp"), 'gui/trophys/bronze1.png', None],
        "charhunter": [_("Charakterjäger"), _("Schalte den ersten Charakter frei"), 'gui/trophys/bronze2.png', None],
        "musichunter": [_("Musikboxjäger"), _("Schalte die Musikbox frei"), 'gui/trophys/bronze3.png', None],
        "chapter1": [_("Runter vom Boot"), _("Du hast Rokkenjima erreicht"), 'gui/trophys/bronze4.png', 'hidden'],
        "rules": [_("Kenner der Spielregeln"), _("Rokkenjimas Spielregeln erlernt"), 'gui/trophys/bronze5.png', 'hidden'],
        "ayato": [_("Das hat jemand überlebt?"), _("Ayato vor dem sterben bewahrt"), 'gui/trophys/bronze6.png', 'hidden'],
        "letter": [_("Post ist da!"), _("Einen seltsamen Brief von Beatrice erhalten"), 'gui/trophys/bronze7.png', 'hidden'],
        "midnight": [_("05. Oktober"), _("Wer hat die Nacht wohl überlebt?"), 'gui/trophys/bronze8.png', 'hidden'],
        "fight": [_("Wortgefecht"), _("Du hast dir mit Beatrice einen Kampf des Intellekts geliefert"), 'gui/trophys/bronze9.png', 'hidden'],
        "wedding": [_("Bis der Tod euch scheidet"), _("An der 'Hochzeit' teilgenommen"), 'gui/trophys/bronze10.png', 'hidden'],
        "separate": [_("Trennung"), _("In zwei Gruppen aufgeteilt"), 'gui/trophys/bronze11.png', 'hidden'],
        "accused": [_("Angeklagt"), _("Werde vom Senat der Hexen angeklagt"), 'gui/trophys/bronze12.png', 'hidden'],
        "family": [_("Familienprobleme"), _("Die eigene Mutter.... Wie grausam...."), 'gui/trophys/bronze13.png', 'hidden'],
        "panic": [_("Den Spiegel durchbrechen"), _("Dein anderes Ich ist entkommen!"), 'gui/trophys/bronze14.png', 'hidden'],
        "lllusions": [_("Illusionen zu Illusionen"), _("Die Illusion der Falschen Hexe gebrochen"), 'gui/trophys/bronze15.png', 'hidden'],
        "final": [_("Ich bin der pragmatische Teil!"), _("Wieder eins geworden!"), 'gui/trophys/bronze16.png', 'hidden'],
        "charcollector": [_("Charaktersammler"), _("Schalte alle Charaktere frei"), 'gui/trophys/silver1.png', 'hidden'],
        "secret": [_("Autorentreffen"), _("Du hast den Autor gefunden"), 'gui/trophys/silver2.png', 'hidden'],
        "tipscollector": [_("Tippsfanatiker"), _("Erhalte alle Tipps und Grimoireeinträge"), 'gui/trophys/silver3.png', 'hidden'],
        "mainclear": [_("Der Sieger des Spiels ist..."), _("Schließe Episode 0 ab"), 'gui/trophys/silver4.png', None],
        "teaclear": [_("Eins zu einer Quadrillion"), _("Schließe die Tee Party ab"), 'gui/trophys/silver5.png', None],
        "gameclear": [_("Auferstehung der Goldenen Hexe"), _("Schließe ???? ab"), 'gui/trophys/gold1.png', None],
        "bonusclear": [_("Verbotene Erinnerungen"), _("Schließe alle Bonuskapitel ab"), 'gui/trophys/gold2.png', 'hidden'],
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
default achievement_silver1 = Achievement(name=achievement_name['charcollector'][0], message=achievement_name['charcollector'][1], image=achievement_name['charcollector'][2])
default achievement_silver2 = Achievement(name=achievement_name['secret'][0], message=achievement_name['secret'][1], image=achievement_name['secret'][2])
default achievement_silver3 = Achievement(name=achievement_name['mainclear'][0], message=achievement_name['mainclear'][1], image=achievement_name['mainclear'][2])
default achievement_silver4 = Achievement(name=achievement_name['teaclear'][0], message=achievement_name['teaclear'][1], image=achievement_name['teaclear'][2])
default achievement_gold1 = Achievement(name=achievement_name['gameclear'][0], message=achievement_name['gameclear'][1], image=achievement_name['gameclear'][2])
default achievement_platinum = Achievement(name=achievement_name['gamemaster'][0], message=achievement_name['gamemaster'][1], image=achievement_name['gamemaster'][2])