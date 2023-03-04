label startde:

    $ quick_menu = False
    $ chaptername = "\"Ich schreibe an dich in einer Quadrillion Jahren\""
    $ chapternumber = "Prolog"
    $ songname = "-"
    scene black with doorfade
    pause(3)
    stop sound fadeout 3
    stop music fadeout 3
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

    Generaldirektor XXX

    An den Polizeipräsidenten und alle Abteilungsleiter.

    Über den Fall im Dorf Hinamizawa.

    Über den Fall im Dorf Hinamizawa wurde in einigen Massenmedien berichtet.

    Er hat weltweit Aufmerksamkeit erregt, was schwerwiegende Auswirkungen
    auf die Bewohner hatte. Die Lage ist sehr ernst geworden.

    Um das Leben und das Wohlergehen der Anwohner zu schützen, wurde die folgende Bekanntmachung veröffentlicht.

    1. die folgenden strafrechtlichen Ermittlungen als Verschlusssache zu behandeln

    Station Okinomiya 1983 Fallnummer 862
    """
    scene ke5 with dissolve
    """
    Tötung einer alleinerziehenden Mutter mit zwei Kindern im Dorf Hinamizawa (Datum: April 1983).

    Dieser Fall steht in keinem Zusammenhang mit den jährlichen Morden vom Juni 1979 bis 1982.

    Die Leiche einer alleinerziehenden Mutter wurde an einem Morgen im April 1983
    in ihrem Haus, genauer gesagt in ihrer Küche, tot aufgefunden.

    Wir konnten nur eines der beiden Kinder bergen, das andere wird noch vermisst.

    Wahrscheinlich handelt es sich um eine Kindesentführung. Die Polizei tut bereits alles
    um das entführte Kind zu finden.

    Das geborgene Kind steht noch unter schwerem Schock und kann noch nicht sprechen, es wurde in das örtliche Krankenhaus gebracht und wird dort medizinisch versorgt.

    Ende der öffentlichen Mitteilung.

    Das Kind wurde im selben Raum wie die Leiche gefunden. Es gab keine Blutspuren oder ähnliches an dem Kind.
    Das Kind war vermutlich zu Hause, hat den Mord nicht mitbekommen, fand später seine eigene Mutter tot auf und rief die Polizei.

    Die Küche, in der die Tote gefunden wurde, sah aus wie ein großes Schlachthaus.

    Als die Beamten die Leiche fanden, fiel ihnen auf,
    dass es so aussah, als hätte sich die Frau mit einem Strick umgebracht.

    Ihre Hände und Füße waren abgetrennt. Laut Obduktionsbericht wurde dazu eine Machete benutzt.

    Dem Bericht zufolge war das Blut an Händen und Füßen schon etwas älter, da die Spuren am Hals deutlich frischer waren,
    was bedeuten könnte, dass ihr bei lebendigem Leib die Gliedmaßen abgehackt wurden und sie Höllenqualen litt.

    Außerdem gab es Kampfspuren im Raum. Die Frau muss den Täter gesehen und sich gewehrt haben.

    Sie muss aber vorher an dem Schock und dem immensen Blutverlust gestorben sein.
    und erst danach habe der Täter ihr den Strick umgelegt, so der Obduktionsbericht.

    Im weiteren Bericht heißt es, dass das Opfer zuvor hochprozentige alkoholische Getränke konsumiert hatte
    und während der Tat unter starkem Alkoholeinfluss stand.

    Außerdem wurden in Blutproben geringe Spuren von Tetrahydrocannabinol,
    MDMA und anderen Betäubungsmitteln gefunden, die auf einen aktiven Drogenmissbrauch hindeuten.

    Der Täter befindet sich nach wie vor auf freiem Fuß und es gibt keine Spuren oder Hinweise auf die Identität des Täters.
    Bei einer Hausdurchsuchung wurden keine versteckten Abschiedsbriefe oder ähnliches gefunden.

    Was mir an der ganzen Sache überhaupt nicht gefällt, ist, dass das Haus komplett verriegelt war.

    Alle Fenster waren von innen verriegelt und die Haustür war mit einem Kettenschloss von innen verschlossen.

    Meine Kollegen mussten diese Tür aufbrechen.

    Gut, nur die einzigen Schlüssel, einer für die Mutter, zwei für die Kinder,
    die diese Haustür öffnen und schließen können, wurden in der Küche bei der Leiche gefunden.

    Also alle drei möglichen Schlüssel für das Haus wurden in der Küche gefunden.

    Da brennen mir natürlich einige Fragen auf der Zunge, auch weil das überlebende Kind
    auch in diesem Raum war, es aber keine Spuren an ihm gab.

    Eine Analyse des Schlüssels ergab, dass nur das Opfer selbst diesen Schlüssel angefasst hatte.

    Eine Hausdurchsuchung ergab, dass die einzigen möglichen Wege aus dem Haus nur durch die Fenster und die Eingangstür führten.

    Es gab keine Geheimwege oder Schlupflöcher, und es wurden auch keine potentiellen Täter im und um das Haus herum gefunden,
    was die Aufklärung des Falles um einiges schwieriger machte als zunächst angenommen.

    Für die Dorfbewohner war es sehr wahrscheinlich, dass hier Teufel oder Hexen am Werk waren,
    was die Suche nach Zeugen ebenfalls sehr schwierig macht.

    Mehr konnten meine Kollegen und ich bisher nicht herausfinden, so dass wir leider immer noch im Dunkeln tappen.
    """
    $ songname = "-"
    stop music fadeout 3
    $ quick_menu = False
    pause (0.5)
    scene black with fade
    $ songname = "Katayaku no Tori"
    $ renpy.movie_cutscene("videos/opening.mov")
    stop sound
    jump chapter1de
