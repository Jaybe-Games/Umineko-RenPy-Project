label start:

    $ discord.update(state = "Writing to you in a quadrillion years")
    $ discord.update(details = "Reading Prologue")
    $ chaptername = "“Ich schreibe an dich in einer Quadrillion Jahren”"
    $ chapternumber = "Prolog"
    $ songname = "-"
    window auto
    pause 2
    call showch0 from _call_showch0
    pause 2
    play sound "audio/sfx/umise_028.ogg"
    show disclaimer1 with dissolve
    pause (5)
    hide disclaimer1 with dissolve
    pause (2)
    show disclaimer2 with dissolve
    pause (1)
    play sound "audio/sfx/umise_032.ogg"
    pause (10)
    hide disclaimer2 with dissolve
    pause (2)
    $ renpy.notify("♪At Death's Door")
    $ songname = "At Death's Door"
    play music "audio/bgm/umib_014_intro.ogg"
    queue music "audio/bgm/umib_014_loop.ogg" loop 
    show text "Polizeiliche Kriminalakten zum Fall im Dorf Hinamizawa" with dissolve
    pause (5)
    hide text with fade
    pause (2)
    scene ke_s2 with dissolve
    "01. Mai 1983."
    "An die Abteilungen 1 bis 12,"
    "XX Hauptquartier der Präfekturpolizei."
    "Generaldirektor XXX"
    "An den Polizeipräsidenten und alle Abteilungsleiter."
    "Über den Fall im Dorf Hinamizawa."  
    if persistent.tip == 0:
        $ Achievement.add(achievement_bronze1)
        $ persistent.wiki_unlocked.add("wiki_hina")
        play sound "audio/sfx/umise_1060.ogg"
        $ renpy.notify("Das Tippsmenü wurde unter \"Extras\" freigeschaltet.")
        $ persistent.tip = 1
        $ persistent.tipunlocked = True
    "Über den Fall im Dorf {note_green}Hinamizawa{/note_green} wurde in einigen Massenmedien berichtet."
    "Er hat weltweit Aufmerksamkeit erregt," 
    extend " was schwerwiegende Auswirkungen auf die Bewohner hatte. Die Lage ist sehr ernst geworden."
    "Um das Leben und das Wohlergehen der Anwohner zu schützen, wurde die folgende Bekanntmachung veröffentlicht."
    "1. die folgenden strafrechtlichen Ermittlungen als Verschlusssache zu behandeln"
    "Station Okinomiya 1983 Fallnummer 862"
    scene ke5 with gradientwipeupright
    "Tötung einer alleinerziehenden Mutter mit zwei Kindern im Dorf Hinamizawa (Datum: April 1983)."
    "Dieser Fall steht in keinem Zusammenhang mit den jährlichen Morden vom Juni 1979 bis 1982."
    "Die Leiche einer alleinerziehenden Mutter wurde an einem Morgen im April 1983 in ihrem Haus, genauer gesagt in ihrer Küche, tot aufgefunden."
    "Wir konnten nur eines der beiden Kinder bergen, das andere wird noch vermisst."
    "Wahrscheinlich handelt es sich um eine Kindesentführung. Die Polizei tut bereits alles um das entführte Kind zu finden."
    "Das geborgene Kind steht noch unter schwerem Schock und kann noch nicht sprechen,"
    extend " es wurde in das örtliche Krankenhaus gebracht und wird dort medizinisch versorgt."
    "Ende der öffentlichen Mitteilung."
    "Das Kind wurde im selben Raum wie die Leiche gefunden." 
    extend " Es gab keine Blutspuren oder ähnliches an dem Kind."
    "Das Kind war vermutlich zu Hause, hat den Mord nicht mitbekommen, fand später seine eigene Mutter tot auf und rief die Polizei."
    "Die Küche, in der die Tote gefunden wurde, sah aus wie ein großes Schlachthaus."
    "Als die Beamten die Leiche fanden, fiel ihnen auf, dass es so aussah, als hätte sich die Frau mit einem Strick umgebracht."
    "Ihre Hände und Füße waren abgetrennt." 
    extend " Laut Obduktionsbericht wurde dazu eine Machete benutzt."
    "Dem Bericht zufolge war das Blut an Händen und Füßen schon etwas älter, da die Spuren am Hals deutlich frischer waren,"
    extend " was bedeuten könnte, dass ihr bei lebendigem Leib die Gliedmaßen abgehackt wurden und sie Höllenqualen litt."
    "Außerdem gab es Kampfspuren im Raum. Die Frau muss den Täter gesehen und sich gewehrt haben."
    extend " Sie muss aber vorher an dem Schock und dem immensen Blutverlust gestorben sein."
    extend " und erst danach habe der Täter ihr den Strick umgelegt, so der Obduktionsbericht."
    "Im weiteren Bericht heißt es, dass das Opfer zuvor hochprozentige alkoholische Getränke konsumiert hatte und während der Tat unter starkem Alkoholeinfluss stand."
    "Außerdem wurden in Blutproben geringe Spuren von Tetrahydrocannabinol, MDMA und anderen Betäubungsmitteln gefunden, die auf einen aktiven Drogenmissbrauch hindeuten."
    "Der Täter befindet sich nach wie vor auf freiem Fuß und es gibt keine Spuren oder Hinweise auf die Identität des Täters."
    extend " Bei einer Hausdurchsuchung wurden keine versteckten Abschiedsbriefe oder ähnliches gefunden."
    "Was mir an der ganzen Sache überhaupt nicht gefällt, ist, dass das Haus komplett verriegelt war."
    extend " Alle Fenster waren von innen verriegelt und die Haustür war mit einem Kettenschloss von innen verschlossen."
    extend " Meine Kollegen mussten diese Tür aufbrechen."
    "Gut," 
    extend " nur die einzigen Schlüssel," 
    extend " einer für die Mutter," 
    extend " zwei für die Kinder,"
    extend " die diese Haustür öffnen und schließen können, wurden in der Küche bei der Leiche gefunden."
    "Also alle drei möglichen Schlüssel für das Haus wurden in der Küche gefunden."
    "Da brennen mir natürlich einige Fragen auf der Zunge," 
    extend " auch weil das überlebende Kind auch in diesem Raum war, es aber keine Spuren an ihm gab."
    "Wie konnte der Täter in die Wohnung eindringen," 
    extend " ein grausames Blutbad anrichten und aus dem vollständig verriegelten Haus entkommen," 
    extend " ohne auch nur die geringste Spur zu hinterlassen?"
    "Eine Analyse der Schlüssel ergab," 
    extend " dass nur Mutter und Kinder selbst ihre Schlüssel angefasst haben."
    "Die weitere Hausdurchsuchung ergab," 
    extend " dass die einzigen möglichen Wege aus dem Haus nur durch die Fenster und die Eingangstür führten."
    "Es gab keine Geheimwege oder Schlupflöcher." 
    extend " Es wurden auch keine potentiellen Täter im und um das Haus herum gefunden,"
    extend " was die Aufklärung des Falles um einiges schwieriger machte als zunächst angenommen."
    "Jedenfalls ist dieser Mörder ein absolutes Genie." 
    extend " Detektive aus der ganzen Welt haben sich des Falles angenommen,"
    extend " doch niemand konnte sich erklären, wie dieser Mord begangen worden ist."
    "Für die Dorfbewohner ist das so, als ob hier Teufel oder Hexen am Werk gewesen sind,"
    extend " was die Suche nach Zeugen ebenfalls sehr schwierig macht."
    "Mehr konnten meine Kollegen und ich bisher nicht herausfinden, so dass wir leider immer noch im Dunkeln tappen."
    $ songname = "-"
    stop music fadeout 3
    pause (2)
    scene black with fade
    pause (2)
    $ songname = "Gold Dream Symphony"
    $ renpy.movie_cutscene("videos/opening.mov")
    stop sound
    pause 1.5
    jump chapter1
