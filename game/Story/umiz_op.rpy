label umiz_op:
    pause 3
    ##Kapitel 0 - Eröffnung
    $ chapter = "Eröffnung"
    $ songname = "-"
    $ save_name = _("Episode0 Resurrection of the golden witch\nEröffnung")
    show screen showch
    pause 3
    play sound umise_028
    show text001
    pause 8
    hide text001 with dissolve
    pause 2
    play wind umilse_005
    play rain umilse_012
    pause 2
    show text _("Jaybe Games Präsentiert") with dissolve
    pause 7
    hide text with dissolve
    show text _("Umineko: When They Cry Zero") with dissolve
    pause 7
    hide text with dissolve
    show text _("~Waltz of Reflections and Delusions~") with dissolve
    pause 7
    hide text with dissolve
    scene fure2 with gradientcirclefade
    pause 2
    scene kakera with gradientcirclefade
    pause 2
    window show
    $ _game_menu_screen = "cleanmenu"
    "Der Regen, der heute auf die Insel niederprasselt, fühlt sich so an, als würde mir jeder einzelne Tropfen, etwas mitteilen wollen."
    extend " Selbst wenn es heute nicht regnen würde, würde ich dieses seltsame Gefühl nicht los werden."
    "Heute sind die werten Gäste Ushiromiya Rudolf, Eva und Rosa angereist."
    extend " Als ich meine Pflichten als Bedienstete nachging und ein Teeset vorbereitet habe, hörte ich durch den Türspalt, wie sich die Gäste im Wohnzimmer unterhielten."
    rud "Hast du das neulich mitbekommen?"
    cla "Du meinst, der große Vorfall, der letztens in der Zeitung stand?"
    extend " Ich seh zwar nicht so aus, aber ich lasse mir extra Zeitung auf die Insel liefern."
    eva "Reden wir hier etwa von dem grausamen Mord mit dem verschlossenen Haus?"
    extend " Das klingt für mich eher wie eine Story aus einem Buch von Agatha Christie."
    extend " *kicher*"
    ros "Natsuhi..."
    extend " Hast du zufälligerweise deine Kopfschmerztabletten hier?"
    extend " Seit ein paar Tagen, habe ich diese furchtbaren Kopfschmerzen."
    nat "Ja, habe ich, ich kann dir gleich welche geben, meine Kopfschmerzen sind ebenfalls nicht mehr aushaltbar und ich habe diese seit Jessicas geburt."
    ros "Dankeschön, Natsuhi. Ich wusste, ich kann mich da auf dich verlassen."
    extend " Was anderes: Was ist das für ein Vorfall gewesen?"
    cla "In einem Dorf im Bezirk Shishibone, wurde eine alleinerziehende Mutter ermordet."
    extend " Sie wurde erhangen und ohne Gliedmaßen von ihrem Sohn in ihrer Küche gefunden."
    rud "Sie hatte noch eine Tochter, die wurde wohl vom Mörder entführt."
    eva "Der Sohn von ihr wurde in psychologischer Behandlung gebracht und stet noch heute immer einem enormen Schock."
    cla "Das interessanteste an diesem Vorfall ist allerdings, dass das Haus komplett mit einer Türkette verriegelt war, als die Polizei eintraf."
    extend " Eine Hausdurchsuchung hat keine Geheimgänge oder offene Fenster gefunden."
    cla "Das ist fast so wie in eins dieser Kriminalromane."
    eva "Zumindestens ist dass, das, was die Polizei veröffentlicht hat."
    extend " Man könnte davon ausgehen, dass noch mehr dahinter steckt."
    ros "Das klingt ja schrecklich, wer könnte nur so etwas tun?"
    rud "Wenn diese Kinder in unserer toxischen Familie gewesen wären, dann wären beide in psychologischer Behandlung gelandet."
    eva "Dafür hätte doch auch ein Tag mit dir alleine gereicht..."
    extend " Hmm..?" 
    extend " nicht wahr Rudolf?"
    rud "In dem Alter sollte man es mit der Bosheit lieber ruhiger angehen lassen, sonst kommt der alte Freund \"Karma, der Herzkasper\"."
    eva "Hey... Ich bin immer noch ziemlich fit..." 
    extend " ich betreibe Kampfsport und hätte kein Problem damit, es mal bei dir einzusetzen."
    rud "Eine Frau in ihren fünfzigern, sollte lieber mal die Gelenke schonen."
    "Plötzlich geht die Tür auf und ein Schubwagen voller frisch zubereiteten Tee angeschoben, von einer jungen Bediensteten fährt in den Raum."
    sha "Entschuldigen Sie..."
    extend " I.. Ich habe etwas Tee für Sie zubereitet."
    cla "Dankeschön Shannon."
    extend " Sei so gut und schenke jedem hier eine Tasse ein."
    nat "Welche Teesorte ist das?"
    sha "E.. Earl Gray, Fräulein Natsuhi."
    "Shannon schenkte jedem eine Tasse Tee ein und das Earl Gray fand sofort bei jedem Anklang."
    eva "Es beruhigt die Seele, ich sollte es mal versuchen, vor meinem Training zu trinken."
    rud "Nah.. Du solltest lieber nur den Tee trinken, damit du nicht mehr so aufbrausend bist."
    eva "Wie war das?...."
    sha "Wenn Sie mich jetzt entschuldigen würden..."
    "Shannon nahm die Schubkarre und fuhr wieder hinaus."
    extend " Dieses beklemmende Gefühl, nahm bei diesem Gespräch immer weiter zu."
    "Dieses Gefühl erdrückt mich und wird von Tag zu Tag stärker..."
    extend " Auf der anderen Seite, fühlt es sich auch so vertraut an, als ob es schon mein ganzes Leben ein Teil von mir gewesen ist."
    "Es ist so, als ob vor einigen Tagen auf der Insel etwas sehr mächtiges erwacht wäre."
    "Falsch..."
    extend " Es ist nicht erwacht...."
    extend " Es ist zurückgekehrt...."
    window hide
    $ songname = "-"
    stop music fadeout 3
    pause (2)
    scene black with fade
    pause (2)
    $ songname = "Umineko no Naku Koro ni"
    $ renpy.movie_cutscene("videos/opening.mov")
    stop sound
    pause 1.5
    jump umiz_1