

label schule:
    $ chapter = 1000
    $ songname = "-"
    $ save_name = _("EpisodeX Illusion of the golden witch\nProlog")
    ##Prolog
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
    show screen showsong
    show goddomain with dissolve
    pause 5
    hide goddomain with dissolve
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
    gen "Kanon, Dr. Nanjo-sensei"
    extend " Was ist hier los?"
    kan "Ich weiß es nicht, Genji-sama..."
    extend " ......Es fehlen exakt sechs Leute."
    extend " Vielleicht war es ja die Hexe...."
    eva "Red nicht so einen unsinn, geh lieber weiter suchen, als in so einem Moment an ein dummes Ammenmärchen zu denken."
    kan "Ich bitte um Verzeihung, Eva-sama, das war taktlos von mir..."
    extend " mir ist aber etwas seltsames am Rosengartenschuppen aufgefallen, ich habe es aber nicht näher inspiziert und bin sofort hergekommen."
    gen "Wir werden es uns ansehen. Danke, Kanon."
    nan "Werte Natsuhi-san und Eva-san."
    extend " Ich werde mit Ihnen mitgehen, falls sich jemand verletzt hat."
    extend " ...Hoffen wir, dass es allen gut geht."
    eva "Dann los zum Gartenschuppen!"
    extend " Ich weiß zwar nicht, was George, Krauss und die anderen dort vorhaben, aber es ist unsere einzige Spur."
    nat "Es wäre besser für uns, sie so schnell wie möglich aus dem Regen zu holen."
    eva "Wie geschmacklos!"
    extend " Wer malt den bitte mit Roter Farbe gruselige Symbole an ein Tor?"
    nat " Da denkt man direkt, wir hätten es hier mit einem kindischen Streich zutun."
    eva "Ich bekomme das Tor nicht auf, es ist abgeschlossen, gibt es keinen Schlüssel?"
    gen "Der Schlüssel befindet sich im Bedienstetenraum, ich gehe es sofort holen."
    eva "Lass uns das Tor schnell öffnen und nachsehen."
    extend " Ich weiß schonmal mit wem ich gleich schimpfen werde, wenn die da drin sind und uns verarschen wollen."
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
    show screen showsong
    jes "KYAAAAAAAAAAAAAAAAAA!!!!!!!!"
    extend " GEORGE???!?!?!?!?"
    nat "Genji! Ruf sofort die Polizei!"
    gen "Wie Ihr wünscht, es wird sofort erledigt!"
    extend " Kanon..."
    extend " Erstatte den werten Herrn Kinzo-sama umgehend Bericht!"
    kan "Ich habe verstanden!"
    kum "Was ist hier los? Was soll dieser Aufruhr?"
    extend " Warum sind denn alle hier versammelt?"
    sha "Ist etwas schlimmes passiert?"
    nat "Kumasawa! Shannon! Ihr müsst nicht näher kommen! Bringt Battler und Jessica sofort zurück ins Gästehaus!"
    kum "Ohohohoho, wir sollten dann wohl besser gehen."
    extend " Battler-sama, Jessica-sama, folgt uns bitte."
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
    but "Dad, Kyrie, Gohda, Tante Rosa und wieso auch du George-aniki?"
    extend "Ich versteh nichts mehr, es ist einfach nicht fair!"
    extend " Niemand von euch hat es verdient, dass man euer Gesicht nicht mehr erkennen kann...."
    but "Es wäre viel einfacher gewesen, euch einfach nur ins Jenseits zu schicken und hier rein zu legen..."
    extend " War das wirklich nötig? Macht es das wirklich besser?"
    hid "bleib stark Battler-kun, die Polizei wird Morgen den Täter finden und verhaften."
    extend " ich bin genauso traurig wie du, aber wir dürfen jetzt keine falsche Bewegung machen."
    eva "GEORGE!!!! WAS HABEN SIE DIR ANGETAN!!"
    extend " ahhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh!!!!!!!!!!!!"
    eva "WARUM NUR MEIN GEORGE???!!?!??!"
    nan "Ja, kein Zweifel, das können die nicht überlebt haben."
    extend " Ich bin zwar ein Arzt, aber da kann sogar ich nichts dran aussrichten."
    extend " Es tut mir so unendlich leid, ich kann aber nicht helfen."
    nat "Alles okay, sogar ich sehe, dass Sie da nichts machen können."
    extend " Es gibt keinen Grund sich zu entschuldigen."
    sha "Ist das dort...."
    extend " George-sama?"
    extend " Warum?"
    but "Richtig Shannon-chan, das ist Aniki"
    extend " Sag mir... Shannon-chan..."
    extend " Wie hast du Aniki zuletzt erlebt?"
    but "Ich weiß was du sagen willst."
    extend " Der Ring an deinem Ringfinger ist wunderschön, ich bin mir sicher, er will, dass du ihn so in Erinnerung behältst."
    but "Also bitte, sieh ihn dir nicht an, ich möchte nicht, dass du ihn so sehen musst."
    sha "Battler-sama.... Ich...."
    hid "Es wäre besser diesen Ort der Polizei zu überlassen."
    extend " Wenn wir auch nur etwas näher kommen, könnte es die Ermittlungen beeinträchtigen."
    nat "Hast du die Polizei erreicht, Genji?"
    gen "Leider nicht, die Leitungen sind gekappt worden."
    extend " Ein Anruf kam nicht durch."
    nat "Wer um alles in der Welt??"
    kin "Ich lebe noch."
    extend " Wahahahahaha!!"
    kin "Das Dämonenroulette hat mich wohl noch nicht ausgewählt!"
    extend  "Doch das alles ist völlig egal!"
    kin "Goldene Hexe Beatrice!"
    extend " Nimm dir alles was du von mir willst!"
    kin "Seit dem ich unseren Vertrag aufgelöst habe, besagt die spezielle Klausel, dass mein Reichtum von 10 Tonnen purem Gold, die du mir gegeben hast mit Zinsen zurückbekommst!"
    kin "Wie ich sehe, hast du bereits angefangen diese Zinsen einzuziehen!"
    kin "Oh Beatrice! Bevor das Roulette mich erwählt, möchte ich dich noch ein letztes mal sehen!"
    extend "Ich bin der festen überzeugung, dass du mich unsichtbar von irgendwo in diesem Raum beobachtest und dich über mich lustig machst!"
    extend " ....Ich bitte dich! Zeig mir dein schönes Lächeln noch ein letztes mal!"
    kin "BEATRICE!!!"
    extend " Nimm mir mein Leben mit einem einzigen Fingerschnipsen wenn du willst!!"
    extend " ...Aber bitte zeig dich mir und Lächle dabei wenn du es tust!"
    extend " BEATRICEEEEEEE!!!!"
    ##Kapitel Ende
    $ chapter = 1002
    $ songname = "-"
    $ save_name = _("EpisodeX Illusion of the golden witch\nDie, die sich nahe stehen")
    show screen showch
    ## Kapitel 2 - Die, die sich nahe stehen
    but "Was machen wir jetzt?"
    extend " Hier läuft ein Mörder frei herum..."
    eva " Wir sollten abwarten, bis sich der Sturm verzieht."
    extend " Heißt aber auch, dass wir hier bis morgen früh aussitzen müssen."
    jes "Was ist, wenn der Mörder wieder zuschlägt?"
    extend " ...Wichtiger ist auch, wer der Mörder ist?"
    extend " Es ist entweder eine Person, die sich vorher auf die Insel geschlichen hat oder einer von uns."
    eva "Wir haben jetzt Schrotflinten zur Selbstverteidigung."
    extend " Im ernstfall wissen wir, wie man damit schießt."
    eva "Es gäbe viele Gründe für dritte Personen uns auszumerzen, vorallem wenn man die Legende des Goldes kennt."
    nat "Mein Ehemann, war immer davon überzeugt, dass Vater sein Gold irgendwo auf der Insel versteckt hat."
    extend " Letztes Jahr hat Vater ein Rätsel unter dem Gemälde der Hexe platziert, aber es konnte es nicht lösen."
    but "Dieses Rätsel sieht aber auch abgefahren aus!"
    extend " Zur Zeit der zweiten Dämmerung sollen die, die sich nahe stehen auseinanderreißen oder sowas."
    but "Wie soll man so auf einen Ort auf der Insel schließen können?"
    jes "Das Rätsel konnte man auch als Wiederbelebungszeremonie deuten."
    extend "'Zur Zeit der neunten Dämmerung, wird die Hexe wiederbelebt, und niemand wird am Leben bleiben'."
    eva "Die Hexe Beatrice aus dem Wald, ist bereits ein Gerücht, dass es während unserer Kindheit gegeben hat."
    extend " Wie soll das bitte aussehen?"
    extend " Ein magisches Wesen, tötet uns um sich selber wiederzubeleben?"
    eva "Dieses Rätsel wird doch nur als Deckmantel verwendet!"
    nat "Es wäre aber auch schwachsinnig sich auszudenken, dass irgendjemand sich als Beatrice verkleidet und die Morde ausübt."
    eva "Sich als Beatrice verkleiden?"
    extend " Also jemand wie beispielweise Shannon verkleidet sich als Hexe und tötet uns alle?"
    extend " Der Gedanke klingt einfach schon mehr als absurd."
    but "Richtig!"
    extend " Shannon-chan könnte keiner Fliege was zuleide tun."
    eva "Stille Wasser sind tief, Battler-kun *kicher*"
    extend " Spaß beiseite, dieses unfähige Ding, kann noch nicht einmal ein Buttermesser in die Hand nehmen."
    nat "Eva-san! Das war mehr als nur unhöflich gegenüber meiner angestellten!"
    eva "Oh, entschuldigung!..." 
    extend " ...Kommt bestimmt nicht wieder vor... *kicher*"
    but "Ich würde Shannon niemals verdächtigen!"
    extend " Sie war am boden zerstört als sie erfahren hat, das George-aniki gestorben ist."
    eva "Meine Güte, Battler-kun, ich verdächtige sie nicht, das war doch nur ein Beispiel."
    but "Das war überflüssig, das musste nicht sein..."
    nat "Der Täter muss unter uns sein."
    extend " ...Es gibt keine unsichtbaren Wesen, die einfach Menschen beliebig umbringen und in verschlossene Räume sperren."
    but "Da hast du vermutlich recht mit.."
    extend " aber ich kann auch nicht glauben, dass der Täter gerade seelenruhig mit uns in einem Raum sitzt und zuhört."
    nat "Das stimmt, deswegen sollten wir uns aufteilen."
    eva "Huh, aufteilen?"
    nat "Die einzige Möglichkeit das Tor zum Gartenschuppen zu öffnen ist der Schlüssel aus dem Raum der Bediensteten!"
    extend " Dieser Raum ist aber auch nur mit einem Generalschlüssel zu öffnen, den die Bediensteten bei sich tragen!"
    gen "Der Raum war abgeschlossen, als ich den Schlüssel holen wollte, ich musste meinen Generalschlüssel verwenden."
    eva "Wenn das stimmt, kann nur ein Bediensteter die Tat begannen haben!"
    extend " ....Niemand von uns könnte diesen Raum öffnen um den Schlüssel zu stehlen!"
    but "Das klingt einleuchtend, aber warum sollte ein Bediensteter sowas tun?"
    extend " Darüber nachzudenken ist schon absurd, was sollte das motiv sein?"
    hid "Ich finde es bemerkenswert, wie du niemanden verdächtigen möchtest, aber irgendwer muss es doch gewesen sein."
    extend " ...Vielleicht liegen wir alle falsch und es war wirklich eine Hexe."
    but "Ich weigere mich an so etwas zu glauben! Es gibt keine Magie und auch keine Hexe!"
    but "Achja, wo ist eigentlich Kanon?"
    gen "Er sichert aktuell die Eingänge der Villa und überprüft die Fenster, er sollte gleich zurückkommen."
    but "Ist das nicht super Gefährlich?"
    extend " ...Was wenn ihm dabei der Täter auflauert."
    gen "Kanon ist sehr fähig, er ist nahezu nicht Präsent für irgendjemanden."
    extend " Ich habe großes Vertrauen in ihm"
    but " ich habe schon gehört, dass er gute Arbeit leistet, aber da bin ich echt platt!"
    extend " Er muss mir mal seine Tricks verraten, dann kann ich mich bestimmt mal in ein paar Damenumkleiden schleichen."
    jes "Verdammter perversling! Ich werde Kanon sagen, er soll dir gar nichts beibringen!"
    but "owowowowowo, wieso schlägst du mich schon wieder? Das tut verdammt weh!"
    jes "Ich hätte dich dafür besser erschießen sollen!"
    but "Tut mir leid, tut mir leid, tut mir leid!!!"
    jes "Sollte es dir auch!"
    hid "Was war das eigentlich für ein Symbol auf dem Tor?"
    extend "Es war kein Pentagramm, eher ein Deutsches Kreuz?"
    mar "Kihihihhihihihihih!"
    extend "Das war der siebte magische Kreis der Sonne!"
    mar "Die Schrift auf dem magischen Kreis ist auf Hebräisch. Auf jedem der Arme des Kreuzes stehen die Namen der Engel, die über Wind, Feuer, Erde und Wasser herrschen:" 
    extend " Chasan, Arel, Phorlakh und Taliahad." 
    mar "Ebenso stehen zwischen den Armen des Kreuzes die vier großen Könige der Elemente:" 
    extend " Ariel, Seraph, Tharshis und Cherub. Die Worte, die um das Kreuz herum geschrieben sind, stammen aus Psalm 116:16-17 der Bibel und besagen:" 
    mar "'Der Herr hat mich von meinen Ketten befreit. Ich will dir ein Opfer des Dankes darbringen und den Namen des Herrn anrufen.'"
    but "Wie kommt es, dass du dich mit sowas auskennst?"
    mar "Kihihihihihihi!"
    extend " Ich weiß vieles und es wird nicht der letzte magische Kreis sein, den du sehen wirst!"
    mar "Kihihihihihihi!"
    jes "Euch fällt auch gerade auf, dass Maria sich seltsam benimmt?"
    but "Da ist doch was im Busch!"
    mar "Ich weiß, wer die sechs umgebracht hat!"
    nat "Du weißt es?"
    extend " Rede keinen unsinn Maria-chan!"
    mar "Es war Beatrice!"
    but "Maria... Dafür ist jetzt nicht die Zeit!"
    mar "Uu~....."
    extend " Es war aber Beatrice!"
    extend " BEATRICE!!, BEATRICE!!, BEATRICE!!"
    eva "Wir zwei gehen ins Gästezimmer um uns auszuruhen, zur Not haben wir die Schrotflinten."
    gen "Es wäre besser, wenn Sie trotzdem nicht alleine gehen, wir begleiten euch!"
    nat "Richtig, es wäre töricht uns jetzt so zu trennen!"
    hid "Danke Leute, ihr meint es zu gut mit uns!"
    extend " Wahahahaha!"
    nat "Geht in das Gästezimmer und verschließt eure Tür mit der Kette, damit der Täter nicht reinkommen kann."
    kum "Selbst ein fähiger Killer, müsste die Kette mit einem Bolzen zerschneiden um rein zu kommen."
    extend " Das würde euch die nötige Zeit zum reagieren geben."
    hid "Vielen Dank, damit können wir uns ohne angst mal ausruhen!"
    hid "Schatz, das war ein harter Tag, George würde aber nicht wollen, dass wir jetzt trübsaal blasen."
    extend " Er wird uns vom Himmel aus Schutz bieten, damit wir morgen sicher die Insel verlassen können."
    eva "Schatz!! halt mich!!"
    hid "So ist es gut, lass einfach alles raus, ich bin genauso traurig wie du und es tut so unendlich weh!"
    extend " Er würde aber nicht wollen, dass wir viel um ihn trauern, sondern weitermachen und ihn in guten Erinnerungen behalten!"
    eva "Er war so ein guter Junge, er hatte noch so viel vor sich."
    extend " Warum nur, warum nur?? Wer war das??"
    eva "Ich werde den Täter finden und töten!"
    extend " Wie kann er das nur meinem George antun!!"
    hid "Nana beruhig dich, Eva!"
    extend " George würde keine Rache wollen!"
    extend " Ich versteh dich nur zu gut."
    hid "Wer zum Teufel seid ihr und wo kommt ihr her?"
    eva "Verschwindet sofort, ich bin bewaffnet!"
    zep "Ist euer Liebesband echt?{font=fonts/AOTFShinGoProMedium.otf}♪{/font}"
    extend " Könnt ihr zweifelos bestehen in diesem Test!{font=fonts/AOTFShinGoProMedium.otf}♪{/font}"
    fur "Träumt ihr nur vor euch her?{font=fonts/AOTFShinGoProMedium.otf}♪{/font}"
    extend " Werdet ihr es bald sicherlich bereuen!{font=fonts/AOTFShinGoProMedium.otf}♪{/font}"
    zep "Tretet an zum Gefecht!{font=fonts/AOTFShinGoProMedium.otf}♪{/font}"
    extend " Was wahre Liebe bedeutet wird heute aufgedeckt!{font=fonts/AOTFShinGoProMedium.otf}♪{/font}"
    fur "Heute können sich alle oder keiner hier bewähren!{font=fonts/AOTFShinGoProMedium.otf}♪{/font}"
    extend " Und sich am Traum der wahren Liebe erfreuen!{font=fonts/AOTFShinGoProMedium.otf}♪{/font}"
    zep "Bildet euch nicht ein dass Gottes Wort euch schützt!{font=fonts/AOTFShinGoProMedium.otf}♪{/font}"
    extend " Und dass eure Liebe wird von diesem Gnäd'gen Herrn gestützt!{font=fonts/AOTFShinGoProMedium.otf}♪{/font}"
    fur "So werdet ihr nicht bestehen{font=fonts/AOTFShinGoProMedium.otf}♪{/font}!"
    extend " Beide müsst ihr gehen!{font=fonts/AOTFShinGoProMedium.otf}♪{/font}"
    zep "Geht ihr als liebendes Paar hervor?{font=fonts/AOTFShinGoProMedium.otf}♪{/font}"
    fur " So gewähren wir euch etwas, das habt ihr längst verloren!{font=fonts/AOTFShinGoProMedium.otf}♪{/font}"
    zep "Da hat uns Fräulein Beatrice-sama ja, ein vielversprechendes Liebespaar zugeteilt, nicht wahr Furfur?"
    fur "Ich spüre die Liebe mit jeder Pfaser meines Körpers, es ist Elektrizierend, nicht wahr Zepar?"
    eva "Was wollt ihr von uns?"
    extend " ..Kommt näher und ich schieße!"
    zep "Ich bin einer der 72 Großen Dämonen, die Dämonin der Liebe, mein Name lautet Zepar!"
    fur "Ich bin einer der 72 Großen Dämonen, die Dämonin der Liebe, mein Name lautet Furfur!"
    eva "Ihr sollt Dämonen sein?"
    extend " ...Und von was für einen Test habt ihr gesungen?"
    zep "Hast du das gehört Furfur?"
    fur "Laut und deutlich, Zepar!"
    zep "Ihr werdet euch eine Prüfung unterziehen müssen!"
    fur "Wenn ihr euch weigert, wartet nur der tot auf euch!"
    zep "Ihr wurdet von der Großen Fräulein Beatrice-sama für die Zweite Dämmerung auserkoren!"
    eva "Das ist doch lächerlich!"
    extend " Was glaubt ihr wer ihr seid!?!!"
    hid "Die Kette bewegt sich nicht!"
    extend " Ich kann die Tür nicht öffnen!"
    zep "Sieh nur Furfur!"
    extend " Sie versuchen zu entkommen!"
    fur "Das ist absolut unmöglich, sie denken, sie könnten Großen Dämonen entkommen, Zepar!"
    hid "Was müssen wir für diesen Test machen?"
    eva "Schatz, du willst doch nicht wirklich..."
    zep "Dafür müsst ihr uns eine einfache Frage beantworten!"
    fur "Wenn ihr sie richtig beantwortet, dürft ihr den Raum verlassen!"
    eva "Dann raus damit, welche Frage ist es?"
    hid "Eva!"
    extend " Wir dürfen die Dinge nicht überstürzen!"
    zep "Nun denn, wir sollten keine Zeit verschwenden, Beatrice-sama wird langsam ungeduldig, Furfur"
    fur "Dann sollten wir mit dem Test beginnen, Zepar!"
    zep "Die Frage die wir euch stellen wollen lautet..."
    $ songname = "Dancing pipe"
    show screen showsong
    fur "Was ist das, was ihr zwei gemeinsam am meisten liebt?"
    zep "Beantwortet die Frage mit Bedacht, von der hängt euer Liebesleben ab!"
    fur "Bedenkt, dass ihr nur eine gemeinsame Antwort abgeben könnt und zwar nur einmal!"
    hid "Die Frage ist wohl ein Scherz, es gibt nur diese eine Antwort, Eva!"
    eva "Deswegen hab ich dich geheiratet, ich weiß genau, was du meinst!"
    hid "Da gibt keine zwei Meinungen."
    extend " Unsere gemeinsame Antwort lautet.."
    extend " Unser Sohn George!"
    eva "George war das beste, was uns jemals passiert ist!"
    extend " Wir lieben ihn mehr als alles andere!"
    hid "Seht ihr, wir sind fest entschlossen!"
    zep "Hast du gehört, was sie gerade gesagt haben, Furfur?"
    fur "Das ist ja sowas von romantisch, Zepar!"
    zep "Aber die Antwort ist leider nicht richtig!"
    fur "Damit ist das Spiel vorbei und euer Leben gehört Beatrice-sama!"
    eva "Wollt ihr uns verarschen? Wie kann die Antwort nicht richtig sein?"
    hid "Genau!"
    extend " Das ist so ein Test den man nicht bestehen kann, weil die richtige Antwort immer das ist, was euch gerade so passt!"
    extend " ...Ich hab doch recht!"
    zep "Sie sehen ziemlich sauer aus, Furfur!"
    fur "Dabei haben beide offensichtlich gelogen, Zepar!"
    eva "Das ist doch wohl die Höhe!"
    extend " Verschwindet, oder Schrotmunition fliegt in eure dünnen Körper!"
    hid "Das kann nicht sein!"
    extend " George???"
    eva "Du bist doch gestorben???"
    extend " Ich hab deine Leiche gesehen, wie ist das möglich?"
    geo "Ihr liebt mich nicht am aller meisten!"
    extend " Das habt ihr noch nie getan!"
    eva "Nein, George! Bitte! Das stimmt so nicht!"
    extend " Du warst immer das aller wichtigste für uns!"
    hid "George! Bitte wir können über alles reden!"
    geo "Ja, ich war für euch das wichtigste..."
    extend " Ich war wichtig dafür, euern Profit zu erweitern!"
    geo " Ich wurde von euch immer streng zu einem 'Gentlemen' erzogen, damit ich zu eurem Vorteil agiere!"
    eva "Nein George! So ist das nicht!"
    geo "Oh doch!"
    extend " Euch hat es immer nur interessiert, wie ihr Großvaters Erbe einstreichen könnt!"
    geo "Es war euch wichtiger, dass ich Geld ohne Ende scheffel, eine Frau aus reichem Hause heirate!"
    extend " Ihr wolltet nicht, dass ich Shannon-chan zur Frau nehme"
    geo "Und warum? Weil es euch keinen Geldsegen bringt!"
    extend " Solange ich weiter diesen Weg gehen würde, würdet ihr mich unterstützen, aber sobald ich von diesem Weg abweiche, habe ich niemals unterstützung erfahren!"
    geo "Ihr seid grauenhafte Eltern, sowas dem einzigen Sohn anzutun!"
    extend " Ihr habt den Test nicht bestanden, also werde ich euch eigenhändig Beatrice-sama ausliefern!"
    eva "Bitte George! Es tut uns leid! Bitte verzeih uns!"
    hid "Wir haben das alles nur für dich getan, damit du nicht so wirst wie unsere Geschwister!"
    geo "Erspart mir das, ihr Geldgierigen Piranhas!"
    kan "Eva-sama, Hideyoshi-sama!"
    extend " Wir haben etwas zu essen vorbereitet."
    kum "Ohohohohoh,"
    extend " Es gibt saftige Makrelle und selbstgemachter Sahnesauce"
    extend " Dass dürfen Sie auf keinen Fall verpassen!"
    kan "Es antwortet niemand..."
    kum "Eva-sama! Hideyoshi-sama! Können Sie mich hören?"
    extend " antworten Sie bitte!"
    kan "Ich muss die Tür öffnen!"
    kan "Das Kettenschloss ist angebracht, ich komme nicht durch!"
    extend ".....Ich höre das plätschern von Wasser, es muss die Dusche sein, sind sie im Badezimmer?"
    gen "Was ist mit den werten Gästen?"
    kan "Sie antworten nicht und die Tür geht nicht auf, ich brauche einen Bolzenschneider."
    gen "Im Bedienstetenraum müsste einer sein."
    kan "Alles klar, ich hole es schnell."
    kum "WAAAAAAAAAAAAAA!" 
    extend " ...Was ist das denn und wo kommt das her?"
    kum "Wieder eins dieser magischen Kreise von denen Maria-sama erzählt hat?"
    kan "Lass mich die Kette zerschneiden!"
    kan "......."
    kan "Kumasawa, holen sie die anderen her!"
    but "Jo, Kanon-kun, was ist mit den beiden?"
    nat "Ich ahne übles!"
    extend " Sag mir bitte, dass es nicht das ist was ich denke!"
    but "Ich geh rein!"
    $ songname = "goldenslaughterer"
    show screen showsong
    but "NEIN!!! NEIN!!! NEIN!!!"
    extend "WIESO SCHON WIEDER?"
    but "TANTE EVA!!!!"
    nat "KYAAAAAAAA"
    extend "WAS UM ALLES IN DER WELT???"
    jes "Wo ist Onkel Hideyoshi??"
    kum "Oh nein, das ist ganz und gar nicht gut, wir sind wohl die nächsten!"
    jes "AHHHHHHHHHHHHHHHHHHHHHHHHHHH ONKEL HIDEYOSHI!"
    but "Beiden hat man so ein Eispickel ähnliches Teil in die Stirn gerammt, wieso hat der Täter so viel spaß dabei, die toten zu erniedrigen?"
    extend " Wurden beide etwa mit diesem Ding getötet?"
    but "Es reicht nun entgültig!"
    extend " Das war definitiv einer zu viel!"
    but "Diese Grausamkeit muss ein Ende finden, jetzt hast du mich wirklich zum Feind gemacht!"
    extend " ...Du wirst es noch bittlerlich bereuen dir Ushiromiya Battler zum Feind gemacht zu haben du gottverdammter Serienmörder!"
    but "Dieses Kettenschloss war doch nur ein ganz mieser Trick!"
    extend " Beatrice ist nichts weiter als ein Märchen, damit wir die Fassung verlieren!"
    but "Es kann niemand unsichtbares existieren, der einfach so Leute tötet!"
    extend " Ich werde dich finden, ich werde dich packen und eigenhändig in die Hölle schicken!"
    but "So langsam ist schluss! Das wars!"
    extend " Wenn ich dich in die Finger bekomme, wirst du dir wünschen nie geboren worden zu sein!"
    but "Ich werde dich kriegen, wie auch immer du heißt!"
    extend " Wenn du Beatrice sein willst, dann werde ich dein fettes Kleid packen und es dir in den Hals rammen!"
    but "Ich prügel die Scheiße aus dir raus, das schwör ich dir!!!"
    extend "BEATRICEEEEEEEEEEEEE!!!!!"
    ## Kapitel 2 Ende
    $ chapter = 1003
    $ songname = "-"
    $ save_name = _("EpisodeX Illusion of the golden witch\nVerkettung der Ereignisse")
    show screen showch
    ## Kapitel 3 Verkettung der Ereignisse






















