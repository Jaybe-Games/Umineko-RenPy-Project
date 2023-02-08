label start:

    $ chaptername = "'Ich schreibe an dich in einer Quadrillion Jahren'"
    $ chapternumber = "Prolog"
    $ songname = "-"
    stop sound fadeout 3
    stop music fadeout 3
    $ quick_menu = False
    scene black with dissolve
    pause (3)
    play sound "audio/sfx/umise_028.ogg" noloop
    show portrait3
    show text "Dieses Spiel ist reine Fiktion! Alle Ähnlichkeiten mit Dingen aus der Realität sind purer Zufall! Alle Rechte der verwendeten Assets gehen an 07th Expansion, Alchemist, Entergram und weitere rechtmäßige Rechteinhaber. Dieses Spiel ist unabhängig von der originalen Umineko Geschichte" at truecenter with dissolve
    with dissolve
    pause (10)
    hide text
    with dissolve
    hide portrait3
    with dissolve
    pause (7)
    $ songname = "At Death's Door"
    $ play_music(deaths_door)
    show text "Polizeiliche Kriminalakten zum Fall im Dorf Hinamizawa" with dissolve
    pause (5)
    hide text with fade
    pause (2)
    scene ke_s2 with dissolve
    pause (2)
    $ quick_menu = True
    $ renpy.notify("Ich schreibe an dich in einer Quadrillion Jahren")
    """
    01. Mai 1983

    An die Abteilungen 1 bis 12,

    XX Hauptquartier der Präfekturpolizei.

    Direktor-General XXX

    An den Polizeipräsidenten und alle Einrichtungsleiter.

    Zu dem Fall im Dorf Hinamizawa.

    Über den Fall im Dorf Hinamizawa wurde in einigen Massenmedien berichtet.

    Es hat weltweit Aufmerksamkeit erregt, was ernste Auswirkungen
    auf die Anwohner hat. Die Situation ist sehr ernst geworden.

    Zum Schutz des Lebens und des Wohlstands der Anwohner wurde die folgende Bekanntmachung veröffentlicht.

    1. Benennung der folgenden strafrechtlichen Ermittlung als Verschlusssache.

    Station Okinomiya 1983 Fallnummer 862
    """
    scene ke5 with dissolve
    """
    Mord an einer alleinerziehenden Mutter mit zwei Kindern im Dorf Hinamizawa (Datum: April 1983)

    Dieser Fall steht nicht mit den jährlichen Mordfällen vom Juni 1979 bis 1982 in Verbindung.

    Die Leiche einer alleinerziehenden Mutter wurde an einem Morgen
    im April 1983 tot in ihrem Haus, genauer gesagt in ihrer Küche, gefunden.

    Wir konnten nur Eines der beiden Kinder bergen, das Andere wird noch vermisst.

    Es handelt sich hierbei sehr wahrscheinlich um Kindesentführung. Die Polizei tut bereits alles,
    was in ihrer Macht steht, um das entführte Kind zu finden.

    Das geborgene Kind steht noch unter schwerem Schock und kann noch nicht reden, es wurde ins örtliche Krankenhaus gebracht und wird dort medizinisch versorgt.

    Ende der öffentlichen Bekanntmachung.

    Das Kind wurde im selben Raum mit der Leiche gefunden. An dem Kind gab es keinerlei Blutspuren oder Ähnliches.
    Es ist wahrscheinlich Zuhause gewesen, hat den Mord nicht mitbekommen, die eigene Mutter später tot aufgefunden und rief die Polizei.

    Die Küche in der die Verstorbene gefunden wurde, sah aus wie ein großes Schlachthaus.

    Als die Beamten die Leiche gefunden haben, ist ihnen aufgefallen,
    dass es so aussah, als hätte sich die Frau mit einem Strick das eigene Leben genommen.

    Dabei wurden ihr Hände und Füße abgetrennt. Laut dem Autopsiebericht wurde dafür eine Machete benutzt.

    Laut Bericht war das Blut an den Händen und Füßen schon etwas älter, da die Spuren an ihrem Hals deutlich frischer waren,
    was bedeuten könnte, dass man ihr die Gliedmaßen bei lebendigem Leib abgeschnitten hat und sie Höllenqualen erlitt.

    Außerdem gab es in dem Raum Kampfspuren. Die Frau muss den Täter gesehen und sich verteidigt haben.

    Die Frau muss aber schon vorher an dem Schock und dem immensen Blutverlust verstorben sein
    und erst danach, hat der Täter ihr den Strick angelegt, so laut dem Autopsiebericht.

    Im weiterem Bericht heißt es, dass das Opfer vorher hochprozentige Spirituosen konsumiert
    hat und während der Tat unter starken Alkoholeinfluss stand.

    Außerdem wurden bei Blutproben leichte Spuren von Tetrahydrocannabinol,
    MDMA und weiteren Rauschmitteln gefunden, die auf einen aktiven Rauschmittelmissbrauch zurückführen.

    Der Täter ist noch immer auf freiem Fuß und es gibt keine Spuren oder Hinweise, wer es gewesen sein könnte.
    Es gab bei einer Hausdurchsuchung keine versteckten Abschiedsbriefe oder Ähnliches.

    Was mir an der ganzen Sache überhaupt nicht schmeckt ist, dass das Haus komplett abgeschlossen war.

    Alle Fenster waren von innen verriegelt und die Haustür abgeschlossen, samt von innen angelegtes Kettenschloss.

    Meine Kollegen mussten diese Tür eintreten.

    Schön und gut, nur die einzigen Schlüssel, einen von der Mutter, zwei für die Kinder,
    die diese Haustür öffnen und schließen können wurden in der Küche bei der Leiche gefunden.

    Damit sind alle Drei möglichen Schlüssel für das Haus in der Küche geborgen worden.

    Da brennen mir natürlich einige Fragen auf der Zunge, auch weil das überlebende Kind
    ebenfalls in diesem Raum war, es aber an diesem keinerlei Spuren gab.

    Eine Analyse des Schlüssels ergab, dass nur das Opfer selber, diesen Schlüssel berührt hat.

    Bei einer Hausdurchsuchung ergab, dass die einzig möglichen Wege aus dem Haus, nur durch die Fenster und die Haustür führen.

    Es gab keinerlei Geheimwege oder Schlupflöcher, es wurde auch kein potenzieller Täter im und um das Haus herum gefunden,
    was den Fall zu knacken um einiges schwieriger gestaltet als ursprünglich gedacht.

    Für die Dorfbewohner werden hier sehr wahrscheinlich Teufel oder Hexen am Werk gewesen sein,
    das gestaltet die Suche nach Zeugen ebenfalls als sehr schwierig.

    Mehr konnten meine Kollegen und ich noch nicht herausfinden, damit tappen wir leider immernoch im dunkeln.
    """
    $ songname = "-"
    stop music fadeout 3
    $ quick_menu = False
    pause (0.5)
    scene black with fade
    $ songname = "Katayaku no Tori"
    $ renpy.movie_cutscene("videos/opening.mov")
    stop sound
    jump chapter1
