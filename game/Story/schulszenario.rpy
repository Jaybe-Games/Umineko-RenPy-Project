label school:
    ##Kapitel 1 - Die sechs außerwählten
    $ chapter = "Die sechs außerwählten"
    $ songname = "-"
    $ save_name = _("EpisodeX Illusion of the golden witch\nDie sechs außerwählten")
    ##Prolog
    show screen showch
    $ _game_menu_screen = "cleanmenu"
    pause 3
    play sound umise_028
    show text001
    pause 8
    hide text001 with dissolve
    pause 2
    play wind umilse_005
    play rain umilse_012
    pause 2
    show oct_5_1986 with fastdissolve
    pause 5
    hide oct_5_1986 with fastdissolve
    pause 1
    show m_o1a 
    show rainbackscroll
    show rainfrontscroll
    with gradientcirclefade
    window auto
    "Die Insel Rokkenjima war am Vortag von einem schweren Taifun getroffen worden."
    extend " Wind, der sich anfühlt, als würde er einem die Luft aus den Lungen peitschen."
    extend " Starker Regen, der wie das gleichmäßige, aber relativ heftige Klopfen eines Masseurs auf der Haut spürbar wird."
    window hide
    stop wind fadeout 2.0
    scene mhal_2cr at bgani
    show expression(CustomParticles("images/system/particle.png", 10))
    with gradientcirclefade
    $ songname = "White Shadow"
    show screen showsong
    play music umib_009
    show nat a43headache1 at m
    pause 0.5
    window auto
    nat "Meine Kopfschmerzen sind seit gestern Abend deutlich schlimmer geworden."
    extend " Es gibt nicht einen Tag an dem mein Kopf nicht schrecklich weh tut."
    extend " Ob es auch mit am Wetter liegt?"
    nat "Der Sturm hält nun schon seit gestern Mittag an und wird von Minute zu Minute stärker..."
    nat a11komaru1 "Genji..."
    extend " Hast du meinen Mann irgendwo gesehen?"
    extend " Ich habe ihn seit der gestrigen Konferenz nicht mehr gesehen."
    show nat a11komaru1 at l
    show gen a11defo1 at r 
    with fastdissolve
    gen "Nein."
    extend " Leider habe ich Herrn Krauss nicht gesehen."
    gen "Ich muss gestehen, nicht nur Krauss-sama ist nirgends zu sehen, auch Gohda ist nicht an seinem Arbeitsplatz."
    gen "Inzwischen sind auch Rosa-sama, Kyrie-sama und Rudolf-sama verschwunden."
    nat a12nayamu1 "Fünf von uns sind spurlos verschwunden?"
    extend " Genji. Hilf mir, sie zu finden, es ist ungewöhnlich, dass auch nur einer von ihnen so lange weg ist, vor allem, wenn wegen des Wetters sowieso niemand von hier weggehen kann."
    gen a11komaru1 "Wie Sie wünschen."
    window hide
    scene black with quickgradientwipedown
    "Der Bedienstete und Natsuhi stellten die ganze Villa auf den Kopf, aber von den Vermissten fehlte jede Spur."
    "Als die beiden in die Eingangshalle zurückkehrten, lief ihnen ein bekanntes Gesicht entgegen."
    show mhal_1ar_bg at bgani
    show rainbackscroll
    show rainfrontscroll
    show mhal_1ar at bgani
    show expression(CustomParticles("images/system/particle.png", 10))
    with quickgradientwipedown
    show eva b23komaru2 at r
    pause 0.5
    window auto
    eva "Natsuhi!"
    extend " ...Genji!"
    show nat a11komaru1 at l
    nat "Guten Morgen Eva-san"
    nat "Hast du irgendwo meinen..."
    eva "Mann gesehen?"
    extend " ...Nein. Aber ich bin auf der Suche nach meinem George..."
    nat a12nayamu1 "Ist dein Sohn auch verschwunden?"
    extend " Das kann nicht sein. Wo sind sie hin?"
    nat "Was ist mit den Kindern passiert, Eva?"
    eva "Alle außer George schlafen noch."
    nat a11komaru1 "Gott sei Dank, ich bete, dass den anderen nichts passiert ist."
    eva b25komaru4 "George käme nie auf die Idee, sich irgendwo zu verstecken, da ist was faul!"
    eva "Hideyoshi und Shannon suchen in der Nähe der Kapelle."
    extend " ...Ich hoffe, sie werden schnell gefunden."
    nat a12defo1 "Wir sollten uns ebenfalls draußen umsehen, hier im Haus ist niemand."
    eva b21akire1go "Gute Idee."
    extend " Genji..."
    extend " Bring uns Regenschirme, auch einen für dich."
    show gen a11defo1 at m
    gen "Wie Sie wünschen"
    show gen a11komaru1 at m
    "In diesem Moment wurde die Villa von zwei weiteren Leuten betreten." 
    extend " Ein Arzt mit leichtem Übergewicht, der sich jetzt in seinem Ruhestand befindet."
    "Dazu ein sehr ruhiger Bediensteter, der immer konzentriert wirkt und dessen Präsenz nahezu unsichtbar ist."
    gen "Kanon, Dr. Nanjo-sensei"
    extend " Was ist hier los?"
    scene mhal_1ar_bg at bgani
    show rainbackscroll
    show rainfrontscroll
    show mhal_1ar at bgani
    show expression(CustomParticles("images/system/particle.png", 10))
    show kan a11defo1 at m
    with quickgradientwipeleft
    kan "Ich weiß es nicht, Genji-sama..."
    extend " ......Es fehlen genau sechs Personen."
    extend " Vielleicht war es ja die Hexe...."
    show eva b25komaru4 at l
    eva "Rede nicht so einen Unsinn, geh lieber weiter auf die Suche, als in so einem Moment an ein dummes Ammenmärchen zu denken."
    kan a13defo2 "Das war taktlos von mir, ich bitte um Verzeihung, Eva-sama..."
    scene mhal_1ar_bg at bgani
    show rainbackscroll
    show rainfrontscroll
    show mhal_1ar at bgani
    show expression(CustomParticles("images/system/particle.png", 10))
    show nan a1defo1 at m
    with quickgradientwipeleft
    nan "Werte Natsuhi-san und Eva-san."
    extend " Ich bin bei Ihnen, für den Fall, dass jemand zu Schaden gekommen ist."
    extend " ...Hoffen wir, dass es allen gut geht."
    hide nan
    show nat a11ikari1 at m
    with fastdissolve
    nat "Wir müssen sie schnellstmöglich aus dem Regen holen."
    window hide
    pause 2
    $ songname = "-"
    stop music fadeout 2.0
    play wind umilse_005
    scene black with quickergradientwiperight
    window show
    "Durch einem erbarmungslosen Sturm machten sich alle auf den Weg in den Rosengarten."
    window hide
    scene rose_1ar
    show rainbackscroll
    show rainfrontscroll
    with gradientwipedownleft
    window show
    "Kanon schien irgendetwas aufgefallen zu sein, denn er blieb stehen und zeigte leise mit dem Finger in Richtung eines alten Gartenschuppens."
    "Auffällig ist, dass aus Richtung des Schuppens ein seltsamer Rotstich zu sehen ist, der Kanon ins Auge gefallen sein muss."
    "Der Gartenschuppen ist sehr gut versteckt, es ist schwer zu erkennen, wenn man durch den Garten läuft."
    "Schließlich soll es nur die nötigen Gartenwerkzeuge lagern und nicht den schönen Anblick der Rosen ruinieren."
    "Da allerdings Kanon für den Rosengarten verantwortlich ist, weiß er genau, dass dort ein Schuppen ist."
    window hide
    pause 1.5
    scene warehous_o1an
    show rainbackscroll
    show rainfrontscroll
    with gradientwipedownleft
    pause 2
    show nat a32ikari1 behind rainfrontscroll at m
    pause 0.5
    window auto
    nat "Was zum Geier ist das denn?"
    extend " Wer denkt sich bitte so einen schlechten Scherz aus?"
    nat "Was hat das alles zu bedeuten?"
    extend " Wer oder Was um alles in der Welt???"
    nat "Ich habe ein ziemlich mieses Gefühl!"
    window hide
    pause 0.5
    scene black with gradientwipedown
    "Bei der Ankunft am Gartenschuppen bemerkten die Anwesenden, dass etwas nicht in Ordnung war."
    extend " Es war absolut unmöglich zu übersehen und es jagte jeden, der es erblickte einen intensiven Schauer über den Rücken"
    play sound umise_024
    scene magicsquare_sun7 with fastdissolve
    pause 4
    $ songname = "Lure"
    show screen showsong
    play music umib_018
    "Auf dem Tor war ein seltsames Symbol abgebildet, es sieht aus als hätte jemand blutrote Farbe verwendet."
    "Eine eigenartige Schrift war deutlich zu erkennen und etwas dass so aussieht wie ein Deutsches Kreuz."
    eva "Wie geschmacklos!"
    extend " Wer malt bitte mit roter Farbe gruselige Symbole auf ein Tor?"
    nat "Will uns da jemand Angst machen?"
    extend " Ist das alles nur Verarsche?"
    scene warehous_o1an
    show rainbackscroll
    show rainfrontscroll
    show nat a12nayamu1 behind rainfrontscroll at m
    with gradientwipedownleft
    play sound umise_032
    pause 0.5
    play sound umise_032
    pause 1.0
    nat "Ich kann das Tor nicht öffnen, es ist verschlossen, gibt es keinen Schlüssel?"
    "Natsuhi versuchte, das Tor zu öffnen, aber es rührte sich nicht von der Stelle."
    "Einer scheint nicht überrascht zu sein."
    extend " Genji geht langsam und in aller Ruhe auf das Tor zu."
    hide nat
    show gen a11defo1 behind rainfrontscroll at m
    pause 0.5
    gen "Fräulein Natsuhi-sama, normalerweise klemmt das Tor nur." 
    extend " Lassen Sie es mich versuchen."
    window hide
    play sound umise_032
    pause 0.5
    play sound umise_032
    pause 1.0
    window auto
    "Genji versuchte ebenfalls das Tor zu öffnen, aber es ging trotzdem nicht auf, ein Schlüssel muss her."
    gen "Es tut mir leid, aber es ist abgeschlossen..."
    extend " Der Schlüssel ist im Dienstzimmer, ich hole ihn sofort."
    nat "Ich bitte darum!"
    gen a11komaru1 "Wie Sie wünschen."
    hide gen
    "Genji ging zurück in die Villa, um den Schlüssel zu holen."
    hide nat
    show nan a1defo1 behind rainfrontscroll at m
    with quickergradientwipeleft
    nan "Ich denke, wir sollten Ruhe bewahren und nichts überstürzen."
    extend " ...Wir sollten erstmal auf einen Schlüssel warten."
    "Genji kehrte kurze Zeit später zurück, doch statt eines Schlüssels hält er eine Feuerwehraxt in der Hand."
    hide nan
    show gen a21kashikomari1  behind rainfrontscroll at m
    gen "Ich bitte um Verzeihung, ich konnte den Schlüssel nicht finden, wir müssen das Schloss zerstören."
    show eva b21akire1go behind rainfrontscroll at r
    eva "Sehr gute Idee!"
    show kan a11defo1 behind rainfrontscroll at l
    kan "Das Tor ist schon sehr alt und dürfte der Axt nicht lange standhalten."
    extend " Einmal durchgebrochen, sollte es einfach sein, das Tor zu öffnen."
    hide kan
    hide eva
    "Genji beginnt nun das Schloss mit der Axt zu zerstören, die anderen sind zwei Schritte zurück gegangen."
    hide kan
    show gen a11defo1 behind rainfrontscroll at m
    pause 1
    play sound umise_020
    pause 1.0
    play sound umise_012
    show gen a11defo1 behind rainfrontscroll at m with vpunch
    pause 1.0
    play sound umise_020
    pause 1.0
    play sound umise_012
    show gen a11defo1 behind rainfrontscroll at m with vpunch
    pause 1.0
    play sound umise_020
    pause 1.0
    play sound umise_012
    show gen a11defo1 behind rainfrontscroll at m with vpunch
    play sound umise_039
    pause 1.0
    "Drei kräftige Hiebe waren ausreichend um das alte Schloss zu zerstören."
    "Genji kann nun das Tor in den Schuppen mit leichtigkeit öffnen."
    window hide
    pause 1
    play sound umise_017
    stop music fadeout 2.0
    $ songname = "-"
    scene white zorder 99
    with gradientwipeup
    pause(1.5)
    scene black with dissolve
    pause 2
    scene g_o1an
    show rainbackscroll
    show rainfrontscroll
    with gradientcirclefade
    window show
    "Währenddessen ist es im Gästehaus noch sehr ruhig, die Kinder der Erwachsenen wachen gerade auf."
    extend " Diese haben von den Ereignissen noch überhaupt nichts mitbekommen."
    window hide
    pause 0.5
    scene g_o1cn 
    show rainbackscroll
    show rainfrontscroll
    with gradientcirclefade
    pause 2
    scene g2f_r1b_bg at bgani
    show rainbackscroll
    show rainfrontscroll
    show g2f_r1b at bgani
    show expression(CustomParticles("images/system/particle.png", 10))
    with gradientcirclefade
    pause 1
    show mar a11uuu1 at m
    window show
    pause 0.5
    $ songname = "Towering cloud in summer"
    play music umib_011_intro
    queue music umib_011_loop loop 
    show screen showsong
    stop wind fadeout 2.0
    mar "Uu!"
    extend " Ist es schon morgen?"
    show jes a11warai1 at l
    jes "Guten Morgen Maria-chan!"
    jes a11majime1 "Huh?"
    extend " Warum rennen die Erwachsenen draußen wie aufgescheuchte Hühner herum?"
    mar a22warai2 "Wie aufgescheuchte Hühner! Wie aufgescheuchte Hühner!"
    extend " *kicher*kicher*!"
    extend " Uu~! Uu~!"
    hide mar
    hide jes
    but "hmpff hmmmmm"
    extend " ..............Hühner? pfmmmm *gähn*"
    "Battler ist noch völlig schlaftrunken, für ihn ergeben die Worte von Jessica noch keinen Sinn."
    show but a21nayamu2 at m
    but "Bitte lass mich noch 5 Minuten weiterschlafen..... nur noch einen winzigen Augenblick..."
    play sound umise_012
    show but a21kuyasigaru1 at m
    show jes a12ikari1 at l
    with vpunch
    hide but with quickgradientwipedown
    play sound umise_013
    jes "Wach auf, Battler-kun!"
    extend " Es ist schon Morgen!"
    but "Wowowowow, musst du mich gleich schlagen?"
    show but b11aseru1 at r
    extend " Jetzt tut mir der Kopf weh, aber dafür bin ich jetzt wach."
    show mar a22warai2 at m
    mar "*kicher*kicher* Kopf tut weh! Kopf tut weh!"
    extend " Uu~!! Uu~!!"
    jes a11majime1 "Maria! Bitte etwas ruhiger, Okay?"
    extend " Unsere hohle Birne muss sich erst einmal vom Aufwachen erholen!"
    hide jes
    hide mar
    but a11defo1 "Jo, Jessica-chan!"
    extend " Was meinst du mit aufgescheuchten Hühnern?"
    show jes a11majime1 at l
    jes "Die Erwachsenen liefen panisch durch den Rosengarten, es sah nach etwas Ernsthaftem aus."
    but "Wo ist eigentlich George-aniki?"
    extend " Er ist in der Nacht auf die Toilette gegangen, seitdem habe ich nichts mehr von ihm gehört."
    jes "Stimmt er fehlt, ob er bei den Erwachsenen ist?"
    but "Könnte sein, schließlich ist er schon fast ein richtiger 'Erwachsener'."
    extend " ...Lass uns doch einfach ein bisschen nach draußen gehen."
    jes a11warai1 "Klingt gut, aber bitte die Regenschirme nicht vergessen!"
    extend " Komm Maria, wir gehen raus!"
    show mar a11uuu1 at m
    mar "Uu~!"
    window hide
    pause 0.5
    stop music fadeout 1.0
    $ songname = "-"
    scene black with gradientwiperight
    play wind umilse_005
    "Die drei schnappten sich einen Regenschirm und gingen nach draußen zum Gartenschuppen."
    extend " Auch sie bemerkten welche Ausmaße dieser Taifun angenommen hat."
    play music umib_036
    $ songname = "Play"
    show screen showsong
    "Dort angekommen, merkten sie schnell, dass die Erwachsenen wohl nicht viel davon hielten, dass die drei auf sie zukamen."
    "Eva und Natsuhi fuchteln wie die Wilden mit den Armen, um zu signalisieren, dass es besser ist, sich nicht zu nähern."
    scene warehous_o2ar
    show rainbackscroll
    show rainfrontscroll
    show nat a32ikari1 behind rainfrontscroll at r
    show eva b25naku5s behind rainfrontscroll at l
    with quickergradientwipeleft
    nat "NICHT NÄHER KOMMEN!!!"
    eva "BATTLER!!!" 
    extend " JESSICA!!!"
    extend " NEHMT MARIA UND GEHT ZURÜCK INS GÄSTEHAUS!!!"
    extend " IHR DÜRFT NICHT NÄHER KOMMEN!"
    "Die beiden wirkten so, als haben sie im Schuppen ein schreckliches Monster gesehen."
    extend " Einfach nur zu sagen, beide sehen traumatisiert aus, wäre völlig untertrieben!"
    "Aber es war schon zu spät, der Blick in den Schuppen war unvermeidlich."
    stop music fadeout 1.0
    "Wahrscheinlich wird sich der Anblick, der sich in diesem Moment allen bot, für immer in die Köpfe der Anwesenden brennen."
    scene black
    pause 1
    $ songname = "goldenslaughterer"
    show screen showsong
    play music umib_024
    play sound umise_013
    jes "KYAAAAAAAAAAAAAAAAAA!!!!!!!!"
    extend " GEORGE???!?!?!?!?"
    extend " DAAAAAAAAAAAAD????!?!?!?!?"
    "Ein schmerzhafter Schrei war zu hören, Jessica konnte ihren Augen nicht trauen."
    extend " Im Schuppen lagen sechs Personen auf dem Boden."
    "Mindestens zwei von ihnen wurden wohl bereits identifiziert."
    scene warehous_o2ar
    show rainbackscroll
    show rainfrontscroll
    show nat a33hisu1 behind rainfrontscroll at l
    show gen a21kashikomari1 behind rainfrontscroll at r
    with quickergradientwipeleft
    pause 0.5
    window show
    nat "Genji! Ruf sofort die Polizei!"
    gen "Wie Sie wünschen."
    gen "Kanon..."
    extend " Bitte erstatte dem werten Herrn Kinzo-sama so schnell wie möglich Bericht!"
    hide nat
    show kan a13defo2 behind rainfrontscroll at l
    with fastdissolve
    kan "Ich habe verstanden!"
    hide kan
    hide gen
    "Genji und Kanon stürmten aus unterschiedlichen Gründen auf die Villa zu."
    "Kurz nachdem beide in der Dunkelheit des Taifuns verschwunden waren, tauchten drei neue Gesichter am Tatort auf."
    hid "Halloooooo, seid ihr da hinten bei diesem Schuppen?"
    "Aus der Ferne hört man Hideyoshis Stimme, zwei weitere Überlebende nähern sich dem Gartenschuppen."
    show kum a12majime1 behind rainfrontscroll at m
    kum "Was ist hier los? Was soll diese Aufregung?"
    extend " Warum sind hier alle versammelt?"
    show sha a11odoroki1 behind rainfrontscroll at r
    sha "Ist etwas Schlimmes passiert?"
    show nat a32ikari1 behind rainfrontscroll at l
    nat "Kumasawa! Shannon! Hideyoshi!"  
    extend " Ihr müsst nicht näher kommen!" 
    extend " Bringt Battler und Jessica sofort zurück ins Gästehaus!"
    kum "Ohohohoho, dann sollten wir wohl besser gehen."
    extend " Battler-sama, Jessica-sama, folgt uns bitte."
    hide kum
    hide sha
    hide nat
    show hid a11komaru2 behind rainfrontscroll at m
    hid "Was sehen meine Augen da? Liegt da George?"
    extend " Eva! Was ist hier passiert?"
    show eva b25naku5s behind rainfrontscroll at l
    eva "Unser George ist....."
    hid "Das darf nicht wahr sein...."
    extend " Wieso nur?....."
    extend " Warum nur unser Sohn?"
    window hide
    pause 0.5
    scene black with gradientwipeleft
    "Hideyoshi ist zu tiefst bestürzt."
    extend " Niemals im Leben hätte er sich vorstellen können, dass er seinen enzigen Sohn tot in einem Gartenschuppen sehen würde."
    "Auch Battler hat etwas im Schuppen gesehen, dass seine Welt zum Stillstand gebracht hat."
    extend " Er geht mit langsamen Schritten immer näher in den Schuppen."
    jes "Battler-kun! Geh bitte nicht rein!"
    "Trotz aller Aufforderungen, den Tatort zu verlassen, geht Battler zur Torschwelle, um sich zu vergewissern, dass seine Augen ihm keinen Streich spielen."
    window hide
    pause 0.5
    scene warehous_i1ar2_bg at bgani
    show rainbackscroll
    show rainfrontscroll
    show warehous_i1ar2 at bgani
    show expression(CustomParticles("images/system/particle.png", 10))
    with quickergradientwipeleft
    pause 0.5
    play sound umise_013
    show but b11naku1 at m with vpunch
    window show
    but "Das darf doch wohl nicht wahr sein?!!?!?"
    extend " Welches grausame Monster könnte so etwas tun?"
    but "Ja, ich sehe es ganz deutlich, oh man was für eine Schande."
    but "Ah, es bringt nichts... Es bringt alles überhaupt nichts...."
    extend " Ich weiß, dass du ein Womanizer und ein ziemliches Arschloch warst..."
    but "Aber dass man dich tötet und dein Gesicht auf grausamste Weise entstellt, das hast nicht einmal du verdient."
    extend " Wenn du deine Kleider nicht anhättest, wüsste ich gar nicht, wer da vor mir liegt."
    but "Das ist einfach viel zu viel, wieso ist das passiert?"
    play sound umise_013
    show but b26naku2 at m with vpunch
    extend " ICH VERSTEH ES NICHT!!!"
    but "Warum nur? Warum nur? Warum nur?"
    window hide
    pause 0.5
    scene black with dissolve
    extend " Wer... liegt.. da... neben.. dir...??"
    play sound umise_038
    scene blood_1a
    extend " Nein!!! Nein!!! Kyrie-san!!!"
    but "Wieso auch noch du?"
    extend " Ich habe dich nie für meine neue Mutter gehalten, aber das ist übertrieben!"
    play sound umise_038
    scene blood_1ar with dissolve
    extend " Nie im Leben hätte ich mir für einen von euch ein solches Ende gewünscht."
    but "Natürlich sagt man manchmal aus Wut, dass man jemanden tot sehen will, aber ihn dann wirklich tot zu sehen, das ertrage ich nicht..."
    but "Dad, Kyrie, Gohda, Tante Rosa und wieso auch du George-aniki?"
    extend " Ich verstehe das nicht mehr, das ist unfair!"
    extend " Dass man euer Gesicht nicht mehr erkennt, hat keiner von euch verdient...."
    but "Es wäre viel einfacher gewesen, euch ins Jenseits zu schicken und hier reinzulegen..."
    extend " War das wirklich nötig? Macht es das wirklich besser?"
    window hide
    pause 0.5
    scene warehous_i1ar2_bg at bgani
    show rainbackscroll
    show rainfrontscroll
    show warehous_i1ar2 at bgani
    show expression(CustomParticles("images/system/particle.png", 10))
    with quickergradientwipeleft
    pause 0.5
    show hid a11komaru2 at m
    pause 0.5
    hid "Bleib stark, Battler-kun, die Polizei wird den Täter morgen finden und verhaften."
    extend " Ich bin genauso traurig wie du, aber wir dürfen jetzt keine falsche Bewegung machen."
    hide hid
    show nan a2fumu1 at m
    nan "Ja, es ist nicht zu bezweifeln, dass sie nicht überlebt haben."
    extend " Es tut mir so unendlich leid, aber es gibt nichts, was ich tun kann."
    show nat a11komaru1 at l
    nat "Alles in Ordnung, ... auch ich sehe, dass man da nichts machen kann."
    extend " ...Es gibt keinen Grund, sich für etwas zu entschuldigen."
    "Auch Natsuhi, die versucht, einen kühlen Kopf zu bewahren, ist anzumerken, dass sie der Tod ihres Mannes nicht kalt lässt."
    nan "Was erblicken meine Augen da?"
    "Nanjos Hand nähert sich vorsichtig der Hosentasche von Gohda, dort scheint etwas drin zu sein."
    nan a1defo1 "Tatsächlich, wie kommt der hier rein? Das ist absolut unmöglich!"
    nat a32ikari1 "Wie kann das bitte sein?"
    "Der Schlüssel zu diesem Gartenschuppen wurde in Gohdas Hosentasche gefunden."
    extend " Normalerweise sollte es doch unmöglich sein, da der Schuppen nur von außen abgeriegelt werden kann."
    nat "Das wird alles immer seltsamer und seltsamer."
    "Auch die bedienstete Shannon sieht sehr bedrückt aus."
    hide nat
    hide nan
    show sha a11odoroki1 at r
    sha "Ist das dort...."
    extend " George-sama?"
    extend " Warum?"
    show but b23naku3 at l
    but "Richtig Shannon-chan, das ist Aniki..."
    extend " Sag mir... Shannon-chan..."
    extend " Wie hast du Aniki zuletzt erlebt?"
    show sha b31majime1 at r
    but "Nein, sag nichts! Ich weiß, was du sagen willst...."
    extend " Der Ring an deinem Ringfinger ist wunderschön, ich bin sicher, er will, dass du ihn so in Erinnerung behältst."
    but "Also bitte, sieh ihn nicht so an, ich will nicht, dass du ihn so siehst."
    sha "Battler-sama.... Ich...."
    show hid a11komaru2 at m
    hid "Es wäre besser, diesen Ort der Polizei zu überlassen."
    extend " Wenn wir uns auch nur ein wenig nähern, könnte das einen Einfluss auf die Untersuchung haben."
    window hide
    pause 0.5
    scene warehous_o2ar
    show rainbackscroll
    show rainfrontscroll
    with quickergradientwipeleft
    pause 0.5
    window show
    show nat a12nayamu1 behind rainfrontscroll at l
    nat "Hast du die Polizei erreicht, Genji?"
    show gen a11defo1 behind rainfrontscroll at r
    gen "Leider nicht, die Leitungen wurden gekappt."
    extend " Ein Anruf ist nicht durchgekommen."
    nat a33hisu1 "Wer um alles in der Welt??"
    "Genji ist mit der schlechten Nachricht zurückgekehrt, dass die Polizei nicht informiert wurde, es sieht so aus, als müssten die Überlebenden bis Montag warten."
    window hide 
    pause 1
    call chapterendb from _call_chapterendb
    pause 1
    play audio umise_030
    show geo a11defo1 at m with fastdissolve
    pause 0.3
    scene black with instant
    play audio umise_046
    scene blood_1b with instant
    pause 0.5
    scene black with instant
    play audio umise_030
    show rud a11defo1 at m with fastdissolve
    pause 0.3
    scene black with instant
    play audio umise_046
    scene blood_1a with instant
    pause 0.5
    scene black with instant
    play audio umise_030
    show kir a11defo1 at m with fastdissolve
    pause 0.3
    scene black with instant
    play audio umise_046
    scene blood_2c with instant
    pause 0.5
    scene black with instant
    play audio umise_030
    show ros a11komaru4 at m with fastdissolve
    pause 0.3
    scene black with instant
    play audio umise_046
    scene blood_1ar with instant
    pause 0.5
    scene black with instant
    play audio umise_030
    show cla a11defo1 at m with fastdissolve
    pause 0.3
    scene black with instant
    play audio umise_046
    scene blood_1ar with instant
    pause 0.5
    scene black with instant
    play audio umise_030
    show goh a11defo1 at m with fastdissolve
    pause 0.3
    scene black with instant
    play audio umise_046
    scene bite with instant
    pause 0.5
    scene black with instant
    play audio umise_030
    show no83_0051
    show bea a11akuwarai2 at m with fastdissolve
    pause 1
    scene black with instant
    play audio umise_046
    show text _("Zur Zeit der ersten Dämmerung:\nsollst du die sechs, die der Schlüssel ausgewählt hat,\nals Opfer darbringen.")
    pause 7
    scene black with kanon_r 
    pause 3
    show screen clockschoolch1
    play sound "<from 0 to 5>/audio/sfx/umilse_1050.ogg"
    pause 10
    hide screen clockschoolch1 with dissolve
    pause 2
    ## Kapitel Ende
    ## Kapitel 2 - Die Zwei, die sich nahe stehen
    $ chapter = "Die Zwei, die sich nahe stehen"
    $ songname = "Witch in Gold"
    $ save_name = _("EpisodeX Illusion of the golden witch\nDie Zwei, die sich nahe stehen")
    play music umib_017
    play wind umilse_005
    play rain umilse_012
    show screen showch
    show screen showsong
    pause 0.5
    scene m_cy1a
    show rainbackscroll
    show rainfrontscroll
    with gradientcirclefade
    pause 0.5
    window show
    "Nach der Tragödie zogen sich die Hinterbliebenen in das Wohnzimmer der Villa zurück."
    extend " Eine hitzige Diskussion darüber, wer als Täter in Frage kommt, ist entbrannt."
    "Die Situation ist seit dem Auffinden der Sechs merklich angespannt."
    extend " Jeder wäre gestresst, vor allem, wenn man weiß, dass man wegen des Wetters auf der Insel festsitzt."
    window hide
    stop wind fadeout 2.0
    pause 0.5
    scene m1f_s1cr at bgani
    play clocktick umilse_015
    show expression(CustomParticles("images/system/particle.png", 10))
    with gradientcirclefade
    show but b11odoroki3 at m
    pause 0.5
    window show
    but "Was machen wir jetzt?"
    extend " Hier läuft ein Mörder frei herum..."
    show eva b23komaru2 at l
    eva " Warten wir, bis sich der Sturm gelegt hat."
    extend " Das bedeutet aber auch, dass wir bis morgen früh hier sitzen müssen."
    show jes a23majime1 at r
    jes "Was ist, wenn der Mörder ein zweites Mal zuschlägt?"
    extend " ...Die Frage, wer der Mörder ist, ist ebenfalls wichtig."
    extend " Es ist entweder jemand, der sich vorher auf die Insel geschlichen hat, oder einer von uns."
    hide but
    hide jes
    hide eva
    show nat a11komaru1 at m
    nat "Es ist sehr gut möglich, dass es ein Leichtes gewesen wäre, die Insel kurz vor dem Taifun zu erreichen, ohne dass es jemand bemerkt hätte."
    extend " Andererseits braucht er ein sehr gutes Verständnis aller Räume und Wege, die es hier auf der Insel gibt."
    show but b23nayamu1 at l
    but "Mit anderen Worten: Der Täter kennt uns sehr gut und ist kein Eindringling von außen."
    "Zwischenzeitlich wurden auf einen Tipp von Genji hin Kinzos Schrotflinten geholt."
    extend " Dies sind von Kinzo modifizierte Varianten mit mehr Munition und weniger Streuung."
    play audio umise_030
    hide but
    hide nat
    show hid a12defo1 at m
    show eva b24defo1 at l
    show nat a16defo1 at r
    "Die Waffen gehören jetzt Hideyoshi, Eva und Natsuhi."
    extend " Die anderen waren entweder zu jung für Schusswaffen oder lehnten ab."
    window hide
    pause 0.5
    scene m1f_s1ar_bg at bgani
    show rainbackscroll
    show rainfrontscroll
    show m1f_s1ar at bgani
    show expression(CustomParticles("images/system/particle.png", 10))
    with quickergradientwipeleft
    pause 0.5
    show eva b24akirenigo at m with dissolve
    window show
    eva "Es gäbe viele Gründe für Dritte, uns auszulöschen, vor allem wenn man die Legende des Goldes kennt."
    show nat a16komaru1 at l
    nat "Mein Mann, war immer davon überzeugt, dass Vater sein Gold irgendwo auf der Insel versteckt hatte."
    extend " Vor zwei Jahren hat Vater ein Rätsel mit dem Bild dieser Hexe in der Eingangshalle aufgehängt, aber er konnte es nicht lösen."
    hide nat
    show eva b24akirenigo at l
    show jes a11atya2 at r
    with dissolve
    jes "Das Rätsel besteht einfach darin, an einen bestimmten Ort zu gehen und dort nach einem bestimmten Muster zu töten."
    extend " Danach soll BEATRICE wieder zum Leben erwachen."
    extend " 'Zur Zeit der neunten Dämmerung, wird die Hexe wiederbelebt, und niemand wird am Leben bleiben'."
    eva b21futeki1 "Die Hexe BEATRICE aus dem Wald ist schon ein Gerücht, das in unserer Kindheit existierte."
    extend " Wie soll das bitte aussehen?"
    extend " Ein magisches Wesen, das uns tötet, um sich selbst wiederzubeleben?"
    eva "Dieses Rätsel wird doch nur benutzt, um sich zu verstecken!"
    show nat a12nayamu1 at m
    nat "Aber es wäre auch absurd, sich vorzustellen, dass sich jemand als BEATRICE verkleidet und die Morde begeht."
    eva a11hohoemi1 "Sich als BEATRICE verkleiden?"
    extend " Jemand, wie zum Beispiel Shannon, verkleidet sich als Hexe und bringt uns dann alle um?"
    extend " Der Gedanke klingt einfach schon mehr als absurd."
    window hide
    pause 0.5
    scene m1f_s1cr at bgani
    show expression(CustomParticles("images/system/particle.png", 10))
    with quickgradientcirclefade
    show but b11oya1 at m with dissolve
    pause 0.5
    window show
    but "Shannon-chan könnte keiner Fliege etwas zuleide tun."
    show eva b22akire2 at r
    eva "Stille Wasser sind tief, Battler-kun... *kicher*"
    extend a11hohoemi1 " Spaß beiseite, dieses inkompetente Ding könnte nicht einmal ein Buttermesser in die Hand nehmen."
    hide but
    show nat a11ikari1 at l
    nat "Eva-san! Das war mehr als nur unhöflich gegenüber meiner Angestellten!"
    eva "Oh, Entschuldigung!..." 
    extend " ...Wird nicht wieder vorkommen... *kicher*"
    "Eva scheint eine gewisse Abneigung gegen Shannon zu haben."
    extend " Irgendwo ist das auch zu erwarten, schließlich wollte sie nie, dass so eine wie sie etwas mit ihrem verstorbenen Sohn anfängt."
    hide eva
    hide nat
    show but a11aseru5 at m
    but "Das war nicht nötig, das hätte nicht sein müssen..."
    extend " In solch einer Situation jemand so nahe zu treten, selbst wenn es nicht ernst gemeint war!"
    hide but  
    hide eva
    show sha a11hajirai2 at m
    sha "Battler-sama.... Ich... uhm..."
    extend " Sie müssen das nicht für mich tun."
    extend " ...An so etwas bin ich schon gewöhnt."
    show but b11warai2 at l
    but "Nein, Shannon-chan, das musst du dir nicht gefallen lassen."
    sha a12hajirai3 "B............."
    extend "Battler-sama, was soll ich sagen?... uhm..."
    "Shannon errötete leicht, es war ihr sichtlich unangenehm."
    extend " Gleichzeitig kehrte für einen kurzen Moment ihr Lächeln zurück."
    window hide
    pause 0.5
    scene m1f_s1ar_bg at bgani
    show rainbackscroll
    show rainfrontscroll
    show m1f_s1ar at bgani
    show expression(CustomParticles("images/system/particle.png", 10))
    with quickergradientwipeleft
    pause 0.5
    show nat a12nayamu1 at m with dissolve
    window show
    $ songname = "Suspicion"
    play music umib_027
    show screen showsong
    nat "Der Täter muss unter uns sein."
    extend " ...Es gibt keine unsichtbaren Wesen, die nach Belieben Menschen töten und in verschlossene Räume sperren."
    show but a11niramu3 at rightedge
    but "Wahrscheinlich hast du Recht..."
    extend " Aber dass der Täter jetzt mit uns in einem Raum sitzt und ruhig zuhört, kann ich auch nicht glauben."
    show eva a11hohoemi1 at l
    eva "Huh, wer soll es denn gewesen sein?"
    nat "Das Tor zum Gartenhaus kann nur mit dem Schlüssel aus dem Dienstzimmer geöffnet werden!"
    eva "Wurde der Schlüssel nicht bei Gohdas Leiche gefunden?"
    extend " ....Der Raum war offenbar verschlossen, obwohl der Schlüssel im Schuppen selbst lag."
    but "Das klingt sehr merkwürdig, hat das Tor sicher nicht geklemmt?"
    extend " Ich meine, haben mehrere versucht, es zu öffnen?"
    hide nat
    show gen a11defo1 at m
    gen "Ich habe es mit Natsuhi-sama überprüft, es war definitiv abgeschlossen..."
    window hide
    pause 0.5
    scene firsttwilight with gradientcirclefade
    "Der Tatort ist ein verschlossener Gartenschuppen, in dem sechs Leichen gefunden wurden." 
    extend " Alle Leichen wurden von Dr. Nanjo als tot bestätigt."
    "Zu den Opfern zählen:"
    scene black with dissolve
    show geo a11defo1 at leftedge
    extend " Ushiromiya George, der Sohn von Eva und Hideyoshi."
    show rud a11defo1 at m
    extend " Ushiromiya Rudolf, der Vater von Battler."
    show kir a11defo1 at rightedge
    extend " Ushiromiya Kyrie, die Stiefmutter von Battler."
    scene black with fastdissolve
    show cla a11defo1 at leftedge
    "Ushiromiya Krauss, Ehemann von Natsuhi und Jessicas Vater."
    show ros a11komaru4 at m
    extend " Ushiromiya Rosa, die Mutter von Maria."
    show goh a11defo1 at rightedge
    extend " und der Bedienstete Gohda."
    scene firsttwilight with gradientcirclefade
    "Außerdem wurde der einzige Schlüssel zum Öffnen und Schließen des Schuppens in der Hosentasche von Gohdas Leiche gefunden."
    extend " Natsuhi und Genji konnten bestätigen, dass das Tor vollständig verschlossen war."
    "Bedeutet, dass der verschlossene Schuppen erst geöffnet wurde, nachdem das Schloss mit einer Feuerwehraxt zerstört worden war."
    "Es gibt auch keine Möglichkeit, den Schuppen von innen zu verschließen."
    "Das einzige vorhandene Fenster war ebenfalls verschlossen und intakt."
    extend " Es gibt auch keine Geheimgänge oder andere zweifelhafte Schlupflöcher, durch die man entkommen könnte."
    "Mit anderen Worten: Der Täter hat die sechs ermordet, den Schlüssel in Gohdas Tasche gesteckt, ist rausgegangen und hat dann den Schuppen auf unbekannte Weise verschlossen."
    window hide
    pause 0.5
    scene m1f_s1cr at bgani
    show expression(CustomParticles("images/system/particle.png", 10))
    show hid a11majime1 at r
    hid "Ich finde es bemerkenswert, wie du niemanden verdächtigen willst, aber irgendjemand muss es ja gewesen sein."
    extend " ...Vielleicht irren wir uns alle und es war wirklich eine Hexe."
    show but b11kuyasigaru1 at l
    but "Ich weigere mich, an so etwas zu glauben! Es gibt keine Magie und keine Hexe!"
    extend " Aber es ist auch sehr schwierig, jemanden zu verdächtigen."
    extend " ...Gibt es überhaupt einen Verdächtigen?"
    hid "Ist es für einen Menschen möglich, den passenden Schlüssel in den verschlossenen Raum zu legen?"
    but "Ach man... Das bringt doch alles nichts.... Das bringt doch alles nichts.."
    show hid a11defo1 at m
    hid "Was war das eigentlich für ein Symbol auf dem Tor?"
    extend " Es war kein Pentagramm, eher ein Deutsches Kreuz?"
    window hide
    play sound umise_027
    pause 0.9
    scene black with flash
    $ songname = "Witch of the Painting"
    show screen showsong
    play music umib_026_intro
    queue music umib_026_loop loop
    mar "Kihihihhihihihihihihihihihi!"
    "Kaum hatte Hideyoshi diese Frage ausgesprochen, ertönte ein schrilles Gelächter, das sofort alle Aufmerksamkeit auf sich zog."
    window hide
    pause 0.5
    scene m1f_s1ar_bg at bgani
    show rainbackscroll
    show rainfrontscroll
    show m1f_s1ar at bgani
    show expression(CustomParticles("images/system/particle.png", 10))
    with quickergradientwipeleft
    pause 0.5
    show mar a22akuwarai2 at m with dissolve
    window show
    mar "Das war der siebte magische Kreis der Sonne!"
    mar "Der magische Kreis ist in Hebräisch beschriftet."
    extend " Die Worte, die um das Kreuz geschrieben sind, stammen aus Psalm 116:16-17 der Bibel und lauten:" 
    mar "'Der Herr hat mich von meinen Ketten befreit. Ich will dir ein Opfer des Dankes darbringen und den Namen des Herrn anrufen.'"
    "Alle Anwesenden sind geschockt, die neunjährige Maria, die noch nie ganze Sätze ohne 'uu' sagen konnte, spricht plötzlich von magischen Kreisen und Bibelzitaten."
    "Schlimmer noch, sie sagte es mit einem furchterregenden Gesichtsausdruck. So selbstsicher, als wüsste sie etwas, was andere nicht wissen."
    show but a11aseru1 at l
    but "Whoaaa..."
    extend " Woher hast du das Wissen über diese Dinge?"
    scene c0101_b with fastdissolve
    mar "Kihihihihihihi!"
    extend " Ich bin auf Okkultismus spezialisiert."
    mar "Es wird nicht der letzte magische Kreis sein, den du siehst!"
    mar "Kihihihihihihi!"
    extend " Ich habe ein ganzes Buch über die magischen Kreise und was sie zu bedeuten haben."
    window hide
    play sound umise_034
    scene c0101_c with fastdissolve
    pause 2
    window show
    mar "BEATRICE wird uns schon bald ins Goldene Land einladen."
    extend " Danach ist alles andere unwichtig!"
    extend " Kihihihihihihi!!!"
    mar "Man kann machen, was man will, sie kommt durch jede verschlossene Tür!"
    extend " Versucht gar nicht erst, euch zu wehren!" 
    extend " Kihihihihihihi!"
    pause 0.5
    scene m1f_s1ar_bg at bgani
    show rainbackscroll
    show rainfrontscroll
    show m1f_s1ar at bgani
    show expression(CustomParticles("images/system/particle.png", 10))
    with quickergradientwipeleft
    pause 0.5
    show jes a11atya2 at m with dissolve
    window show
    jes "Ist euch auch aufgefallen, dass Maria sich auf eine merkwürdige Weise verhält?"
    extend " ...Dass ihre Mutter ermordet wurde, macht sie überhaupt nicht traurig."
    jes "Im Gegenteil, sie sieht überglücklich aus."
    show mar a11niyari1 at l
    mar "Ich weiß, wer die sechs umgebracht hat!"
    show nat a32ikari1 at r
    nat "Du weißt es?"
    mar "Es ist egal, ob ich sterbe, sie nimmt mich sowieso mit ins Goldene Land."
    nat "Maria-chan, rede doch keinen Unsinn!"
    mar "Es war BEATRICE!"
    hide jes
    show but b22odoroki2 at m
    but "Maria... Jetzt ist nicht die Zeit dafür!"
    extend " Jemanden wie BEATRICE gibt es nicht..."
    mar a22sakebu1 "Uu!!!....."
    extend " Es war aber BEATRICE!"
    play sound umise_013
    hide but
    hide nat
    show mar a22sakebu1 at m with vpunch
    extend " BEATRICE!!, BEATRICE!!, BEATRICE!!"
    "Maria wird immer wütend, wenn jemand in ihrer Gegenwart die Existenz der Hexe leugnet."
    "Irgendwie ist es klar, sie ist noch ein Kind und der Glaube an das Übernatürliche ist noch sehr ausgeprägt."
    window hide
    scene black with dissolve
    "Eva deutet an, dass sie Ruhe braucht, der Morgen war sehr anstrengend für sie."
    window hide
    pause 0.5
    scene m1f_s1cr at bgani
    show expression(CustomParticles("images/system/particle.png", 10))
    show eva b25komaru4 at m
    eva "Wir ziehen uns zu zweit ins Gästezimmer zurück, um uns auszuruhen, zur Not haben wir die Gewehre."
    show kum a12majime1 at l
    kum "Aber besser nicht alleine, wir begleiten euch!"
    show nat a16komaru1 at r
    nat "Richtig, es wäre töricht uns jetzt so leichtfertig zu trennen!"
    hide eva
    show hid a12defo1 at m
    hid "Danke Leute, ihr meint es zu gut mit uns!"
    extend " Wahahahaha!"
    nat "Geht ins Gästezimmer und schließt die Tür mit der Kette ab, damit der Täter nicht hereinkommen kann."
    kum "Selbst ein geschickter Killer müsste die Kette mit einem Bolzen durchschneiden, um hineinzukommen."
    extend " Dies würde Zeit zum Reagieren geben."
    hid "Vielen Dank, so können wir uns beruhigt ausruhen!"
    window hide
    $ songname = "-"
    stop music fadeout 2
    stop clocktick fadeout 2
    scene m2f_p1ar_bg at bgani
    show rainbackscroll
    show rainfrontscroll
    show m2f_p1ar at bgani
    with gradientwiperight
    pause 2
    scene m_door1 with gradientcirclefade
    pause 2
    scene m2f_r4ars_bg at bgani
    stop rain fadeout 1
    show m2f_r4ar at bgani
    show expression(CustomParticles("images/system/particle.png", 10))
    with gradientcirclefade
    pause 0.5
    window show
    "Nachdem Eva und Hideyoshi das Gästezimmer betreten und die Türkette umgelegt hatten, warfen sich beide auf das Bett."
    "Eva kann sich nicht mehr zurückhalten und fängt bitterlich an zu weinen, sie hat sich die ganze Zeit mehr oder weniger zurückhalten müssen."
    $ songname = "Hope"
    play music umib_008
    show screen showsong
    show hid a11odayaka1 at l
    hid "Schatz, es war ein harter Tag, aber George würde nicht wollen, dass wir jetzt Trübsal blasen."
    extend " Er wird uns vom Himmel aus schützen, damit wir die Insel morgen sicher verlassen können."
    show eva b25naku5s at r
    eva "Warum hat es ihn getroffen?...."
    extend " Seine Zukunft war vielversprechend...."
    eva "Das ist doch wohl nicht fair!"
    extend " Warum nur?"
    eva "George!! Komm zu mir zurück, komm zu mir zurück!!!"
    eva "Schatz!! Halt mich fest!!"
    play sound umise_013
    hide eva with quickergradientwipeleft
    "Eva bricht in Tränen aus, die sonst so kühle und ruhige Eva zeigt nur ihrem Mann gegenüber ihre weiche Seite."
    hid a11naku4 "So ist es gut, lass alles raus, ich bin genauso traurig wie du und es tut so unendlich weh!"
    extend " Aber er würde nicht wollen, dass wir viel um ihn trauern, sondern dass wir weitermachen und ihn in guter Erinnerung behalten!"
    "Auch Hideyoshi kann seine Tränen nicht mehr zurückhalten."
    extend " Zu groß ist die emotionale Belastung, auch für Hideyoshi, der selbst jetzt noch tröstende Worte findet."
    stop music fadeout 2
    $ songname = "-"
    window hide
    pause 2
    call butterfly1 from _call_butterfly1_2
    pause 2
    window show
    "Genau in diesem Moment erscheinen wunderschöne goldene Schmetterlinge im Raum, buchstäblich aus dem Nichts."
    window hide
    pause 0.5
    scene efe1 with fastdissolve
    pause 2
    scene m2f_r4ars_bg at bgani
    show m2f_r4ar at bgani
    show zep a11defo1 at l
    show fur a11defo1 at r
    show expression(CustomParticles("images/system/particle.png", 10))
    play sound umise_055
    with witchfadeinslow
    pause 0.5
    window show
    "Die Goldenen Schmetterlinge haben sich in seltsame Zwillinge verwandelt?"
    "Hideyoshi und Eva gingen sofort in Alarmbereitschaft."
    play audio umise_030
    show e0903a with quickergradientwiperight
    eva "Wer seid ihr, verdammt noch mal, und woher kommt ihr?"
    extend " Raus hier, ich bin bewaffnet!"
    eva "Zwingt mich nicht abzudrücken!"
    hide e0903a with quickgradientwiperight
    "Die beiden Eindringlinge bewegen sich nicht, im Gegenteil, sie posieren im Duett."
    window hide
    play music umib_142
    $ songname = "Kina no Kaori"
    show screen showsong
    play sound umise_002
    show zep a12defo1 at l
    show fur a12defo1 at r
    with quickflash
    pause 1
    window show
    zep "Das sind also die beiden Auserwählten, Furfur?"
    fur "Was sehe ich? Ein verliebtes Paar! Ist das nicht schön, Zepar?"
    zep "Heute entscheidet sich, ob ihr als Paar weiterleben dürft oder in eine Welt ohne Liebe verbannt werdet!"
    fur "Das ist ja absolut fantastisch, die beiden sehen so vielversprechend aus!"
    play audio umise_030
    show e0903a with quickergradientwiperight
    eva "Was wollt ihr von uns?"
    extend " ..Kommt näher und ich werde euch erschießen!"
    hide e0903a 
    show zep a11defo1 at l
    show fur a11defo1 at r
    with quickgradientwiperight
    "Die beiden lassen sich von Evas Drohungen überhaupt nicht beeindrucken und ignorieren sie die ganze Zeit."
    zep "Ich bin einer der 72 großen Dämonen, der Dämon der Liebe, mein Name ist Zepar!"
    fur "Ich bin einer der 72 großen Dämonen, der Dämon der Liebe, mein Name ist Furfur!"
    zep "Ihr werdet euch jetzt einer Prüfung unterziehen müssen!"
    fur "Wer sich weigert, auf den wartet nur der Tod!"
    zep "Denn ihr beide seid von Fräulein BEATRICE-sama für die Zweite Dämmerung auserwählt worden!"
    hide zep
    hide fur
    show eva b26ikari2 at m
    eva "Das ist doch lächerlich!"
    extend " Was glaubt ihr wer ihr seid!?!!"
    "Eva ist außer sich vor Wut, während Hideyoshi versucht, die Tür zu öffnen."
    scene m_door1
    show hid a12komaru2 at m 
    with quickgradientwipeleft
    play sound umise_032
    hid "Die Kette rührt sich nicht!"
    extend " Ich bekomme die Tür nicht auf!"
    window hide
    pause 0.5
    scene m2f_r4ars_bg at bgani
    show m2f_r4ar at bgani
    show zep a11defo1 at l
    show fur a11defo1 at r
    show expression(CustomParticles("images/system/particle.png", 10))
    with quickergradientwipeleft
    zep "Sieh nur, Furfur!"
    extend " Sie sind auf der Suche nach einem Ausweg!"
    fur "Das ist absolut unmöglich, sie glauben, sie könnten den Großen Dämonen entkommen, Zepar!"
    "Hideyoshi wird klar, dass es keinen Sinn hat, an der Tür zu rütteln, sie müssen den Anweisungen der Dämonen Folge leisten."
    hide zep
    hide fur
    show eva b26ikari2 at l
    show hid a12komaru2 at r
    hid "Okay, okay, was müssen wir für diesen Test tun?"
    eva "Schatz, du willst doch nicht wirklich..."
    hide eva
    hide hid
    show zep a11defo1 at l
    show fur a11defo1 at r
    zep "Dafür müsst ihr uns eine einfache Frage beantworten!"
    fur "Ihr dürft den Raum verlassen, wenn ihr sie richtig beantwortet!"
    hide zep
    hide fur
    show eva b26ikari2 at l
    show hid a12komaru2 at r
    eva "Dann raus damit, welche Frage ist es?"
    hid "Eva!"
    extend " Wir haben keine Zeit für Hektik und Eile!"
    hid "Sie haben gesagt, wenn wir nicht bestehen, sterben wir..."
    eva "Als ob du das auch noch glaubst..."
    hide eva
    hide hid
    show zep a11defo1 at l
    show fur a11defo1 at r
    zep "Nun, wir sollten keine Zeit verlieren, BEATRICE-sama wird langsam ungeduldig, Furfur!"
    fur "Dann lass uns mit dem Test beginnen, Zepar!"
    zep "Die Frage, die wir stellen wollen, lautet..."
    show zep a12defo1 at l
    show fur a12defo1 at r
    play sound umise_002
    with quickflash
    fur "Was ist das, was ihr zwei gemeinsam am meisten liebt?"
    zep "Beantwortet die Frage mit Bedacht, denn davon hängt euer Liebesleben ab!"
    fur "Bitte denkt daran, dass ihr nur eine gemeinsame Antwort geben könnt und diese auch nur einmal!"
    hide zep
    hide fur
    show hid a11majime1 at r
    hid "Ich glaube, die Frage ist nur ein Scherz, denn es gibt nur eine einzige Antwort, Eva!"
    show eva b21akire1go at l
    eva "Deshalb habe ich dich geheiratet, ich weiß genau, was du meinst!"
    hid "Darüber lässt sich nicht streiten."
    "Hideyoshi und Eva sind sich absolut sicher, was sie den Dämonen antworten wollen, da muss man nicht lange überlegen."
    hid "Unsere gemeinsame Antwort darauf lautet wie folgt"
    eva "Unser Sohn George!"
    hid "Das ist der Beweis für unsere Entschlossenheit!"
    extend " Nichts sollte ein Ehepaar mehr lieben als die eigenen Kinder!"
    extend " Sie gesund aufwachsen zu sehen, ist das größte Geschenk."
    hide eva
    hide hid
    show zep a11defo1 at l
    show fur a11defo1 at r
    zep "Hast du gehört, was sie gerade gesagt haben, Furfur?"
    fur "Das ist ja sowas von romantisch, Zepar!"
    show zep a12defo1 at l
    show fur a12defo1 at r
    play sound umise_002
    with quickflash
    zep "Aber die Antwort ist leider falsch!"
    fur "Damit ist das Spiel vorbei und euer Leben gehört BEATRICE-sama!"
    zep "Die sehen aber sauer aus, Furfur!"
    fur "Aber beide haben offensichtlich gelogen, Zepar!"
    play audio umise_030
    show e0903d with quickgradientwiperight
    eva "Das ist doch wohl die Höhe!"
    extend " Verschwindet, oder die Schrotkugeln fliegen durch eure dünnen Körper!"
    eva "Ja, ich werde euch mit Löchern durchbohren, bis nichts mehr von euch übrig sein wird!"
    extend " Hahahahahahaha!!!!!"
    hide e0903d with quickgradientwiperight
    pause 2
    hide zep
    hide fur
    play sound umise_056
    with witchfadeout
    stop music fadeout 1
    pause 1
    play sound umise_052
    show geo a11majime2 at m with witchfadein
    pause 0.5
    play music umib_077
    $ songname = "miragecoordinator"
    show screen showsong
    geo "Ich bin mehr als nur enttäuscht von euch..."
    extend " Mom.... Dad....."
    "Plötzlich waren die Dämonen verschwunden und an ihrer Stelle erschien wie aus dem Nichts ihr verstorbener Sohn."
    show hid a11naku4 at leftedge
    hid "Das kann nicht sein!"
    extend " George???"
    show eva b25naku5s at rightedge
    eva "Du bist doch gestorben???"
    extend " Ich habe deine Leiche gesehen, wie ist das möglich?"
    geo "Ich bin nicht der, den ihr am meisten liebt!"
    extend " Das habt ihr noch nie gemacht!"
    eva "Nein, George! Bitte nicht! Das ist nicht wahr!"
    extend " Du warst immer das Wichtigste für uns!"
    hid "George! Bitte, wir können über alles reden!"
    geo a21majime4 "Ja, ich war das Wichtigste für euch..."
    extend " Ich war wichtig für euch, damit ihr einen großen Nutzen aus mir ziehen könnt!"
    geo "Ihr habt mich immer streng zum 'Gentleman' erzogen, damit ich zu Eurem Vorteil handle!"
    eva "Nein George! So ist das nicht!"
    scene black
    show geo a11niramu1 at m
    play sound umise_027
    with quickflash
    geo "Oh doch!"
    extend " Euch hat immer nur interessiert, wie ihr an Opas Erbe kommt!"
    play sound umise_057
    show chain1r_sp with quickflash
    geo "Es war euch wichtiger, dass ich Geld verdiene ohne Ende, dass ich eine Frau heirate, die aus reichem Hause stammt!"
    extend " Ihr wolltet nicht, dass ich Shannon-chan zur Frau nehme..."
    play sound umise_057
    show chain4r_sp with quickflash
    geo "Und warum? Weil ihr keinen Nutzen drauß ziehen könntet!"
    extend " Solange ich diesen Weg gehe, habt ihr mich unterstützt, aber sobald ich von diesem Weg abweiche, habt ihr mich nie unterstützt!"
    play sound umise_057
    show chain5r_sp with quickflash
    geo "Ihr seid schreckliche Eltern, dass ihr das eurem einzigen Sohn antut!"
    extend " Ihr habt den Test nicht bestanden, also werde ich euch BEATRICE-sama eigenhändig ausliefern!"
    window hide
    scene m2f_r4ars_bg at bgani
    show m2f_r4ar at bgani
    show eva b25naku5s at m
    play sound umise_027
    with quickflash
    show expression(CustomParticles("images/system/particle.png", 10))
    eva "George, bitte! Es tut uns leid! Bitte vergib uns!"
    extend " Wir haben das für dich getan, damit du nicht wirst wie unsere Geschwister!"
    geo "Lasst mich in Ruhe, ihr gierigen Piranhas!"
    play sound umise_057
    show chain1r_sp with quickflash
    pause 0.5
    play sound umise_057
    show chain4r_sp with quickflash
    pause 0.5
    play sound umise_057
    show chain5r_sp with quickflash
    pause 0.5
    scene black with instant
    play audio no59
    show no59
    pause 3
    play sound umise_035
    scene blood_2a
    pause 1
    play sound umise_035
    scene blood_2b
    pause 1
    play sound umise_035
    scene blood_2c
    pause 2
    hid "EVAAAAA????!!?!?!?!"
    "George hat mit magischer Energie ein Loch in Evas Kopf geschossen. Sie fiel rückwärts aufs Bett und war sofort tot."
    "Hideyoshis Schock ist unbeschreiblich, er versucht, sich irgendwie ins Badezimmer zu retten."
    scene mbat_1a
    show hid a11naku4 at m
    play sound umise_027
    with quickflash
    hid "Bitte, George, verschone mich!"
    geo "Dein Flehen kommt zu spät, alter Mann!"
    play sound umise_057
    show chain1r_sp with quickflash
    pause 0.5
    play sound umise_057
    show chain4r_sp with quickflash
    pause 0.5
    play sound umise_057
    show chain5r_sp with quickflash
    pause 0.5
    scene black with instant
    play audio no59
    show no59
    pause 3
    play sound umise_038
    scene blood_1b with vpunch
    pause 1
    "Auch Hideyoshi war sofort tot, es gab keine Chance, diesen Angriff zu überleben."
    extend " George durchbohrte auch seine Stirn."
    geo "Meine Aufgabe ist erfüllt, ich nehme mir die Freiheit, die Bühne für immer zu verlassen und meinen Eltern in die Hölle zu folgen."
    scene black with gradientcirclefade
    stop music fadeout 2
    $ songname = "-"
    pause 2
    scene m2f_p1ar_bg at bgani
    play rain umilse_012
    show rainbackscroll
    show rainfrontscroll
    show m2f_p1ar at bgani
    with gradientwiperight
    pause 0.5
    show kan a11defo1 at m
    play sound umise_019
    kan "Eva-sama, Hideyoshi-sama!"
    extend " Wir haben etwas zu essen vorbereitet."
    show kum a12defo2 at l
    kum "Ohohohohoh,"
    extend " Es gibt saftige Makrelen in meiner hausgemachten Sahnesauce!"
    extend " Lassen Sie sich diese Spezialität nicht entgehen!"
    "Kurze Zeit später standen Kanon und Kumasawa vor der Tür und fragten Eva und Hideyoshi, ob sie mit den anderen essen wollten."    
    kan "Es meldet sich niemand..."
    kum "Eva-sama! Hideyoshi-sama! Können Sie mich hören?"
    extend " Antworten Sie bitte!"
    play sound umise_031
    kan "Ich muss die Tür öffnen!"
    window hide
    scene black with instant
    play audio umise_032
    show chain
    pause 3
    play audio umise_032
    scene m_door1 at bgani
    play rain umilse_012
    with fastdissolve
    pause 1
    show kan a11defo1 at m
    $ songname = "Lure"
    show screen showsong
    play music umib_018
    kan "Die Türkette ist angebracht... Ich komme nicht durch!"
    extend ".....Ich höre Wasser plätschern, das muss die Dusche sein, sind sie im Bad?"
    scene m2f_p1ar_bg at bgani
    play rain umilse_012
    show rainbackscroll
    show rainfrontscroll
    show m2f_p1ar at bgani
    with quickergradientwiperight
    pause 0.5
    show gen a11defo1 at m
    gen "Was ist mit den werten Gästen?"
    show kan a13defo2 at r
    kan "Sie antworten nicht, die Tür geht nicht auf, ich brauche einen Bolzenschneider wegen der Kette."
    gen "Im Dienstraum sollte sich einer befinden."
    kan "Alles klar, ich hole es schnell."
    extend " Kumasawa! Holen sie die anderen her!"
    show kum a12majime1 at l
    kum "Ohohohoh, wird gemacht!"
    hide kum
    hide gen
    "Kumasawa und Genji machten sich sofort auf den Weg, um den anderen zu sagen, dass mit Eva und Hideoyshi etwas nicht stimmte."
    scene black with fastdissolve
    "Battler, Jessica, Natsuhi, Maria und Shannon machten sich sofort auf den Weg."
    scene m2f_p1ar_bg at bgani
    play rain umilse_012
    show rainbackscroll
    show rainfrontscroll
    show m2f_p1ar at bgani
    with quickergradientwiperight
    show but b11odoroki3 at m
    pause 0.5   
    but "Kanon-kun, was ist mit den beiden?"
    show nat a33hisu1 at r
    nat "Ich ahne übles!"
    extend " Bitte sag mir, dass es nicht das ist, was ich denke!"
    nat "Schon wieder so ein Gekritzel??"
    show kum a12majime1 at l
    kum "Das war eben noch nicht hier!"
    hide kum
    show kan a13defo2 at l
    kan "Eva-sama und Hideyoshi-sama haben nicht auf mich reagiert..."
    extend " Deshalb musste ich die Türkette mit einem Bolzenschneider durchtrennen."
    kan "Als ich zurück kam, war dieses Symbol auf der Tür!"
    hide but
    hide kan
    hide nat
    show mar a22akuwarai2 at m
    play sound umise_024
    scene magicsquare_moon1 with fastdissolve
    mar "Kihihihihihihihih!!"
    mar "Das ist der erste magische Kreis des Mondes!"
    extend " Das Design des magischen Kreises ähnelt der Darstellung einer Tür. Der hebräische Vers darauf ist Psalm 107:16 entnommen und lautet:" 
    mar "'Denn er hat eherne Tore zerbrochen und eiserne Riegel durchschnitten'."
    mar "Die Hexe lässt sich nicht einmal von einer Türkette aufhalten!"
    extend " Kihihihihihihihi!!!"
    scene m2f_p1ar_bg at bgani
    play rain umilse_012
    show rainbackscroll
    show rainfrontscroll
    show m2f_p1ar at bgani
    show but a11aseru5 at l
    play sound umise_012
    show mar a22sakebu1 at m
    with vpunch
    hide mar with quickgradientwipedown
    play sound umise_013
    mar "Auauauauau, was sollte das?"
    but "Quatsch nicht so viel!"
    extend " Hör auf mit diesem unangenehmen Verhalten in dieser Situation!"
    extend " Hast du überhaupt kein Mitgefühl?"
    but "Deine Mutter ist verstorben. Magische Kreise oder Hexen scheinen dich mehr zu interessieren...."
    extend " Naja, kann mir auch egal sein..."
    extend  " Ich geh jetzt rein!"
    play sound umise_020
    stop rain
    hide but with dissolve
    $ songname = "goldenslaughterer"
    show screen showsong
    play music umib_024
    play sound umise_013
    scene black with quickflash
    play rain umilse_007 volume 0.2
    but "NEIN!!! NEIN!!! NEIN!!!"
    extend " WIESO SCHON WIEDER?"
    but "TANTE EVA!!!!"
    nat "KYAAAAAAAA"
    extend " DAS KANN NICHT WAHR SEIN!!!"
    play sound umise_038
    scene blood_1b with fastdissolve
    "Tante Eva lag auf dem Bett im Gästezimmer."
    extend " Ihr Blut hat das Bettlaken vollständig durchtränkt."
    "In ihre Stirn wurde eine Art Pfahl gerammt."
    extend " In ihr konnte kein Lebenszeichen mehr wahrgenommen werden..."
    window hide
    scene m2f_r4ars_bg at bgani
    show m2f_r4ar at bgani
    window show
    show nan a2fumu1 at m
    pause 0.5
    nan "Sie ist tot. Ihr Puls ist nicht mehr zu spüren."
    extend " Ich kann hier nichts mehr tun."
    "Nanjo überprüfte die Leiche von Eva und stellte fest, dass jede Hilfe zu spät kam."
    hide nan
    show but b23kayasigaru1 at m
    but "Es reicht jetzt endgültig!"
    extend " Das war definitiv einer zu viel!"
    but b25sakebu2 "Diese Grausamkeit muss aufhören. Du hast mich jetzt wirklich zum Feind gemacht!"
    extend " ...Du wirst es noch bitter bereuen, dass du Ushiromiya Battler zum Feind gemacht hast, du gottverdammter Bastard!"
    but "Diese Türkette war doch nur ein ganz mieser Trick!"
    scene black with quickergradientwiperight
    "Das Geräusch einer Dusche war laut zu hören, Battler öffnete vorsichtig die Tür zum Badezimmer."
    play sound umise_034
    show g0102 with quickflash
    jes "Ihhhhkkkssss!!!" 
    extend " Onkel Hideyoshi? Was ist mit dir passiert??"
    extend " Ich kann das alles nicht mehr....."
    kum "Leck mich doch am Zückerli, wir sind bestimmt die nächsten!!"
    extend " Ihihihihhih!!!"
    "Hideoyoshi lag nackt in der Badewanne. Ein Pfahl wurde ihm wie schon bei Eva in die Stirn gerammt."
    extend " Das Wasser aus dem Duschkopf plätschert ununterbrochen auf den Rücken des Mannes."
    stop rain
    extend " Das ist eine enorme Wasserverschwendung. Die Dusche wurde schnell abgestellt."
    "Battler war von Wut und Traurigkeit überwältigt. Seine Emotionen kochten buchstäblich hoch."
    window hide
    scene m2f_r4ars_bg at bgani
    show m2f_r4ar at bgani
    window show
    play sound umise_013
    show but b25sakebu2 at m with vpunch 
    pause 0.5
    but "Ich bin sehr wütend und kann es nicht richtig ausdrücken."
    extend " ...BEATRICE ist nichts weiter als ein Märchen, damit wir die Fassung verlieren!"
    but "Es kann niemand unsichtbar existieren und einfach so Menschen töten!"
    extend " Ich werde dich finden!!!" 
    extend " Ich werde dich packen und eigenhändig in die Hölle schicken!!!"
    but "Wenn ich dich in die Finger bekomme, wirst du dir wünschen nie geboren worden zu sein!"
    extend " GNHAAAAAAAAAAAAAAAAAAAAAAAAAAAA!!!!!!"
    extend " BEATRICEEEEEEEEEEEEE!!!!!"
    window hide
    pause 2
    $ songname = "-"
    call chapterendb from _call_chapterendb_1
    pause 1
    play audio umise_030
    show eva a11hohoemi1 at m with fastdissolve
    pause 0.3
    scene black with instant
    play audio umise_046
    scene blood_1b with instant
    pause 0.5
    scene black with instant
    play audio umise_030
    show hid a11defo1 at m with fastdissolve
    pause 0.3
    scene black with instant
    play audio umise_046
    scene blood_2b with instant
    pause 0.5
    scene black with instant
    play audio umise_030
    show no83_0051
    show bea a11akuwarai4 at m with fastdissolve
    pause 1
    scene black with instant
    play audio umise_046
    show text _("Zur Zeit der zweiten Dämmerung:\nsollen die Übriggebliebenen die beiden,\ndie sich nahe stehen, auseinanderreißen.")
    pause 7
    scene black with kanon_r 
    pause 3
    show screen clockschoolch2
    play sound "<from 0 to 5>/audio/sfx/umilse_1050.ogg"
    pause 10
    hide screen clockschoolch2 with dissolve
    pause 2
    ## Kapitel 2 Ende
    $ chapter = "Verdacht"
    $ songname = "-"
    $ save_name = _("EpisodeX Illusion of the golden witch\nVerdacht")
    show screen showch
    ## Kapitel 3 Verdacht
    pause 2
    scene g_o1ar
    play rain umilse_012
    play wind umilse_005
    show rainbackscroll
    show rainfrontscroll
    with gradientcirclefade
    $ songname = "Dead Angle"
    play music umib_039
    show screen showsong
    "Verzweiflung macht sich unter denen breit, die noch übrig geblieben sind."
    extend " Inzwischen wurde die Villa verlassen und im Gästehaus Zuflucht gesucht."
    "Die Überlebenden beten einfach, dass von nun an niemand mehr sterben muss."
    scene glob_1ar_bg at bgani
    stop wind fadeout 2
    show rainbackscroll
    show rainfrontscroll
    show glob_1ar at bgani
    with gradientcirclefade
    show nat a12defo1 at l
    pause 0.5
    nat "Ich weiß nicht, ob sich der Täter nur in der Villa aufhält. Aber hier gibt es etwas mehr zu essen."
    show jes a11naku3 at r
    jes "Warum passiert das alles? War es notwendig, auch nur einen von ihnen zu töten?"
    show nan a1defo1 at m
    nan "Jessica-chan, nur der Täter selbst kennt sein Motiv."
    extend " Es nützt leider nichts, darüber nachzudenken, so sehr ich deinen Schmerz auch fühle."
    "Jessicas Worte trafen einen Nerv, denn niemand hat auch nur die geringste Ahnung, warum Menschen sterben."
    hide nan
    hide nat
    jes a11majime1 "Wo steckt eigentlich Großvater die ganze Zeit?"
    show gen a11defo1 at l
    gen "Der Herr befindet sich noch in seinem Arbeitszimmer."
    jes a11tereru1 "Natürlich... Hier geht alles den Bach runter und er versteckt sich in seiner stinkenden Hütte!"
    extend " Wahahahaha....."
    hide gen
    show kan a13defo2 at l
    kan "Jessica-sama, der Herr ist ein alter Freund der Hexe, sie würde ihn nicht ohne weiteres töten."
    hide kan
    hide jes
    show but a11aseru1 at m
    but "Diese Hexenlegende, von der ich gehört habe, hat damit zu tun, dass Großvater von der Hexe 10 Tonnen Gold bekommen haben soll."
    show kum a12defo2 at r
    kum "Ohohohoh..." 
    extend " Das ist in der Tat wahr, und das Gold gibt es wirklich!"
    kum "Das Rätsel der Inschrift soll direkt dorthin führen."
    extend " Bisher ist es jedoch niemandem gelungen, dieses zu lösen."
    show mar a22akuwarai2 at l
    mar "Kihihihihihihihihih"
    extend " Ich habe das ganze Rätsel aufgeschrieben."
    extend " Vielleicht sollten wir endlich damit anfangen, denn das war von Anfang an unsere Siegbedingung."
    hide kum
    show nat a11ikari1 at r
    nat "Maria! Dafür haben wir jetzt keine Zeit!"
    but a11niramu3 "Ich weiß auch nicht, wie uns dieses Rätsel weiterhelfen soll."
    mar a11uuu1 "Uu~!"
    extend " BEATRICE sagte, was passieren würde, am Abend vor der ersten Dämmerung!"
    nat "Du meinst den Brief, den du von woher bekommen hast?"
    but "Ich erinnere mich, dass da etwas stand, dass wir das Rätsel lösen sollten, bevor die Zinsen fällig werden, weil Großvater den Vertrag mit ihr gekündigt hat."
    hide nat
    show jes a23majime1 at r
    jes "Und dass sie alles von der Familie Ushiromiya bekommt, plus Zinsen, und diese Zinsen sind......"
    mar a22akuwarai2 "Unsere Leben!"
    extend " Kihihihihihihi!!!"
    mar "Die einzige Möglichkeit, alles zurückzubekommen, ist das Rätsel der Inschrift zu lösen!"
    hide mar
    hide but
    hide jes
    show nan a2fumu1 at m
    nan "Ich habe einmal versucht, diese Inschrift zu entziffern, aber ich bin daran verzweifelt, und das, obwohl ich Kinzo-san seit den alten Tagen kenne."
    nan "Aber wie heißt es so schön? Man kann einem Menschen nur vor den Kopf sehen, nicht in den Kopf."
    hide nan
    show jes b22warai1 at r
    jes "Lass uns lesen, was auf der Inschrift stand, Maria-chan..."
    show but b11warai2 at l
    but "Um ehrlich zu sein, ich bin auch daran interessiert, ich habe mir das noch nie vorher durchgelesen."
    show mar a11niyari1 at m
    mar "Bitte sehr, prägt es euch gut ein, Kihihihihi!!"
    "Maria kramt ein wenig in ihrer Handtasche und holt ein seltsames Buch heraus, blättert ein wenig darin und beginnt vorzulesen."
    mar "Seht den Süßfischfluss, der durch meine geliebte Heimatstadt fließt. Ihr, die ihr das Goldene Land sucht, folgt seinem Weg stromabwärts auf der Suche nach dem Schlüssel."
    hide jes
    show nat a43headache1 at r
    nat "Wir haben schon jetzt keine Chance, denn keiner von uns weiß, wo Vaters alte Heimat war."
    extend " Warte, Genji, weißt du es vielleicht?"
    hide but
    show gen a11defo1 at l
    gen "Entschuldigung, ich weiß es nicht."
    nat "Verdammt... Aber Eva wusste es, ich weiß es."
    hide gen
    show jes a23majime1 at l
    jes "Wie können sie wohl schlecht danach fragen."
    hide nat
    show but b23nayamu2 at r
    but "Das ist ja abgefahren, ich weiß zwar nicht, was Süßfischfluss heißt, aber die Morde liefen bislang exakt wie hier niedergeschrieben."
    but "Ich glaube aber, dass jemand ohne Japanischkenntnisse dieses Rätsel nicht lösen kann."
    jes "Zuerst waren es sechs außerwählte vom Schlüssel, dann Eva und Hideyoshi als die beiden, die sich nahe stehen und jetzt sind wir bei?"
    mar "Preist meinen noblen Namen, die dritte Dämmerung!"
    but "Da kommen noch ein paar Dämmerungen mit Stichen ins Knie, Bauch, Bein und so weiter, wie verrückt."
    stop music
    scene black with instant
    nat "Ihr vier, nehmt sofort die Hände hoch!"
    "Plötzlich verstummten nach diesem Schrei alle Gespräche, Natsuhi richtete ihre Waffe auf das Personal."
    "Während sich das Thema auf die Hexeninschrift konzentrierte, tauchte neben den Bediensteten, die im Hintergrund zusahen, ein Briefumschlag auf."
    $ songname = "Fishy Aroma"
    play music umib_019
    scene glob_1ar_bg at bgani
    show rainbackscroll
    show rainfrontscroll
    show glob_1ar at bgani
    with gradientcirclefade
    show screen showsong
    show c_e0101_wall
    show c_e0101_a
    with quickgradientwipeleft
    nat "Woher kommt dieser Umschlag und warum ist er gerade bei euch vier?"
    extend " Überlegt euch jetzt gut, was ihr mir antwortet!"
    show kum a12majime1 at leftedge
    kum "Bitte, Fräulein Natsuhi-sama, das muss ein Irrtum sein!"
    extend " Bitte nehmen Sie die Waffe runter!"
    hide c_e0101_a
    show c_e0101_b
    nat "Ich hatte schon die ganze Zeit ein mulmiges Gefühl bei euch Bediensteten!"
    extend " Wir sind hier mit der Inschrift beschäftigt und ganz plötzlich taucht in eurer Nähe ein Briefumschlag auf??"
    extend " Ich weiß ganz genau, dass da gerade eben noch keiner war!"
    nat "Ihr könnt gerne jemand anderen für dumm verkaufen!"
    hide kum
    hide c_e0101_b
    hide c_e0101_wall
    show but b22odoroki2 at m
    but "Also hat das jemand heimlich dort hingelegt?"
    show nan a2fumu1 at rightedge
    nan "Die Möglichkeit besteht, aber wer sollte es gewesen sein?"
    hide but  
    hide nan
    show c_e0101_wall
    show c_e0101_b
    with quickergradientwipeleft
    nat "Vielleicht du, Kumasawa, die immer zu Streichen aufgelegt ist. Oder du, Shannon, die den ganzen Tag nur träumt!"
    show sha a11odoroki1 at leftedge
    sha ".....Huh... Fräulein Natsuhi-sama....."
    nat "Kanon du bist auch nicht aus dem Schneider, deine Fähigkeit deine Präsenz fast vollständig zu verbergen, ist noch am allermeisten Verdächtig!"
    hide sha
    show kan a13defo2 at leftedge
    kan "Fräulein Natsuhi-sama Ich..."
    nat "Genji, du warst von allen Bediensteten immer Vater am nächsten, du hättest es für ihn tun können."
    hide kan
    show gen a21kashikomari1 at leftedge
    gen "........."
    scene black with dissolve
    "Natsuhi ist sich ganz sicher: Einer der vier ist der Täter!"
    extend " ...Es ist unmöglich, dass ein solcher Brief aus dem Nichts auftaucht..."
    "Entweder handelte es sich um reine Absicht, oder der Täter war bei der Platzierung des Briefes nicht geschickt genug gewesen."
    scene glob_1ar_bg at bgani
    show rainbackscroll
    show rainfrontscroll
    show glob_1ar at bgani
    with quickergradientwiperight
    show nat a17ikari2 at l
    nat "Ihr alle kennt die Wege auf der Insel genau, es wäre ein Leichtes für euch, die Morde geschickt zu begehen, ohne erwischt zu werden!"
    nat "Es wäre das Beste für uns, wenn wir uns trennen würden!"
    nat "Battler, Jessica, Maria, Nanjo und ich bleiben hier!"
    nat "Wir haben alle ein Alibi, ihr nicht!"
    hide nat
    show but b11oya1 at l
    but "Wollen wir sie wirklich von hier verbannen?"
    show mar a22akuwarai2 at r
    mar "Kihihihihihihihi!!!"
    extend " BEATRICE wird sie opfern für die Dämmerungen, die noch kommen werden!"
    hide but
    hide mar
    show kum a12majime1 at r
    kum "Natsuhi-sama, vielleicht sollten wir noch einmal darüber reden!"
    show nat a17ikari2 at l
    nat "Es tut mir leid, ich will euch nicht verdächtigen, aber ich kann euch allen nicht trauen..."
    extend " Bitte geht zurück in die Villa."
    extend " Ich bete zu Gott, dass euch nicht passiert."
    nat "Aber es ist auch zu riskant, euch hier zu behalten, wenn der Täter wirklich einer von euch ist."
    nat "Wenn ich euch in den Tod schicke, dann soll die Hexe mich auch mitnehmen, denn ich habe es verdient."
    show gen a21kashikomari1 at m
    gen "Das war ein Befehl unserer Vorgesetzten, wir müssen jetzt gehen."
    kum "Passt auf Euch auf!"
    nat "Es tut mir so unendlich leid, bitte überlebt!"
    "Natsuhi muss eine folgenschwere Entscheidung treffen. Schließlich kann der Brief nicht von denjenigen, die sich mit der Inschrift befassten, platziert worden sein."
    scene black with dissolve
    play sound umise_016
    "Die vier verdächtigen Bediensteten haben nun das Gästehaus verlassen und laufen in Richtung Villa."
    "Natsuhi selbst fühlt sich am schlimmsten von allen, denn es besteht die Möglichkeit, dass sie die vier gerade in den Tod geschickt hat."
    "Aber auch in dieser Situation wäre es viel zu riskant gewesen, die vier hier zu behalten."
    scene glob_1ar_bg at bgani
    show rainbackscroll
    show rainfrontscroll
    show glob_1ar at bgani
    with quickergradientwiperight
    show mar a11niyari1 at m
    mar "Wollt ihr nicht sehen, was in dem Brief steht?"
    show but b22nayamu1 at l
    but "Ich habe eigentlich gar keine Lust dazu, da kommt bestimmt so was wie 'Ha ha, ihr habt die anderen rausgeschmissen, jetzt bringe ich die um'. Weil das hat sie erwartet."
    show jes a11majime1 at r
    jes "Machen wir ihn erst einmal auf!"
    "Vorsichtig öffnet Jessica den Brief, der mit dem Siegel der Familie Ushiromiya versiegelt ist."
    play sound sysse_page
    scene letter1 with quickgradientwiperight
    ntxt "Sehr geehrte Ushiromiya Familie,"
    ntxt "ich hoffe, das kleine Rätsel von Kinzo-sama gefällt Ihnen."
    extend " Es gibt hoffentlich kein Missverständnis, dass sie jetzt nur noch ihre Zeit absitzen können."
    extend " Sobald der nächste Tag um Mitternacht anbricht, gewinne ich automatisch, daran führt kein Weg vorbei."
    extend " Ich bitte Sie also, das Rätsel meiner Inschrift zu lösen, um von mir all das zurückzubekommen, was Sie verloren haben."
    extend " Aber ich bin mir sicher, dass Sie nicht gewinnen werden. Also preist meinen noblen Namen!"
    ntxt "BEATRICE, die Goldene"
    nvl clear
    scene glob_1dr_bg at bgani
    show rainbackscroll
    show rainfrontscroll
    show glob_1dr at bgani
    with quickergradientwiperight
    show but a21kuyasigaru1 at m
    but "Will die uns verarschen?"
    extend " Wir sollen ernsthaft das Rätsel lösen?"
    "Für BEATRICE scheint das alles nur ein Spiel zu sein, das man gewinnen oder verlieren kann..." 
    extend " Battler und die anderen können nicht glauben, was sie da lesen."
    show nat a43headache1 at r
    nat "Meine Kopfschmerzen lassen es nicht zu, darüber nachzudenken."
    but "Das ist alles Quatsch! Wir haben nicht das Wissen, um es zu lösen!"
    show jes a23majime1 at l
    jes "Stattdessen sollten wir uns ein wenig ausruhen."
    extend " Wir müssen bereit sein, wenn der Täter wieder zuschlagen will..."
    but b22nayamu1 "Gute Idee, vielleicht hat ja jemand einen Geistesblitz und wir können das Rätsel in den nächsten sechs Stunden lösen."
    nat "Ohne Eva können wir es sowieso nicht lösen..."
    hide but
    hide jes
    hide nat
    show mar a22akuwarai2 at m
    mar "Das ist ein Riesenfehler!"
    extend " Kihihihihi!!"
    pause 1
    scene black with instant
    play audio umise_046
    show text _("Zur Zeit der dritten Dämmerung:\nPreist meinen noblen Namen!")
    pause 5
    scene black with kanon_r 
    pause 3
    stop music fadeout 2
    stop rain fadeout 2
    show screen clockschoolch3
    play sound "<from 0 to 5>/audio/sfx/umilse_1050.ogg"
    pause 10
    hide screen clockschoolch3 with dissolve
    pause 2
    ## Kapitel 3 Ende
    $ chapter = "Die Goldene Hexe"
    $ songname = "-"
    $ save_name = _("EpisodeX Illusion of the golden witch\nDie Goldene Hexe")
    show screen showch
    ## Kapitel 4 Die Goldene Hexe
    play rain umilse_023
    pause 2
    but "Das Telefon klingelt?"
    extend " Wurden die Leitungen nicht getrennt?"
    "Einige Stunden später klingelt aus heiterem Himmel plötzlich das Telefon im Gästehaus."
    scene glob_1dr_bg at bgani
    show rainbackscroll
    show rainfrontscroll
    show glob_1dr at bgani
    with quickergradientwiperight
    show jes a23majime1 at l
    jes "Vielleicht hat der Täter nur die äußeren Leitungen durchtrennt."
    show nat a33hisu1 at r
    nat "Battler-kun übernimmt das für mich, ich habe zu starke Kopfschmerzen."
    hide nat
    hide jes
    show but b11odoroki3 at m
    but "Da bin ich mal gespannt."
    stop rain
    but "Hallo?....." 
    extend " Wer ist da?"
    $ songname = "Happy Maria!"
    play music umib_104
    show screen showsong
    play sound umise_002
    scene black with quickflash
    bea "<congratulations>"
    bea "<I am fineeeee and youuuuuuuu?~>"
    extend " Kyahahahahahahahahha!!!!!"
    scene glob_1dr_bg at bgani
    show rainbackscroll
    show rainfrontscroll
    show glob_1dr at bgani
    with quickergradientwiperight
    show but a11niramu3 at m
    but "Wer zum Teufel bist du?"
    extend " ....Willst du mich auf den Arm nehmen? Was soll das?"
    bea "<In english please!>"
    extend " Komm schon, das hast du doch die ganze Zeit gemacht, als du ein Kind warst, Ushiromiya Battler!"
    "Spöttisches Englisch dröhnt aus der Ohrmuschel, die Stimme hat Battler noch nie zuvor gehört."
    but b22odoroki2 "Du..." 
    extend " Du bist absolut irre!"
    but "Sag mir sofort, wer du bist!"
    scene mlib_1a_bg at bgani
    show rainbackscroll
    show rainfrontscroll
    show mlib_1a at bgani
    $ bea_pose ="a11"
    $ bea_face = "akuwarai4"
    show bea at m
    play sound umise_002
    with fastdissolve
    pause 1
    voice "audio/voice/bea/bea_001.wav"
    bea bea_001 "Komm schon... rate doch mal..."
    voice "audio/voice/bea/bea_002.wav"
    extend bea_002 " Du kannst eine Reise nach Hawaii gewinnen!"
    $ bea_face = "akuwarai2"
    voice "audio/voice/bea/bea_003.ogg"
    extend bea_003 " hahaha.... Kyahahahahahahah!!"
    but "BEATRICE?" 
    extend " .....Du bist BEATRICE?!!!"
    play sound umise_002
    scene black with quickflash
    bea "<Yeessssssss I aaaaaammmmm!!>"
    extend " Kyahahahahahhahahah!!!!!!"
    extend " Ich wollte euch nur gratulieren, denn ich lade euch ins Goldene Land ein!"
    scene beabut
    show but b11kuyasigaru1 at rightedge
    show bea a11akuwarai5 at leftedge2
    with quickergradientwiperight
    but "Das kannst du dir woanders in den Arsch stecken!"
    extend " Was ist aus Shannon, Kumasawa und den anderen geworden?"
    bea "Ohhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh"
    extend " Ich habe sie geopfert für meine Auferstehung..."
    extend " Das ist doch fantastisch, oder nicht????" 
    extend " Uhhhshirooomiyaaa Battorraaaaa????"
    but a21kuyasigaru1 "Ich werde dir dumme Bitch niemals verzeihen!"
    extend " Wie kannst du es nur wagen???"
    scene mlib_1a_bg at bgani
    show rainbackscroll
    show rainfrontscroll
    show mlib_1a at bgani
    show kin a11warai1 at r
    kin "Wahahahahahaha!!"
    extend " Du bist heute sehr gut gelaunt, BEATRICE."
    show bea a11warai1 at l
    bea "Hey Kinzo!"
    extend a11akuwarai4 " Wie wäre es?" 
    extend " Der Wein war arsch teuer, machen wir ihn auf!"
    extend " Danach können wir uns ja gegenseitig mit der leeren Flasche die Köpfe einschlagen!"
    bea "Meine Auferstehung ist ein Grund zum Feiern!"
    extend " Keheheheheheh!!"
    kin "Oh, du bist ein bisschen zu aufgeregt!"
    extend " Beruhige dich erst einmal."
    scene black with fastdissolve
    but "Ist der alte Sack auch bei dir?"
    extend " Was hast du vor mit deinem betrunkenen Arsch?"
    extend " Wo sind Shannon und die anderen?"
    extend " Wohin hast du sie verschleppt?"
    bea "Nicht so weit weg, wie du denkst!" 
    extend " Schau mal in der Villa vorbei, ich wünsche gutes Gelingen!"
    extend " Kyahahahaahhaha!!!!"
    scene glob_1dr_bg at bgani
    show rainbackscroll
    show rainfrontscroll
    show glob_1dr at bgani
    with quickergradientwiperight
    show but b25sakebu2 at m
    but "Dich schnapp ich mir als Nächstes, du wirst schon sehen, du Miststück!"
    play sound umise_012
    stop music fadeout 1
    play rain umilse_012
    $ songname = "-"
    "Wütend legt Battler auf, der Täter hat auch noch die Dreistigkeit, sich persönlich zu melden und sich über Battler lustig zu machen..."
    hide but
    show jes a11atya3 at r
    jes "War das BEATRICE?"
    extend " Was ist passiert?"
    show but b11kuyasigaru1 at l
    but "Wir müssen sofort zur Villa, es könnte schon zu spät sein!"
    show nat a32ikari1 at m
    nat "Dann schnell!"
    stop rain fadeout 2
    scene black with gradientcirclefade
    pause 1
    scene mlib_1b_bg
    show rainbackscroll
    show rainfrontscroll
    show mlib_1b
    with gradientcirclefade
    "Während sich die vier auf den Weg zur Villa machen, sind Kinzo und BEATRICE immer noch in Kinzos Arbeitszimmer."
    show kin a11warai2 at r
    kin "Heute ist ein großer Tag, endlich durfte ich dein Lächeln wiedersehen!"
    extend " Wenn du mir jetzt mein Leben wegnimmst, würde es mir nichts ausmachen!"
    show bea a11gaman4 at l
    bea "Ich denke mir einfach, dass das genau das ist, was ich tun werde!"
    kin a11fukigen1  "Ich schenke dir gerne mein Leben!"
    extend " Nichts hält mich mehr in dieser Welt..."
    bea a11futeki1 "So soll es sein *Gackle*Gackle*"
    pause 1
    show no64
    play sound umise_055
    pause 1
    play sound umise_055
    pause 1
    play sound umise_055
    kin "ahhhhhhhhhhhhhhhhhrggggggghhhhhhhhhhhhhhh"
    extend " OHHHHH BEATOOORICHEEEEE!!!!!"
    extend " ICH DANKE DIRRRR!!!!!"
    "Mit einem Fingerschnippen geht Kinzos Körper in Flammen auf, Haut und Kleidung verbrennen vollständig."
    scene black with instant
    play sound umise_012
    "Der alte Mann konnte der Hexe noch in seinen letzten Momenten danken."
    extend " Er verließ diese Welt ohne Reue!"
    bea "Ushiromiya Kinzo, du gehörst schon lange nicht mehr in diese Welt...."
    extend " Wir sehen uns im Goldenen Land wieder..."
    pause 2
    show m_o1a
    play wind umilse_005
    play rain umilse_012
    show rainbackscroll
    show rainfrontscroll
    with gradientcirclefade
    play music umib_036
    $ songname = "Play"
    scene mhal_1ar_bg at bgani
    stop wind fadeout 1
    show rainbackscroll
    show rainfrontscroll
    show mhal_1ar at bgani
    show expression(CustomParticles("images/system/particle.png", 10))
    with gradientcirclefade
    "Inzwischen sind die vier in der Eingangshalle angekommen."
    extend " Von den verbannten Bediensteten fehlt noch jede Spur."
    show but a11niramu3 at r
    but "Wo sollen wir den Anfang machen?"
    show jes a23majime1 at l
    jes "Hier liegt ein Brief auf dem Boden!"
    "Jessica nahm den Brief auf und öffnete ihn."
    ntxt "Ich bin im Wohnzimmer, komm und hol mich, Ushiromiya Battler!!"
    but b22odoroki2 "Die macht sich über mich lustig!"
    hide but
    hide jes
    "Alle rannten so schnell wie möglich zur Wohnzimmertür!"
    extend " Jessica versucht sofort, die Tür zu öffnen!"
    scene m2f_p1br_bg at bgani
    stop wind fadeout 1
    show rainbackscroll
    show rainfrontscroll
    show m2f_p1br at bgani
    show expression(CustomParticles("images/system/particle.png", 10))
    with gradientcirclefade
    show jes a11atya2 at m
    play sound umise_032
    pause 0.5
    play sound umise_032
    pause 1.0
    jes "Die Tür zum Wohnzimmer ist verschlossen!"
    extend " Es war noch geöffnet, als wir zum Gästehaus gingen!"
    show but b22nayamu2 at rightedge
    but "Lass mich mal!"
    play sound umise_032
    pause 0.5
    play sound umise_032
    pause 1.0
    extend b22odoroki2 ".............Sie ist zu........"
    jes "Sagte ich bereits, wieso glaubst du mir nicht?"
    but "Ich wollte es einfach selbst ausprobieren, hehe...."
    show nat a11komaru1 at l
    nat "Haben wir einen Schlüssel?"
    but b11odoroki3 "Die Generalschlüssel waren sicher noch bei den Bediensteten!"
    nat a33hisu1 "Habe ich wieder mal toll gemacht."
    jes a11tohoho4 "Mama, gib dir nicht die Schuld, du hattest unser aller Sicherheit im Sinn, es wäre sowieso hierher gekommen!"
    nat a12nayamu1 "Wir könnten versuchen, von außen durch das Fenster einzusteigen."
    hide but
    show nan a1defo1 at rightedge
    nan "Vielleicht haben wir noch eine Chance, jemanden zu retten!"
    jes a11warai1 "Gute Idee!"
    scene black with gradientcirclefade
    pause 1
    scene m_cy1a
    show rainbackscroll
    show rainfrontscroll
    play wind umilse_005
    "Da man nicht daran gedacht hatte, den Verbannten wenigstens einen Generalschlüssel abzunehmen, mussten sie improvisieren."
    "Battler nimmt einen großen Stein und will ihn gegen das Wohnzimmerfenster donnern."
    play sound umise_020
    pause 1
    play sound umise_1006
    scene black with instant
    "Die Scheibe wurde von Battler eingeschlagen und das Loch ist nun groß genug, um das innere Schloss zu erreichen und zu öffnen."
    $ songname = "-"
    stop music fadeout 2
    "Battler betritt vorsichtig das Wohnzimmer und sieht jemanden..."
    play music umib_024
    stop wind
    $ songname = "goldenslaughterer"
    show screen showsong
    scene m1f_s1cr at bgani
    show but b23kayasigaru1 at m
    play sound umise_012
    with instant
    but "Kanon-kun!!!"
    jes "Battler-kun, was siehst du?"
    but "Kanon-kun ist hier drin!"
    extend " Nanjo-sensei, sehen Sie ihn bitte an!"
    play sound umise_038
    scene blood_1a
    nan "Er atmet nicht mehr, er ist vor kurzem von uns gegangen."
    play sound umise_038
    scene blood_1b
    extend " Sein Kopf wurde durchbohrt, aber der Pfahl hatte wohl keinen Halt und ist herausgefallen."
    but "Verdammt! Verdammt! Verdammt!"
    extend " Die anderen sind sicher auch ermordet worden!"
    scene m1f_s1cr at bgani
    show jes b33naku1 at m
    jes "KANON-KUN!!!! *sob*sob*"
    extend " ICH VERFLUCHE DICH, BEATRICE!!!"
    jes "WARRRUMMMM NUUURRRR??!?!?!?!?"
    extend " .........*schnief*.........."
    "Es war dieser Anblick, der Jessica mit am meisten berührt hat."
    extend " Schließlich mochte sie ihn immer ein bisschen mehr als die anderen."
    hide jes
    show mar a22akuwarai2 at m
    mar "Kihihihihihi!"
    extend " Stich in den Kopf und töte!"
    extend " Von jetzt an wird alles ganz schnell vorbei sein!"
    show but a11aseru5 at l
    but "Und jetzt halt endlich die Klappe!"
    extend " Das kann doch nicht wahr sein, Maria!"
    extend " Du hast jetzt Redeverbot bis zum bitteren Ende!"
    but "Kein Wort mehr!"
    mar a22defo1k  "Uu......"
    hide but
    hide mar
    show nat a32ikari1 at m
    nat "Da liegt ein Brief!"
    "Natsuhi öffnet vorsichtig den Brief und nimmt zwei Schlüssel heraus."
    nat "Das ist der Generalschlüssel von Kanon und der Schlüssel zu meinem Zimmer oben!"
    extend " Wir müssen sofort dorthin!"
    pause 0.5
    scene black with instant
    play audio umise_030
    show kan a11defo1 at m with fastdissolve
    pause 0.3
    scene black with instant
    play audio umise_046
    scene blood_2b with instant
    pause 0.5
    scene black with instant
    play audio umise_030
    show no83_0051
    show bea a11akuwarai5 at m with fastdissolve
    pause 1
    scene black with instant
    play audio umise_046
    show text _("Zur Zeit der vierten Dämmerung:\nStich in den Kopf und Töte!")
    pause 3
    scene black with kanon_r 
    "So schnell wie möglich eilten sie zu Natsuhis Zimmer."
    extend " Die Tür ist tatsächlich auch verschlossen."
    "Battler öffnet die Tür mit Natsuhis Schlüssel."
    play sound umise_017
    scene white zorder 99
    with kanon_r
    scene black with fastdissolve
    scene mnat_1ar_bg at bgani
    stop wind fadeout 1
    show rainbackscroll
    show rainfrontscroll
    show mnat_1ar at bgani
    show expression(CustomParticles("images/system/particle.png", 10))
    with gradientcirclefade
    show but b11naku1 at m
    but "Kumasawa-baa-chan....."
    extend " Das darf nicht wahr sein, das hast du am wenigsten verdient!"
    play sound umise_038
    scene blood_1ar
    nan "Ihre Brust wurde durchbohrt, wieder mit einem dieser Pfähle."
    extend " Ich kann nur bestätigen, dass sie tot ist."
    scene mnat_1ar_bg at bgani
    stop wind fadeout 1
    show rainbackscroll
    show rainfrontscroll
    show mnat_1ar at bgani
    show expression(CustomParticles("images/system/particle.png", 10))
    with quickgradientwiperight
    show jes a11naku3 at m
    jes "Hier ist auch ein Brief...." 
    extend " Wieder ein Generalschlüssel und der andere Schlüssel führt in mein Zimmer!"
    pause 0.5
    scene black with instant
    play audio umise_030
    show kum a11defo2 at m with fastdissolve
    pause 0.3
    scene black with instant
    play audio umise_046
    scene blood_2b with instant
    pause 0.5
    scene black with instant
    play audio umise_030
    show no83_0051
    show bea a11akuwarai2 at m with fastdissolve
    pause 1
    scene black with instant
    play audio umise_046
    show text _("Zur Zeit der fünften Dämmerung:\nStich in die Brust und Töte!")
    pause 3
    scene black with kanon_r 
    "Alle rannten so schnell sie konnten in Jessicas Zimmer."
    "Dort wurde die Leiche von Genji gefunden. Sein Bauch war mit einem Pfahl durchbohrt." 
    "Auch hier wurde ein Brief mit einem Generalschlüssel und einem Schlüssel für den Heizungskeller gefunden."
    pause 0.5
    scene black with instant
    play audio umise_030
    show gen a11defo1 at m with fastdissolve
    pause 0.3
    scene black with instant
    play audio umise_046
    scene blood_2b with instant
    pause 0.5
    scene black with instant
    play audio umise_030
    show no83_0051
    show bea a11futeki1 at m with fastdissolve
    pause 1
    scene black with instant
    play audio umise_046
    show text _("Zur Zeit der sechsten Dämmerung:\nStich in den Bauch und Töte!")
    pause 3
    scene black with kanon_r
    scene mboi_1c with gradientcirclefade
    show expression(CustomParticles("images/system/particle.png", 10))
    show but a21kuyasigaru1 at rightedge
    but "Stinkt ja wie die Pest hier drin!"
    show jes a11atya2 at l
    jes "Das ist ja widerlich!"
    show nat a12nayamu1 at m
    nat "Da liegt Vater!"
    jes "Bist du dir da sicher?"
    extend " Ich finde, dass man Kinzo gar nicht mehr wieder erkennen kann..."
    nat "Schau dir seinen Fuß an, er hat sechs Zehen, das hatte nur Vater."
    but a21nayamu2 "Ich glaube, BEATRICE hatte schon nach kurzer Zeit keine Lust mehr auf den Alten!"
    nat "Wie auf der Inschrift beschrieben, steckt der Pfahl in seinem Knie...."
    hide but  
    hide jes
    hide nat
    show nan a1fumu1 at m
    nan "Das ist in der Tat Kinzo-san..."
    extend " Ruhe in Frieden... Alter Freund..."
    "Der Brief, der sich im Heizungskeller befand, enthielt nur den Schlüssel für die Kapelle."
    pause 0.5
    scene black with instant
    play audio umise_030
    show kin a11defo1 at m with fastdissolve
    pause 0.3
    scene black with instant
    play audio umise_046
    scene blood_2b with instant
    pause 0.5
    scene black with instant
    play audio umise_030
    show no83_0051
    show bea a11warai1 at m with fastdissolve
    pause 1
    scene black with instant
    play audio umise_046
    show text _("Zur Zeit der siebten Dämmerung:\nStich in das Knie und Töte!")
    pause 3
    scene black with kanon_r
    scene cha_o2an
    show rainbackscroll
    show rainfrontscroll
    with gradientcirclefade
    play wind umilse_005
    "Alle machten sich so schnell wie möglich auf den Weg zur Kapelle!"
    extend " Natsuhi zückt sofort den Schlüssel und ist zu allem bereit!"
    show nat a32ikari1 at m
    nat "Ich öffne jetzt die Kapelle!"
    play sound umise_017
    scene white zorder 99
    with kanon_r
    scene black with fastdissolve
    "Natsuhi öffnete mit dem Schlüssel die Tür und der Anblick in der Kapelle war wohl der schlimmste an diesem Abend..."
    scene cha_i1ad at bgani
    show expression(CustomParticles("images/system/particle.png", 10))
    show but b26naku2 at m
    play sound umise_013
    with quickflash
    but "Shannon-chan!!!!"
    extend " Neiiiinnnn!!!!!!!"
    but "Warum nur? Warum nur?"
    show jes b33naku1 at l
    jes "Wir werden auch sterben!"
    play sound umise_038
    scene blood_1b   
    "Shannon wurde über dem Altar der Kapelle aufgehängt..."
    extend " Ihr Bein ist durchbohrt und der Pfahl liegt unter ihr auf dem Boden."
    extend " Niemand im Raum konnte sich vorstellen, wie ein einzelner Mörder so etwas Grausames tun konnte..."
    but "BEATRICE wollte für das Finale noch einmal den grausamsten Mord aller Zeiten begehen."
    but "Du hast keinen Respekt vor dem Tod! Das ist das Allerletzte!"
    "Natsuhi öffnete den Brief in der Kapelle, darin war Shannons Generalschlüssel und der Schlüssel zum Wohnzimmer."
    nat "Der Schlüssel in diesem Brief führt ins Wohnzimmer, wo Kanon liegt."
    scene map10
    extend " Eine absolut perfekte Schleife, das ist doch absolut unmöglich!!"
    "Diese Aneinanderreihung von geschlossenen Räumen ist eine perfekte Schleife!"
    extend " Im ersten Raum befindet sich der Schlüssel für den nächsten Raum, bis im letzten Raum der Schlüssel für den ersten Raum gefunden werden kann."
    "Man läuft einmal perfekt im Kreis."
    pause 0.5
    scene black with instant
    play audio umise_030
    show sha a11defo1 at m with fastdissolve
    pause 0.3
    scene black with instant
    play audio umise_046
    scene blood_2b with instant
    pause 0.5
    scene black with instant
    play audio umise_030
    show no83_0051
    show bea a11akuwarai5 at m with fastdissolve
    pause 1
    scene black with instant
    play audio umise_046
    $ songname = "-"
    stop music
    show text _("Zur Zeit der achten Dämmerung:\nStich in das Bein und Töte!")
    pause 3
    scene black with kanon_r
    play music umib_159
    $ songname = "Infant Queen Bee"
    show screen showsong
    scene cha_i1ad at bgani
    show expression(CustomParticles("images/system/particle.png", 10))
    show but b26naku2 at m
    play sound umise_013
    with quickflash
    pause 2
    but "Das bringt überhaupt nichts mehr...."
    extend " ....Es bringt überhaupt gar nichts mehr irgendwas...."
    play sound umise_020
    hide but
    pause 0.5
    show nat a32ikari1 at m
    nat "Battler-kun? Wohin gehst du?"
    extend " Bleib bei uns, es ist zu gefährlich!"
    pause 1
    show m_o1a
    show rainbackscroll
    show rainfrontscroll
    with gradientcirclefade
    "Battler stürmte aus der Kapelle und lief auf die Villa zu."
    scene mhal_1ar_bg at bgani
    stop wind fadeout 1
    show rainbackscroll
    show rainfrontscroll
    show mhal_1ar at bgani
    show expression(CustomParticles("images/system/particle.png", 10))
    with gradientcirclefade
    "Er rannte in die Eingangshalle zu dem Bild von BEATRICE, so schnell er konnte."
    scene beato with gradientcirclefade
    but "BEATRICE!!!"
    but "Bist du jetzt zufrieden?"
    extend " Hier und jetzt stell dich mir!"
    extend " Trau dich und leg dich mit mir an!"
    but "Alle Morde sind geschehen, jetzt komm raus!!"
    extend " Dreizehn von uns mussten deinetwegen sterben!!"
    call butterfly1 from _call_butterfly1_3
    bea "*Gacker*Gacker*"
    extend " Was für ein charmanter Mann!"
    "Schier endlose goldene Schmetterlinge tanzten durch die Eingangshalle!"
    extend " BEATRICE wird jeden Moment das Tor zum Goldenen Land öffnen!"
    but "Genau, zeig dich mir!!!"
    extend " Komm schon!!!!" 
    extend " BEATRICEEEEE!!!!!"
    pause 1
    scene black with instant
    stop rain
    play audio umise_046
    show text _("Zur Zeit der neunten Dämmerung:\nWird die Hexe wiederbelebt\nund niemand wird am leben bleiben!")
    pause 5
    scene black with kanon_r
    scene schoolcredit at credits_scroll_school
    pause 90
    stop music fadeout 5
    pause 5
    scene black with kanon_r
    pause 5
    ## Kapitel 3 Ende


































