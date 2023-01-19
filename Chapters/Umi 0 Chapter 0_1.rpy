label chapter1:

    ## Just a fake clock cuz I have no Idea how to recreate the Umi Project Clock
    $ current_chapter = 1
    pause (2)
    show text "Der erste Tag\n04. Oktober 1986\n09:25 Uhr" with dissolve
    pause (2)
    play sound "audio/sfx/umilse_1050.ogg"
    show text "Der erste Tag\n04. Oktober 1986\n09:26 Uhr"
    pause (0.8)
    show text "Der erste Tag\n04. Oktober 1986\n09:27 Uhr"
    pause (0.8)
    show text "Der erste Tag\n04. Oktober 1986\n09:28 Uhr"
    pause (0.8)
    show text "Der erste Tag\n04. Oktober 1986\n09:29 Uhr"
    pause (0.8)
    show text "Der erste Tag\n04. Oktober 1986\n09:30 Uhr"
    stop sound
    pause (5)
    hide text with dissolve
    pause (2)
    ## scene on boat to rokkenjima
    camera:
        anchor (0.5, 0.5)
        pos (960, 540)
        matrixcolor IdentityMatrix()
    $ persistent.alreadystarted = True
    $ renpy.notify("Willkommen auf Rokkenjima")
    $ play_music(hane)
    play audio "audio/sfx/umilse_004.ogg" loop
    scene sea_1c with dissolve
    pause (3)
    $ quick_menu = True
    """
    In der Luft liegt der typische Meeresgeruch von Salz und auch etwas nach Alge.
    Ein Duft der den Geruchssinn sofort in Ekstase versetzt, wenn nicht sogar die Seele selber begeistert.

    Weil sogar ein Taub-Stummer mit extremer Sehschwäche sofort weiß, dass das Meer sich in unmittelbarer Nähe befindet
    und in Hochstimmung kommt, wenn die Seemöwen wieder weinen.

    Die Ushiromiya Familie ist von der Insel Niijima zur Insel Rokkenjima mit dem Boot unterwegs.
    Doch einer von ihnen scheint die Fahrt gar nicht zu gefallen, schreit herum, dass er vom Boot fällt und sowas.
    """
    scene sea_1c at screenshake_big_transform
    play sound "audio/sfx/umise_003.ogg"
    show but_b23_kuyasigaru1 at zero_center,screenshake_long_transform with dissolve
    but "whaoooo!!!! ich falle runter, ....ich falle runteeeeeer!!!"
    but "Ich hasse Boote! ...Gleich muss ich kotzen, ich falleeeee!!!"
    but "Das wars!... ich werde diese Insel nicht mehr erreichen, eher sterbe ich hier..."
    show but_b23_kuyasigaru1 at zero_left,sprite_highlight('but') with move
    play sound "audio/sfx/umise_047.ogg"
    show mar_a11_warai1 at zero_right,jump_transform,sprite_highlight('mar') with dissolve
    mar "*kicher*kicher* Battler fällt runter, Battler fällt runter! uu-uu-uu!!"
    mar "uu-uu-uu! Battler fällt runter, Battler fällt runter! uu-uu-uu!"
    hide but_b23_kuyasigaru1
    show but_b23_nayamu1 at zero_left,sprite_highlight('but')
    but "Bitte, Maria-chan, bitte etwas ruhiger, das macht alles mein Magen nicht mit."
    show mar_a11_uuu1 at zero_right,sprite_highlight('mar')
    mar "uu...? du findest das nicht lustig?"
    hide mar_a11_uuu1
    play sound "audio/sfx/umise_047.ogg"
    show mar_a11_warai1 at zero_right,jump_transform,sprite_highlight('mar')
    mar "Ich finde das super lustig! *kicher*kicher* uu-uu!"
    """
    Während die Ushiromiya Familie zur jährlichen Familienkonferenz fahren möchte,
    bekommt Battler, wie schon zu früheren Konferenzen es mit der Angst zu tun.

    Battler hat sowas wie eine Reiseangst, wenn er mit dem Flugzeug unterwegs ist, dreht er durch,
     wenn das Flugzeug zu stark wackelt, es könnte ja abstürzen und wenn er auf einem Boot ist dann, na ja, das sehen wir gerade.

    Maria, die nicht ansatzweise seekrank ist, fängt lautstark an zu kichern,
    weil das Zusehen von einem zu Tode verängstigten Battler so viel Spaß macht.

    Die beiden scheinen allerdings von zwei Erwachsenen beobachtet zu werden und selbst die können sich das Lachen nicht verkneifen.
    """
    scene ship_s2bf with dissolve
    pause (0.5)
    show rud_a11_akuwarai1 at zero_center with dissolve
    rud "...Hey Battler-kun! Wenn du kotzen musst, dann bitte in einen Eimer, bei dem, was du dir reinschaufelst, würdest du viele Fische auf dem Gewissen haben... hehe..."
    rud "Unglaublich, dass du selbst im Flugzeug schon so durchgedreht bist, du konntest noch nicht einmal im Auto still sitzen."
    show rud_a11_akuwarai1 at zero_right,sprite_highlight('rud') with move
    show but_b22_odoroki2 at zero_left,sprite_highlight('but')
    but "Lass mich in Ruhe, das ist echt kein guter Zeitpunkt!"
    hide rud_a11_akuwarai1
    show rud_a11_defo1 at zero_right,sprite_highlight('rud')
    rud "Es ist bei dir doch nie ein guter Zeitpunkt, wenn du mit irgendwas fahren musst und wag es dich ins Meer zu kotzen!"
    hide but_b22_odoroki2
    show but_b22_nayamu2 at zero_left
    but "Ich gebe mir hier die größte Mühe..."
    hide rud_a11_defo1 with dissolve
    hide but_b22_nayamu2 with dissolve
    pause (0.3)
    show rud_a11_warai1 at zero_center with dissolve
    """
    Das ist mein Vater Rudolf, der alte Bastard ist genauso groß wie ich und macht sich gerne bei Gelegenheit über mich lustig.
    Sein Name wird im Japanischen Ushiromiya Rudorufu ausgesprochen, fast die ganze Familie hat so eine seltsame Namenstradition.

    Seit dem Tot meiner Mutter Asumu ist unser Verhältnis stark auseinander gebrochen,
    aber ich bin mir sicher, dass auch dies über die Zeit wieder funktionieren kann.
    """
    hide rud_a11_warai1 with dissolve
    show kir_a11_defo1 at zero_left,sprite_highlight('kyr') with dissolve
    show rud_a11_warai1 at zero_right,sprite_highlight('rud') with dissolve
    kyr "Ist es nicht schön, dass Battler-kun wieder hier ist?... Ich meine nach 6 Jahren der Abwesenheit immer noch ein Theater bei der Anreise?... *kicher*"
    rud "Ja, aber das war als er noch jünger war, deutlich schlimmer, da hatte man die komplette Anreise über keinerlei Ruhe."
    hide kir_a11_defo1
    show kir_a11_majime1 at zero_left,sprite_highlight('kyr')
    kyr "Daran ist er aber auch selber Schuld, wenn er da herum turnt, wenn er doch weiß, dass er seekrank wird."
    hide rud_a11_warai1 with dissolve
    hide kir_a11_majime1 with dissolve
    show kir_a11_defo1 at zero_center,active with dissolve
    """
    Das ist Kyrie-san, der alte Bastard hat sie kurz nach dem Tot meiner Mutter geheiratet,
    aber das sind Dinge, die bereits hinter uns liegen.

    Sie ist sehr intelligent und hat mir sehr viel über das Schachbrettdenken beigebracht,
    wo man ein Spiel aus den Augen des Gegners betrachten muss. Ich betrachte sie zwar nicht als Mutter,
    wir kommen aber trotzdem gut miteinander aus.

    Ihr wollt wissen, wie sie im Japanischen ausgesprochen wird? Das ist ganz einfach: Ushiromiya Kirie
    und nein das spricht man nicht seltsam aus, ihr Name ist absolut perfekt,
    ich hasse Großvater den alten Kauz dafür, dass wir so seltsame Namen haben.
    """
    hide kir_a11_defo1 with dissolve
    show but_b23_kuyasigaru1 at zero_center with dissolve
    but "Ich finde das gar nicht lustig... Ich kämpfe hier schließlich um mein... Leben... *würg*"
    play sound "audio/sfx/umise_003.ogg"
    scene ship_s2bf at screenshake_big_transform
    show but_b23_kuyasigaru1 at zero_center,run_transform
    hide but_b23_kuyasigaru1 with dissolve
    """
    Battler wurde so schlecht, dass er es nicht mehr zurückhalten konnte und er hat den ganzen gekochten Reis von heute Morgen ins Wasser befördert.
    """
    show rud_a11_akuwarai1 at zero_right,active,sprite_highlight('rud') with dissolve
    rud "Jetzt hat dieser Kasper tatsächlich die Fische gefüttert, ach herrje... ahahaha"
    show mar_a11_warai1 at zero_left,sprite_highlight('mar') with dissolve
    mar "uu-uu! Battler hat sich übergeben, Battler hat sich übergeben! *kicher*kicher*"
    hide rud_a11_akuwarai1 with dissolve
    hide mar_a11_warai1 with dissolve
    show mar_a11_niyari1 at zero_center with dissolve
    """
    Das kleine Mädchen, dass definitiv mehr Freude daran hat mir zuzuschauen,
    als mit dem Boot zu fahren ist meine jüngste Cousine Maria.

    Auch sie hat unsere Namenstradition erwischt, anstelle von einem normalen japanischen Namen heißt sie Ushiromiya Maria
    und das spricht man auch so aus, nur eben in kurzen Silben gesprochen.
    """
    hide mar_a11_niyari1 with dissolve
    show ros_a11_ikari1 at zero_right,sprite_highlight('ros') with dissolve
    show mar_a11_majime1 at zero_left,sprite_highlight('mar') with dissolve
    ros "Maria! Es reicht jetzt, lass Battler-kun in Ruhe!"
    hide mar_a11_majime1
    show mar_a11_defo1 at zero_left,sprite_highlight('mar')
    mar "........uu..."
    hide ros_a11_ikari1
    show ros_a11_ikari2 at zero_right,sprite_highlight('ros')
    ros "und hör auf mit diesem uu-uu, du bist kein kleines Kind mehr!"
    """
    Maria war nicht sehr begeistert davon, dass ihre Mama ihre Freude unterbricht.
    Sie ist es sicher gewohnt die ganze Zeit schelte zu kriegen, das arme Kind.
    """
    hide mar_a11_defo1 with dissolve
    show but_b11_odoroki3 at zero_left,sprite_highlight('but') with dissolve
    show ros_a11_komaru4 at zero_right,sprite_highlight('ros')
    hide ros_a11_ikari2
    ros "Entschuldige bitte, Battler-kun, ich bekomme es einfach nicht aus ihr raus."
    hide but_b11_odoroki3
    show ros_a11_komaru4 at zero_right,sprite_highlight('ros')
    show but_b22_warai1 at zero_left,sprite_highlight('but')
    but "Ist schon okay Tante Rosa, sie meint es ja nicht böse, also bin ich es auch nicht."
    hide ros_a11_komaru4
    show ros_a11_majime1 at zero_right,sprite_highlight('ros')
    ros "...Aber, dass dein größter Gegner das Fahren mit Fahrzeugen ist, verstehe ich nicht..."
    ros "Du wirkst eigentlich so erwachsen und gereift und jetzt das?"
    hide ros_a11_majime1 with dissolve
    hide but_b22_warai1 with dissolve
    show ros_a11_warai1 at zero_center with dissolve
    """
    Das ist Tante Rosa, sie ist die Mutter von Maria und erzieht sie in meinen Augen etwas zu streng.
    Da dies allerdings nicht wirklich mein Bier ist, werde ich mich da raushalten.

    Ihre Aussprache ist trotz ihres bescheuerten Namens aber immerhin nur Ushiromiya Rooza,
    was nur halb so schlimm ist wie der Name meines Vaters.
    """
    hide ros_a11_warai1 with dissolve
    show rud_a11_akuwarai1 at zero_right,sprite_highlight('rud') with dissolve
    rud "Er schafft es einfach nicht ruhig sitzen zu bleiben, aus irgendeinem Grund."
    rud "Das ist richtig unangenehm, erzähl das besser niemanden."
    show but_b23_nayamu1 at zero_left,sprite_highlight('but') with dissolve
    but ".......Ey, halt den Mund......."
    hide rud_a11_akuwarai1 with dissolve
    hide but_b23_nayamu1 with dissolve
    show but_b11_warai2 at zero_center with dissolve
    """
    Wie wir schon wissen, heiße ich, der sich gerade schön ins Wasser übergeben hat Ushiromiya Battler.
    Ich bin das Kind von Rudolf und Asumu, wobei Asumu vor 6 Jahren verstorben ist

    und habe darauf die Familie wegen eines Konflikts mit Dad für 6 lange Jahre verlassen und lebte bei meinen Großeltern mütterlicherseits.
    Diese sind aber auch kürzlich von uns gegangen.

    Mein Name wird übrigens im Japanischen so geschrieben: Ushiromiya Batora.
    Ja, man spricht mich nicht Battler, sondern Batora aus, klingt echt komisch.

    Bei mir hört der Spaß mit den seltsamen Namen aber definitiv nicht auf.
    Hier sind einige, die ihren Namensgeber am liebsten in dunkle Räume sperren würden.
    """
    hide but_b11_warai2 with dissolve
    show rud_a11_akuwarai2 at zero_right,sprite_highlight('rud') with dissolve
    rud "Ja Battler-kun, das Frühstück, dass gerade im Meer gelandet ist, hat Geld gekostet und Lebensmittel werden nicht billiger..."
    show but_b22_nayamu1 at zero_left,sprite_highlight('but') with dissolve
    but ".....ähm....."
    hide but_b22_nayamu1
    show but_b22_nayamu2 at zero_left,sprite_highlight('but')
    but "...Also wenn du es unbedingt wiederhaben willst, kannst du ja ins Meer springen und es wieder rausfischen... hihihihi..."
    but "Aber mal ernsthaft, das Wackeln wurde gerade richtig schlimm..."
    hide rud_a11_akuwarai2
    show rud_a11_defo2 at zero_right,sprite_highlight('rud')
    rud "Battler..."
    show rud_a11_defo2 at zero_left2,sprite_highlight('rud') with move
    hide rud_a11_defo2
    show rud_a11_defo1 at zero_left2
    play sound "audio/sfx/umise_047.ogg"
    hide but_b22_nayamu2
    show but_b11_kuyasigaru1 at zero_left
    but "owowow du alter Bastard, scheiße owowowow"
    """
    Einen Moment hat Battler nicht aufgepasst und schon hat Rudolf nach seinem Ohrläppchen gegriffen und behandelt es nicht gerade stiefmütterlich.
    """
    but "owowowowowowowow.... lass los! owowowowowowow"
    but "Das tut richtig weh, Hör auf damit, owowowow"
    rud "Du.... willst.... also...., dass ich es mir zu...rück....ho...le...jaaaa~?"
    """
    Rudolf hat einen sehr kräftigen Griff, vor allem dann, wenn es um Battlers Ohrläppchen geht, da bekommt man das Gefühl, er reißt sie jeden Moment ab.
    """
    but "........."
    but ".....owowowow..... lass doch endlich los owowowowow... es tut weh...."
    rud "....Das ist halt deine Bestrafung, wenn du frech wirst, Battler-kun"
    kyr "Lasst es für heute gut sein ihr zwei."
    kyr "Ihr könnt das später auf der Insel klären."
    """
    Nachdem Kyrie den kleinen Konflikt erfolgreich beendet hat, konnte man hören, dass jemand von unterm Deck nach draußen geht.
    """
    jes "...B...Battler-kun hast du gerade vom Deck gekotzt?, ich schaue nach draußen und plötzlich segelt da so eine seltsame Suppe von oben runter, das war ekelhaft!"
    jes "Das nächste Mal nimmst du dir einen Eimer mit!"
    but "entschuldige, die Geschwindigkeit ist mir einfach zu hoch, ....das Boot wackelt und es wackelt und wackelt....."
    but "ahhhhhh!!! Macht das es aufhört, sonst falle ich wieder!"
    mar "Vielleicht sollte der Kapitän etwas langsamer fahren, sonst geht es Battler noch schlechter... uu!"
    jes "Gute Idee Maria-chan, ich gehe sofort den Kapitän fragen, ob er etwas langsamer fahren könnte, aber bitte brech nicht mehr ins Meer..."
    jes "Du solltest übrigens unters Deck gehen, da sollte es besser sein."
    but "ähm ja, vielen Dank, Jessica-chan."
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
    jes "Battler-kun du solltest definitiv unters Deck dich ausruhen, wir sind schon bald auf der Insel."
    but "Ja, das kann ich versuchen, jetzt wo das Boot etwas langsamer fährt."
    but "Ich kann aber nicht garantieren, dass ich den Rest meines Frühstücks bei mir behalte."
    """
    Daraufhin gingen Battler und Jessica unters Deck zu den anderen, die anders als Battler ruhig darauf warten endlich anzukommen.
    """
    geo "Wie geht es dir Battler-kun?"
    geo "Wir alle wissen bereits, dass es dich schon erwischt hat."
    """
    Mit einem leichten aber auch nicht ganz überzeugenden Nicken stimmt Battler ihm zu.
    """
    but "Den Umständen entsprechend geht es mir gut."
    but "Der Kapitän hat doch absichtlich das Boot so wackeln lassen."
    geo "Ja gut,... das glaube ich eher weniger."
    geo "Leg dich am besten hin, du hast es schon bald geschafft."
    geo "Das erinnert doch an die alten Zeiten, nicht wahr, Jessica-chan?"
    jes "Ja, es ist so, als wäre er nie weg gewesen."
    jes "Nur mit dem Unterschied, dass er heute das erste mal sich übergeben hat."
    geo "Ahahahahaha, ja, einige Dingen ändern sich, während andere sich niemals ändern."
    """
    Das ist mein Cousin George, er wird von Tante Eva und Onkel Hideyoshi zu einem echten Gentlemen erzogen.
    Er arbeitet sehr hart und will auch schon sein eigenes Business starten, was ich sehr beeindruckend finde.

    Er wird von den anderen Familienmitgliedern sehr geschätzt.
    da er für sein Alter schon sehr reif und kenntnisreich ist.

    Ushiromiya Joji

    So wird er bei uns ausgesprochen und ich bin der festen Überzeugung,
    dass es ihm bestimmt gegen den Strich geht und er heute einen Massenmord veranstaltet.

    Ich würde auch am liebsten die ermorden, die für diese furchtbare Namenstradition verantwortlich sind.
    """
    but "Ich finde es ist auch besonders heute, weil heute Mittag ein Sturm aufziehen soll, der erst Montag wieder abklingen soll."
    but "Es kommt das erste mal vor, dass wir länger als einen Tag auf der Insel bleiben."
    geo "Ja, wir hatten allerdings auch immer Glück, dass sonst nie ein solch starker Sturm auf unserer Familienkonferenz getobt hat."
    geo "Was sagt man da so schön? Es gibt immer ein erstes mal."
    geo "..ähm... Battler-kun wusstest du, dass es sogenannte Sturmgötter gibt?"
    but "Ähhhhm.... meinst du Zeus...?"
    geo "Auch richtig, aber nein, ich rede von dem Sturmgott in einem selber"
    but ".....was?"
    geo "Okay, es geht um folgendes:"
    geo """
    In der tantrischen Spiritualität gibt es intensivere Gefühlsregungen und auch bei den Griechen gab es die dionysische Spiritualität,
    die auch besonders heftige Gefühle beinhaltet. In diesem Sinne hat jeder Mensch auch Sturmgötter in sich,

    die er auch in sich aktivieren kann. Die Sturmgötter können ihn auch zu schlimmen Handlungen veranleiten, zu Verbrechen und Gewalt.
    Sie können ihn aber auch dazu veranlassen, intensiv voran zu preschen und aus der Bequemlichkeit des Alltags hinauszugehen.
    """
    but "............."
    but "ähm...... ähm......"
    but "Tantrisch?..... Gefühlsregungen?..... Dionysische Spiritualität?....."
    but ".......................Du hast das aus dieser einen Yoga Zeitschrift entnommen....."
    geo "ähm......."
    geo "oh...."
    geo "Hahahaha, ich habe dich aber gut zum Nachdenken gebracht."
    geo "Meine Mom hat sich so eine Zeitschrift geholt und hin und wieder werfe auch ich einen Blick hinein."
    but "Hihihi, du hast nur pech gehabt, dass ich vor der Abreise auf dem Klo so eine Yoga-Zeitschrift in der Hand hatte, weil ich mich vergriffen habe."
    geo "Ein echter Sturmgott ist allerdings Aigaion aus der griechischen Mythologie."
    but "Das einzige Griechische, dass ich schätze ist einen leckeren Teller voll Gyros-Geschnetzeltes."
    but "Namnamnamnam"
    geo ".........."
    geo "Wie dem auch sei, dieser Gott kann Meeresstürme auslösen, so wie einer der uns heute treffen wird."
    but "Du willst mir also sagen, dass irgendeine Gottheit, auf die wir keinen Einfluss haben, diesen Sturm ausgelöst hat?"
    geo "......hmm......"
    geo "So könnte man es ausdrücken ja!"
    but "....Na ja, fest steht, dass wir die Zeit, die uns Aigaion nun gibt, nutzen können um wieder mehr Zeit miteinander zu verbringen."
    jes "Ja, das hast du definitiv bitter nötig Battler-kun!"
    jes "Du musstest die Familie ja auch unbedingt für 6 Jahre verlassen...."
    but ".....Da ist was dran."
    jes "Die Familienkonferenz ist etwas, auf dass ich mich mit am meisten freue..."
    jes "Es ist die kurze Zeit, wo sich mein langweiliger Alltag mal auflockert."
    but "Ja, ich freue mich auch wieder hier bei euch zu sein, das hat mir in 6 Jahren mit am meisten gefehlt."
    jes "Es ist furchtbar nur mit meinen Eltern und Großvater auf der Insel zu wohnen."
    jes "Jeden Tag muss ich ziemlich früh aufstehen, da meine Schule nicht wirklich in der Nähe liegt, sondern auf Niijima."
    jes "Nach der Schule muss ich sofort zurück nach Hause, ich kann deshalb keine Zeit mit meinen Freunden verbringen."
    """
    Jessica redet sich immer mehr in Rage und die Wut steht ihr wie ins Gesicht geschrieben.
    """
    jes "Danach habe ich nur Zeit für Hausaufgaben und in meinem Zimmer zu verweilen,.... es gibt absolut nichts zutun."
    jes "...Am liebsten würde ich diese dämliche Insel für immer verlassen und auf dem Festland ein neues Leben beginnen."
    jes "....argh...."
    jes "Und ich muss mir jeden Tag des Gemecker von meiner Mutter anhören, das geht Morgens los und hört Abends auf, ich ertrage das einfach nicht mehr länger!"
    jes "Dadurch, dass ich keinen direkten Kontakt zu meinen Schulfreunden habe, ....fühle ich mich ziemlich einsam hier."
    jes "Und jeden neuen Tag an dem ich das durchmache, frage ich mich, was ich hier eigentlich noch mache..."
    """
    Man merkt es sofort, dass Jessica es sehr nahe geht, dass sie nach der Schule isoliert von der Außenwelt leben muss.

    George und Battler sind beide ebenfalls bedrückt aber verständnisvoll, als sie Jessicas Worte über ihren Inselalltag hörten.

    Onkel Hideyoshi scheint das Gespräch mitbekommen zu haben und erhebt sich aus seinem gemütlichen Sitz.
    """
    hid "Na, na Jessica-chan, du musst es positiv sehen!"
    hid "Eines Tages wirst du wirklich in der Lage sein, die Insel zu verlassen und dein eigenes Leben zu führen."
    jes "Aber wie lange soll das noch dauern? ..... und was ist, wenn meine Schulfreunde mit mir nichts mehr zu tun haben wollen?"
    hid "Auch deine Schulfreunde werden Verständnis für deine Situation haben, eines Tages wirst du zu ihnen gehen können und eine ganze Menge Zeit mit ihnen verbringen"
    hid "Bis dahin solltest du immer dein Bestes geben, denn das wird sich am Ende des Tages definitiv auszahlen!"
    jes "....... eines Tages?"
    jes "Aber ich warte schon seit so vielen Jahren....."
    hid "...Du hast immerhin noch dein ganzes Leben vor dir, glaub mir, deine Zeit als Teenager auf der Insel wird später nur noch eine Erinnerung sein..."
    hid "Jetzt habe ich mich aber verquatscht, wahahahahaha"
    hid "Lass aber wirklich den Kopf nicht hängen und häng dich weiter rein, ja?"
    jes "Danke Hideyoshi, ich denke der Plan ist gut, ich werde ihn mir zu Herzen nehmen."
    jes "Ich fühle mich schon besser."
    hid "So ist es richtig, du schaffst das schon, wahahahaha"
    """
    Das ist Georges Vater und mein Onkel Hideyoshi, er ist ein herzensguter und sympathischer Mann und ich denke, ich mag ihn von allen Erwachsenen am meisten.
    Er ist der Mann von Tante Eva und er hat sein Unternehmen von Grund auf neu aufgebaut

    und arbeitet jetzt als Präsident einer mittelgroßen Restaurantkette. Die Kette scheint zu wachsen und sehr gut zu laufen.
    Sein Name wird Ushiromiya Hideyoshi ausgesprochen, wie Kyrie ist sein Name absolut perfekt!

    Das liegt daran, dass er als Japaner in die Familie eingeheiratet hat..... ich beneide jeden mit normalen Namen.
    """

    geo "Jessica-chan, alleine ein Ziel zu haben, auf das man hinarbeiten kann, ist etwas, was dich jeden Tag motivieren sollte nicht aufzugeben."
    geo "Auch ich oder Battler-kun haben so unsere Sorgen und Probleme die wir überall mit hinnehmen, also halte noch ein wenig durch, okay?"
    jes "Ja vielen Dank, das hilft mir wirklich sehr, danke!"
    """
    Die Worte von Hideyoshi und George waren sehr effizient, wenn es darum ging Jessica aufzuheitern.

    Denn man sieht deutlich wie ein Lächeln in Jessicas Gesicht zurückkehrt.
    """
    eva "Hey, wie es aussieht, sind wir gleich da, Battler-kun..."
    eva "Wusstest du, dass Seekrankheit auch nach der Reise noch etwas anhalten kann?"
    but "............."
    but "Mach mir doch bitte keine Angst Tante Eva!"
    eva "Oh... entschuldige, ich wollte dir nur sagen, dass, wenn dein Körper sich an die Bewegungen des Bootes gewöhnt hat, sich dein Körper an Land wieder umgewöhnen muss."
    eva "Aber mach dir keinen Kopf. Battler-kun, das passiert nicht unbedingt. *kicher*"
    """
    Das ist meine Tante Eva und die Mutter von George. Sie bildet mit dem alten Bastard Dad sowas wie ein Scherzkeksduo,
    wenn die beiden richtig loslegen, dann bleibt kein Stein mehr auf den anderen.

    Sie beherrscht auch einige Chinese Martial Arts Techniken, einer ihrer Roundhousekicks
    soll bei einem Trainingsmatch mal getroffen haben und ihr Gegner wurde kaltgestellt wie ein Softdrink.

    Ich möchte definitiv keinen Tritt von ihr unter die Dachlatte bekommen.
    Ach ja! Ich habe ja fast ihren Namen vergessen. Sie heißt hier Ushiromiya Eba...... mit b.....
    """
    but ".....Nein, du verarscht mich doch Tante Eva...."
    eva "Oh nein, .....sowas würde ich niemals machen *kicher*"
    eva "....Ich wollte dir nur etwas über die Seekrankheit erzählen... mehr nicht... *kicher*"
    """
    Tante Eva wollte mir mit hoher Wahrscheinlichkeit keine Angst machen,
    sondern meinen Kopf auf die Probe stellen, denn wenn ich gleich an Land an ihre Worte denke,

    dann wird mir definitiv wieder übel werden, ......ganz schön rafiniert.
    """
    kyr "Wir sind jetzt gleich da! .....Die Insel ist ganz nah!"
    """
    Abrupt wird unser plausch unterbrochen mit der erfreulichen Meldung, dass wir sehr bald an Land gehen werden!
    """
    but "Wird sich wohl gleich zeigen, ob du recht hast Tante Eva"
    eva "*kicher*"
    eva "Forder es besser nicht heraus.... Battler-kun...."
    hid "wahahahahaha, ihr zwei seid mir ja welche,..... lasst uns lieber ans Deck gehen, da wir gleich an Land gehen!"
    jes "Ja, das ist eine gute Idee!"
    """
    So erhoben sich alle von ihren Sitzen und haben bemerkt, dass draußen die Wolken sich unerwartet, viel zu früh verdunkelt haben.
    """
    kyr "War der Typhoon nicht für heute Mittag angekündigt?"
    kyr "Es könnte sein, dass es gleich anfängt zu regnen."
    rud "Wir sind in ungefähr 10 Minuten da, aber gemütlich wird es nicht mehr."
    kyr "Stimmt,... der Wind hat bereits zugenommen."
    """
    Der Wind der minutenweise immer stärker über das Meer peitscht,
    ist kein Wind, wie sie die meisten Leute auf dem Festland kennen.

    Der Wind kann ungehindert und mit voller Kraft über das Wasser fegen,
    während auf dem Land es immer wieder Häuser, Berge und Terrain gibt, dass den Wind abschwächen kann.
    """
    kyr "Dass die Wettervorhersage sich mal in der Zeit irrt? *kicher*"
    rud "Ich habe mal wegen eines angeblichen Typhoons ein Geschäftsessen abgesagt..."
    rud "Der Typhoon kam erst 2 Tage später, ich habe mich noch nie so dämlich gefühlt, wie in dieser Situation."
    kyr "War doch bestimmt ein Erlebnis, sowas am Ende erklären zu müssen..."
    rud "Bitte erinnere mich nicht daran...."
    """
    Besorgt sind nicht nur Rudolf und Kyrie, sondern all die anderen sind ebenfalls überrascht,

    Dass der Sturm einige Stunden zu früh kommt. Dabei wurde vom Wetterbericht garantiert, dass es erst Mittags losgeht.
    Die folgen könnten turbolente Flüge sein, die noch für Kurzflüge eine Starterlaubnis bekommen haben.

    Rudolf zog sich für erste zurück um etwas alleine zu sein.
    """
    rud "*seufz*"
    """
    Nach ungefähr 5 Minuten stoßte er einen tiefen Seufzer aus, während er sich eine Zigarette anzündet, da ihn etwas sehr beschäftigt und niemand außer Eva hat anscheinend diesen Seufzer mitbekommen.
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
    """
    Die ältere Frau heißt Kumasawa. Sie ist eine Teilzeitkraft, die zwar mehrmals gekündigt hat, aber insgesamt schon viele Jahre im Dienst der Familie steht.
    Sie ist geschickt und mehr als fähig, wenn es darum geht, ihre Aufgaben zu erfüllen,

    aber wegen ihrer Geschwätzigkeit und ihrer Vorliebe für Gerüchte ist sie als Bedienstete nicht sehr angesehen.
    Ihr Name im Japanischen? Der lautet auch bei uns Kumasawa, ihre Eltern haben ihr einen vernünftigen Namen gegeben... *seufz*....
    """
    jes "Aber.... ich habe heute Morgen in der Küche gar keine Makrelen gesehen, Kumasawa..."
    jes "Daher, kann es heute leider keine Makrelen geben!"
    kum "Ohohohoh, Ihr habt mich voll erwischt, Jessica-sama."
    rud "Hey Battler! Wenn dir immer noch schwindelig ist und du gleich auf den Esstisch kotzt, darfst du Nachhause schwimmen."
    but "Lass es gut sein!.... Mir geht es bereits wieder besser."
    rud "Na,.... das hoffe ich doch,..... ich will mich nicht vor den anderen rechtfertigen müssen, warum du Holzkopf den Esstisch ruinierst."
    but "Keine Sorge Dad, wenn es hart auf hart kommt, passt mir dein Schicker Anzug auch ganz gut hihihihi"
    goh "Liebe Gäste, wir haben Zeitverzug! Wir müssen jetzt unverzüglich zum Gästehaus!"
    """
    Battler und Rudolf wollten gerade wieder ihre Vater-Sahn Beziehung stärken, da grätscht Gohda rein, der etwas angefressen mit dem Zeigefinger auf seine Armbanduhr tickt.
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
    Marias Mutter Rosa konnte in unmittelbarer Nähe gesehen werden, die mit einem wütenden Blick Marias Freude jeden Moment unterbrechen wird.
    """
    ros "Maria!"
    "*slap*"
    """
    Zu hören war nur ein Dumpfes Klatschen und zwar das Geräusch von einer Handfläche die unsanft mit hoher Geschwindigkeit an die Backen eines kleinen Mädchens landen.

    Aus Marias Freuden Uus wurde ein sofortiges schweigen
    """
    ros "Wie oft muss ich dir sagen, dass du diesen Magie und Beatrice Unsinn sein lassen sollst?"
    ros "Die ganze Zeit Magie hier, Beatrice da, wann hörst du endlich damit auf?"
    "*slap*"
    """
    Ein weiteres mal darf Marias Schmerzen verursacht von der Wut ihrer Mutter spüren.

    Jeder der Marias Gesicht sehen könnte, möchte am liebsten selber in Tränen ausbrechen.
    """
    ros "Weißt du eigentlich wozu du mich hier zwingst?"
    ros "Benimm dich doch endlich mal deinem alter entsprechend und hör auf mir so viele Probleme zu machen!"
    ros ".....Sonst wird Papa.... niemals von seiner Geschäftsreise zurückkehren..... *sob*"
    """
    Maria die zwar eine menge Tränen im Gesicht hat, sieht ihre Mutter an, die sogar noch viel mehr Tränen weint und einen Nervenzusammenbruch hat.

    Während diesem Ausbruch der Gefühle sind die anderen bereits vorgelaufen, haben sich allerdings auch jetzt auf den Weg gemacht das Gästehaus zu erreichen.
    """
    but "Ich glaube das ist deren Angelegenheit, auch wenn Maria mir ziemlich leid tut."
    jes "Da dürfen wir uns auch nicht einmischen, so ist das leider, da sind wir absolut machtlos."
    """
    Ganz vorne laufen Gohda und Kumasawa voran, die beiden sind wohl endlich froh,
    die Familie in Richtung Gästehaus bewegt zu haben, weil jede weitere Verzögerung Madam Natsuhi ziemlich wütend machen würde.
    """

    goh "Verdammt, warum kam das Boot so spät?"
    goh "Madam Natsuhi wird uns dafür köpfen und den anderen zum Abendessen servieren..."
    goh "Das schlechte daran ist, dass ich meinen eigenen Kopf nicht zubereiten kann, was das Endprodukt schmälert."
    kum "ohohohoh, ich denke, so wie Madam drauf ist, werden wir so oder so geköpft werden...."
    kum "Aber immerhin sind Ihre verwandten jetzt da und damit haben wir unseren Auftrag erfüllt."
    kum "Was Jessica-sama nicht weiß ist, dass ich tatsächlich Makrelen besorgt habe, du erinnerst dich?"
    goh "Ja, auch wenn dieser Scherz ein wenig überspitzt ist, werde ich für Jessica-sama auch einen normalen Teller vorbereiten."
    goh "Sobald sie die Makrelen bemerkt, werde ich nicht zögern den Teller wieder gegen einen leckeren auszuwechseln."
    kum "ohohohoh, das ist in Ordnung, Gohda-san, wir wollen ja nicht, dass sie dein Gericht am Ende nicht isst... ohohoho...."
    """
    Bereit für den Tot durch Madam Natsuhi und einen gemeinen Scherz geplant, ist die Familie auf direktem Weg zum Gästehaus.

    Damit kann die Ushiromiya Familienkonferenz auf Rokkenjima im Jahre 1986 nun beginnen!
    """
