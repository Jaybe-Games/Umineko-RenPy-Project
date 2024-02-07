

label schule:
    $ chapter = 1000
    $ songname = "-"
    $ save_name = _("EpisodeX Illusion of the golden witch\nProlog")
    ##Prolog
    if persistent.showch == True:
        show screen showch
    $ _game_menu_screen = "cleanmenu"
    pause 3
    play sound "audio/sfx/umise_028.ogg"
    show text001
    pause 8
    hide text001 with dissolve
    pause 2
    $ songname = "Frenzy"
    play music "audio/bgm/Frenzy.mp3"
    if persistent.showbgm == True:
        show screen showsong
    show goddomain with dissolve
    pause 5
    hide goddomain with dissolve
    $ _game_menu_screen = "cleanmenu"
    vir "Eure Hoheit..."
    vir "So früh habe ich Euch hier tatsächlich nicht erwartet..."
    extend " Pu ku ku ku"
    "\"Virgilius!"
    extend " ..Hast du das Fragment vorbereitet, um das ich dich gebeten habe?"
    "Ich muss jeden Aspekt der Illusion der Goldenen Hexe genaustens kennen, damit mein Vorhaben gelingen kann\""
    vir "Aber natürlich Eure Hoheit, ich habe sehr vielversprechende Fragmente über Fräulein Beatrice zusammentragen können."
    extend " Ihr werdet euch alle Geheimnisse und tükischen Rätsel an einem Ort ansehen können."
    "\"Das hast du sehr gut gemacht, Virgilius."
    "Die Goldene Hexe Beatrice spielt in meinem neuen Spiel eine sehr wichtige Rolle."
    extend " Deswegen wäre es für mich von Vorteil, wenn ich mir eine gute Zusammenfassung ihrer Spiele ansehen kann"
    "Die dreizehn Opfer die die Inschrift der Hexe einfordert."
    extend " .....Morde die unmöglicher nicht sein können, geschlossene Räume die nicht zu brechen sind."
    "Jedes Detail über die Methoden der Hexe ist Gold wert.\""
    vir "Pu ku ku ku"
    extend " ...Wenn Ihr wollt, könnt Ihr sofort anfangen."
    vir "Das extra für Euch vorbereitete Fragment, kann jederzeit angesehen werden."
    "\"Sehr gut!"
    extend " ...Ich werde für ungefähr hundert Jahre damit beschäftigt sein, dieses Fragment zu studieren."
    extend " Aurora-san wird mich für diese Zeit die so lang ist wie ein winziger Wimpernschlag vertreten.\""
    vir "Ich werde die große Featherine-sama umgehend darüber in Kenntnis setzen."
    vir "Ich bin mir sicher, dass jemand der die Null kontrolliert wie Ihr es tut, es schon früh im ersten Durchlauf herausfinden wird."
    extend " ...Pu ku ku ku"
    $ renpy.movie_cutscene("videos/opening.mov")
    ##Kapitel 1 - Die sechs außerwählten
    $ chapter = 1001
    $ songname = "-"
    $ save_name = _("EpisodeX Illusion of the golden witch\nDie sechs außerwählten")
    if persistent.showch == True:
        show screen showch
    nat "Der Sturm hält jetzt schon seit gestern Mittag an und es von Minute zu Minute stärker..."
    nat "Genji..."
    extend " Hast du irgendwo meinen Ehemann gesehen?"
    extend " Ich habe ihn seit der Konferenz gestern nicht mehr zu gesicht bekommen."
    gen "Nein."
    extend " Leider habe ich den Herrn Krauss nicht gesehen."
    gen "Ich muss gestehen, es ist nicht nur der Herr nirgends zu sehen, sondern auch Gohda, er befindet sich nicht an seinem Arbeitsplatz."
    gen "Derweilen werden auch Rosa-sama, Kyrie-sama, Rudolf-sama und George-sama vermisst."
    nat "Es sind gleich sechs von uns spurlos verschwunden?"
    extend "Genji. Hilf mir sie zu suchen, es ist untypisch für auch nur einen von ihnen so lange weg zu sein, vorallem, wenn aufgrund des Wetters eh niemand von hier weg gehen könnte."
    gen "Wie Sie wünschen Fräulein Natsuhi."
    eva "Natsuhi!"
    extend " ...Genji!"
    nat "Guten Morgen Eva-san"
    nat "Hast du irgendwo meinen..."
    eva "Ehemann gesehen?"
    extend " ...Nein, aber ich suche meinen George..."
    nat "Ist dein Sohn auch verschwunden?"
    extend " Das kann doch gar nicht sein, wohin sollen sie denn gegangen sein?"
    nat "Was ist mit den Kindern, Eva?"
    eva "Alle bis auf George sind noch am schlafen."
    nat "Gott sei dank, ich bete dafür, dass den anderen nichts passiert ist."
    eva "George würde sich nie auf die Idee kommen, sich irgendwo zu verstecken, da ist was faul!"
    gen "Wir sollten uns draußen umsehen, bitte nehmen Sie einen Regenschirm mit, sonst holen Sie sich eine Erkältung."
    gen "Kanon."
    extend " Hast du die vermissten gefunden?"
    kan "Nein ohne Chance..."
    extend " mir ist aber etwas seltsames am Rosengartenschuppen aufgefallen, ich habe es aber nicht näher inspiziert und bin sofort hergekommen."
    gen "Gut gemacht, Kanon."
    eva "Dann los zum Gartenschuppen!"
    extend " Ich weiß zwar nicht, was George, Krauss und die anderen dort"
    nat "Es wäre besser für uns, sie so schnell wie möglich aus dem Regen zu holen."
    mar "Uu!"
    "Ist es schon morgen?"
    jes "Guten Morgen Maria!"
    jes "Huh?"
    extend " Wieso laufen die Erwachsenen draußen rum wie aufgescheuchte Hühner?"
    mar " Wie aufgescheuchte Hühner! Wie aufgescheuchte Hühner! *kicher*kicher*!"
    extend " Uu~! Uu~!"
    but "hmpff hmmmmm"
    extend " ..............Hühner? pfmmmm"
    but "Bitte lass mich noch 5 Minuten weiterschlafen..... nur noch einen winzigen Augenblick"
    jes "Aufwachen Battler-kun!"
    extend " Es ist schon Morgen!"
    but "owowow, musst du mich sofort schlagen?"
    extend " Jetzt tut mein Kopf weh, aber dafür bin ich jetzt wach."
    mar "*kicher*kicher* Kopf tut weh! Kopf tut weh!"
    extend " Uu~!!"
    jes "Maria! Bitte etwas leiser Okay?"
    but "Jo, Jessica-chan!"
    extend " Was meintest du mit aufgescheuchte Hühner?"
    jes "Die Erwachsenen sind richtig panisch durch den Rosengarten gelaufen, es sah nach was ernstem aus."
    but "Wo ist eigentlich George?"
    extend " Er ist in der Nacht aufs Klo gegangen, seit dem habe ich nichts mehr von ihm gehört."
    jes "Stimmt er fehlt, ob er bei den Erwachsenen ist?"
    but "Das könnte sein, schließlich ist er schon nahezu ein richtiger 'Erwachsener'"
    extend " ...Lass uns einfach mal nach draußen gehen."
    jes "Klingt gut, aber vergiss deinen Regenschirm nicht!"
    extend " Komm Maria, wir gehen raus!"
    mar "Uu~!"
    nat "NICHT NÄHER KOMMEN!!!"
    eva "BATTLER!!! JESSICA!!!"
    extend " NEHMT MARIA UND GEHT ZURÜCK INS GÄSTEHAUS!!!"
    extend " IHR DÜRFT NICHT NÄHER KOMMEN!"
    $ songname = "goldenslaughterer"
    if persistent.showbgm == True:
        show screen showsong
    jes "KYAAAAAAAAAAAAAAAAAA!!!!!!!!"













