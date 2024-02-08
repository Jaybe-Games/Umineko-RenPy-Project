

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
    eva "Hideyoshi und Shannon sind in der nähe der Kapelle auf die Suche gegangen."
    extend " ...Ich hoffe sie werden schnell gefunden."
    gen "Wir sollten uns ebenfalls draußen umsehen, bitte nehmen Sie einen Regenschirm mit, sonst holen Sie sich eine Erkältung."
    gen "Kanon."
    extend " Was ist hier los?"
    kan "Ich weiß es nicht, Genji-sama..."
    extend " ......Es fehlen exakt Sechs leute."
    extend " Vielleicht war es ja die Hexe...."
    eva "Red nicht so einen unsinn, geh lieber weiter suchen, als in so einem Moment an ein dummes Ammenmärchen zu denken."
    kan "Ich bitte um Verzeihung, Eva-sama, das war taktlos von mir..."
    extend " mir ist aber etwas seltsames am Rosengartenschuppen aufgefallen, ich habe es aber nicht näher inspiziert und bin sofort hergekommen."
    gen "Wir werden es uns ansehen. Danke, Kanon."
    eva "Dann los zum Gartenschuppen!"
    extend " Ich weiß zwar nicht, was George, Krauss und die anderen dort vorhaben, aber es ist unsere einzige Spur."
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
    jes "Maria! Bitte etwas leiser, Okay?"
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
    nat "Genji! Ruf sofort die Polizei!"
    gen "Wie Ihr wünscht, es wird sofort erledigt!"
    extend " Kanon..."
    extend " Erstatte den werten Herrn Kinzo-sama umgehend Bericht!"
    kan "Ich habe verstanden!"
    kum "Was ist hier los?"
    extend " Warum sind denn alle hier versammelt?"
    nat "Kumasawa! Das musst du nicht sehen! Bring Battler und Jessica zurück ins Gästehaus!"
    kum "Ohohohoho, wir sollten dann wohl besser gehen."
    extend " Battler-sama, Jessica-sama, folgt mir bitte."
    jes "Battler-kun! Geh bitte nicht rein!"
    but "Das darf doch wohl nicht wahr sein?!!?!?"
    extend " Welches Grausame Monster könnte so etwas tun?"
    but "Ja ich seh es klar und deutlich, oh man was für eine Schande."
    extend " Ich weiß, dass du ein Womanizer und ein ziemliches Arschloch warst..."
    but "Aber dass man dich tötet und dein Gesicht auf grausamste Art und Weise verunstaltet, hats selbst du nicht verdient."
    extend " Würde er seine Kleidung nicht tragen, dann wüsste ich noch nicht einmal wer hier vor mir liegt."
    but "Das ist einfach viel zu viel, wieso ist das passiert?"
    extend " ICH VERSTEH ES NICHT!!!"
    but "Warum nur? Warum nur? Warum nur?"
    extend " Wer... liegt.. da... neben.. dir...??"
    extend " Nein!!! Nein!!! Kyrie-san!!!"
    but "Wieso auch noch du?"
    extend " Ich habe dich zwar nie für meine neue Mutter gehalten, aber sowas ist doch übertrieben!"
    extend " Nie im Leben hätte ich mir für einen von euch so ein Ende gewünscht."
    but "Klar sagt man mal aus Wut, dass man jemanden tot sehen will, aber sie dann wirklich tot zu sehen, verkrafte ich nicht..."
    but "Dad, Kyrie, Gohda, Tante Rosa und wieso auch du George?"
    extend "Ich versteh nichts mehr, es ist einfach nicht fair!"
    extend " Niemand von euch hat es verdient, dass man euer Gesicht nicht mehr erkennen kann...."
    but "Es wäre viel einfacher gewesen, euch einfach nur ins Jenseits zu schicken und hier rein zu legen..."
    extend " War das wirklich nötig? Macht es das wirklich besser?"
    hid "bleib stark Battler-kun, die Polizei wird Morgen den Täter finden und verhaften."
    extend " ich bin genauso traurig wie du, aber wir dürfen jetzt keine falsche Bewegung machen."
    eva "GEORGE!!!! WAS HABEN SIE DIR ANGETAN!!"
    extend " ahhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh!!!!!!!!!!!!"
    eva "WARUM NUR MEIN GEORGE???!!?!??!"
    eva "Es wäre besser diesen Ort der Polizei zu überlassen."
    extend " Wenn wir auch nur etwas näher kommen, könnte es die Ermittlungen beeinträchtigen."















