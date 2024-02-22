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
    extend " Einmal durchgebrochen, sollte es einfach sein, das Tor zu öffnen"
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
    but b11oya1 "Mir ist gerade etwas eingefallen!"
    extend " Was wäre, wenn der verschlossene Raum, so wie er heute ist, nie als solcher gedacht war?"
    hide hid
    show eva a11hohoemi1 at r
    eva "Oho, Battler-kun..." 
    extend " Wie stellst du dir das vor? Lass mich raten, der Täter ist an Ort und Stelle bei einem Unfall ums Leben gekommen?"
    but b22nayamu2 "Fast! Der Täter hat fünf von uns in den Schuppen geworfen und dann Selbstmord begangen!"
    extend " Er konnte nicht damit leben, seine eigene Familie auf dem Gewissen zu haben und hat sich als sechste Person umgebracht!"
    show nat a12nayamu1 at m
    nat "Und wer war deiner Meinung nach der Täter?"
    but "Nun ja haha..." 
    extend " Vielleicht war es Gohda?"
    extend b24futeki3 " Genau! Schließlich hatte er den Schlüssel in der Tasche!"
    eva "Der Typ konnte nur Zwiebeln schneiden, sonst hatte er keine nennenswerten Fähigkeiten. *Kicher*"
    hide but
    hide eva
    hide nat
    show nan a2fumu1 at m
    nan "Wenn ich etwas sagen dürfte, Battler-san."
    extend " Bei einem Selbstmord wäre es für den Täter unmöglich, das Tor zu verschließen."
    nan "Selbst wenn... Ich glaube nicht, dass man sich solche tödlichen Verletzungen so leicht selbst zufügen kann, das sieht nach einem absolut skrupellosen Mörder aus."
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
    but " Woher hast du das Wissen über diese Dinge?"
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
    window hide
    pause 0.5
    scene black with dissolve
    "Maria hat wegen ihrer kindlichen Art in der Schule nicht viele Freunde. Ihre Mutter Rosa, die inzwischen verstorben ist, schimpfte deshalb oft mit ihr."
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
    show eva b25naku5s at r
    eva "Er hatte noch so viel vor sich, er war so ein guter Junge."
    extend " Warum nur, warum nur? Wer war das?"
    eva "Ich werde den Täter finden und töten!"
    extend " Wie konnte er das meinem George antun?!"
    hid a11komaru2 "Nana, beruhige dich, Eva!"
    extend " George würde sich nicht rächen wollen!"
    extend " Ich kann dich nur zu gut verstehen."
    "Evas Trauer verwandelte sich in blanken Hass."
    stop music fadeout 2
    $ songname = "-"
    window hide
    pause 2
    call butterfly1
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
    zep "Wir wurden von der Goldenen Hexe BEATRICE-sama herbeigerufen, um euch zu testen!"
    hide zep
    hide fur
    show eva b26ikari2 at l
    show hid a12komaru2 at r
    eva "Ihr sollt Dämonen sein?"
    extend " ...Wer soll euch das bitte glauben?"
    extend " Was denn für ein Test?"
    hid "Uns ist nicht nach dummen Scherzen zumute!"
    extend " Verlasst diesen Raum!"
    hide eva
    hide hid
    show zep a11defo1 at l
    show fur a11defo1 at r
    zep "Hast du das gehört Furfur?"
    fur "Laut und deutlich, Zepar!"
    zep "Ihr werdet euch einer Prüfung unterziehen müssen!"
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
    zep "Nun, wir sollten keine Zeit verlieren, BEATRICE-sama wird langsam ungeduldig, Furfur"
    fur "Dann lass uns mit dem Test beginnen, Zepar!"
    zep "Die Frage, die wir stellen wollen, lautet.."
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
    eva "George war das Beste, was uns je passiert ist!"
    extend " Wir lieben ihn über alles!"
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
    hide zep
    hide fur
    show eva b26ikari2 at l
    show hid a12komaru2 at r
    eva "Wollt ihr uns verarschen? Wie kann die Antwort falsch sein?"
    hid "Genau!"
    extend " Das ist ein Test, den man nicht bestehen kann, weil die richtige Antwort immer das ist, was einem gerade in den Kram passt!"
    extend " ...Ich habe doch Recht!"
    hide eva
    hide hid
    show zep a11defo1 at l
    show fur a11defo1 at r
    zep "Die sehen aber sauer aus, Furfur!"
    fur "Aber beide haben offensichtlich gelogen, Zepar!"
    play audio umise_030
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
    gen "Wir gehen zu dritt, das ist in diesen Zeiten zu gefährlich."
    scene black with dissolve
    "Die drei gingen gemeinsam in den Dienstraum, um den Bolzenschneider zu holen."
    extend " Als die drei zurückkamen, trauten sie ihren Augen nicht..."
    play sound umise_024
    scene magicsquare_moon1 with fastdissolve
    pause 4
    $ songname = "Lure"
    show screen showsong
    play music "audio/bgm/umib_018.ogg"
    kum "WAAAAAAAAAAAAAA!" 
    extend " ...Was ist das und woher ist es gekommen?"
    kum "Wieder einer dieser magischen Kreise, von denen Maria-sama erzählt hat?"
    kan "Das war vor ein paar Minuten noch nicht da...."
    kan "Lass mich die Kette durchschneiden!"
    play sound umise_039
    kan "......."
    "Kanon hat die Kette durchtrennt und öffnet vorsichtig die Tür."
    play sound umise_017
    scene white zorder 99
    with kanon_r
    scene black with fastdissolve
    extend " Er schaut in den Raum, hält einen Moment inne und atmet tief durch..."
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
    hide but
    hide kan
    hide nat
    show mar a22akuwarai2 at m
    mar "Kihihihihihihihih!!"
    mar "Das ist der erste magische Kreis des Mondes!"
    extend " Das Design des magischen Kreises ähnelt der Darstellung einer Tür. Der hebräische Vers darauf ist Psalm 107:16 entnommen und lautet:" 
    mar "'Denn er hat eherne Tore zerbrochen und eiserne Riegel durchschnitten'."
    mar "Die Hexe lässt sich nicht einmal von einer Türkette aufhalten!"
    extend " Kihihihihihihihi!!!"
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
    extend " Ich werde dich kriegen, wie auch immer du heißt!"
    extend " Wenn du BEATRICE sein willst, nehme ich dein fettes Kleid und ramme es dir in den Hals!"
    but "Ich werde dir die Scheiße aus dem Leib prügeln, das schwöre ich dir!!!"
    but "Verschlossener Gartenschuppen mit dem Schlüssel innerhalb?" 
    extend " Eine Türkette?" 
    extend " Einfach nur lächerlich!"
    extend " Ich werde jedes Detail deiner billigen Tricks herausfinden und dich zum Schafott bringen!"
    but "Ich werde dich eigenhändig umbringen!!!"
    extend " GNHAAAAAAAAAAAAAAAAAAAAAAAAAAAA!!!!!!"
    extend " BEATRICEEEEEEEEEEEEE!!!!!"
    window hide
    pause 2
    $ songname = "-"
    call chapterendb
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
    $ chapter = 1003
    $ songname = "-"
    $ save_name = _("EpisodeX Illusion of the golden witch\nDie Illusion der Goldenen Hexe")
    show screen showch
    ## Kapitel 3 Die Illusion der Goldenen Hexe
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
    "Die Verzweiflung macht sich unter den verbliebenden breit."
    extend " Mittlerweile wurde die Villa verlassen und Schutz im Gästehaus gesucht."
    "Die Überlebenden beten einfach, dass ab jetzt niemand mehr sterben muss."
    scene glob_1ar_bg at bgani
    stop wind fadeout 2
    show rainbackscroll
    show rainfrontscroll
    show glob_1ar at bgani
    with gradientcirclefade
    show nat a12defo1 at l
    pause 0.5
    nat "Ich weiß nicht, ob der Täter sich nur in der Villa aufhält, aber hier ist der Vorrat an Essen ein wenig größer."
    show jes a11naku3 at r
    jes "Wieso passiert das alles überhaupt? War es nötig auch nur einen von ihnen zu töten?"
    show nan a1defo1 at m
    nan "Jessica-chan, nur der Täter selbst kennt sein Tatmotiv."
    extend " Es bringt leider überhaupt nichts darüber nachzudenken, so sehr ich deinen Schmerz auch fühle."
    "Jessicas Worte haben irgendwie einen nerv getroffen, denn niemand hat auch nur den Hauch einer Ahnung, warum nach und nach Leute sterben."
    hide nan
    hide nat
    jes a11majime1 "Wo steckt eigentlich Großvater die ganze Zeit?"
    show gen a11defo1 at l
    gen "Der Herr befindet sich nach wie vor in seinem Arbeitszimmer."
    jes a11tereru1 "Natürlich... Hier geht alles den Bach runter und er versteckt sich in seinem übel riechenden Kabuff!"
    extend " Wahahahaha....."
    hide gen
    show kan a13defo2 at l
    kan "Jessica-sama, der Herr ist ein alter Freund der Hexe, sie würde ihn nicht ohne weiteres Töten."
    hide kan
    hide jes
    show but a11aseru1 at m
    but "Diese Hexenlegende, von der ich gehört hab, hat ja damit was zutun, dass Großvater von der Hexe 10 Tonnen Gold erhalten haben soll."
    show kum a12defo2 at r
    kum "Ohohohoh..." 
    extend " das ist tatsächlich wahr und das Gold existiert wirklich!"
    kum "Das Rätsel der Inschrift soll direkt dahin führen."
    extend " Allerdings war bisher keiner in der Lage es zu lösen."
    show mar a22akuwarai2 at l
    mar "Kihihihihihihihihih"
    extend " Ich hab das ganze Rätsel aufgeschrieben."
    extend " Wir sollen es vielleicht endlich anfangen zu lösen, schließlich war das von Anfang an unsere Siegesbedingung"
    hide kum
    show nat a11ikari1 at r
    nat "Maria! Wir haben jetzt keine Zeit für sowas!"
    but a11niramu3 "Ich weiß auch nicht wie uns dieses Rätsel weiterhelfen soll"
    mar a11uuu1 "Uu~!"
    extend " BEATRICE hat doch den Abend vor der ersten Dämmerung gesagt, was passieren wird!"
    nat "Du meinst diesen Brief den du von was weiß ich wo erhalten hast?"
    but "Ich erinnere mich, da stand irgendwas drin von, wir sollen das Rätsel lösen, bevor Zinsen eingeholt werden, weil Großvater den Vertrag mit ihr aufgelöst hat."
    hide nat
    show jes a23majime1 at r
    jes "Und dass sie alles von der Ushiromiya Familie erhält plus Zinsen und diese Zinsen sind...."
    mar a22akuwarai2 "Unsere Leben!"
    extend " Kihihihihihihi!!!"
    mar "Der einzige Weg alles zurück zu erhalten, ist es das Rätsel der Inschrift zu lösen!"
    hide mar
    hide but
    hide jes
    show nan a2fumu1 at m
    nan "Ich habe mal versucht diese Inschrift zu lösen, ich bin aber dran verzweifelt und das obwohl ich Kinzo-san schon seit den alten Tagen kenne."
    nan "Aber wie sagt man so schön? Man kann einem Menschen nur vor den Kopf gucken und nicht in den Kopf."
    hide nan
    show jes b22warai1 at r
    jes "Lass uns mal lesen, was auf der Inschrift stand, Maria-chan..."
    show but b11warai2 at l
    but "Ich bin ehrlich gesagt auch daran interessiert, ich hab mir das noch nie durchgelesen."
    show mar a11niyari1 at m
    mar "Bitte sehr, prägt es euch gut ein, Kihihihihi!!"
    "Maria kramt ein wenig in ihrer Handtasche und holt ein seltsames Buch raus, sie blättert etwas darin herum und fängt an vorzulesen."
    mar "Seht den Süßfischfluss, der durch meine geliebte Heimatstadt fließt. Ihr, die ihr das Goldene Land sucht, folgt seinem Weg stromabwärts auf der Suche nach dem Schlüssel."
    hide jes
    show nat a43headache1 at r
    nat "Wir haben jetzt schon keine Chance, da niemand von uns weiß, wo Vaters alte Heimat war."
    extend " Moment, Genji, weißt du es vielleicht?"
    hide but
    show gen a11defo1 at l
    gen "Entschuldigung, ich weiß es nicht."
    nat "Verdammt... Eva wusste es aber, ich weiß das."
    hide gen
    show jes a23majime1 at l
    jes "Wie können sie wohl schlecht danach fragen."
    hide nat
    show but b23nayamu2 at r
    but "Das ist ja abgefahren, ich weiß zwar nicht, was Süßfischfluss heißt, aber die Morde liefen bislang exakt wie hier niedergeschrieben."
    but "Ich denke aber, dass jemand ohne Japanisch Kenntnisse dieses Rätsel gar nicht lösen kann."
    jes "Erst waren es sechs außerwählte vom Schlüssel, dann Eva und Hideyoshi als die beiden, die sich nahe stehen und jetzt sind wir bei?"
    mar "Preiset meinen Edlen Namen, die dritte Dämmerung!"
    but "Da kommen noch ein paar Dämmerungen mit stich ins Knie, Bauch, Bein und so weiter, wie abgedreht."
    stop music
    scene black with instant
    nat "Sofort die Hände nach oben ihr vier!"
    "Plötzlich wurden nach diesen Ruf alle Gespräche eingestellt, Natsuhi hat angefangen ihre Waffe auf die Bediensteten zu richten."
    "Während das Thema bei der Hexeninschrift lag, ist in der nähe der Bediensteten, die im Hintergrund zugesehen haben, ein Briefumschlag erschienen."
    $ songname = "Fishy Aroma"
    play music umib_019
    scene glob_1ar_bg at bgani
    stop wind fadeout 2
    show rainbackscroll
    show rainfrontscroll
    show glob_1ar at bgani
    with gradientcirclefade
    show screen showsong
    show c_e0101_wall
    show c_e0101_a
    with quickgradientwipeleft
    nat "Wo kommt dieser Briefumschlag her und wieso liegt er genau bei euch vieren?"
    extend " Überlegt euch jetzt gut, was ihr mir antwortet!"
    show kum a12majime1 at leftedge
    kum "Ich bitte Sie Fräulein Natsuhi-sama, dies muss ein Irrtum sein!"
    extend " Bitte nehmen Sie die Waffe runter!"
    hide c_e0101_a
    show c_e0101_b
    nat "Ich hatte schon die ganze Zeit ein mulmiges Gefühl bei euch Bediensteten!"
    extend " Wir sind hier mit der Inschrift beschäftigt und ganz plötzlich taucht in eurer Nähe ein Briefumschlag auf??"
    extend " Ich weiß ganz genau, dass da gerade eben noch keiner war!"
    nat "Ihr könnt gerne jemand anderes für Blöd verkaufen!"
    hide kum
    hide c_e0101_b
    hide c_e0101_wall
    show but b22odoroki2 at m
    but "Also hat den jemand von euch heimlich dahin gelegt?"
    show nan a2fumu1 at rightedge
    nan "Die Möglichkeit besteht durchaus, aber wer soll es gewesen sein?"
    hide but  
    hide nan
    show c_e0101_wall
    show c_e0101_b
    with quickergradientwipeleft
    nat "Vielleicht ja du Kumasawa, du warst immer für irgendwelche Streiche zu haben, oder du Shannon, die den ganzen Tag nur vor sich hin träumt!"
    show sha a11odoroki1 at leftedge
    sha ".....Huh... Fräulein Natsuhi-sama....."
    nat "Kanon du bist auch nicht aus dem Schneider, deine Fähigkeit deine Präsenz fast vollständig zu verbergen, ist noch am allermeisten Verdächtig!"
    hide sha
    show kan a13defo2 at leftedge
    kan "Fräulein Natsuhi-sama Ich..."
    nat "Genji, du warst von allen Bediensteten immer Vater am nächsten, du könntest dies für ihn gemacht haben."
    hide kan
    show gen a21kashikomari1 at leftedge
    gen "........."
    scene black with dissolve
    "Natsuhi ist sich sehr sicher, der Täter ist einer der vier!"
    extend " ...Es ist unmöglich, dass so ein Brief aus dem nichts erscheinen kann..."
    "Es war entweder pure Absicht oder der Täter war beim hinlegen des Briefes nicht geschickt genug."
    scene glob_1ar_bg at bgani
    stop wind fadeout 2
    show rainbackscroll
    show rainfrontscroll
    show glob_1ar at bgani
    with quickergradientwiperight
    show nat a17ikari2 at l
    nat "Ihr alle wisst exakt, welche Wege es auf der Insel gibt, es wäre für euch ein leichtes die Morde geschickt zu begehen ohne erwischt zu werden!"
    nat "Es wäre das beste für uns, wenn wir uns aufteilen würden!"
    nat "Battler, Jessica, Maria, Nanjo und ich bleiben hier!"
    nat "Wir alle haben ein Alibi, ihr habt das nicht!"
    hide nat
    show but b11oya1 at l
    but "Wollen wir sie wirklich von hier verbannen?"
    show mar a22akuwarai2 at r
    mar "Kihihihihihihihi!!!"
    extend " BEATRICE wird sie für die nächsten Dämmerungen opfern!"
    hide but
    hide mar
    show kum a12majime1 at r
    kum "Natsuhi-sama vielleicht sollten wir nochmal drüber reden!"
    show nat a17ikari2 at l
    nat "Es tut mir leid, ich selber möchte euch nicht verdächtigen, aber ich kann euch allen nicht trauen..."
    extend " Bitte begebt euch zurück in die Villa."
    extend " Ich bete zu Gott, dass euch nicht passiert."
    nat "Das Risiko ist aber auch zu hoch, euch hier zu behalten, wenn der Täter wirklich einer von euch sein sollte."
    nat "Sollte ich euch in den tot schicken, dann möge die Hexe auch mich mitnehmen, denn ich hätte es verdient."
    show gen a21kashikomari1 at m
    gen "Dies war ein Befehl von unserer Vorgesetzten, wir müssen nun gehen."
    kum "Passt bitte auch auf euch auf!"
    nat "Es tut mir so unendlich leid, bitte überlebt!"
    "Natsuhi muss hier eine folgenschwere Entscheidung treffen. Schließlich kann der Brief nicht von denen dahingelegt worden sein, die mit der Inschrift beschäftigt waren."
    scene black with dissolve
    play sound umise_016
    "Die verdächtigen vier Bediensteten haben nun das Gästehaus verlassen und laufen Richtung Villa."
    "Natsuhi selber fühlt sich von allen am schlechtesten, da die Möglichkeit besteht, dass sie die vier gerade in den tot geschickt hat."
    "Es wäre aber auch in dieser Situation viel zu riskant gewesen, die vier hier zu behalten."
    scene glob_1ar_bg at bgani
    stop wind fadeout 2
    show rainbackscroll
    show rainfrontscroll
    show glob_1ar at bgani
    with quickergradientwiperight
    show mar a11niyari1 at m
    mar "Wollt ihr nicht schauen, was in dem Brief steht?"
    show but b22nayamu1 at l
    but "Ich hab eigentlich gar keinen bock darauf, da steht bestimmt sowas drin wie 'Haha, ihr habt die anderen wohl rausgeschmissen, jetzt töte ich die!' Weil die das doch erwartet hat."
    show jes a11majime1 at r
    jes "Machen wir ihn erst einmal auf!"
    "Jessica öffnet vorsichtig den Brief der mit dem Siegel der Ushiromiya Familie versiegelt wurde."
    play sound sysse_page
    scene letter1 with quickgradientwiperight
    ntxt "Ich hoffe euch gefällt Kinzo-samas kleines Rätsel."
    ntxt "Hoffentlich tun Sie nicht missverstehen, dass sie jetzt die Zeit einfach absitzen können."
    extend " Sobald um 0 Uhr der nächste Tag anbricht, gewinne ich automatisch, da führt kein Weg dran vorbei."
    nvl clear 
    ntxt "Ich bitte Sie also darum, das Rätsel meiner Inschrift zu lösen um all dies, dass Sie verloren haben von mir zurück zu erhalten."
    extend " Allerdings bin ich mir sehr sicher, dass Sie nicht gewinnen werden, also Preiset meinen edlen Namen!"
    ntxt "gez. BEATRICE, die Goldene"
    nvl clear
    but "Will die uns verarschen?"
    extend " Wir sollen allen ernstes das Rätsel lösen?"
    "Für BEATRICE scheint das alles nur ein Spiel zu sein, dass man gewinnen und verlieren kann, Battler und die anderen können gar nicht glauben, was sie da gelesen haben."
    nat "Meine Kopfschmerzen, lassen ein nachdenken darüber gar nicht zu."
    but "Das ist alles bullshit! Wir haben nicht das nötige Wissen um es zu lösen!"
    jes "Wir sollten uns ein wenig ausruhen."
    extend " Wir müssen bei Kräften sein, wenn der Täter wieder zuschlagen will..."
    but "Gute Idee, vielleicht kommt einem ja ein Geistesblitz und wir schaffen es in den nächsten sechs Stunden das Rätsel zu lösen."
    but "Ein Telefon klingelt?"
    extend " Wurden die Leitungen nicht getrennt?"
    "Einige Stunden später klingelt aus heiterem Himmel plötzlich das Telefon im Gästehaus."
    jes "Vielleicht hat der Täter ja nur die äußeren Leitungen gecappt."
    nat "Battler-kun übernimmt das für mich, meine Kopfschmerzen sind zu stark."
    but "Da bin ich mal gespannt."
    but "Hallo?....." 
    extend " Wer ist da?"
    $ songname = "Happy Maria!"
    play music umib_104
    show screen showsong
    bea "<congratulations>"
    bea "<I am fine, and youuuuuuuu?~>"
    but "Wer zum Teufel bist du?"
    extend " ....Willst du mich verarschen was soll das?"
    bea "<In english please!>"
    extend " Komm schon, dass hast du als Kind doch ständig gemacht, Ushiromiya Battler!"
    "Spöttisches Englisch dröhnt aus der Ohrmuschel, die Stimme hat Battler noch nie zuvor gehört."
    but "Du..." 
    extend " Du bist absolut irre!"
    but "Sag mir sofort wer du bist!"
    bea "Komm schon... rate doch mal, du könntest einen Trip nach Hawaii gewinnen!"
    extend " Kyahahahahahahah"
    but "BEATRICE?" 
    extend " .....Du bist BEATRICE?!!!"
    bea "<Yeessssssss I aaaaaammmmm!!>"
    extend "Ich wollte euch vier nur gratulieren, ich lade euch nämlich ins Goldene Land ein!"
    but "Das kannst du dir sonst wo hinstecken!"
    extend " Was ist mit Shannon, Kumasawa und den anderen passiert?"
    bea "Ohhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh"
    extend " Ich habe sie für meine Auferstehung geopfert..."
    extend " Kyahahahahahahaha ahahahahahahhahahahah!!!!!??!?!?!?!?!"
    but "Ich werde dir dumme Bitch niemals verzeihen!"
    extend " Wie kannst du es nur wagen???"
    kin "Wahahahahahaha!!"
    extend " Du bist heute sehr gut drauf, BEATRICE."
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
    "Wütend legt Battler auf, der Täter ruft doch allen ernstes an und behauptet wieder gemordet zu haben..."
    jes "War das BEATRICE?"
    extend " Was ist passiert?"
    but "Wir müssen sofort zur Villa, es könnte schon zu spät sein!"
    nat "Dann schnell!"
    "Während sich die vier aufmachen um zur Villa zu gehen, waren Kinzo und BEATRICE noch immer in Kinzos Arbeitszimmer."
    kin "Heute ist ein großer Tag, endlich durfte ich dein Lächeln wiedersehen!"
    extend " Es würde mir überhaupt nichts ausmachen, würdest du mir mein Leben nun entreißen!"
    bea "Ich denke einfach mal, dass ich genau dies machen werde!"
    kin "Warte bitte, was..."
    extend " ahhhhhhhhhhhhhhhhhrggggggghhhhhhhhhhhhhhhhhhhhhhhhhhhhh"
    bea "Tut mir leid Kinzo, aber du gehörst schon lange nicht mehr in diese Welt."
    "Kinzos Körper ist in Flammen aufgegangen und seine Haut und Kleidung verbrennem vollständig."
    bea "Für meine Vollständige Wiederauferstehung brauch ich immer noch ein Opfer und das bist dann doch du."
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
    "Da nicht daran gedacht wurde, den verbannten Bediensteten mindestens einen Generalschlüssel abzunehmen, müssen sie improvisieren"
    "Battler nimmt sich einen Stein und macht sich bereit es in das Wohnzimmerfenster zu donnern."
    $ songname = "goldenslaughterer"
    show screen showsong
    but "Kanon!"
    jes "Was ist siehst du Battler-kun?"
    but "Hier drin liegt Kanon!"
    extend " Nanjo-sensei, bitte schauen Sie sich ihn an!"
    nan "Er atmet nicht mehr, er ist erst kürzlich von uns gegangen."
    extend " Sein Kopf wurde durchbohrt, aber sein Pfahl hat nicht gehalten und ist rausgefallen."
    but "Verdammt! Verdammt! Verdammt!"
    extend " Die anderen sind bestimmt ebenfalls ermordet worden!"
    nat "Da liegt ein Brief!"
    "Natsuhi öffnet vorsichtig den Brief und nimmt zwei Schlüssel raus."
    nat " Das ist ein Generalschlüssel und einer für mein Zimmer in der oberen Etage!"
    but "Nicht wie hin!"
    "So schnell wie möglich, eilten sie in das Gästezimmer"
    but "Kumasawa....."
    extend " Du hast das am aller wenigsten Verdient, das darf nicht wahr sein!"
    nan "Ihre Brust wurde durchbohrt und das erneut mit einem dieser Pfähle."
    jes "Hier ist auch ein Brief, wieder ein Generalschlüssel und der andere Schlüssel führt in mein Zimmer!"
    "In Jessicas Zimmer wurde Genji gefunden. Sein Bauch wurde durchbohrt und auch hier ein Brief mit Generalschlüssel und ein Schlüssel in den Heizungskeller."
    but "Das stinkt ja bestialisch!"
    jes "Das ist ja widerlich!"
    nat "Da liegt Vater!"
    jes "Bist du sicher?"
    extend " Ich finde man erkennt Kinzo gar nicht wieder..."
    nat "Sieh dir sein Fuß an, er hat sechs Zehen, sowas hatte nur Vater."
    but "BEATRICE hatte wohl sehr schnell keine lust mehr auf den alten!"
    "Der Brief in dem Heizungskeller beinhaltete nur einen Schlüssel zur Kapelle."
    extend " Alle machten sich so schnell wie möglich auf den Weg dorthin!"
    nat "Ich öffne jetzt die Kapelle!"
    "Natsuhi öffnete mit dem Schlüssel die Tür und dieser Anblick innerhalb der Kapelle, ist wohl der schlimmste überhaupt."
    but "Shannon!!!!"
    extend "Neiiiinnnn!!!!!!!"
    but "wieso nur? wieso nur?"
    jes "Wir werden auch sterben!"
    "Jemand wurde über den Altar in der Kapelle erhangen..."
    extend " Es war Shannon..."
    but "BEATRICE wollte zum Finale hin nochmal den grausamsten Mord überhaupt durchführen."
    extend " Es hat ja nicht gereicht sechs von uns zu entstellen, nein...."
    but " Man muss ja unbedingt jemanden erhängen, der bereits tot ist..."
    "Natsuhi öffnete den Brief in der Kapelle, dort drin, war Shannons Generalschlüssel und der Schlüssel ins Wohnzimmer."
    nat "Der Schlüssel in diesem Brief führt ins Wohnzimmer, wo Kanon liegt."
    extend " Eine absolut perfekte Schleife, das ist doch absolut unmöglich!!"
    but "Es bringt alles absolut gar nichts mehr...."
    extend " ....Es bringt überhaupt gar nichts mehr irgendwas...."
    nat "Battler-kun? Wo willst du hin?"
    "Battler stürmte aus der Kapelle und rannte in Richtung Villa."
    "Er rannte so schnell er konnte in die Eingangshalle zum Gemälde von BEATRICE."
    but "BEATRICE!!!"
    but "Bist du jetzt glücklich?"
    extend "Stell dich mir hier und jetzt!"
    extend " Trau dich und leg dich mit mir an!"
    but "Alle Morde wurden durchgeführt, jetzt komm endlich raus!!"
    extend " Ich schneid dir deine Kuhtitten auf und mach mir ein Sandwich drauß!"
    bea "*Gacker*Gacker*"
    extend " Was ein charmanter Mann!"
    but "Ganz genau, zeig dich mir!!!"
    extend " Komm schon!!!!" 
    extend " BEATRICEEEEE!!!!!"
    ## Kapitel 3 Ende


































