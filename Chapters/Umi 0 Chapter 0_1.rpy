label chapter1:

    $ chaptername = "\"Willkommen auf Rokkenjima\""
    $ chapternumber = "Kapitel 1"
    $ songname = "-"
    $ renpy.notify("Willkommen auf Rokkenjima")
    pause (2)
    show text "Der erste Tag\nSamstag, 04. Oktober 1986\n09:25 Uhr" with dissolve
    pause (2)
    play sound "audio/sfx/umilse_1050.ogg"
    show text "Der erste Tag\nSamstag, 04. Oktober 1986\n09:26 Uhr"
    pause (0.8)
    show text "Der erste Tag\nSamstag, 04. Oktober 1986\n09:27 Uhr"
    pause (0.8)
    show text "Der erste Tag\nSamstag, 04. Oktober 1986\n09:28 Uhr"
    pause (0.8)
    show text "Der erste Tag\nSamstag, 04. Oktober 1986\n09:29 Uhr"
    pause (0.8)
    show text "Der erste Tag\nSamstag, 04. Oktober 1986\n09:30 Uhr"
    stop sound
    pause (5)
    hide text with dissolve
    pause (2)
    $ persistent.alreadystarted = True
    $ songname = "HANE"
    $ play_music(hane)
    play audio "audio/sfx/umilse_004.ogg" loop
    scene sea_1c at Shake(None, 907200, dist=2)
    pause (3)
    $ quick_menu = True
    """
    In der Luft liegt der typische Meeresgeruch von Salz und auch ein wenig von Algen.
    Ein Duft, der den Geruchssinn sofort in Ekstase versetzt, wenn nicht sogar die Seele selbst begeistert.

    Denn selbst ein taubstummer, extrem sehbehinderter Mensch weiß sofort, dass das Meer in der Nähe ist
    und in Hochstimmung gerät, wenn die Möwen wieder schreien.

    Die Familie Ushiromiya ist mit dem Boot von der Insel Niijima zur Insel Rokkenjima unterwegs.
    Aber einer von ihnen scheint die Fahrt gar nicht zu mögen, er schreit herum, dass er vom Boot fällt und so.
    """
    play sound "audio/sfx/umise_003.ogg"
    show but_b23_kuyasigaru1 at zero_center,Shake(None, 907200, dist=2) with dissolve
    but "\"whaoooo!!!! ....Ich falle runter, ....ich falle runteeeeeer!!!"
    but "....Ich hasse Boote! ...Gleich muss ich kotzen, ich falleeeee!!!"
    but "Das wars!... Ich werde diese Insel nicht mehr erreichen, eher sterbe ich hier...\""
    show but_b23_kuyasigaru1 at zero_left,sprite_highlight('but'),Shake(None, 907200, dist=2) with fastdissolve
    play sound "audio/sfx/umise_047.ogg"
    show mar_a11_warai1 at zero_right,jump_transform,sprite_highlight('mar'),Shake(None, 907200, dist=2) with dissolve
    mar "\"*kicher*kicher* Battler fällt runter, Battler fällt runter! uu-uu~!!"
    mar "uu~! Battler fällt runter, Battler fällt runter! uu~!\""
    hide but_b23_kuyasigaru1
    show but_b23_nayamu1 at zero_left,sprite_highlight('but'),Shake(None, 907200, dist=2)
    but "\"Bitte, Maria-chan, bitte etwas ruhiger, das macht alles mein Magen nicht mit.\""
    show mar_a11_uuu1 at zero_right,sprite_highlight('mar'),Shake(None, 907200, dist=2)
    mar "\"uu~...? du findest das nicht lustig?"
    hide mar_a11_uuu1
    play sound "audio/sfx/umise_047.ogg"
    show mar_a11_warai1 at zero_right,jump_transform,sprite_highlight('mar'),Shake(None, 907200, dist=2)
    mar "Ich finde das super lustig! *kicher*kicher* uu~!\""
    """
    Als die Familie Ushiromiya zur jährlichen Familienkonferenz fahren will,
    hat Battler, wie schon bei früheren Konferenzen, mit Angstzuständen zu kämpfen.

    Battler hat eine Art Reiseangst, wenn er im Flugzeug sitzt, dreht er durch,
    wenn das Flugzeug zu sehr schaukelt, es könnte abstürzen, und wenn er auf einem Schiff ist, dann, na ja, das sehen wir ja gerade.

    Maria, die überhaupt nicht seekrank ist, beginnt laut zu kichern,
    weil es so lustig ist, einem zu Tode erschrockenen Battler zuzusehen.

    Aber die beiden scheinen von zwei Erwachsenen beobachtet zu werden, und auch die können sich das Lachen nicht verkneifen.
    """
    scene ship_s2bf at Shake(None, 907200, dist=2) with dissolve
    pause (0.5)
    show rud_a11_akuwarai1 at zero_center,Shake(None, 907200, dist=2) with dissolve
    rud "\"...Hey Battler-kun! Wenn du kotzen musst, dann bitte in einen Eimer, bei dem, was du dir in den Hals schaufelst, würdest du eine Menge Fische auf dem Gewissen haben... hehe..."
    rud "Unglaublich, dass du schon im Flugzeug so durchgedreht bist, du konntest ja nicht mal im Auto still sitzen.\""
    show rud_a11_akuwarai1 at zero_right,sprite_highlight('rud'),Shake(None, 907200, dist=2) with fastdissolve
    show but_b22_odoroki2 at zero_left,sprite_highlight('but'),Shake(None, 907200, dist=2)
    but "\"Lass mich in Ruhe, das ist echt kein guter Zeitpunkt!\""
    hide rud_a11_akuwarai1
    show rud_a11_defo1 at zero_right,sprite_highlight('rud'),Shake(None, 907200, dist=2)
    rud "\"Es ist nie ein guter Zeitpunkt, wenn du mit irgendetwas fahren musst. Wag es nicht, ins Meer zu kotzen!\""
    hide but_b22_odoroki2
    show but_b22_nayamu2 at zero_left,Shake(None, 907200, dist=2)
    but "\"Ich gebe mir hier die größte Mühe...\""
    hide rud_a11_defo1 with fastdissolve
    hide but_b22_nayamu2 with fastdissolve
    pause (0.3)
    show rud_a11_warai1 at zero_center with fastdissolve
    """
    Das ist mein Vater Rudolf, der alte Bastard ist so groß wie ich und macht sich bei Gelegenheit gerne über mich lustig.
    Sein Name wird auf Japanisch Ushiromiya Rudorufu ausgesprochen, fast die ganze Familie hat diese seltsame Namenstradition.

    Seit meine Mutter Asumu gestorben ist, hat sich unser Verhältnis sehr verschlechtert,
    aber ich bin sicher, dass es mit der Zeit wieder funktionieren kann.
    """
    hide rud_a11_warai1 with dissolve
    show kir_a11_defo1 at zero_left,sprite_highlight('kyr'),Shake(None, 907200, dist=2) with dissolve
    show rud_a11_warai1 at zero_right,sprite_highlight('rud'),Shake(None, 907200, dist=2) with dissolve
    kyr "\"Ist es nicht schön, dass Battler-kun wieder da ist? Ich meine, nach 6 Jahren Abwesenheit immer noch ein Theater bei der Ankunft? *kicher*\""
    rud "\"Ja, aber das war viel schlimmer, als er noch jünger war, da hatte man die ganze Anreise keine Ruhe.\""
    hide kir_a11_defo1
    show kir_a11_majime1 at zero_left,sprite_highlight('kyr'),Shake(None, 907200, dist=2)
    kyr "\"Aber er ist selbst schuld, wenn er da rumturnt, obwohl er weiß, dass er seekrank wird.\""
    hide rud_a11_warai1 with dissolve
    hide kir_a11_majime1 with dissolve
    show kir_a11_defo1 at zero_center with dissolve
    """
    Das ist Kyrie-san, der alte Bastard hat sie kurz nach dem Tod meiner Mutter geheiratet,
    aber das liegt hinter uns.

    Sie ist sehr intelligent und hat mir viel über das Schachbrettdenken beigebracht,
    wo man eine Partie mit den Augen des Gegners sehen muss.
    Ich sehe sie nicht als Mutter, aber wir verstehen uns gut.

    Wollt ihr wissen, wie man sie auf Japanisch ausspricht? Ganz einfach: Ushiromiya Kyrie.
    Und nein, man spricht es nicht komisch aus, ihr Name ist absolut perfekt,
    Ich hasse Opa den alten Kauz dafür, dass wir so komische Namen haben.
    """
    hide kir_a11_defo1 with dissolve
    scene ship_s2bf at Shake(None, 907200, dist=5)
    show but_b23_kuyasigaru1 at zero_center,Shake(None, 907200, dist=5) with dissolve
    but "\"Ich finde das gar nicht lustig... Ich kämpfe hier schließlich um mein... ....Leben... *würg*\""
    play sound "audio/sfx/umise_003.ogg"
    show but_b23_kuyasigaru1 at zero_center,run_transform
    hide but_b23_kuyasigaru1 with dissolve
    """
    Battler wurde so übel, dass er sich nicht zurückhalten konnte und den ganzen gekochten Reis vom Vormittag ins Wasser schleuderte.
    """
    scene ship_s2bf at Shake(None, 907200, dist=2)
    show rud_a11_akuwarai1 at zero_right,active,sprite_highlight('rud'),Shake(None, 907200, dist=2) with dissolve
    rud "\".....Jetzt hat dieser Kasper tatsächlich die Fische gefüttert, ach herrje... ahahaha\""
    show mar_a11_warai1 at zero_left,sprite_highlight('mar'),Shake(None, 907200, dist=2) with dissolve
    mar "\"uu-uu~! Battler hat sich übergeben, Battler hat sich übergeben! *kicher*kicher*\""
    hide rud_a11_akuwarai1 with dissolve
    hide mar_a11_warai1 with dissolve
    show mar_a11_niyari1 at zero_center with dissolve
    """
    Das kleine Mädchen, das definitiv mehr Spaß daran hat, mir zuzusehen, als mit dem Boot zu fahren, ist meine jüngste Cousine Maria,

    Auch sie hat unsere Namenstradition übernommen, statt eines normalen japanischen Namens heißt sie Ushiromiya Maria
    und das wird auch so ausgesprochen, nur in kurzen Silben.
    """
    hide mar_a11_niyari1 with dissolve
    show ros_a11_ikari1 at zero_right,sprite_highlight('ros') with dissolve
    show mar_a11_majime1 at zero_left,sprite_highlight('mar') with dissolve
    ros "\"Maria! Es reicht jetzt, lass Battler-kun in Ruhe!\""
    hide mar_a11_majime1
    show mar_a11_defo1 at zero_left,sprite_highlight('mar')
    mar "\"........uu~...\""
    hide ros_a11_ikari1
    show ros_a11_ikari2 at zero_right,sprite_highlight('ros')
    ros "\"und hör auf mit diesem uu-uu, .....du bist kein kleines Kind mehr!\""
    """
    Maria war nicht begeistert, dass ihre Mama ihre Freude unterbrach.
    Sie ist es wohl gewöhnt, dass man mit ihr schimpft, das arme Kind.
    """
    hide mar_a11_defo1 with dissolve
    show but_b11_odoroki3 at zero_left,sprite_highlight('but') with dissolve
    show ros_a11_komaru4 at zero_right,sprite_highlight('ros')
    hide ros_a11_ikari2
    ros "\"Tut mir leid, Battler-kun, ich kriege es einfach nicht aus ihr raus.\""
    hide but_b11_odoroki3
    show ros_a11_komaru4 at zero_right,sprite_highlight('ros')
    show but_b22_warai1 at zero_left,sprite_highlight('but')
    but "\"Schon gut, Tante Rosa, sie meint es nicht böse, also bin ich es auch nicht.\""
    hide ros_a11_komaru4
    show ros_a11_majime1 at zero_right,sprite_highlight('ros')
    ros "\".....aber dass dein größter Feind das Fahrzeugfahren ist, verstehe ich nicht..."
    ros ".....Du wirkst so erwachsen und reif und jetzt das?\""
    hide ros_a11_majime1 with dissolve
    hide but_b22_warai1 with dissolve
    show ros_a11_warai1 at zero_center with dissolve
    """
    Das ist Tante Rosa, sie ist die Mutter von Maria und erzieht sie in meinen Augen etwas zu streng.
    Aber da das nicht wirklich mein Bier ist, halte ich mich da raus.

    Trotz ihres blöden Namens ist ihre Aussprache nur Ushiromiya Rooza,
    was nur halb so schlimm ist wie der Name meines Vaters.

    Trotzdem ist der Name in jeder Hinsicht lächerlich. Danke Opa nochmal dafür.
    """
    hide ros_a11_warai1 with dissolve
    show rud_a11_akuwarai1 at zero_right,sprite_highlight('rud') with dissolve
    rud "\"Er kann einfach nicht still sitzen, aus irgendeinem Grund."
    rud "Das ist wirklich peinlich, das darfst du niemandem erzählen.\""
    show but_b23_nayamu1 at zero_left,sprite_highlight('but') with dissolve
    but "\".......Ey, .....halt den Mund!\""
    hide rud_a11_akuwarai1 with dissolve
    hide but_b23_nayamu1 with dissolve
    show but_b11_warai2 at zero_center with dissolve
    """
    Wie wir bereits wissen, ist mein Name Ushiromiya Battler, der sich gerade schön ins Wasser übergeben hat.
    Ich bin das Kind von Rudolf und Asumu, Asumu ist vor 6 Jahren gestorben.

    und danach habe ich die Familie wegen eines Konflikts mit Dad für 6 lange Jahre verlassen und habe bei meinen Großeltern mütterlicherseits gelebt.
    Aber auch die sind vor kurzem gestorben.

    Mein Name wird im Japanischen übrigens so geschrieben: Ushiromiya Batora.
    Ja, man spricht mich nicht Battler aus, sondern Batora, klingt echt komisch.

    Aber der Spaß hört bei mir noch lange nicht auf.
    Hier sind einige, die ihren Namensgeber am liebsten in dunkle Kammern sperren würden.

    Meine Japanischen Schriftzeichen machen mich wütend. Ich werde mit den Zeichen von 'Person' und 'Kampf' geschrieben
    Deswegen denkt ein typischer Japaner ich heiße Sento-kun. Niemand würde auch nur im Traum daran denken, dass es 'Battler'
    ausgesprochen wird.
    """
    hide but_b11_warai2 with dissolve
    show rud_a11_akuwarai2 at zero_right,sprite_highlight('rud') with dissolve
    rud "\"Ja Battler-kun, das Frühstück, dass gerade im Meer gelandet ist, hat Geld gekostet und Lebensmittel werden nicht billiger...\""
    show but_b22_nayamu1 at zero_left,sprite_highlight('but') with dissolve
    but "\".....ähm....."
    hide but_b22_nayamu1
    show but_b22_nayamu2 at zero_left,sprite_highlight('but')
    but "...Also wenn du es unbedingt wiederhaben willst, kannst du ja ins Meer springen und es wieder rausfischen... hihihihi..."
    but "....Aber mal ernsthaft, das Wackeln wurde gerade richtig schlimm...\""
    hide rud_a11_akuwarai2
    show rud_a11_defo2 at zero_right,sprite_highlight('rud')
    rud "\"........Battler...\""
    show rud_a11_defo2 at zero_left2,sprite_highlight('rud') with move
    hide rud_a11_defo2
    show rud_a11_defo1 at zero_left2
    play sound "audio/sfx/umise_047.ogg"
    hide but_b22_nayamu2
    show but_b11_kuyasigaru1 at zero_left
    but "\"....owowowowowow...... Du alter Bastard! Scheiße...... owowowow......\""
    """
    Einen Moment hat Battler nicht aufgepasst und schon hat Rudolf sein Ohrläppchen gepackt und behandelt es nicht gerade zimperlich.
    """
    but "\"owowowowowowowow.... lass los! owowowowowowow"
    but ".......Das tut richtig weh, Hör auf damit, .....owowowow\""
    rud "\"Du.... willst.... also...., dass ich es mir zu...rück....ho...le...jaaaa~?\""
    """
    Rudolf hat einen sehr starken Griff, besonders wenn es um Battlers Ohrläppchen geht, man hat das Gefühl, er reißt es jeden Moment ab.
    """
    but "........."
    but "\".....owowowow..... lass doch endlich los owowowowow... es tut weh....\""
    rud "\"....Das ist deine Strafe, wenn du frech wirst, Battler-kun.\""
    kyr "\"Lasst es für heute gut sein, ihr beiden."
    kyr "Das könnt ihr später auf der Insel austragen.\""
    """
    Nachdem Kyrie den kleinen Konflikt erfolgreich beendet hatte, hörte man jemanden von unter Deck nach draußen gehen.
    """
    jes "\"...B...Battler-kun hast du gerade von Deck gekotzt?, ich schaue nach draußen und plötzlich kommt so eine komische Suppe von oben runter, das war eklig!"
    jes "Nächstes Mal nimm einen Eimer mit!\""
    but "\"......Entschuldigung, die Geschwindigkeit ist mir einfach zu hoch, ....das Schiff schaukelt und schaukelt und schaukelt....."
    but "ahhhhhh!!! Mach, dass es aufhört, sonst falle ich wieder!\""
    jes "\"Vielleicht sollte der Kapitän etwas langsamer fahren, sonst geht es Battler gleich noch schlechter..."
    jes "Ich werde sofort den Kapitän bitten, etwas langsamer zu fahren, aber bitte nicht mehr ins Meer kotzen....\""
    but "\"Ja, vielen Dank, Jessica-chan.\""
    """
    Das war meine Cousine Ushiromiya Jessica, sie ist echt cool drauf
    und ist wohl aktuell in dieser Phase, wo man gegen seine Eltern rebelliert.

    Sie ist aber auch in dieser Phase, wo die Mädchen so große Brüste bekommen.
    hihihihih... ich würde sie mal gerne in die Hand nehmen....

    Aber dann würde sie mich windelweich schlagen, denn mit ihr ist es nicht gut Kirschen zu essen, wenn man es sich mit ihr verscherzt.
    Jessica klingt sehr nach englischer Herkunft und wird bei uns Ushiromiya Jeshka ausgesprochen, sie muss richtig unzufrieden mit ihrem Namen sein.

    Nichtmal eine Minute später ist Jessica zurückgekommen, um mir zu sagen:
    dass der Kapitän die Geschwindigkeit verringert hat.
    """
    jes "\"Battler-kun, du solltest dich wirklich unter Deck ausruhen, wir sind bald auf der Insel.\""
    but "\"Ja, das kann ich versuchen, jetzt, wo das Boot etwas langsamer fährt."
    but "Aber ich kann nicht garantieren, dass ich den Rest meines Frühstücks bei mir behalte.\""
    """
    Dann gingen Battler und Jessica unter Deck zu den anderen, die im Gegensatz zu Battler ruhig warteten, bis sie endlich an der Reihe waren.

    Moment mal, dieses \"ruhig\" sein ist falsch! Ich sehe es klar und deutlich! Die verkneifen sich doch alle gerade das Lachen....
    """
    geo "\"Wie geht es dir Battler-kun?"
    geo "Wir alle wissen bereits, dass es dich schon erwischt hat.\""
    """
    Mit einem leichten, aber nicht ganz überzeugten Nicken stimmt Battler zu.
    """
    but "Mir geht es gut, den Umständen entsprechend."
    but "Der Kapitän hat das Schiff absichtlich so schaukeln lassen."
    geo "Ja gut, ...eher nicht."
    geo "Leg dich am besten hin, du hast es gleich geschafft."
    geo "Erinnert an alte Zeiten, nicht wahr, Jessica-chan?"
    jes "Ja, es ist, als wäre er nie weg gewesen."
    jes "Mit dem Unterschied, dass er sich heute zum ersten Mal übergeben hat."
    geo "Ahahahahaha, ja, manche Dinge ändern sich, andere nie."
    """
    Das ist mein Cousin George, er wird von Tante Eva und Onkel Hideyoshi zu einem echten Gentleman erzogen.
    Er arbeitet sehr hart und will schon sein eigenes Unternehmen gründen, was ich sehr beeindruckend finde.

    Er wird von den anderen Familienmitgliedern sehr geschätzt.
    Er ist für sein Alter sehr reif und kennt sich gut aus.

    Ushiromiya Joji

    So spricht man ihn bei uns aus, und ich bin fest davon überzeugt,
    dass er heute einen Massenmord begehen wird.

    Am liebsten würde ich auch diejenigen umbringen, die für diese schreckliche Namenstradition verantwortlich sind.
    """
    but "Ich finde, heute ist auch ein besonderer Tag. Denn um die Mittagszeit soll ein Sturm aufziehen, der sich erst am Montag wieder legen soll."
    but "Es ist das erste Mal, dass wir länger als einen Tag auf der Insel bleiben."
    geo "Ja, aber wir haben auch immer Glück gehabt, dass so ein Sturm nie über unsere Familienkonferenz hereingebrochen ist."
    geo "Wie heißt es so schön? Es gibt immer ein erstes Mal."
    geo "...ähm... Battler-kun, wusstest du, dass es so genannte Sturmgötter gibt?"
    but "Ähhhhm.... Meinst du Zeus...?"
    geo "Auch richtig, aber nein, ich spreche vom Sturmgott in einem selbst."
    but ".....Was?"
    geo "Okay, es geht um folgendes:"
    geo """
    In der tantrischen Spiritualität gibt es intensivere Gefühle und auch bei den Griechen gab es die dionysische Spiritualität,
    die auch besonders heftige Gefühle beinhaltet. In diesem Sinne hat jeder Mensch auch Sturmgötter in sich,

    die er auch in sich aktivieren kann. Diese Sturmgötter können ihn auch zu schlimmen Taten, zu Verbrechen und Gewalt verleiten.
    Sie können ihn aber auch dazu bringen, sich intensiv vorwärts zu bewegen und aus der Bequemlichkeit des Alltags auszubrechen.
    """
    but "............."
    but "Ähm...... ähm......"
    but "Tantrisch?..... Gefühlsregungen?..... Dionysische Spiritualität?....."
    but ".......................Das hast du aus dieser einen Yoga-Zeitschrift....."
    geo "Ähm......."
    geo "Oh...."
    geo "Hahahaha, aber ich habe dich zum Nachdenken gebracht."
    geo "Meine Mutter hat so eine Zeitschrift, und ab und zu schaue ich auch mal rein."
    but "Hihihi, du hast nur Pech gehabt, dass ich vor der Abreise auf der Toilette so ein Yoga-Magazin in der Hand hatte, weil ich mich vergriffen habe."
    geo "Ein echter Sturmgott ist jedoch Aigaion aus der griechischen Mythologie."
    but "Ein leckerer Teller Gyros-Geschnetzeltes ist das einzige Griechische, das ich schätze."
    but "Namnamnamnam"
    geo ".........."
    geo "Jedenfalls kann dieser Gott Meeresstürme auslösen, wie wir ihn heute erleben."
    but "Du willst mir also sagen, dass irgendeine Gottheit, auf die wir keinen Einfluss haben, diesen Sturm ausgelöst hat?"
    geo "......Hmm......"
    geo "So könnte man es ausdrücken ja!"
    but "....Auf jeden Fall können wir die Zeit, die uns Aigaion jetzt schenkt, nutzen, um wieder mehr Zeit miteinander zu verbringen."
    jes "Ja, das hast du wirklich nötig, Battler-kun!"
    jes "........Es war ja auch notwendig, dass du deine Familie für sechs Jahre verlassen hast....."
    but ".....Ach man...."
    jes "Auf die Familienkonferenz freue ich mich am meisten...."
    jes "Es ist die kurze Zeit, die meinen langweiligen Alltag auflockert."
    but "Ja, ich bin auch froh, wieder bei euch zu sein, das hat mir in den 6 Jahren am meisten gefehlt."
    jes "Es ist schrecklich, nur mit meinen Eltern und meinem Großvater auf der Insel zu leben."
    jes "Ich muss jeden Tag ziemlich früh aufstehen, weil meine Schule nicht wirklich in der Nähe ist, sondern auf Niijima."
    jes "Nach der Schule muss ich sofort nach Hause, so dass ich keine Zeit mit meinen Freunden verbringen kann."
    """
    Jessica wird immer wütender und die Wut steht ihr ins Gesicht geschrieben.
    """
    jes "Danach habe ich nur noch Zeit, meine Hausaufgaben zu machen und in meinem Zimmer zu bleiben,.... Es gibt nichts zu tun."
    jes "...Am liebsten würde ich diese blöde Insel für immer verlassen und auf dem Festland ein neues Leben beginnen."
    jes "........"
    jes "Und ich muss mir jeden Tag den Bullshit meiner Mutter anhören, das fängt morgens an und hört abends auf, ich halte das einfach nicht mehr aus!"
    jes "Da ich keinen direkten Kontakt zu meinen Schulfreunden habe, ....fühle ich mich hier ziemlich einsam."
    jes "Und an jedem neuen Tag, an dem ich das erlebe, frage ich mich: Was mache ich hier eigentlich noch? Verfluchte Scheiße!..."
    """
    Man merkt sofort, dass es Jessica sehr nahe geht, nach der Schule von der Außenwelt abgeschnitten zu sein.

    Auch George und Battler sind bedrückt, aber verständnisvoll, als sie Jessicas Worte über ihren Alltag auf der Insel hören.

    Onkel Hideyoshi scheint das Gespräch mitgehört zu haben und erhebt sich von seinem bequemen Platz.
    """
    hid "Na, na Jessica-chan, du musst es positiv sehen!"
    hid "Eines Tages wirst du die Insel wirklich verlassen und dein eigenes Leben führen können."
    jes "Aber wie lange noch? ..... Und wenn meine Schulfreunde nichts mehr mit mir zu tun haben wollen?"
    hid "Auch deine Schulfreunde werden deine Situation verstehen, eines Tages wirst du sie besuchen und viel Zeit mit ihnen verbringen können."
    hid "Bis dahin solltest du immer dein Bestes geben, denn das wird sich am Ende des Tages definitiv auszahlen!"
    jes ".......Eines Tages?"
    jes "Aber ich warte schon so viele Jahre....."
    hid "...Du hast dein ganzes Leben noch vor dir, glaub mir, deine Zeit als Teenager auf der Insel wird später nur noch eine Erinnerung sein...."
    hid "Jetzt habe ich mich aber verquatscht, wahahahahaha"
    hid "Aber lass den Kopf nicht hängen und häng dich weiter rein, ja?"
    jes "Danke Hideyoshi, ich denke der Plan ist gut, ich werde ihn mir zu Herzen nehmen."
    jes "Ich fühle mich schon besser."
    hid "So ist's gut, du schaffst es!, wahahahaha"
    """
    Das ist Georges Vater und mein Onkel Hideyoshi, er ist ein netter und sympathischer Mann und ich glaube, ich mag ihn von allen Erwachsenen am meisten.
    Er ist der Ehemann von Tante Eva und hat seine Firma von Grund auf neu aufgebaut.

    und arbeitet jetzt als Präsident einer mittelgroßen Restaurantkette. Die Kette scheint zu wachsen und sehr gut zu laufen.
    Sein Name wird Ushiromiya Hideyoshi ausgesprochen, wie Kyrie ist sein Name absolut perfekt!

    Das liegt daran, dass er als Japaner in die Familie eingeheiratet hat. ..... Ich beneide jeden, der einen normalen Namen hat.
    """

    geo "Jessica-chan, allein ein Ziel zu haben, auf das man hinarbeiten kann, ist etwas, das einen jeden Tag motivieren sollte, nicht aufzugeben."
    geo "Auch ich oder Battler-kun haben unsere Sorgen und Probleme, die wir überall mit hinnehmen. Also halte noch ein bisschen durch, okay?"
    jes "Ja vielen Dank, das hilft mir wirklich sehr, danke!"
    """
    Die Worte von Hideyoshi und George haben Jessica sehr gut aufgemuntert.

    Man sieht deutlich, wie Jessica wieder lächelt.
    """
    eva "Hey, sieht so aus, als wären wir gleich da, Battler-kun..."
    eva "Wusstest du, dass die Seekrankheit auch noch nach der Reise anhalten kann?"
    but "............."
    but "Bitte mach mir keine Angst, Tante Eva!"
    eva "Oh... Entschuldige, ich wollte dir nur sagen, dass, wenn sich dein Körper an die Bewegungen des Bootes gewöhnt hat, er sich an Land wieder umgewöhnen muss."
    eva "Aber mach dir darüber keinen Kopf. Battler-kun, das passiert nicht unbedingt. *kicher*"
    """
    Das ist meine Tante Eva, die Mutter von George. Sie und der alte Bastard Papa sind so etwas wie ein Spaßvogel-Duo,
    Wenn die beiden richtig loslegen, bleibt kein Stein auf dem anderen.

    Sie beherrscht auch einige chinesische Kampfsporttechniken. Einer ihrer Roundhousekicks
    soll einmal bei einem Trainingskampf getroffen haben, und ihr Gegner wurde kaltgestellt wie ein Softdrink.

    Auf keinen Fall möchte ich von ihr unter die Dachlatte getreten werden.
    Ach ja! Fast hätte ich ihren Namen vergessen. Sie heißt hier Ushiromiya Eba...... mit b.....
    """
    but ".....Nein, du verarschst mich Tante Eva...."
    eva "Oh nein, .....das würde ich nie tun... *kicher*"
    eva "....Ich wollte dir nur etwas über die Seekrankheit erzählen... mehr nicht... *kicher*"
    """
    Tante Eva wollte mich wahrscheinlich nicht erschrecken,
    sondern meinen Kopf auf die Probe stellen, denn wenn ich an ihre Worte denke, sobald ich an Land bin,

    dann wird mir bestimmt wieder schlecht, ......ganz schön raffiniert.
    """
    kyr "Wir sind jetzt gleich da! .....Die Insel ist ganz nah!"
    """
    Unser Gespräch wird jäh unterbrochen durch die erfreuliche Nachricht, dass wir bald an Land gehen werden!
    """
    but "....Wir werden sehen, ob du Recht hast Tante Eva..."
    eva "*kicher*"
    eva "Forder es besser nicht heraus.... Battler-kun...."
    hid "Wahahahahaha, ihr zwei seid mir ja welche,..... lasst uns lieber an Deck gehen, wir gehen gleich an Land!"
    jes "Ja, das ist eine gute Idee!"
    """
    So erhoben sich alle von ihren Plätzen und bemerkten, dass sich draußen die Wolken unerwartet und viel zu früh verdunkelt hatten.
    """
    kyr "War der Taifun nicht für heute Mittag angekündigt?"
    kyr "Vielleicht fängt es gleich an zu regnen."
    rud "In etwa 10 Minuten sind wir da, aber gemütlich wird es nicht."
    kyr "Stimmt,... der Wind hat bereits zugenommen."
    """
    Der Wind, der von Minute zu Minute stärker über das Meer peitscht,
    ist kein Wind, wie ihn die meisten Menschen vom Festland kennen.

    Der Wind kann ungehindert und mit voller Kraft über das Wasser fegen,
    während es auf dem Land immer Häuser, Berge und Gelände gibt, die den Wind abschwächen können.
    """
    kyr "Dass die Wettervorhersage sich mal irrt?"
    rud "Ich habe einmal ein Geschäftsessen wegen eines angeblichen Taifuns abgesagt...."
    rud "Der Taifun kam erst 2 Tage später, ich habe mich noch nie so dumm gefühlt wie in dieser Situation."
    kyr "Das war sicher eine Erfahrung, so etwas am Ende erklären zu müssen...."
    rud "Bitte erinnere mich nicht daran...."
    """
    Nicht nur Rudolf und Kyrie sind beunruhigt, auch alle anderen sind überrascht,

    dass der Sturm einige Stunden zu früh kommt. Dabei hatte der Wetterbericht garantiert, dass es erst um die Mittagszeit losgehen würde.
    Die Folge könnten turbulente Flüge sein, die noch eine Starterlaubnis für Kurzflüge haben.

    Inzwischen hat sich Maria ganz vorne auf der Brücke niedergelassen, und ihr Blick schweift nicht mehr von einer ganz bestimmten Klippe ab.
    """
    mar "......................Uu~..........."
    mar "..................................."
    mar "......................Es ist weg................."
    mar "......................Uu~.............."
    mar "......Uu~........nicht mehr da......"
    but "hmm?...... Was ist los Maria?"
    jes "Etwas scheint sie sehr zu beunruhigen..."
    mar "Dieses schreinähnliche Ding ist weg!.... Uu!"
    mar "Es ist weg!... uu...!"
    mar "Es war immer da, aber jetzt ist es weg!... Uu!.."
    jes "Stimmt ja... Der Schrein fehlt, er war letztes Jahr noch da...."
    jes "Es sieht auch so aus, als wäre ein Teil des Riffs mitgerissen worden...."
    kum "Ohohohoh, der Schrein wurde während eines Gewitters von einem gewaltigen Blitz getroffen und zerstört."
    """
    Die ältere Frau heißt Kumasawa. Sie ist eine Teilzeitarbeiterin, die zwar mehrmals gekündigt hat, aber insgesamt schon viele Jahre im Dienst der Familie steht.
    Sie ist geschickt und mehr als fähig, ihre Aufgaben zu erfüllen,

    aber wegen ihrer Geschwätzigkeit und ihrer Vorliebe für Gerüchte ist sie als Angestellte nicht sehr beliebt.
    Ihr Name auf Japanisch? Auch bei uns Kumasawa, ihre Eltern haben ihr einen vernünftigen Namen gegeben... *seufz*....
    """
    jes "Ein Blitzeinschlag?..."
    jes "Ein Blitz kann so gewaltig sein?"
    kum "Die Fischer sagen, es sei ein Zeichen von Unglück...."
    mar "Ein Zeichen von Unglück....Uu~..."
    mar "..........................."
    """
    Kumasawas Worte haben die sonst so entspannte Atmosphäre auf dem Schiff in ein beklemmendes Gefühl verwandelt.
    Maria hat ihren Blick noch immer nicht von der Stelle abgewandt, an der der Schrein stehen soll...

    Und es scheint, als würde der heftige Wind für einen Moment nachlassen.
    """
    mar "Unglück..."
    mar "Unglück...Unglück..."
    mar "UnglückUnglückUnglückUnglückUnglückUnglückUnglückUnglückUnglückUnglückUnglückUnglückUnglückUnglückUnglückUnglückUnglückUnglück"
    geo "Kumasawa-san bitte gehen Sie mit ihren Witzen etwas vorsichtiger um!"
    geo "Maria-chan nimmt sowas ziemlich ernst, verstehen Sie?"
    mar "UnglückUnglückUnglück"
    but "Hey Maria!"
    but "Wenn du so oft \"Unglück\" sagst, wird es wirklich ein Unglück geben, also beruhige dich, ja?"
    geo "Maria-chan, es wird nichts schlimmes passieren."
    mar "............Úu~.............."
    mar "............................"
    """
    Die anderen versuchen Maria zu beruhigen, um das Thema irgendwie abzuschließen.

    Aber Maria wendet den Blick vom Riff ab, dreht sich um, hebt den rechten Arm zum Himmel und öffnet langsam den Mund...
    """
    mar "Es geschieht definitiv....."
    mar "Ein Unglück wird geschehen!......"
    """
    Mit diesen Worten, als hätte Maria gerade den Befehl dazu gegeben, hörte man es donnern und sofort begann es zu regnen.

    Nicht nur Battler lief ein kalter Schauer über den Rücken.
    """
    but "............................"
    but "Hä?........................."
    """
    Alle haben in diesem Moment ein mulmiges Gefühl.
    Es ist fast so, als ob Maria ahnt, dass dieses Familientreffen etwas ganz Besonderes sein wird.

    Doch Battler scheint zu erkennen, dass Marias erhobener Arm und das \"Unglück\" wohl nur das Wetter meinen.
    """
    but "Du hast also gemerkt, dass es ein schlimmes Unwetter wird?"
    mar "..........Uu~....."
    but "Die Wettervorhersage sagt, dass der Sturm erst gegen Mittag kommen wird. Aber er ist schon da...."
    but "Das nenne ich wirklich ein Unglück... hihihihi"
    but "Maria, ich bin sicher, dass dieser Taifun schneller vorbei ist, als du bis zehn zählen kannst. Alles wird gut."
    """
    Battler versucht Maria zu beruhigen, dass sie keine Angst vor dem Taifun haben muss, aber Marias Gesichtsausdruck spricht eine ganz andere Sprache.
    """
    mar "Uu~!!"
    mar "Uu~!!Uu~!!Uu~!!Uu~!!Uu~!!Uu~!!"
    mar "Ein Unglück wird geschehen! Uu~!!"
    jes "Maria, warum sagst du sowas?"
    kum "Es ist klar, dass sie etwas im Blick hat, das im Alter schnell verloren geht."
    kum "Sehr junge Menschen haben einen Sinn für das Übernatürliche..."
    kum "Aber dieses Gefühl wird schwächer, je älter man wird."
    kum "Was Maria fühlen kann, kann nur sie fühlen, weil sie die Jüngste hier ist."
    """
    Battler erstarrt bei diesen Worten, ist das wirklich möglich? denkt er, das kann es doch gar nicht geben...
    """
    kum "Es scheint so, dass in der Vergangenheit von Rokkenjima eine Hexe...."
    jes "Es reicht, Kumasawa! Darüber reden wir nicht!"
    kum "Ohohohoh, ich muss mich entschuldigen, ich wollte nicht unhöflich sein."
    """
    Kumasawas Geschichten sind im Moment eher ungünstig, denn es geht darum, Maria zu beruhigen und nicht darum, ihr noch mehr Dinge in den Kopf zu setzen.
    Jessica hat richtig gehandelt, als sie Kumasawa unterbrochen hat.
    """
    but "Eine....... Hexe?........."
    but "Hat Kumasawa Hexe gesagt?"
    but "Weiß Jessica irgendwas?"
    but "Hexe.........."
    """
    Weit weg vom Geschehen konnte man Rudolf sehen, der sehr nachdenklich wirkte.
    """
    rud "*seufz*"
    """
    Nach etwa fünf Minuten stieß er einen tiefen Seufzer aus, während er sich eine Zigarette anzündete, weil ihn etwas sehr beschäftigte, und niemand außer Eva schien diesen Seufzer gehört zu haben.
    """
    eva "Was ist los Rudolf?.... irgendwelche Bedenken wegen heute Abend?"
    eva "Wir müssen uns nur exakt an das halten, was wir besprochen haben um gegen Krauss gewinnen zu können"
    rud "....Ja, am Plan liegt es nicht..... Was wäre, wenn unsere Vermutung falsch ist?...."
    rud "Wir würden wegen Hochverrat an die Ushiromiya Familie den Haien zum Fraß vorgeworfen werden."
    rud "Das wäre das absolute Ende von meinem Leben und von deinem auch Eva-san"
    rud "Damit würden wir unser Ziel um ungefähr einer Quadrillion Kilometern verfehlen."
    """
    Die Stimmung kippt bei diesem Gespräch auf ungefähr -500 Prozent Rudolf sieht sehr angespannt aus, während Eva versucht ein leichtes Grinsen zu behalten...

    Aber auch ihr sieht man an, dass sie so kurz vor der Familienkonferenz, wo es um das Erbe vom Oberhaupt geht ein wenig weiche Knie bekommt.
    """
    eva "Mach dir mal darum keine Sorgen... Rudolf... Es ist ein sehr hoher Einsatz, aber ein Treffer wird mit Vaters Erbe belohnt."
    eva "Außerdem finde ich, dass das Erbe, dass man hier rausbekommen kann, das Risiko definitiv wert ist."
    eva "Ich lass nicht zu dass mein hinterhältiger Bruder das ganze Erbe für sich behält!"
    rud "Das scheint einleuchtend zu sein... solange du dich an die Aufteilung hälst und im ernstfall Rede und Antwort stehst, bin ich dabei."
    eva "Genau das wollte ich hören, wenn etwas schiefgeht, werde ich uns da wieder rausholen."
    rud "Ich hoffe einfach auf das beste..."
    """
    Sagte er während er einen großen Zug von seiner Zigarre nimmt und den feinen weißen Qualm wieder in die Luft pustet.

    Genau in diesem Moment ertönt die Stimme von Shannon, eine Bedienstete, die die Familienmitglieder zusammen mit Gohda heute abholen sollte.
    """
    sha "Entschuldigen Sie werte Gäste, bitte machen Sie sich bereit, das Boot wird jeden Moment anlegen!"
    sha "Bitte seien sie Vorsichtig, wenn Sie über die Planke laufen, dankeschön"
    geo "Das hast du toll gesagt, Shannon-chan"
    sha "George-sama.... D..das ist zu viel des lobs..."
    sha "....I...ich bin nur Mobiliar der Familie, ich musste das sagen....."
    """
    Shannon wurde knallrot, als sie diese Worte von George hörte.
    """
    geo "Shannon-chan du weißt selber nicht, was für eine tolle Bedienstete du bist, du machst dich einfach nur unnötig runter."
    geo "Und wenn ich schon mal dabei bin, du bist auf gar keinen Fall sowas wie Mobilar, du bist ein Mensch."
    sha "G...george-sama......"
    """
    Die bedienstete heißt wie wir schon wissen Shannon sie ist eine junge, aber erfahrene Bedienstete.

    Normalerweise ist sie ruhig und verrichtet ihre Arbeit effizient, aber wenn sie nervös wird, macht sie Fehler.

    Außerdem ist Shannon nur ein Pseudonym, das sie im Dienst benutzt, nicht ihr richtiger Name und da sie kein Familienmitglied ist,

    ist ihr Name absolut inordnung und ist nicht seltsam.
    """
    but "Sag mal Jessica-chan... kann es sein, dass die beiden sich ein wenig nahe stehen?"
    jes ".....wahahahaha....wahahahaha..... das hast du so schnell kapiert?"
    but "Also sind die wirklich ein Paar?"
    jes "So genau weiß ich es nicht, aber es macht mir den Anschein, als würde George wirklich was für sie empfinden."
    but "Wenn ich absolut ehrlich bin, dann glaube ich, dass ich auch mal so ein wenig in sie verliebt war."
    but "Ich war damals auch in so einer Phase, wo ich bei ihr immer so komisches Zeug gequatscht habe...."
    but "Sowas wie <see you again> oder so ein absolut schnulzigen Kram wie: ....Ich komme auf..... einem weißen Pferd zu dir geritten oder so ähnlich."
    jes "wahahahahahaha <see you again?> du hattest echt einen Vogel! Ich bin mir ziemlich sicher, dass Shannon das heute super unangenehm finden würde."
    but "Das glaube ich auch, mir ist das selber maximal peinlich, also bitte behalte das für dich, okay?"
    but "Ich bin absolut Tot, wenn sie sich auch an diesen peinlichen Kram erinnert."
    jes "Ja, das geht klar! Ich schweige wie ein Grab!"
    but "Okay, wir versprechen es uns!"
    "Versprochen ist Versprochen und wer es bricht dem wird ganz Radikal ein Finger abgehakt!"
    """
    Während alle fröhlich miteinander ein wenig plaudern, wurde die Planke bereitgemacht und alle beginnen,
    das Boot nach und nach zu verlassen.

    Auf der anderen Seite wartet auch bereits der Chefkoch Gohda, der die Familie empfangen soll.
    """
    goh "Ich hoffe ihr alle, hattet eine angenehme Reise!"
    goh "Willkommen auf der Insel Rokkenjima meine Damen und Herren!"
    """
    Ein freundlicher Bediensteter der Familie empfängt die angereisten Verwandten, um sie und ihr Gepäck zum Gästehaus zu bringen.
    """
    goh "Auch wenn uns heute am Nachmittag ein Taifun erwartet, werde ich, Gohda, Euch immer erstklassige Mahlzeiten zubereiten!"
    jes "Vielen Dank Gohda, ich denke die meisten kommen jedes Jahr nur hierher, um deine super leckeren Gerichte zu speisen."
    goh "Es macht sofort mehr Spaß für Euch zu kochen, wenn man solche Worte hören darf!"
    goh "Allerdings muss ich sagen, dass wir euch bereits 20 Minuten früher erwartet haben, dass ist nicht gut für unseren Zeitplan...."
    goh "Dazu scheint sich dieser Typhoon früher als angekündigt aufzubauen, also sollten wir schnell zur Villa."
    """
    Gohda ist ein Bediensteter, der als Koch eingestellt wurde.

    Er ist noch nicht lange bei dieser Familie angestellt, aber durch seine früheren Tätigkeiten und Erfahrungen hat er ein Talent für die Bewirtung von Gästen entwickelt.

    Aus diesem Grund ist er als Bediensteter sehr hoch angesehen. Da er nicht zur Familie gehört, hat er wie Shannon auch nicht einer unserer seltsamen Namen.
    """
    kum "Vergiss aber nicht, dass es heute mein spezielles Spaghetti mit würziger Makrelen Sahnesauce nach meinem Geheimrezept zum Mittagessen gibt, Gohda! ohohohohoh!"
    kum "Ihr müsst das unbedingt probieren, es gibt doch nichts besseres als frische saftige Makrelen. ohohohoh!"
    jes ".....Ich denke mal, da pass ich lieber...."
    kum "Aber Jessica-sama, Ihr könnt Euch doch nicht ständig von Junk-Food ernähren!"
    kum "Gebt der Makrele doch eine Chance!"
    jes "Aber.... ich habe heute Morgen in der Küche gar keine Makrelen gesehen, Kumasawa..."
    jes "Daher, kann es heute leider keine Makrelen geben!"
    kum "Ohohohoh, Ihr habt mich voll erwischt, Jessica-sama."
    rud "Hey Battler! Wenn dir immer noch schwindelig ist und du gleich auf den Esstisch kotzt, darfst du Nachhause schwimmen."
    but "Lass es gut sein!.... Mir geht es bereits wieder besser."
    rud "Na,.... das hoffe ich doch,..... ich will mich nicht vor den anderen rechtfertigen müssen, warum du Holzkopf den Esstisch ruinierst."
    but "Keine Sorge Dad, wenn es hart auf hart kommt, passt mir dein Schicker Anzug auch ganz gut... ihihihi"
    goh "Liebe Gäste, wir haben Zeitverzug und der Sturm wird stärker! Wir müssen jetzt unverzüglich zum Gästehaus!"
    """
    Battler und Rudolf wollten gerade wieder ihre Vater-Sohn Beziehung stärken, da grätscht Gohda rein, der etwas angefressen mit dem Zeigefinger auf seine Armbanduhr tickt.
    """
    goh "Wir müssen uns jetzt beeilen, wir haben viel Zeit verloren und Madam wird sehr wütend sein, wenn wir nicht in der nächsten Zeit eintreffen."
    but "Beruhig dich Gohda-san, wir sind ja jetzt alle da und bereit um zum Gästehaus zu gehen."
    jes "Wenn du dich nicht ins Meer übergeben hättest und ich den Kapitän nicht angefleht hätte langsamer zu fahren, wären wir jetzt nicht im Zeitverzug, Freund Nase!"
    jes "Dafür müsste ich dich über die komplette Insel jagen, bis dir die Puste ausgeht..."
    but "....hihihi...."
    but "Da scheint was dran zu sein, tut mir voll traurig."
    but "Das nächste mal werde ich mich mit Magie einfach herzaubern, wirst schon sehen!"
    jes "ahahahaha, das würde ich zu gerne sehen!"
    mar "uu???......"
    mar "Battler kann Magie benutzen?"
    jes "Ganz genau Maria-chan, Battler kann Magie benutzen, aber nicht nur Battler!"
    jes "Jeder kann Magie benutzen, denn jeder trägt etwas Magie im Herzen auch du!"
    mar "Uu-uu! Wir alle haben Magie! Wir alle haben Magie! Uu-uu!"
    mar "Uu-uu! Ich möchte dir unbedingt Beatrice vorstellen, Battler! Uu!"
    but ".....Beatrice?....."
    mar "Wer Magie hat, kann sie sehen, also kannst du sie auch sehen! Uu-uu!"
    """
    Battler war erneut nicht vorsichtig gegenüber Maria und hat sie versehentlich glauben lassen, dass er Magische Kräfte besitzt, was natürlich unsinn ist.
    """
    geo "Battler-kun, Jessica-chan... Ihr müsst vorsichtiger sein, welche Scherze ihr in Marias Umgebung bringt, wie ihr seht nimm sie alles viel zu ernst."
    but "Entschuldige... Aniki..."
    """
    >Aniki< bedeutet sowas wie >Großer Bruder< was aber trotzdem kein Sinn macht, da wir beide ja Cousins sind und keine Geschwister...

    Es hat sich allerdings so eingebürgert bei uns, also ist das in Ordnung, auch da George älter ist als ich.

    Zusätzlich gibt es noch >Aneki< das sowas wie >Große Schwester< heißt.
    """
    mar "uu~!... Battler hat Magie! Battler hat Magie!"
    geo "Du hast recht Maria-chan! Nur kann Battler-kun keine Hexen sehen."
    geo "Das ist nämlich etwas, dass nur du sehen kannst, da du was ganz besonderes bist."
    mar "Battler kann Beatrice nicht sehen?......."
    mar "..........."
    mar ".........uu~.........."
    """
    George-aniki hat es geschafft Maria schnell zu beruhigen, solche Momente zeigen immer wieder, wie gut er mit Kindern umgehen kann, er wird mal ein großartiger Ehemann.
    """
    but "Irgendwas ist anders dieses Jahr...."
    but "ich habe das Gefühl, dass hier etwas fehlt..."
    but "hmmm........."
    but "Ach stimmt...... Die Seemöwen sind weg, wir wurden doch sonst immer von den Seemöwen begrüßt oder irre ich mich?"
    jes "Jetzt wo du es sagst... Das Weinen der Seemöwen war immer zu hören..."
    mar "..uu~..... Keine Seemöwen?"
    mar "Wo sind die Seemöwen? uu~..."
    geo "Die Seemöwen sind schon lange in ihre Nester zurückgekehrt, da der Typhoon sich bereits aufbaut."
    geo "Auch für Seemöwen ist so ein Typhoon gefährlich, weswegen sie bereits Schutz gesucht haben."
    but "Da hätte ich ja selber drauf kommen können."
    """
    George, Battler, Jessica und Maria quatschen fröhlich miteinander doch der Sturm wird
    von Minute zu Minute stärker und werden deswegen von Gohda unterbrochen
    """
    goh "Entschuldigt mich, aber wir sollten zur Villa, da der Typhoon stärker wird und wir möchten unter gar keinen Umständen, dass ihr nass ankommt."
    """
    Darauf hin sind alle den Weg durch den Waldweg zur Villa der Ushiromiya Familie
    angetreten und damit wird die Familienkonferenz im Jahre 1986 beginnen!
    """
    scene black with dissolve
    $ renpy.notify("BGM: Ride on")
    $ renpy.movie_cutscene("videos/intro.mov")
    jump chapter2
