label schule:
    ##Kapitel 1 - Die sechs außerwählten
    $ chapter = 1001
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
    play music "audio/bgm/umib_018.ogg"
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
    show gen a11defo1 behind rainfrontscroll at r
    show nat a12nayamu1 behind rainfrontscroll at l
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
    scene black with quickergradientwipeleft
    scene warehous_o1an
    show rainbackscroll
    show rainfrontscroll
    show nan a1defo1 behind rainfrontscroll at m
    with gradientwipedownleft
    nan "Ich denke, wir sollten Ruhe bewahren und nichts überstürzen."
    extend " ...Wir sollten erstmal auf einen Schlüssel warten."
    "Genji kehrte kurze Zeit später zurück, doch statt eines Schlüssels hält er eine Feuerwehraxt in der Hand."
    scene black with quickergradientwipeleft
    scene warehous_o1an
    show rainbackscroll
    show rainfrontscroll
    show gen a21kashikomari1  behind rainfrontscroll at m
    with gradientwipedownleft
    gen "Ich bitte um Verzeihung, ich konnte den Schlüssel nicht finden, wir müssen das Schloss zerstören."
    show eva b21akire1go behind rainfrontscroll at r
    eva "Sehr gute Idee!"
    show kan a11defo1 behind rainfrontscroll at l
    kan "Das Tor ist schon sehr alt und dürfte der Axt nicht lange standhalten."
    extend " Einmal durchgebrochen, sollte es einfach sein, das Tor zu öffnen"
    scene black with quickergradientwipeleft
    "Genji beginnt nun das Schloss mit der Axt zu zerstören, die anderen sind zwei Schritte zurück gegangen."
    scene warehous_o1an
    show rainbackscroll
    show rainfrontscroll
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
    window hide
    pause 0.5
    scene g2f_r1b_bg
    show rainbackscroll
    show rainfrontscroll
    show g2f_r1b
    show expression(CustomParticles("images/system/particle.png", 10))
    with quickergradientwipeleft
    pause 1
    window show
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
    window hide
    pause 0.5
    scene g2f_r1b_bg
    show rainbackscroll
    show rainfrontscroll
    show g2f_r1b
    show expression(CustomParticles("images/system/particle.png", 10))
    show but a11defo1 at l
    with quickergradientwipeleft
    window show
    but "Jo, Jessica-chan!"
    extend " Was meinst du mit aufgescheuchten Hühnern?"
    show jes a11majime1 at r
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
    window hide
    pause 0.5
    scene warehous_o2ar
    show rainbackscroll
    show rainfrontscroll
    with quickergradientwipeleft
    pause 0.5
    window show
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
    window hide
    pause 0.5
    scene warehous_o2ar
    show rainbackscroll
    show rainfrontscroll
    with quickergradientwipeleft
    pause 0.5
    show hid a11komaru2 behind rainfrontscroll at m
    pause 0.5
    window show
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
    extend " Wenn du deine Kleider nicht anhättest, wüsste ich gar nicht, wer da vor mir steht."
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
    show hid a11komaru2 at m
    pause 0.5
    hid "Bleib stark, Battler-kun, die Polizei wird den Täter morgen finden und verhaften."
    extend " Ich bin genauso traurig wie du, aber wir dürfen jetzt keine falsche Bewegung machen."
    window hide
    pause 0.5
    scene warehous_i1ar2_bg at bgani
    show rainbackscroll
    show rainfrontscroll
    show warehous_i1ar2 at bgani
    show expression(CustomParticles("images/system/particle.png", 10))
    with quickergradientwipeleft
    show nan a2fumu1 at m
    pause 0.5
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
    "Der Schlüssel zu diesem Gartenschuppen wurde im Schuppen bei der Leiche von Gohda gefunden."
    extend " Normalerweise sollte es doch unmöglich sein, da der Schuppen nur von außen abgeriegelt werden kann."
    nat "Das wird alles immer seltsamer und seltsamer."
    "Auch die bedienstete Shannon sieht sehr bedrückt aus."
    window hide
    pause 0.5
    scene warehous_i1ar2_bg at bgani
    show rainbackscroll
    show rainfrontscroll
    show warehous_i1ar2 at bgani
    show expression(CustomParticles("images/system/particle.png", 10))
    with quickergradientwipeleft
    pause 0.5
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
    call chapterendb
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
    scene blood_2e with instant
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
    $ chapter = 1002
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
    "Nach der Tragödie, zogen sich dich überlebenden in das Wohnzimmer der Villa zurück."
    extend " Dabei ist eine hitzige Diskussion entfacht, wer ein potenzieller Täter sein könnte."
    "Die Lage ist spürbar angespannt seit dem die sechs im Gartenschuppen gefunden wurden."
    extend " Es würde jeden stressen, vorallem, wenn man weiß, dass man auf der Insel aktuell gefangen ist aufgrund des Wetters."
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
    eva " Wir sollten abwarten, bis sich der Sturm verzieht."
    extend " Heißt aber auch, dass wir hier bis morgen früh aussitzen müssen."
    show jes a23majime1 at r
    jes "Was ist, wenn der Mörder wieder zuschlägt?"
    extend " ...Wichtig ist auch, wer der Mörder ist."
    extend " Es ist entweder eine Person, die sich vorher auf die Insel geschlichen hat oder einer von uns."
    window hide
    pause 0.5
    scene m1f_s1cr at bgani
    show nat a11komaru1 at m
    show expression(CustomParticles("images/system/particle.png", 10))
    with quickgradientwipeleft
    window show
    nat "Gut möglich, es wäre einfach gewesen kurz vor dem Taifun die Insel zu erreichen, ohne dass es jemand merkt."
    extend " Auf der anderen Seite benötigt der Täter ein sehr gutes Verständnis über absolut alle Räume und Wege die es hier auf der Insel gibt."
    show but b23nayamu1 at l
    but "In anderen Worten: Der Täter kennt uns sehr gut und ist kein Eindringling von außerhalb."
    but b23kayasigaru1 "Verdammt!" 
    extend " Ich bekomme es nicht in meine Birne, warum jemand von uns irgendwen ermorden sollte..."
    hid "Hey Leute! Ich habe ein paar Waffen gefunden!"
    window hide
    pause 0.5
    scene m1f_s1cr at bgani
    show hid a11defo1 at m
    show expression(CustomParticles("images/system/particle.png", 10))
    with quickgradientwipeleft
    window show  
    "Zwischenzeitlich sollte auf einen Tipp von Genji hin Hideyoshi Kinzos Schrotflinten holen."
    extend " Diese sind von Kinzo modifizierte Varianten, abgesägt mit mehr Munition und weniger Streuung"
    play audio umise_030
    show hid a12defo1 at m
    show eva b24defo1 at l
    show nat a16defo1 at r
    "Waffen besitzen jetzt Hideyoshi, Eva und Natsuhi."
    extend " Die anderen waren entweder zu Jung für Schusswaffen oder haben abgelehnt."
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
    eva "Wir haben jetzt endlich Schrotflinten zur Selbstverteidigung."
    extend " Im Ernstfall wissen wir, wie man damit schießt."
    eva "Es gäbe viele Gründe für dritte Personen uns auszumerzen, vorallem wenn man die Legende des Goldes kennt."
    show nat a16komaru1 at l
    nat "Mein Mann, war immer davon überzeugt, dass Vater sein Gold irgendwo auf der Insel versteckt hat."
    extend " Vor zwei Jahren hat Vater ein Rätsel zusammen mit dem Gemälde dieser Hexe in der Eingangshalle platziert, aber er konnte es nicht lösen."
    show but b11aseru1 at r
    but "Dieses Rätsel sieht aber auch abgefahren aus!"
    extend " 'Zur Zeit der zweiten Dämmerung sollen die, die sich nahe stehen auseinanderreißen' oder sowas."
    but "Wie soll man so auf einen Ort auf der Insel schließen können?"
    but "Ich hab es aber auch ehrlich gesagt nie komplett gelesen."
    hide but
    hide nat
    show eva b24akirenigo at l
    show jes a11atya2 at r
    with dissolve
    jes "Das Rätsel besagt einfach nur, geh zu einem Ort und töte nach einem bestimmten Muster."
    extend " Danach soll BEATRICE auferstehen."
    extend " 'Zur Zeit der neunten Dämmerung, wird die Hexe wiederbelebt, und niemand wird am Leben bleiben'."
    eva b21futeki1 "Die Hexe BEATRICE aus dem Wald, ist bereits ein Gerücht, dass es während unserer Kindheit gegeben hat."
    extend " Wie soll das bitte aussehen?"
    extend " Ein magisches Wesen, tötet uns um sich selber wiederzubeleben?"
    eva "Dieses Rätsel wird doch nur als Deckmantel verwendet!"
    show nat a12nayamu1 at m
    nat "Es wäre aber auch schwachsinnig sich auszudenken, dass irgendjemand sich als BEATRICE verkleidet und die Morde ausübt."
    eva a11hohoemi1 "Sich als BEATRICE verkleiden?"
    extend " Also jemand wie beispielweise Shannon verkleidet sich als Hexe und tötet uns alle?"
    extend " Der Gedanke klingt einfach schon mehr als absurd."
    window hide
    pause 0.5
    scene m1f_s1cr at bgani
    show expression(CustomParticles("images/system/particle.png", 10))
    with quickgradientcirclefade
    show but b11oya1 at m with dissolve
    pause 0.5
    window show
    but "Richtig!"
    extend " Shannon-chan könnte keiner Fliege was zuleide tun."
    show eva b22akire2 at r
    eva "Stille Wasser sind tief, Battler-kun *kicher*"
    extend a11hohoemi1 " Spaß beiseite, dieses unfähige Ding, könnte noch nicht einmal ein Buttermesser in die Hand nehmen."
    hide but
    show nat a11ikari1 at l
    nat "Eva-san! Das war mehr als nur unhöflich gegenüber meiner Angestellten!"
    eva "Oh, entschuldigung!..." 
    extend " ...Kommt bestimmt nicht wieder vor... *kicher*"
    "Eva klingt so, als habe sie eine gewisse Abneigung gegen Shannon."
    extend " Irgendwo ist das auch zu erwarten, schließlich wollte sie nie, dass so eine wie sie etwas mit ihrem verstorbenen Sohn anfängt."
    "Als Reaktion stellt sich Battler schützend vor Shannon, da er nicht möchte, dass Eva so respektlos über sie redet."
    hide eva
    hide nat
    show but a11aseru5 at m
    but "Ich würde Shannon-chan niemals verdächtigen!"
    extend " Sie war am boden zerstört als sie erfahren hat, das George-aniki ermordet wurde."
    show eva b22akire2 at l
    eva "Meine Güte, Battler-kun, ich verdächtige sie nicht, das war doch nur ein Beispiel."
    but "Das war überflüssig, das musste nicht sein..."
    hide but  
    hide eva
    show sha a11hajirai2 at m
    sha "Battler-sama.... Ich... uhm..."
    extend " Sie müssen das nicht für mich machen."
    extend " ...Ich bin sowas bereits gewohnt."
    show but b11warai2 at l
    but "Nein, Shannon-chan, du musst dir das nicht gefallen lassen."
    sha a12hajirai3 "B............."
    extend "Battler-sama, ich weiß nicht, was ich sagen soll.... uhm..."
    "Shannon errötete leicht, es war ihr offensichtlich etwas unangenehm."
    extend " Gleichzeitig kehrte aber ihr Lächeln für einen kurzen Augenblick zurück."
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
    nat "Der Täter muss unter uns sein."
    extend " ...Es gibt keine unsichtbaren Wesen, die einfach Menschen beliebig umbringen und in verschlossene Räume sperren."
    show but a11niramu3 at rightedge
    but "Da hast du vermutlich recht mit..."
    extend " Aber ich kann auch nicht glauben, dass der Täter gerade seelenruhig mit uns in einem Raum sitzt und zuhört."
    $ songname = "Suspicion"
    play music umib_027
    show screen showsong
    nat "Das stimmt, deswegen sollten wir uns aufteilen."
    show eva a11hohoemi1 at l
    eva "Huh, aufteilen?"
    nat "Die einzige Möglichkeit das Tor zum Gartenschuppen zu öffnen ist der Schlüssel aus dem Raum der Bediensteten!"
    eva "Wurde der Schlüssel nicht neben Gohdas Leiche gefunden?"
    extend " ....Der Raum war offenbar abgeschlossen, obwohl der Schlüssel im Schuppen selbst lag."
    but "Das klingt super seltsam, hat das Tor auch ganz sicher nicht geklemmt?"
    extend " Ich meine haben es mehrere versucht zu öffnen?"
    hide nat
    show gen a11defo1 at m
    gen "Ich habe es mit Natsuhi-sama überprüft, es war definitiv abgeschlossen..."
    but "Ich finde es auch ehrlich gesagt etwas blöd sich aufzuteilen."
    extend " Wenn der Täter sich in einer Gruppe befindet, sind die anderen ihm ausgeliefert."
    eva "Da hast du recht, es würde vielleicht sinn machen, wenn ein paar von uns verdächtigt werden."
    window hide
    pause 0.5
    scene firsttwilight with gradientcirclefade
    "Der Tatort ist ein verschlossener Gartenschuppen in dem sechs Leichen gefunden wurden." 
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
    "Des weiteren wurde der einzige Schlüssel, der den Gartenschuppen öffnen und schließen kann, in der Hosentasche von Gohdas Leiche gefunden."
    extend " Natsuhi und Genji konnten bestätigen, dass das Tor komplett abgeschlossen war."
    "Bedeutet, der verschlossene Schuppen wurde erst geöffnet, als mit einer Feuerwehraxt das Schloss zerstört wurde."
    "Es gibt auch keinerlei Möglichkeiten den Schuppen von innen zu verschließen."
    "Das einzig existierende Fenster war auch abgeschlossen und unversehrt."
    extend " Es existieren auch keine Geheimgänge oder irgendwelche dubiosen Schlupflöcher zum entkommen."
    "In anderen Worten: Der Täter hat die sechs ermordet, den Schlüssel in Gohdas Hosentasche gelegt, ist rausgekommen und hat dann mit unbekannten Mitteln den Schuppen versiegelt."
    window hide
    pause 0.5
    scene m1f_s1cr at bgani
    show expression(CustomParticles("images/system/particle.png", 10))
    show hid a11majime1 at r
    hid "Ich finde es bemerkenswert, wie du niemanden verdächtigen möchtest, aber irgendwer muss es doch gewesen sein."
    extend " ...Vielleicht liegen wir alle falsch und es war wirklich eine Hexe."
    show but b11kuyasigaru1 at l
    but "Ich weigere mich an so etwas zu glauben! Es gibt keine Magie und auch keine Hexe!"
    extend " ...Ich glaube an Anime und Manga, aber nicht an irgend einer magischen Blondine, weil man sich die Sache mit dem Schlüssel nicht erklären kann!"
    "Aus dieser Diskussion lässt sich schließen, dass man zu keinem gemeinsamen Nenner kommen kann."
    extend " Es ist auch schließlich super schwierig jemanden zu verdächtigen.."
    "Gibt es überhaupt einen Verdächtigen?"
    hid "Ist es einem Menschen möglich den passenden Schlüssel in den verschlossenen Raum zu legen?"
    but "Ach man... Es bringt einfach gar nichts.... Es bringt doch alles überhaupt nichts.."
    but b11oya1 "Mir fällt gerade etwas ein!"
    extend " Was wäre wenn der Verschlossene Raum so wie er jetzt ist nie als solches gedacht war?"
    hide hid
    show eva a11hohoemi1 at r
    eva "Oho, Battler-kun..." 
    extend " Wie stellst du dir das vor? Lass mich raten, der Täter ist an Ort und Stelle wegen einem Unfall umgekommen?"
    but b22nayamu2 "Fast! Der Täter hat fünf von uns in den Schuppen geworfen und danach Selbstmord begangen!"
    extend " Er konnte nicht damit Leben, dass er seine eigene Familie auf dem Gewissen hat und hat sich als sechste Person selbst ermordet!"
    show nat a12nayamu1 at m
    nat "Und wer soll deiner Meinung nach der Täter gewesen sein?"
    but "Nun ja haha..." 
    extend " es könnte Gohda gewesen sein?"
    extend b24futeki3 " Genau! Schließlich hatte er den Schlüssel in der Tasche!"
    eva "Der Typ ist doch nur in der Lage Zwiebeln zu schneiden, er hatte sonst keine nennenswerten Kompetenzen. *Kicher*"
    hide but
    hide eva
    hide nat
    show nan a2fumu1 at m
    nan "Wenn ich etwas sagen dürfte, Battler-san."
    extend " Bei einem Selbstmord wäre es unmöglich für den Täter das Tor zu verschließen."
    nan "Selbst wenn... Ich denke nicht, dass man sich solche fatalen Wunden so einfach selber zufügen kann, das sah nach der Arbeit eines absolut skrupellosen Killers aus."
    hide nan
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
    "Kaum hatte Hideyoshi diese Frage ausgesprochen, ertönte eine schrille Lache, die sofort die komplette Aufmerksamkeit auf sich ziehen konnte."
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
    mar "Die Schrift auf dem magischen Kreis ist auf Hebräisch. Auf jedem der Arme des Kreuzes stehen die Namen der Engel, die über Wind, Feuer, Erde und Wasser herrschen:" 
    extend " Chasan, Arel, Phorlakh und Taliahad." 
    mar "Ebenso stehen zwischen den Armen des Kreuzes die vier großen Könige der Elemente:" 
    extend " Ariel, Seraph, Tharshis und Cherub. Die Worte, die um das Kreuz herum geschrieben sind, stammen aus Psalm 116:16-17 der Bibel und besagen:" 
    mar "'Der Herr hat mich von meinen Ketten befreit. Ich will dir ein Opfer des Dankes darbringen und den Namen des Herrn anrufen.'"
    "Alle Anwesenden stehen unter Schock, die neunjährige Maria, die noch nie ganze Sätze ohne 'Uu' sagen konnte, spricht plötzlich von magischen Kreisen und Bibelzitaten."
    "Schlimmer noch, sie sagte es mit einem gruseligen Gesichtsausdruck, so selbstsicher, als wüsste sie etwas, was andere nicht wissen."
    show but a11aseru1 at l
    but "Whoaaa..."
    but " Woher hast du das Wissen über diese Dinge?"
    scene c0101_b with fastdissolve
    mar "Kihihihihihihi!"
    extend " Der Okkultismus ist mein Spezialgebiet."
    mar "Es wird nicht der letzte magische Kreis sein, den du siehst!"
    mar "Kihihihihihihi!"
    extend " Ich habe ein ganzes Buch über die magischen Kreise und was sie zu bedeuten haben."
    window hide
    play sound umise_034
    scene c0101_c with fastdissolve
    pause 2
    window show
    mar "BEATRICE wird uns schon bald ins Goldene Land einladen."
    extend " Danach ist alles andere egal!"
    extend " Kihihihihihihi!!!"
    mar "Ihr könnt machen was ihr wollt, sie kommt durch jede verschlossene Tür durch!"
    extend " Versucht erst gar nicht euch zur Wehr zu setzen, Kihihihihihihi!"
    window hide
    pause 0.5
    scene black with dissolve
    "Maria hat wegen ihrer kindlichen Art in der Schule nicht viele Freunde. Ihre Mutter Rosa, die inzwischen verstorben ist, schimpfte deswegen oft mit ihr."
    extend " Allerdings ist sie ein großer Fan des Okkulten, was diesen Auftritt zumindest ein wenig erklären könnte."
    window hide
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
    jes "Fällt euch auch auf, dass Maria sich merkwürdig verhält?"
    extend " ...Dass ihre Mutter ermordet wurde, macht sie überhaupt nicht traurig."
    jes "Stattdessen sieht sie überglücklich aus."
    show mar a11niyari1 at l
    mar "Ich weiß, wer die sechs umgebracht hat!"
    show nat a32ikari1 at r
    nat "Du weißt es?"
    mar "Es ist egal ob ich sterbe, sie wird mich eh ins Goldene Land mitnehmen."
    nat "Rede keinen unsinn Maria-chan!"
    mar "Es war BEATRICE!"
    hide jes
    show but b22odoroki2 at m
    but "Maria... Dafür ist jetzt nicht die Zeit!"
    extend " So jemand wie BEATRICE existiert nicht..."
    mar a22sakebu1 "Uu!!!....."
    extend " Es war aber BEATRICE!"
    play sound umise_013
    hide but
    hide nat
    show mar a22sakebu1 at m with vpunch
    extend " BEATRICE!!, BEATRICE!!, BEATRICE!!"
    "Maria fängt immer an zu toben, wenn jemand in ihrer Gegenwart leugnet, dass die Hexe existiert."
    "Es ist irgendwo klar, sie ist noch ein Kind und der Glauben an übernatürliches ist da noch ausgeprägt."
    window hide
    scene black with dissolve
    "Eva macht Andeutungen, dass sie Ruhe braucht, der Morgen war extrem Kräftezehrend für sie"
    window hide
    pause 0.5
    scene m1f_s1cr at bgani
    show expression(CustomParticles("images/system/particle.png", 10))
    show eva b25komaru4 at m
    eva "Wir zwei ziehen uns ins Gästezimmer zurück um uns auszuruhen, zur Not haben wir die Schrotflinten."
    show kum a12majime1 at l
    kum "Es wäre besser, wenn Sie trotzdem nicht alleine gehen, wir begleiten euch!"
    show nat a16komaru1 at r
    nat "Richtig, es wäre töricht uns jetzt so leichtfertig zu trennen!"
    hide eva
    show hid a12defo1 at m
    hid "Danke Leute, ihr meint es zu gut mit uns!"
    extend " Wahahahaha!"
    nat "Geht in das Gästezimmer und verschließt eure Tür mit der Kette, damit der Täter nicht reinkommen kann."
    kum "Selbst ein fähiger Killer, müsste die Kette mit einem Bolzen zerschneiden um rein zu kommen."
    extend " Das würde euch die nötige Zeit zum reagieren geben."
    hid "Vielen Dank, damit können wir uns ohne Angst mal ausruhen!"
    window hide
    $ songname = "-"
    stop music fadeout 2
    stop clock fadeout 2
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
    "Nach dem Eva und Hideyoshi das Gästezimmer betraten und die Türkette angelegt haben, schmissen sich beide auf das Bett."
    "Eva kann es nicht mehr zurückhalten und fängt bitterlich an zu weinen, sie musste sich die ganze Zeit mehr oder weniger zurückhalten."
    $ songname = "Hope"
    play music umib_008
    show screen showsong
    show hid a11odayaka1 at l
    hid "Schatz, das war ein harter Tag, George würde aber nicht wollen, dass wir jetzt trübsaal blasen."
    extend " Er wird uns vom Himmel aus Schutz bieten, damit wir morgen sicher die Insel verlassen können."
    show eva b25naku5s at r
    eva "Warum gerade hat es ihn erwischt?...."
    extend " Er hatte eine vielversprechende Zukunft...."
    eva "Das ist nicht fair!"
    extend " Warum nur?"
    eva "George!! Komm zu mir zurück...."
    eva "Schatz!! halt mich!!"
    play sound umise_013
    hide eva with quickergradientwipeleft
    "Eva bricht in Tränen aus, die sonst so kühle und gelassene Eva zeigt sich nur ihrem Mann gegenüber, von ihrer weichen Seite."
    hid a11naku4 "So ist es gut, lass einfach alles raus, ich bin genauso traurig wie du und es tut so unendlich weh!"
    extend " Er würde aber nicht wollen, dass wir viel um ihn trauern, sondern weitermachen und ihn in guten Erinnerungen behalten!"
    "Auch Hideyoshi kann die Tränen nicht mehr zurückhalten."
    extend " Zu stark ist die Emotionale Belastung, selbst für Hideyoshi, der selbst jetzt noch aufmunternde Worte findet."
    show eva b25naku5s at r
    eva "Er war so ein guter Junge, er hatte noch so viel vor sich."
    extend " Warum nur, warum nur?? Wer war das??"
    eva "Ich werde den Täter finden und töten!"
    extend " Wie kann er das nur meinem George antun!!"
    hid a11komaru2 "Nana, beruhig dich, Eva!"
    extend " George würde keine Rache wollen!"
    extend " Ich versteh dich nur zu gut."
    "Evas Trauer ist auf puren Hass umgeschwungen."
    stop music fadeout 2
    $ songname = "-"
    window hide
    pause 2
    call butterfly1
    pause 2
    window show
    "Genau in diesem Moment, erscheinen wunderschöne Goldene Schmetterlinge im Raum, die buchstäblich aus dem nichts gekommen sind."
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
    "Hideyoshi und Eva sind sofort in Alarmbereitschaft gegangen."
    play audio umise_030
    show e0903a with quickergradientwiperight
    eva "Wer zum Teufel seid ihr und wo kommt ihr her?"
    extend " Verschwindet sofort, ich bin bewaffnet!"
    eva "Zwingt mich nicht den Abzug zu drücken!"
    hide e0903a with quickgradientwiperight
    "Die zwei Eindringliche machen keine Anstalten sich zu bewegen, im Gegenteil, sie posieren in einem Duett."
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
    zep "Das sind also die auserwählten, Furfur?"
    fur "Was sehe ich da? Ein sich liebendes Paar! Das ist ja großartig, nicht wahr Zepar?"
    zep "Heute wird entschieden, ob ihr als Paar weiterleben dürft, oder in eine Welt ohne Liebe verbannt werdet!{font=fonts/AOTFShinGoProMedium.otf}♪{/font}"
    fur "Das ist ja absolut fantastisch, die beiden sehen so vielversprechend aus!{font=fonts/AOTFShinGoProMedium.otf}♪{/font}"
    show e0903a with quickergradientwiperight
    eva "Was wollt ihr von uns?"
    extend " ..Kommt näher und ich schieße!"
    hide e0903a 
    show zep a11defo1 at l
    show fur a11defo1 at r
    with quickgradientwiperight
    "Die Zwei sind absolut unbeeindruckt von Evas Drohungen und ignorieren sie konstant."
    zep "Ich bin einer der 72 Großen Dämonen, der Dämon der Liebe, mein Name lautet Zepar!"
    fur "Ich bin einer der 72 Großen Dämonen, der Dämon der Liebe, mein Name lautet Furfur!"
    hide zep
    hide fur
    show eva b26ikari2 at l
    show hid a12komaru2 at r
    eva "Ihr sollt Dämonen sein?"
    extend " ...Wer soll euch das bitte glauben?"
    extend " Was denn für ein Test?"
    hid "Für dämliche Scherze sind wir gerade nicht zu haben!"
    extend " Verlasst diesen Raum!"
    hide eva
    hide hid
    show zep a11defo1 at l
    show fur a11defo1 at r
    zep "Hast du das gehört Furfur?"
    fur "Laut und deutlich, Zepar!"
    zep "Ihr werdet euch eine Prüfung unterziehen müssen!"
    fur "Wenn ihr euch weigert, wartet nur der tot auf euch!"
    zep "Denn ihr zwei wurdet von der Großen Fräulein BEATRICE-sama für die Zweite Dämmerung auserkoren!"
    hide zep
    hide fur
    show eva b26ikari2 at m
    eva "Das ist doch lächerlich!"
    extend " Was glaubt ihr wer ihr seid!?!!"
    "Eva ist außer sich vor Wut, Hideyoshi versucht in der Zwischenzeit die Tür zu öffnen."
    scene m_door1
    show hid a12komaru2 at m 
    with quickgradientwipeleft
    play sound umise_032
    hid "Die Kette bewegt sich nicht!"
    extend " Ich kann die Tür nicht öffnen!"
    window hide
    pause 0.5
    scene m2f_r4ars_bg at bgani
    show m2f_r4ar at bgani
    show zep a11defo1 at l
    show fur a11defo1 at r
    show expression(CustomParticles("images/system/particle.png", 10))
    with quickergradientwipeleft
    zep "Sieh nur Furfur!"
    extend " Sie versuchen zu entkommen!"
    fur "Das ist absolut unmöglich, sie denken, sie könnten Großen Dämonen entkommen, Zepar!"
    "Hideyoshi erkennt, dass es wohl nichts bringt an der Tür zu rütteln, sie müssen machen was die Dämonen sagen."
    hide zep
    hide fur
    show eva b26ikari2 at l
    show hid a12komaru2 at r
    hid "Okay, okay, was müssen wir für diesen Test machen?"
    eva "Schatz, du willst doch nicht wirklich..."
    hide eva
    hide hid
    show zep a11defo1 at l
    show fur a11defo1 at r
    zep "Dafür müsst ihr uns eine einfache Frage beantworten!"
    fur "Wenn ihr sie richtig beantwortet, dürft ihr den Raum verlassen!"
    hide zep
    hide fur
    show eva b26ikari2 at l
    show hid a12komaru2 at r
    eva "Dann raus damit, welche Frage ist es?"
    hid "Eva!"
    extend " Wir dürfen die Dinge nicht überstürzen!"
    hid "Sie haben gesagt, wir sterben, wenn wir nicht bestehen..."
    eva "Als ob du das auch noch glaubst..."
    hide eva
    hide hid
    show zep a11defo1 at l
    show fur a11defo1 at r
    zep "Nun denn, wir sollten keine Zeit verschwenden, BEATRICE-sama wird langsam ungeduldig, Furfur"
    fur "Dann sollten wir mit dem Test beginnen, Zepar!"
    zep "Die Frage die wir euch stellen wollen lautet..."
    show zep a12defo1 at l
    show fur a12defo1 at r
    play sound umise_002
    with quickflash
    fur "Was ist das, was ihr zwei gemeinsam am meisten liebt?"
    zep "Beantwortet die Frage mit Bedacht, von der hängt euer Liebesleben ab!"
    fur "Bedenkt, dass ihr nur eine gemeinsame Antwort abgeben könnt und zwar nur einmal!"
    hide zep
    hide fur
    show hid a11majime1 at r
    hid "Die Frage ist wohl ein Scherz, es gibt nur diese eine Antwort, Eva!"
    show eva b21akire1go at l
    eva "Deswegen hab ich dich geheiratet, ich weiß genau, was du meinst!"
    hid "Da gibt keine zwei Meinungen."
    "Hideyoshi und Eva sind sich absolut sicher, was sie den Dämonen antworten wollen, da bedarf es keiner großen Überlegung."
    hid "Unsere gemeinsame Antwort lautet.."
    eva "Unser Sohn George!"
    eva "George war das beste, was uns jemals passiert ist!"
    extend " Wir lieben ihn mehr als alles andere!"
    hid "Seht ihr, wir sind fest entschlossen!"
    extend " Ein Ehepaar sollte nichts mehr lieben, als die eigenen Kinder!"
    extend " Diese gesund aufwachsen zu sehen, ist das größte Geschenk."
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
    zep "Aber die Antwort ist leider nicht richtig!"
    fur "Damit ist das Spiel vorbei und euer Leben gehört BEATRICE-sama!"
    hide zep
    hide fur
    show eva b26ikari2 at l
    show hid a12komaru2 at r
    eva "Wollt ihr uns verarschen? Wie kann die Antwort nicht richtig sein?"
    hid "Genau!"
    extend " Das ist so ein Test den man nicht bestehen kann, weil die richtige Antwort immer das ist, was euch gerade so passt!"
    extend " ...Ich hab doch recht!"
    hide eva
    hide hid
    show zep a11defo1 at l
    show fur a11defo1 at r
    zep "Sie sehen ziemlich sauer aus, Furfur!"
    fur "Dabei haben beide offensichtlich gelogen, Zepar!"
    play audio umise_030
    show e0903d with quickgradientwiperight
    eva "Das ist doch wohl die Höhe!"
    extend " Verschwindet, oder Schrotmunition fliegt durch eure dünnen Körper!"
    eva "Ja, ich werde euch durchlöchern, bis nichts mehr von euch übrig ist!!"
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
    "Plötzlich sind die Dämonen verschwunden und an ihrer Stelle ist wie aus dem nichts ihr verstorbener Sohn erschienen."
    show hid a11naku4 at leftedge
    hid "Das kann nicht sein!"
    extend " George???"
    show eva b25naku5s at rightedge
    eva "Du bist doch gestorben???"
    extend " Ich hab deine Leiche gesehen, wie ist das möglich?"
    geo "Ihr liebt mich nicht am aller meisten!"
    extend " Das habt ihr noch nie getan!"
    eva "Nein, George! Bitte! Das stimmt so nicht!"
    extend " Du warst immer das aller wichtigste für uns!"
    hid "George! Bitte wir können über alles reden!"
    geo a21majime4 "Ja, ich war für euch das wichtigste..."
    extend " Ich war wichtig dafür, euch eine menge Profit einzubringen!"
    geo "Ich wurde von euch immer streng zu einem 'Gentlemen' erzogen, damit ich zu eurem Vorteil agiere!"
    eva "Nein George! So ist das nicht!"
    scene black
    show geo a11niramu1 at m
    play sound umise_027
    with quickflash
    geo "Oh doch!"
    extend " Euch hat es immer nur interessiert, wie ihr Großvaters Erbe einstreichen könnt!"
    play sound umise_057
    show chain1r_sp with quickflash
    geo "Es war euch wichtiger, dass ich Geld ohne Ende scheffel, eine Frau aus reichem Hause heirate!"
    extend " Ihr wolltet nicht, dass ich Shannon-chan zur Frau nehme..."
    play sound umise_057
    show chain4r_sp with quickflash
    geo "Und warum? Weil es euch keinen Geldsegen bringt!"
    extend " Solange ich weiter diesen Weg gehen würde, würdet ihr mich unterstützen, aber sobald ich von diesem Weg abweiche, habe ich niemals eure Unterstützung erfahren!"
    play sound umise_057
    show chain5r_sp with quickflash
    geo "Ihr seid grauenhafte Eltern, sowas dem einzigen Sohn anzutun!"
    extend " Ihr habt den Test nicht bestanden, also werde ich euch eigenhändig BEATRICE-sama ausliefern!"
    window hide
    scene m2f_r4ars_bg at bgani
    show m2f_r4ar at bgani
    show eva b25naku5s at m
    play sound umise_027
    with quickflash
    show expression(CustomParticles("images/system/particle.png", 10))
    eva "Bitte George! Es tut uns leid! Bitte verzeih uns!"
    extend " Wir haben das alles nur für dich getan, damit du nicht so wirst wie unsere Geschwister!"
    geo "Erspart mir das, ihr Geldgierigen Piranhas!"
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
    "George hat mit magischer Energie ein Loch in Evas Kopf geschossen. Sie ist rückwärts aufs Bett gefallen und sofort gestorben."
    "Hideyoshis Schock ist nicht in Worte zu fassen, er versucht sich noch irgendwie ins Badezimmer zu flüchten."
    scene mbat_1a
    show hid a11naku4 at m
    play sound umise_027
    with quickflash
    hid "Bitte George, verschone mich! Bitte!"
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
    "Auch Hideyoshi ist sofort gestorben, es gab keine Chance diesen Angriff zu überleben."
    extend " Seine Stirn wurde ebenfalls von George durchbohrt."
    extend " BEATRICE-sama muss hoch zufrieden sein."
    geo "Meine Aufgabe ist erfüllt, ich werde mir nun erlauben die Bühne für immer zu verlassen und meinen Eltern in die Hölle zu folgen."
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
    extend " Es gibt saftige Makrelle in meiner hausgemachten Sahnesauce!"
    extend " Diese Spezialität dürfen Sie auf keinen Fall verpassen!"
    "Kurze Zeit später sind Kanon und Kumasawa vor der Tür erschienen, sie wollten Eva und Hideyoshi fragen, ob sie zusammen mit den anderen essen wollen."    
    kan "Es antwortet niemand..."
    kum "Eva-sama! Hideyoshi-sama! Können Sie mich hören?"
    extend " antworten Sie bitte!"
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
    kan "Die Türkette ist angebracht... Ich komme nicht durch!"
    extend ".....Ich höre das plätschern von Wasser, es muss die Dusche sein, sind sie im Badezimmer?"
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
    kan "Sie antworten nicht und die Tür geht nicht auf, ich brauche einen Bolzenschneider wegen der Kette."
    gen "Im Bedienstetenraum müsste einer sein."
    kan "Alles klar, ich hole es schnell."
    gen "Wir gehen zu dritt, es ist zu gefährlich in Zeiten wie diesen."
    scene black with dissolve
    "Die drei gingen zusammen in den Bedienstetenraum um den Bolzenschneider zu holen."
    extend " Als die drei wiedergekommen sind, konnten sie ihren Augen nicht trauen..."
    play sound umise_024
    scene magicsquare_moon1 with fastdissolve
    pause 4
    $ songname = "Lure"
    show screen showsong
    play music "audio/bgm/umib_018.ogg"
    kum "WAAAAAAAAAAAAAA!" 
    extend " ...Was ist das denn und wo kommt das her?"
    kum "Wieder eins dieser magischen Kreise von denen Maria-sama erzählt hat?"
    kan "Das war vor wenigen Minuten noch nicht hier...."
    kan "Lass mich die Kette zerschneiden!"
    play sound umise_039
    kan "......."
    "Kanon hat die Kette zerschnitten und öffnet vorsichtig die Tür."
    play sound umise_017
    scene white zorder 99
    with kanon_r
    scene black with fastdissolve
    extend " Er blickt in den Raum, hält einen Moment inne und atmet tief ein..."
    scene m2f_p1ar_bg at bgani
    play rain umilse_012
    show rainbackscroll
    show rainfrontscroll
    show m2f_p1ar at bgani
    show kan a13defo2 at r
    with quickergradientwiperight
    pause 0.5   
    kan "Kumasawa! Holen sie die anderen her!"
    show kum a12majime1 at l
    kum "Ohohohoh, wird gemacht!"
    hide kum
    "Kumasawa und Genji gingen sofort los um den anderen bescheid zu sagen, dass etwas nicht mit Eva und Hideoyshi stimmt."
    scene black with fastdissolve
    "Die anderen haben sich darauf sofort auf den Weg zum Ort des Geschehens begeben."
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
    extend " Sag mir bitte, dass es nicht das ist, was ich denke!"
    nat "Schon wieder so ein Gekritzel??"
    show kum a12majime1 at l
    kum "Das war eben noch nicht hier!"
    hide but
    hide kum
    hide nat
    show mar a22akuwarai2 at m
    mar "Kihihihihihihihih!!"
    mar "Das ist der erste magische Kreis des Mondes!"
    extend " Das Design des magischen Kreises ähnelt der Darstellung einer Tür. Der hebräische Vers darauf ist Psalm 107:16 entnommen und lautet:" 
    mar "'Denn er hat eherne Tore zerbrochen und eiserne Riegel durchschnitten'."
    mar "Was so viel heißt wie, dass die Hexe nicht mal von einer Türkette aufgehalten werden kann!"
    extend " Kihihihihihihihi!!!"
    show but a11aseru5 at l
    play sound umise_012
    show mar a22sakebu1 at m
    with vpunch
    hide mar with quickgradientwipedown
    play sound umise_013
    mar "auauauauau, was sollte das?"
    but "Quatsch nicht so viel!"
    extend " Hör auf mit diesem gruseligen Mist in so einer Situation!"
    extend " Hast du überhaupt kein Mitgefühl?"
    but "Deine Mama ist gestorben und dich interessieren nur magische Kreise oder Hexen...."
    extend " Naja, kann mir auch egal sein..."
    extend  " Ich geh jetzt rein!"
    play sound umise_020
    hide but with dissolve
    $ songname = "goldenslaughterer"
    show screen showsong
    play music umib_024
    play sound umise_013
    scene black with quickflash
    ## TODO MITTWOCH
    but "NEIN!!! NEIN!!! NEIN!!!"
    extend " WIESO SCHON WIEDER?"
    but "TANTE EVA!!!!"
    nat "KYAAAAAAAA"
    extend " DAS KANN NICHT WAHR SEIN!!!"
    "Auf dem Bett im Gästezimmer lag Tante Eva."
    extend " Der Bettlaken wurde mit ihrem Blut durchtränkt."
    "Jemand hat in ihre Stirn so eine Art von Pfahl reingerammt."
    nan "Ich spüre keinen Puls mehr, sie ist nicht mehr am Leben."
    but "Es reicht nun entgültig!"
    extend " Das war definitiv einer zu viel!"
    but "Diese Grausamkeit muss ein Ende finden, jetzt hast du mich wirklich zum Feind gemacht!"
    extend " ...Du wirst es noch bittlerlich bereuen dir Ushiromiya Battler zum Feind gemacht zu haben du gottverdammter Bastard!"
    but "Dieses Kettenschloss war doch nur ein ganz mieser Trick!"
    "Das Geräusch von einer Dusche war laut zu hören, Battler öffnete vorsichtig die Tür zum Badezimmer."
    jes "Ihhhhkkkssss!!!" 
    extend " Onkel Hideyoshi? Was haben sie dir angetan??"
    extend " Ich kann das alles nicht mehr....."
    kum "Ja leck mich doch am Zückerli, wir sind bestimmt die nächsten."
    extend " Ihihihihhih!!!"
    "Hideoyoshi lag nackt in der Badewanne, wie schon bei Eve wurde ihm ein Pfahl in die Stirn gerammt."
    extend " Das Wasser aus dem DUschkopf plätschert ununterbrochen auf seinen Rücken."
    but "Ich bin so unglaublich sauer, ich kann es gar nicht richtig ausdrücken!"
    extend " ...BEATRICE ist nichts weiter als ein Märchen, damit wir die Fassung verlieren!"
    but "Es kann niemand unsichtbares existieren, der einfach so Leute tötet!"
    extend " Ich werde dich finden, ich werde dich packen und eigenhändig in die Hölle schicken!"
    but "So langsam ist schluss! Das wars!"
    extend " Wenn ich dich in die Finger bekomme, wirst du dir wünschen nie geboren worden zu sein!"
    but "Ich werde dich kriegen, wie auch immer du heißt!"
    extend " Wenn du BEATRICE sein willst, dann werde ich mir dein fettes Kleid packen und es dir in den Hals rammen!"
    but "Ich prügel die Scheiße aus dir raus, das schwör ich dir!!!"
    but "Verschlossener Gartenschuppen mit dem Schlüssel innerhalb? Eine Türkette? Lächerlich!"
    extend " Ich werde jedes Detail herausfinden und dich zum Schafott führen!"
    but "Ich werde dich eigenhändig umbringen!!!"
    extend "GNHAAAAAAAAAAAAAAAAAAAAAAAAAAAA!!!!!!"
    extend "BEATRICEEEEEEEEEEEEE!!!!!"
    ## Kapitel 2 Ende
    $ chapter = 1003
    $ songname = "-"
    $ save_name = _("EpisodeX Illusion of the golden witch\nVerkettung der Ereignisse")
    show screen showch
    ## Kapitel 3 Verkettung der Ereignisse
    nat "Ich weiß nicht, ob der Täter sich nur in der Villa aufhält, aber hier ist der Vorrat an Essen ein wenig größer."
    jes "Wieso passiert das alles überhaupt? War es nötig auch nur einen von ihnen zu töten?"
    nan "Jessica-chan, nur der Täter selbst kennt sein Tatmotiv."
    extend " Es bringt leider überhaupt nichts darüber nachzudenken, so sehr ich deinen Schmerz auch fühle."
    jes "Wo steckt eigentlich Großvater die ganze Zeit?"
    gen "Der Herr befindet sich nach wie vor in seinem Arbeitszimmer."
    jes "Natürlich, hier geht alles den Bach runter und er versteckt sich in seinem übel riechenden Kabuff"
    kan "Jessica-sama, der Herr ist ein alter Freund der Hexe, sie würde ihn nicht ohne weiteres Töten."
    but "Diese Hexenlegende, von der ich gehört hab, hat ja damit was zutun, dass Großvater von der Hexe 10 Tonnen Gold erhalten haben soll."
    kum "Ohohohoh..." 
    extend " das ist tatsächlich wahr und das Gold existiert wirklich!"
    kum "Die Inschrift unter dem Gemälde in der Eingangshalle soll ein Rätsel beinhalten, dass direkt zu diesem Gold führt."
    extend " Allerdings war bisher keiner in der Lage es zu lösen."
    mar "Kihihihihihihihihih"
    extend " Ich hab das ganze Rätsel aufgeschrieben."
    extend " Wir sollen es vielleicht endlich anfangen zu lösen, schließlich war das von Anfang an unsere Siegesbedingung"
    nat "Maria! Wir haben jetzt keine Zeit für sowas!"
    but "Ich weiß auch nicht wie uns dieses Rätsel weiterhelfen soll"
    mar "Uu~!"
    extend " BEATRICE hat doch den Abend vor der ersten Dämmerung gesagt, was passieren wird!"
    nat "Du meinst diesen Brief den du von was weiß ich wo erhalten hast?"
    but "Ich erinnere mich, da stand irgendwas drin von, wir sollen das Rätsel lösen, bevor Zinsen eingeholt werden, weil Großvater den Vertrag mit ihr aufgelöst hat."
    jes "Und dass sie alles von Ushiromiya Familie erhält plus Zinsen und diese Zinsen sind...."
    mar "Unsere Leben!"
    extend " Kihihihihihihi!!!"
    mar "Der einzige Weg alles zurück zu erhalten, ist es das Rätsel der Inschrift zu lösen!"
    nan "Ich habe mal versucht diese Inschrift zu lösen, ich bin aber dran verzweifelt und das obwohl ich Kinzo-san schon seit den alten Tagen kenne."
    nan "Aber wie sagt man so schön? Man kann einem Menschen nur vor den Kopf gucken und nicht in den Kopf."
    jes "Auch wenn du mir von allen am Verdächtigsten bist, zeig mir mal was auf der Inschrift stand, Maria-chan..."
    nat "Ich bin ehrlich gesagt auch daran interessiert, ich hab mir das noch nie durchgelesen."
    mar "Bitte sehr, prägt es euch gut ein, Kihihihihi!!"
    ntxt "Seht den Süßfischfluss, der durch meine geliebte Heimatstadt fließt. Ihr, die ihr das Goldene Land sucht, folgt seinem Weg stromabwärts auf der Suche nach dem Schlüssel."
    ntxt "Auf dem Weg dorthin werdet ihr ein Dorf sehen."
    extend " In diesem Dorf musst du das Ufer suchen, von dem dir die beiden erzählen. Dort schläft der Schlüssel zum Goldenen Land."
    ntxt "Derjenige, der den Schlüssel findet, sollte diesem Weg zum Goldenen Land folgen."
    nvl clear
    ntxt "Zur Zeit der ersten Dämmerung: sollst du die sechs, die der Schlüssel ausgewählt hat, als Opfer darbringen."
    ntxt "Zur Zeit der zweiten Dämmerung: sollen die Übriggebliebenen die beiden, die sich nahe stehen, auseinanderreißen."
    ntxt "Zur Zeit der dritten Dämmerung: sollen die Verbliebenen meinen edlen Namen preisen."
    nvl clear
    ntxt "Zur Zeit der vierten Dämmerung: Stich in den Kopf töte."
    ntxt "Zur Zeit der fünften Dämmerung: Stich in die Brust und töte."
    ntxt "Zur Zeit der sechsten Dämmerung: Stich in den Bauch und töte."
    ntxt "Zur Zeit der siebten Dämmerung: Stich in das Knie und töte."
    ntxt "Zur Zeit der achten Dämmerung: Stich in das Bein und töte."
    nvl clear
    ntxt "Zur Zeit der neunten Dämmerung wird die Hexe wiederbelebt, und niemand wird am Leben bleiben."
    ntxt "Zur Zeit der zehnten Dämmerung ist die Reise zu Ende, und du erreichst die Hauptstadt, in der das Gold wohnt."
    but "Das ist ja abgefahren, ich weiß zwar nicht, was Süßfischfluss heißt, aber die Morde liefen bislang exakt wie hier niedergeschrieben."
    but "Ich denke aber, dass jemand ohne Japanisch Kenntnisse dieses Rätsel gar nicht lösen kann."
    jes "Erst waren es Sechs und dann Eva und Hideyoshi als die beiden, die sich nahe stehen und jetzt sind wir bei?"
    mar "Preiset meinen Edlen Namen, die dritte Dämmerung!"
    nat "Sofort die Hände nach oben ihr vier!"
    extend " Wo kommt dieser Briefumschlag her und wieso liegt er genau bei euch fünfen?"
    nan "Natsuhi-sama, ich bitte Sie, wir wissen gar nicht wer das war!"
    kum "Ich bitte Sie Fräulein Natsuhi-sama, dies muss ein Irrtum sein!"
    nat "Ich habe schon die ganze Zeit ein mulmiges Gefühl bei euch Bediensteten!"
    extend " Wir sind hier mit der Inschrift beschäftigt und ganz plötzlich taucht in eurer Nähe ein Briefumschlag auf!"
    extend " Ich weiß ganz genau, dass da gerade eben noch keiner war!"
    but "Also hat den jemand von denen heimlich dahin gelegt?"
    nan "Die Möglichkeit besteht durchaus, aber wer soll es gewesen sein?"
    nat "Vielleicht ja du Kumasawa, du warst immer für irgendwelche Streiche zu haben, oder du Shannon, die den ganzen Tag nur vor sich hin träumt!"
    sha ".....Huh... Fräulein Natsuhi-sama....."
    extend " Kanon du bist auch nicht aus dem Schneider, deine Fähigkeit dich nahezu unsichtbar zu machen, ist noch am allermeisten Verdächtig!"
    kan "Fräulein Natsuhi-sama Ich..."
    nat "Genji, du warst von den Bediensteten immer Vater am nächsten, du könntest dies für ihn gemacht haben."
    gen "........."
    nat "Es wäre das beste für uns, wenn wir uns aufteilen würden!"
    extend "Battler, Jessica, Maria, Nanjo und ich bleiben hier!"
    nat "Wir alle haben ein Alibi, ihr habt das nicht!"
    but "Wollen wir sie wirklich dem Täter ausliefern?"
    mar "Kihihihihihihihi!!!"
    extend " BEATRICE wird sie für die nächsten Dämmerungen opfern!"
    kum "Natsuhi-sama vielleicht sollten wir nochmal drüber reden!"
    nat "Es tut mir leid, ich selber möchte euch nicht verdächtigen, aber ich kann euch allen nicht trauen..."
    extend " Bitte begebt euch zurück in die Villa."
    extend " ich bete zu Gott, dass euch nicht passiert."
    nat "Das Risiko ist aber auch zu hoch, euch hier zu behalten, wenn der Täter wirklich einer von euch sein sollte."
    nat "Sollte ich euch in den tot schicken, dann möge die Hexe auch mich mitnehmen, denn ich hätte es verdient."
    gen "Dies war ein Befehl von unserer Vorgesetzten, wir müssen nun gehen."
    kum "Passt bitte auch auf euch auf!"
    nat "Es tut mir so unendlich leid, bitte überlebt!"
    mar "Wollt ihr nicht schauen, was in dem Brief steht?"
    but "Ich hab eigentlich gar keinen bock darauf, da steht bestimmt sowas drin wie 'Haha, ihr habt die anderen wohl rausgeschmissen, jetzt töte ich die!' Weil die das doch erwartet hat."
    jes "Machen wir ihn erst einmal auf!"
    ntxt "Ich hoffe euch gefällt Kinzo-samas kleines Rätsel."
    ntxt "Hoffentlich tun Sie nicht missverstehen, dass sie jetzt die Zeit einfach absitzen können."
    extend " Sobald um 0 Uhr der nächste Tag anbricht, gewinne ich automatisch, da führt kein Weg dran vorbei."
    nvl clear 
    ntxt "Ich bitte Sie also darum, das Rätsel meiner Inschrift zu lösen um all dies, dass Sie verloren haben von mir zurück zu erhalten."
    extend "Allerdings bin ich mir sehr sicher, dass Sie nicht gewinnen werden, also Preiset meinen edlen Namen!"
    ntxt "BEATRICE die Goldene"
    nvl clear
    but "Will die uns verarschen?"
    extend " Wir sollen allen ernstes das Rätsel lösen?"
    nat "Meine Kopfschmerzen, lassen ein nachdenken darüber gar nicht zu."
    but "Ein Telefon klingelt?"
    extend " Wurden die Leitungen nicht getrennt?"
    jes "Vielleicht hat der Täter ja nur die äußeren Leitungen gecappt."
    nat "Battler-kun übernimmt das für mich, ich muss mich hinsetzen."
    but "Da bin ich mal gespannt."
    but "Hallo?..... Wer ist da?"
    bea "<congratulations>"
    bea "<I am fine, and youuuuuuuu?~>"
    but "Wer zum Teufel bist du?"
    extend " ....Willst du mich verarschen was soll das?"
    bea "<In english please!>"
    extend " Komm schon, dass hast du als Kind doch ständig gemacht, Ushiromiya Battler!"
    but "Du... Du bist absolut irre!"
    bea "Komm schon... rate doch mal, du könntest einen Trip nach Hawaii gewinnen!"
    extend " Kyahahahahahahah"
    but "BEATRICE?" 
    extend " .....Du bist BEATRICE?!!!"
    bea "<Riiiighttttttt that is correct!!>"
    extend "Ich wollte euch Vier nur gratulieren, ich lade euch nämlich ins Goldenen Land ein!"
    but "Das kannst du dir sonst wo hinstecken!"
    extend " Was ist mit Shannon, Kumasawa und den anderen passiert?"
    bea "Ohhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh"
    extend " Ich habe sie für meine Auferstehung geopfert..."
    extend " Kyahahahahahahaha ahahahahahahhahahahah!!!!!??!?!?!?!?!"
    but "Ich werde dir dumme Bitch niemals verzeihen!"
    kin "Wahahahahahaha!!"
    extend " Du bist heute echt gut drauf BEATRICE."
    bea "Hey Kinzo!"
    extend " Wie wäre es?" 
    extend " sollen wir den Wein aufmachen, der war scheiße teuer!"
    extend " Danach können wir uns ja gegenseitig mit der leeren Flasche die Köpfe einschlagen!"
    bea "Meine Auferstehung muss gefeiert werden!"
    extend " Keheheheheheh!!"
    kin "Oho, du bist mir ein wenig zu aufgeregt!"
    extend " Beruhig dich erstmal."
    but "Ist der alte Sack auch bei dir?"
    extend " Was hast du vor mit deinem betrunkenen Arsch?"
    extend " Wo sind Shannon und die anderen?"
    extend " Wohin hast du sie verschleppt?"
    bea "Gar nicht so weit weg, schau mal in der Villa nach, ich wünsche gutes gelingen!"
    extend "Kyahahahaahhaha!!!!"
    but "Dich pack ich mir als nächstes, du wirst schon sehen du Bitch!"
    jes "War das BEATRICE?"
    extend " Was ist passiert?"
    but "Wir müssen sofort zur Villa, es könnte schon zu spät sein!"
    nat "Dann schnell!"
    kin "Heute ist ein großer Tag, endlich durfte ich dein Lächeln wiedersehen!"
    extend " Es würde mir überhaupt nichts ausmachen, würdest du mir mein Leben nun entreißen!"
    bea "Ich denke einfach mal, dass ich genau dies machen werde!"
    kin "Warte bitte, was..."
    extend " ahhhhhhhhhhhhhhhhhrggggggghhhhhhhhhhhhhhhhhhhhhhhhhhhhh"
    bea "Tut mir leid Kinzo, aber du gehörst schon lange nicht mehr in diese Welt."
    but "Wo fangen wir an?"
    jes "Die Tür zum Wohnzimmer ist versperrt!"
    extend " Sie war noch geöffnet, als wir zum Gästehaus gegangen sind!"
    nat "Haben wir einen Schlüssel?"
    but "Die Generalschlüssel waren bestimmt noch bei den Bediensteten!"
    nat "Hab ich wieder mal toll gemacht."
    jes "Mama, gib dir nicht die schuld, du hattest unser aller Sicherheit im Kopf, es wäre so oder so hier zu gekommen!"
    nat "Wir könnten versuchen durch das Fenster von außerhalb rein zu kommen."
    nan "Vielleicht haben wir noch eine Chance jemanden zu retten!"
    jes "Gute Idee!"
    but "Nichts wie hin!"
    $ songname = "goldenslaughterer"
    show screen showsong
    but "Kanon!"
    jes "Was ist siehst du Battler-kun?"
    but "Kanon ist tot!"
    extend " Nanjo-sensei, bitte schauen Sie sich ihn an!"
    nan "Er atmet nicht mehr, er ist erst kürzlich von uns gegangen."
    but "Verdammt! Verdammt! Verdammt!"
    extend " Die anderen sind bestimmt ebenfalls ermordet worden!"
    nat "Da liegt ein Brief"
    extend " Das ist der Schlüssel drin für ein Gästezimmer in der oberen Etage!"
    but "Nicht wie hin!"
    but "Kumasawa....."
    extend " Du hast das am aller wenigsten Verdient, das darf nicht wahr sein!"
    jes "Hier ist auch ein Brief, dieser Schlüssel hier drin führt in mein Zimmer!"
    nat "Ich öffne jetzt die Kapelle!"
    but "Shannon!!!!"
    extend "Neiiiinnnn!!!!!!!"
    but "wieso nur? wieso nur?"
    jes "Wir werden auch sterben!"
    nat "Der Schlüssel in diesem Brief führt ins Wohnzimmer, wo Kanon liegt."
    extend " Eine absolut perfekte Schleife, das kann nur eine Hexe..."
    extend " BEATRICE...."
    but "Richtig... BEATRICE!!!"
    but "Bist du jetzt glücklich?"
    extend "Stell dich mir hier und jetzt!"
    extend " Trau dich und leg dich mit mir an!"
    bea "*Gacker*Gacker*"
    extend " Was ein charmanter Mann!"
    but "Komm schon!!!! BEATRICEEEEE!!!!!"
    ## Kapitel 3 Ende


































