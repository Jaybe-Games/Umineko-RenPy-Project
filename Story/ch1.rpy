label chapter1:

    $ discord.update(state = "Episode 0")
    $ discord.update(details = "Chapter 1")
    $ chapter = 1
    $ songname = "-"
    $ persistent.openingplayed = True
    $ renpy.free_memory()
    if persistent.showch == True:
        show screen showch
    play sound "audio/sfx/umise_028.ogg"
    show oct_4_1986 with dissolve
    pause (7)
    play ship "audio/sfx/umilse_004.ogg"
    $ songname = "HANE (Feathers)"
    if persistent.showbgm == True:
        show screen showsong
    play music "audio/bgm/umib_003_intro.ogg"
    queue music "audio/bgm/umib_003_loop.ogg" loop 
    show white with m1trans
    camera at normalboat,boatswing
    scene ship_s2a with m1trans1
    window auto
    "In der Luft liegt der typische Meeresgeruch von Salz und auch ein wenig von Algen."
    extend " Ein Duft, der den Geruchssinn sofort in Ekstase versetzt, wenn nicht sogar die Seele selbst begeistert."
    "Denn auch ein taubstummer und sehbehinderter Mensch weiß sofort, dass das Meer in der Nähe ist, und kommt so in die richtige Stimmung."
    "Die Familie Ushiromiya ist mit dem Boot von der Insel Niijima zur jährlichen Familienkonferenz auf der Insel Rokkenjima unterwegs."
    extend " Aber ein Familienmitglied scheint die Fahrt gar nicht gut zu tun, er schreit herum, dass er vom Boot fällt und so." 
    play sound "audio/sfx/umise_003.ogg"
    show but b23kuyasigaru1 at m with dis
    but "“whaoooo!!!!" 
    extend " ....Ich falle runter, ....ich falle runteeeeeer!!!"
    extend " ....Ich hasse Boote! ...Gleich muss ich kotzen, ich falleeeee!!!"
    extend " ...Warum muss das verfluchte Ding auch so stark schaukeln?"
    but "....Das wars!" 
    extend " ....Ich werde diese Insel nicht mehr erreichen, eher sterbe ich hier!”"
    scene ship_s2a
    show but b23kuyasigaru1 at l
    play sound "audio/sfx/umise_047.ogg"
    show mar a11warai1 at r,jump_shake
    with dis
    mar "“*kicher*kicher*" 
    extend " ....Battler fällt runter, Battler fällt runter!" 
    extend " uu-uu~!!"
    but b23nayamu1 "“...Bitte" 
    extend " ...Maria-chan," 
    extend " ...bitte etwas ruhiger," 
    extend " ...das macht alles mein Magen nicht mit.”"
    mar a11uuu1 "“Uu~?" 
    extend " ....du findest das nicht lustig?"
    play sound "audio/sfx/umise_047.ogg"
    extend a11warai1 " .....Ich finde das super lustig!" 
    extend " *kicher*kicher*" 
    extend " uu~!”"
    scene ship_s2a
    show but b11warai2 at m
    with quickergradientwiperight
    if persistent.battler == False:
        $ persistent.newelement1 = True
        $ persistent.battler = True
        $ persistent.menustate = 3
        $ Achievement.add(achievement_bronze2)
        play sound "audio/sfx/umise_1060.ogg"
        show screen charupdate
    "Mein Name ist Ushiromiya Battler."
    extend " Ich bin der Sohn von Rudolf und Asumu, Asumu ist vor ungefähr sechs Jahren gestorben."
    "Danach habe ich die Familie wegen eines Konflikts mit Dad für sechs lange Jahre verlassen und habe bei meinen Großeltern mütterlicherseits gelebt."
    "Mein Name wird im Japanischen übrigens so geschrieben: Ushiromiya Batora."
    extend " Ja, man spricht mich nicht Battler aus, sondern 'Batora', klingt echt komisch."
    "Meine Japanischen Schriftzeichen machen mich wütend. Ich werde mit den Zeichen von 'Person' und 'Kampf' geschrieben."
    extend " Deswegen denkt ein typischer Japaner ich heiße Sento-kun. Niemand würde auch nur im Traum daran denken, dass es 'Battler' ausgesprochen wird."
    "Aber der Spaß hört bei mir noch lange nicht auf..."
    extend " Hier sind einige, die ihren Namensgeber am liebsten in dunkle Kammern sperren würden."
    scene sea_1af with gradientwipeup
    "Wenn es etwas gibt, dass ich an den Familienkonferenzen hasse, dann ist es die Anfahrt."
    extend " Jedes mal schaukelt dieses Boot so extrem, dass ich jeden Moment gefühlt über Bord gehen könnte."
    "Maria, die überhaupt nicht seekrank ist, beginnt laut zu kichern,"
    extend " weil es so lustig ist, mir zuzusehen wie ich den Anfall meines Lebens habe."
    "Ich merke, wir werden beobachtet und der kann sich das Lachen echt nicht verkneifen."
    scene ship_s2bf
    show rud a11akuwarai1 at r
    with quickergradientwiperight  
    rud "“...Hey Battler-kun!" 
    extend " Wenn du kotzen musst, dann bitte in einen Eimer!"
    extend " .....Bei dem, was du dir in den Hals schaufelst, würdest du eine Menge Fische auf dem Gewissen haben." 
    extend " ....hehe."
    rud "....Unglaublich, dass du schon im Flugzeug so durchgedreht bist," 
    extend " du konntest ja nicht mal im Auto still sitzen.”"
    show but b22odoroki2_mouth_closed at l
    with dis
    but "“..........."
    extend b22odoroki2 " ...Lass mich in Ruhe!"
    extend " ....Das ist echt kein guter Zeitpunkt!”"
    rud a11defo1 "“Es ist nie ein guter Zeitpunkt, wenn du mit irgendetwas fahren musst." 
    extend " .....Wag es nicht, ins Meer zu kotzen!”"
    but b22nayamu2 "“...Ich gebe mir hier die größte Mühe.”"
    scene ship_s2bf
    show rud a11warai1 at m
    with quickergradientwiperight  
    if persistent.rudolf == False:
        $ persistent.rudolf = True
        play sound "audio/sfx/umise_1060.ogg"
        show screen charupdate
    "Das ist mein Vater Rudolf. Der alte Bastard ist so groß wie ich und macht sich bei Gelegenheit gerne über mich lustig."
    extend " Sein Name wird auf Japanisch Ushiromiya Rudorfu ausgesprochen, fast die ganze Familie hat diese seltsame Namenstradition."
    "Seit meine Mutter Asumu verstorben ist, hat sich unser Verhältnis sehr verschlechtert,"
    extend " aber ich bin sicher, dass es mit der Zeit wieder funktionieren kann."
    scene black
    camera
    with quickgradientwipedown
    "Vor sechs Jahren, kurz nach dem Tod meiner Mutter, hat mein Vater seine Arbeitskollegin geheiratet."
    extend " Das hat mich gebrochen, weil es einfach viel zu schnell ging, kaum war meine Mutter gestorben, hat er wieder geheiratet."
    "Das nächste Problem war, dass Dad schon eine Affäre mit ihr gehabt hatte."
    extend " Beide haben ein Kind meine Stiefschwester Ange, die heute leider Krank ist und Zuhause geblieben ist."
    "Wenn man sich ausrechnet, wann Ange geboren wurde und wann meine Mutter verstorben ist, wird mir immer ganz übel."
    extend " Da ich mit solchen Leuten nicht in einem Haushalt leben wollte, bin ich zu meinen Großeltern mütterlicherseits gezogen und habe die Ushiromiya-Familie verlassen."
    "Leider sind meine Großeltern vor kurzem verstorben und ich hatte die Gelegenheit, mit meinem Vater und meiner Stiefmutter zu sprechen, und wir konnten irgendwie einen gemeinsamen Nenner finden."
    "Ich bin also wieder Teil der Familie und nehme nach sechs Jahren zum ersten Mal wieder an der Konferenz teil."
    scene ship_s2bf
    show kir a11defo1 at l
    camera at normalboat,boatswing
    with quickergradientwiperight
    kir "“...Ist es nicht schön, dass Battler-kun wieder da ist?"
    extend " Ich meine, nach 6 Jahren Abwesenheit immer noch ein Theater bei der Ankunft? *kicher*”"
    show rud a11warai1 at r with dissolve
    rud "“....Ja"
    extend " ....Aber das war viel schlimmer, als er noch jünger war," 
    extend " ...da hatte man die ganze Anreise keine Ruhe.”"
    kir a11majime1 "“...Aber er ist selbst schuld, wenn er da rumturnt, obwohl er weiß, dass er seekrank wird.”"
    scene ship_s2bf
    show kir a11defo1 at m
    with dis
    if persistent.kyrie == False:
        $ persistent.kyrie = True
        play sound "audio/sfx/umise_1060.ogg"
        show screen charupdate
    "Das ist meine Stiefmutter Kyrie-san, der alte Bastard hat diese Frau kurz nach dem Tod meiner Mutter geheiratet."
    "Sie ist sehr intelligent und hat mir viel über das Schachbrettdenken beigebracht."
    extend " Also wie man eine Partie mit den Augen des Gegners sehen kann."
    "Ich sehe sie nicht als Mutter, aber wir verstehen uns gut."
    extend " Sie ist für mich eher so etwas wie eine freundliche Nachbarin, denn wir sind uns einig, dass wir nicht so tun sollten, als hätten wir eine enge Beziehung, die uns sehr schnell unangenehm werden könnte."
    extend " Also halten wir einfach einen gesunden Abstand, damit wir uns nicht unwohl fühlen."
    "Wollt ihr wissen, wie man sie auf Japanisch ausspricht?" 
    extend " Ganz einfach:" 
    extend " Ushiromiya Kyrie."
    "Und nein, ...."
    extend " man spricht es nicht komisch aus, ihr Name ist absolut perfekt!"
    "Ich hasse Großvater den alten Kauz dafür, dass wir so komische Namen haben."
    camera at extremboat,boatswing
    scene ship_s2bf
    show but b23kuyasigaru1 at m
    with quickergradientwiperight
    but "“...........Ich finde das gar nicht lustig" 
    extend " .......Ich kämpfe hier schließlich um"
    extend " ............mein"
    extend " ............Leben" 
    extend " ...................*würg*”"
    play sound "audio/sfx/umise_003.ogg"
    show but b23kuyasigaru1 at m,run
    hide but with dissolve
    "Battler wurde so übel, dass er sich nicht zurückhalten konnte und den ganzen gekochten Reis vom Vormittag ins Wasser schleuderte."
    show rud a11akuwarai1 at r with dissolve
    rud "“.....Jetzt hat dieser Kasper tatsächlich die Fische gefüttert, ach herrje," 
    extend " ....ahahaha!”"
    camera at normalboat,boatswing
    show mar a22warai2 at l with dissolve
    mar "“uu-uu~!" 
    extend " Battler hat sich übergeben!" 
    extend " Battler hat sich übergeben!" 
    extend " *kicher*kicher*”"
    scene ship_s2a
    show mar a11niyari1 at m
    with quickgradientwiperight
    if persistent.maria == False:
        $ persistent.maria = True
        play sound "audio/sfx/umise_1060.ogg"
        show screen charupdate
    "Das kleine Mädchen, das definitiv mehr Spaß daran hat, mir zuzusehen, als mit dem Boot zu fahren," 
    extend " ist meine jüngste Cousine Maria,"
    "Auch sie hat unsere Namenstradition übernommen," 
    extend " statt eines normalen japanischen Namens heißt sie Ushiromiya Maria."
    extend " Das wird auch so ausgesprochen, nur in kurzen Silben."
    "Das letzte mal als ich sie gesehen habe, war sie wie alt?"
    extend " drei Jahre?"
    extend " Das bedeutet sie müsste heute neun Jahre alt sein und geht zur Grundschule."
    "Am Flughafen war sie überwältigt, als sie erfuhr, dass ich ein Cousin von ihr bin. In jungen Jahren behält man nur wenige Erinnerungen."
    "Aber wir haben uns super schnell angefreundet und haben eine tolle Zeit."
    scene ship_s2a
    show ros a11ikari1 at r
    with quickgradientwiperight
    ros "“Maria!"
    extend " ....Es reicht jetzt," 
    extend " .....lass Battler-kun in Ruhe!”"
    show mar a11defo1 at l with dissolve
    mar "“....uu~”"
    ros a11ikari2 "“...und hör auf mit diesem 'uu-uu'!"
    extend " .....Du bist kein kleines Kind mehr!”"
    "Maria war nicht begeistert, dass ihre Mama ihre Freude unterbrach."
    extend " Rosa ist eine sehr strenge Mutter."
    extend " Sie nimmt Marias eher kindliches Verhalten sehr ernst,"
    extend " was schon zu unangenehm anzusehenden Szenen mit den beiden geführt hat."
    hide mar
    show but b11odoroki3 at l
    with dis
    ros a11komaru4 "“....Tut mir leid," 
    extend " ......Battler-kun," 
    extend " .....ich kriege es einfach nicht aus ihr raus.”"
    but b22warai1 "“Schon gut, Tante Rosa," 
    extend " ....sie meint es nicht böse, also bin ich es auch nicht.”"
    ros a11majime1 "“...Dankeschön, Battler-kun, das beruhigt mich."
    extend " .....Nun, dass dein größter Feind das Fahrzeugfahren ist, verstehe ich nicht,"
    extend " .....denn du wirkst so reif und erwachsen und jetzt das?”"
    but b11warai2 "....Ihihihi!"
    extend " ...Entschuldigung, dass ich einen falschen Eindruck erweckt habe."
    scene ship_s2a
    show ros a11warai1 at m
    with quickgradientwiperight
    if persistent.rosa == False:
        $ persistent.rosa = True
        play sound "audio/sfx/umise_1060.ogg"
        show screen charupdate
    "Das ist Tante Rosa," 
    extend " sie ist die Mutter von Maria die sie sehr streng erzieht."
    "Trotzdem kenne ich Tante Rosa als sehr liebe Person," 
    extend " auch wenn das Taschengeld, dass sie uns Kindern gibt, nicht so hoch ist wie bei den anderen Erwachsenen."
    "Trotz ihres blöden Namens ist ihre Aussprache nur Ushiromiya Rooza,"
    extend " was nur halb so schlimm ist wie der Name meines Vaters."
    "Trotzdem ist der Name in jeder Hinsicht lächerlich." 
    extend " Danke Großvater nochmal dafür."
    scene ship_s2a
    show rud a11akuwarai1 at r
    with quickergradientwiperight
    rud "“Er kann einfach nicht still sitzen, aus irgendeinem Grund."
    extend " ...Das ist wirklich peinlich, das darfst du niemandem erzählen.”"
    show but b23nayamu1 at l with dis
    but "“..Ey!" 
    extend " .....halt den Mund!”"
    rud a11akuwarai2  "“...Ey Battler-kun!" 
    extend " ...Das Frühstück, dass gerade im Meer gelandet ist, hat Geld gekostet und Lebensmittel werden nicht billiger!”"
    but b22nayamu1 "“...Ähm,"
    extend b22nayamu2 " ...also wenn du es unbedingt wiederhaben willst, kannst du ja ins Meer springen und dann ganz weit den Mund aufmachen," 
    extend " ....ihihihi!”"
    rud a11defo2 "“........Battler....”"
    show rud a11defo1 at l2 with MoveTransition(0.1)
    play sound "audio/sfx/umise_047.ogg"
    show but b11kuyasigaru1 behind rud at l
    with vpunch
    but "“....owowowowowow"
    extend " ....Du alter Bastard!" 
    extend " ....Scheiße," 
    extend " .....owowowow”"
    "Einen Moment hat Battler nicht aufgepasst und schon hat Rudolf sein Ohrläppchen gepackt und behandelt es nicht gerade zimperlich."
    but "“....Owowowowowowowow," 
    extend " lass los!" 
    extend " ....Owowowowowowow"
    extend " .......Das tut richtig weh," 
    extend " hör auf damit," 
    extend " .....owowowow”"
    rud "“....Du" 
    extend " ...willst" 
    extend " ...also," 
    extend " ....dass ich es mir zu"
    extend " ....rück"
    extend " ...ho"
    extend " ...le"
    extend " ....jaaaa~?”"
    "Rudolf hat einen sehr starken Griff, besonders wenn es um Battlers Ohrläppchen geht, man hat das Gefühl, er reißt es jeden Moment ab."
    but a11aseru5 "“....Ich hoffe, dass du über das Geländer fällst und ertrinkst, du alter Bastard!"
    extend b11kuyasigaru1 " ....Owowowow"
    extend " lass los!"
    but "...Ich"
    extend " ....gebe"
    extend " ....nicht"
    extend " .....auuuuuuffffff!!!"
    extend " ...owowowow" 
    extend " ....lass doch endlich los owowowowow" 
    extend " ....es tut weh!”"
    rud a11akuwarai1 "“....Das ist deine Strafe, wenn du frech wirst," 
    extend " ....mein lieber Battler-kun.”"
    scene ship_s2bf
    show kir a11majime1 at m
    with quickergradientwiperight
    kir "“Lasst es für heute gut sein, ihr beiden."
    extend " Ihr solltet euren Vater-Sohn Konflikt wann anders austragen.”"
    "Nachdem Kyrie den kleinen Konflikt erfolgreich beendet hatte, waren Schritte zu hören." 
    extend " Jemand scheint von unters Deck nach draußen kommen zu wollen."
    hide kir
    show jes a11atya2 at m
    with dis
    jes "“...B.."
    extend " ...Battler-kun?" 
    extend " hast du gerade eben vom Deck gekotzt?" 
    extend " ...Ich schaue nach draußen und plötzlich kommt so eine widerliche Suppe von oben runter." 
    jes "...Das war eklig!"
    extend " ...Nächstes Mal nimm besser einen Eimer mit!"
    jes a11aisowarai1 "Ach ja," 
    extend " und was war das für ein 'Ich falle, ich falle' -Geschrei?"
    if persistent.tip2 == False:
        $ persistent.tip2 = True
        play sound "audio/sfx/umise_1060.ogg"
        show screen tipupdate
    extend " ...Bist du ein bisschen {note_green}meschugge{/note_green}?"
    extend " ...wahahahahahahahaha!"
    jes ".....Das war die eine Sache,"
    extend " .....und dann war da noch die Kotze, die vom Deck segelte."
    extend " ....pahahahahahahaha!”"
    scene ship_s2a
    show but a11defo1 at r
    with quickergradientwiperight
    but "“......Tut mir voll traurig."
    extend " ....Das verfluchte Boot schaukelt so viel!"
    extend " ....Das Schiff schaukelt und schaukelt und schaukelt!!!"
    but a21kuyasigaru1_open_mouth "....aaaaaaaahhhhhhhhhhhhhhhh!!!!!!!"
    extend a21kuyasigaru1 " Mach, dass es aufhört, sonst falle ich wieder!”"
    show jes a11atya3 at l with dis
    jes "“....Vielleicht sollte der Kapitän etwas langsamer fahren, sonst geht es dir gleich noch schlechter."
    extend " ...Ich werde sofort den Kapitän bitten, etwas langsamer zu fahren, aber bitte nicht mehr ins Meer kotzen.”"
    but b11odoroki3 "“.....Ja" 
    extend " ....Vielen Dank, Jessica-chan.”"
    scene ship_s2bf
    show jes a11warai1 at m
    with quickergradientwiperight  
    if persistent.jessica == False:
        $ persistent.jessica = True
        play sound "audio/sfx/umise_1060.ogg"
        show screen charupdate
    "Das ist meine Cousine Ushiromiya Jessica."
    extend " Sie ist die Tochter von Onkel Krauss und Tante Natsuhi." 
    extend " Jessica ist echt cool drauf und ist wohl aktuell in dieser Phase, wo man gegen seine Eltern rebelliert."
    "Sie ist aber auch in dieser Phase, wo die Mädchen so große Brüste bekommen."
    extend " hihihihih... ich würde sie mal gerne in die Hand nehmen."
    "Aber dann würde sie mich windelweich schlagen, denn mit ihr ist es nicht gut Kirschen zu essen, wenn man es sich mit ihr verscherzt."
    "Jessica klingt sehr nach englischer Herkunft und wird bei uns Ushiromiya Jeshka ausgesprochen," 
    extend " sie muss richtig unzufrieden mit ihrem Namen sein."
    "Sie hat außerdem so eine 'Verrückte Art zu reden'." 
    extend " Sie flucht viel und ihre Wortwahl ist gewöhnungsbedürftig."
    "Früher waren wir das Chaotenduo, haben viel Unsinn gemacht und waren uns auch nicht zu fein, gegenüber ihren Eltern einen sehr rauen Ton anzuwenden."
    extend " Die Vorträge der Erwachsenen über gutes Benehmen nervten uns zwar jedes Mal, aber es war auch einfach zu lustig zu sehen, wie sich die vorbildlichen Erwachsenen aufregten."
    camera at slowerboat,boatswing
    "Der Kapitän hat zugestimmt langsamer zu fahren und jetzt schaukelt das Boot nicht mehr so stark."
    jes "“....Verdammte Scheiße Battler-kun," 
    extend " ...jetzt werden wir uns wegen dir verspäten!”"
    show but b22warai1 at l
    with dis
    but "“.....Halt doch mal dein Maul," 
    extend " ...immerhin kann ich jetzt ein wenig chillen.”"
    jes a11defo2 "“.....Wir sollten besser runter gehen zum 'chillen', wir sind gleich auf der Insel.”"
    but "“....Ja," 
    extend " ...das kann ich versuchen," 
    extend " jetzt, wo das Boot etwas langsamer fährt."
    extend b22nayamu2 " ....Aber ich kann trotzdem nicht garantieren, dass ich den Rest meines Frühstücks bei mir behalte." 
    extend " Ihihihi!”"
    $ songname = "Doorway of Summer"
    if persistent.showbgm == True:
        show screen showsong
    play music "audio/bgm/umib_002_intro.ogg"
    queue music "audio/bgm/umib_002_loop.ogg" loop
    play ship "audio/sfx/umilse_004.ogg" volume 0.2
    scene ship_s3a at bgani
    camera
    show expression(CustomParticles("images/system/particle.png", 10))
    with gradientwiperight
    "Dann gingen Battler und Jessica unter Deck zu den anderen, die im Gegensatz zu Battler ruhig warten, bis sie endlich die Insel erreichen."
    show eva b22akire2 at rightedge
    show hid a21warai1 at m
    show kum a12defo2 at leftedge
    with quickergradientwiperight
    " ....Moment mal, dieses 'ruhig' sein ist falsch! Ich sehe es klar und deutlich! Die anderen Erwachsenen verkneifen sich doch alle gerade das Lachen."
    hide eva
    hide hid
    hide kum
    show geo a11defo1 at m
    with quickergradientwiperight
    geo "“Battler-kun!"
    extend " ....Wir alle wissen bereits, dass es dich schon erwischt hat."
    extend " ...Dir scheint es gerade wohl gar nicht gut zu gehen.”"
    show but b22nayamu1 at leftedge,nod with dis
    "Mit einem leichten, aber nicht ganz ernstgemeinten Nicken stimmte Battler zu."
    but "“Mir geht es gut, den Umständen entsprechend...."
    extend b23kuyasigaru1 " Der Kapitän hat das Schiff doch absichtlich so schaukeln lassen.”"
    geo a11majime2 "“...Ja gut," 
    extend " ...eigentlich nicht."
    extend " ...Leg dich am besten hin, du hast es gleich geschafft."
    geo a11warai1 "Erinnert an alte Zeiten," 
    extend " ....nicht wahr," 
    extend " ....Jessica-chan?”"
    hide but
    show jes b22warai1 at leftedge
    with dis
    jes "“Ja,"
    extend " .....es ist, als wäre er nie weg gewesen,"
    extend " ....nur mit dem Unterschied, dass er sich heute zum ersten Mal auf dem Boot übergeben hat.”"
    geo a11komaru3 "“Ahahahahaha," 
    extend " ....ja,"
    extend " ....manche Dinge ändern sich, andere nie.”"
    show geo a11defo1 at m
    hide jes
    with quickergradientwiperight
    if persistent.george == False:
        $ persistent.george = True
        play sound "audio/sfx/umise_1060.ogg"
        show screen charupdate
    "Das ist mein Cousin George." 
    extend " er wird von Tante Eva und Onkel Hideyoshi zu einem echten Gentleman erzogen."
    "Er arbeitet sehr hart und will schon sein eigenes Unternehmen gründen, was ich sehr beeindruckend finde."
    "Er wird von den anderen Familienmitgliedern sehr geschätzt."
    extend " Außerdem ist er für sein Alter sehr reif und kennt sich gut aus."
    "Ushiromiya Joji..."
    extend " So spricht man ihn bei uns aus, und ich bin fest davon überzeugt,"
    extend " dass er heute einen Massenmord begehen wird."
    "Am liebsten würde ich auch diejenigen umbringen, die für diese schreckliche Namenstradition verantwortlich sind."
    hide geo
    show but b22warai1 at rightedge
    with quickergradientwiperight
    but "“....Ich finde, heute ist auch ein besonderer Tag,"
    extend " ...denn um die Mittagszeit soll ein Sturm aufziehen, der sich erst am Montag wieder legen soll."
    extend b11warai3 " Es ist das erste Mal, dass wir länger als einen Tag auf der Insel bleiben.”"
    show geo a11hohoemi1 at leftedge with quickergradientwiperight
    geo "“...Ja, aber wir haben auch immer ein wenig Glück gehabt, dass so ein starker Sturm nie über unsere Familienkonferenz hereingebrochen ist."
    extend " ...Wie heißt es so schön?" 
    extend " Es gibt immer ein erstes Mal.”"
    "Für Battler war die entspannte Atmosphäre eine sehr gute Ablenkung, um nicht mehr an das schaukelnde Boot denken zu müssen."
    extend " Es wäre ziemlich unvorteilhaft, wenn er die guten Sitze ruinieren würde."
    geo a11majime2 "“...ähm" 
    extend " .....Battler-kun?" 
    extend " Wusstest du, dass es so genannte Sturmgötter gibt?”"
    but b11aseru1 "“....Ähhhhm," 
    extend " ...meinst du Zeus...?”"
    geo a11warai1 "“Auch richtig, aber nein, " 
    extend " ....ich spreche vom Sturmgott in einem selbst.”"
    but b11oya1 "“.........." 
    extend " ...Was?”"
    geo "“Okay, es geht um folgendes:"
    geo "Es gibt die tantrische Spiritualität für intensivere Gefühle und auch bei den Griechen gab es die dionysische Spiritualität,"
    extend " die auch besonders heftige Gefühle beinhaltet." 
    extend " In diesem Sinne hat jeder Mensch Sturmgötter in sich."
    geo ".....Diese können in einem selbst aktiviert werden."
    extend a11majime2 " ....Solche Sturmgötter können aber auch zu schlimmen Taten, zu Verbrechen und Gewalt verleiten."
    geo "Man kann ihn aber auch dazu bringen, sich intensiv vorwärts zu bewegen und aus der Bequemlichkeit des Alltags auszubrechen.”"
    hide geo
    hide but
    show jes a11tereru1 at m
    with quickergradientwiperight
    jes "....Wahahahahahaha "
    extend "Was höre ich da, was laberst du da für einen Scheiß?"
    jes "Ich habe kein Wort verstanden...."
    extend a11atya3 " ...Ich wusste nicht mal, dass Wörter wie tantrisch oder dionysisch existieren."
    extend " Es klingt einfach unironisch, als hätte jemand einfach Wörter erfunden."
    hide jes
    show but b23nayamu1 at rightedge
    with quickergradientwiperight
    but ".............hmm"
    "Battler war ein auch wenig überwältigt von diesem Input, im Leben nicht hätte er jetzt einen Vortrag über Gefühle und Spiritualität erwartet."
    but "“.....Ähm,"
    extend " .....ähm,"
    extend " .......tantrisch," 
    extend " ......intensivere Gefühle," 
    extend " ........dionysische Spiritualität?"
    extend b23nayamu2 " ....Das hast du aus dieser einen Yoga-Zeitschrift von heute Morgen."
    show geo a11komaru1 at leftedge with quickergradientwiperight
    geo "“......Ähm,"
    extend a11komaru3 " ....oh,"
    extend " ....hahahaha," 
    extend " ....aber ich habe dich zum Nachdenken gebracht, nicht wahr?"
    geo a11hohoemi1 "Meine Mutter hat so eine Zeitschrift, und ab und zu schaue ich auch mal rein.”"
    but b11warai2 "“ ....Hihihi" 
    extend " ....Du hast nur Pech gehabt, dass ich vor der Abreise auf der Toilette so ein Yoga-Magazin in der Hand hatte, weil ich mich vergriffen habe.”"
    geo "“Was es manchmal für Zufälle gibt."
    geo a11defo1 ".....Eine kurze Erklärung für dionysisch wäre, dass es eine Spiritualität der Ekstaze, Musik und des Tanzes ist.”"
    but "“Mehr nicht?"
    extend " Klingt ja nicht sehr originell.”"
    geo "“Da kommt noch was und zwar....."
    extend a11komaru3 " uhmmmm na ja...."
    extend " hehe, wie soll ich sagen?"
    geo a23kkomaru5k "Es ist auch eine Spiritualität der...."
    extend " uhmm...."
    extend " ....Sexualität"
    geo " ....Es ist ein Begriff ursprünglich aus Indien, und wird mit 'Zusammenhang' oder auch 'Gefüge' übersetzt."
    extend " ....Berührungen des Körpers sollen also auch die Seele berühren, sie nähren."
    geo "Es ist ein sehr breites Thema...”"
    but b11ero1 "“Geil," 
    extend " .....das muss ich mal ausprobieren!"
    extend " ....Wenn ich für so eine 'Spiritualität' nur dieses Tantra Dings machen muss, bin ich dabei!"
    extend " ...Pralle Brüste von sexy Yoginis, ich kom...”"
    play sound "audio/sfx/umise_012.ogg"
    show but b11kuyasigaru1 with vpunch
    pause (.50)
    hide but b11kuyasigaru1 with quickgradientwipedown
    play sound "audio/sfx/umise_013.ogg"
    but "“.....Auauau, Jessica-chan..."
    extend " Das hat richtig weh getan!”"
    hide geo
    show jes a11ikari1 at leftedge
    with dis
    jes "“...Trottel!"
    extend " ....Du Holzkopf!"
    extend " ......War ja zu erwarten, dass das deine einzige Motivation ist, Trottel-Battler!”"
    "Kaum hatte Battler ausgesprochen, dass er sowas gerne 'ausprobieren' möchte, hatte er auch schon Jessicas Faust im Gesicht."
    "Jessica reagiert immer sehr allergisch darauf, wenn ihr perverser Cousin mit diesem Schweinkram anfängt."
    extend " Battler hat jetzt eine ziemlich rote Wange, als hätte er es auf eine heiße Herdplatte gelegt."
    jes a12ikari1 "“.....Perverser Battler!"
    extend " ...Du bist sofort Feuer und Flamme, sobald es auch nur im Entferntesten in diese Richtung geht!”"
    show but b23nayamu2 at rightedge with dis
    but "“.....Ihihihihi"
    extend " ......Tut mir leid”"
    "Von außen betrachtet sehen wir nicht anders aus, als zwei Blagen die sich zanken und sich gegenseitig Sachen an den Kopf werfen."
    extend " ....Was noch nicht mal das schlimmste Szenario ist, wenn man mal darüber nachdenkt, dass sich sogar die Erwachsenen ständig wie kleine Kinder in die Haare kriegen."
    show geo a11niramu1 at m with dis
    geo "“.....Hey!"
    extend " ....Beruhigt euch bitte!”"
    "George ist nicht sehr begeistert davon, dass Jessica und Battler diese lautstarke Außeinandersetzung haben,"
    extend " vorallem wenn das Thema eigentlich Ruhe und Gelassenheit vermitteln soll und geht prompt dazwischen."
    jes a11atya3 "“.........Ja, ist gut."
    extend " Aber dieses Spiritu-irgendwas klingt für mich so, als hätte jemand einen Vorwand gesucht mit einem anderen Menschen 'engen' Kontakt zu haben.”"
    geo a11warai1  "“....Ja," 
    extend " .....letztlich läuft alles darauf hinaus, dass man in gewisser Weise seine Lust wiederbelebt.”"
    jes a11tereru1 "“Wenn wir so darüber reden, klingt es absolut lächerlich."
    extend "....Wahahahahaha!”"
    geo a11hohoemi1 "“Ahahahaha...."
    extend " Ich denke da hast du Recht."
    hide geo
    hide but
    hide jes
    with quickergradientwiperight
    show geo a11defo1 at m with dis
    geo " Ach ja, wusstet ihr?"
    extend " ....Ein echter Sturmgott aus der griechischen Mythologie. ist jedoch Aigaion.”"
    show but b24futeki3 at leftedge with dis
    but "“....Ein leckerer Teller Gyros-Geschnetzeltes ist das einzige Griechische, das ich schätze."
    extend b24warai1 " ......Yumyumyumyum!”"
    geo a11hohoemi1_closed_mouth "“.........."
    extend a11warai1 " ...Jedenfalls kann dieser Gott Meeresstürme auslösen, ähnlich wie wir ihn heute erleben.”"
    but b11oya1 "“Du willst mir also sagen, dass irgendeine Gottheit, auf die wir keinen Einfluss haben, diesen Sturm ausgelöst hat?”"
    geo a11majime2 "“......Hmm"
    extend " ....So könnte man es ausdrücken ja!”"
    but b11warai3 "“....Auf jeden Fall können wir die Zeit, die uns Aigaion jetzt schenkt, nutzen, um wieder mehr Zeit miteinander zu verbringen.”"
    show jes b22warai1 at rightedge with dis
    jes "“Ja, das hast du wirklich nötig, Battler-kun!"
    extend " ...Es war ja auch dringend notwendig, dass du deine Familie für sechs Jahre verlässt."
    extend " *kicher*”"
    but b11odoroki3 "“.....Ach man”"
    "Es war Battler ein wenig unangenehm das wieder unter die Nase gerieben zu bekommen."
    extend " Es war damals eine sehr schwere Entscheidung die Familie zu verlassen."
    extend " Wer soll ihm das verübeln?"
    hide but
    hide geo
    hide jes
    show jes a11tohoho4 at m
    with quickergradientwiperight
    jes  "“Auf die Familienkonferenz freue ich mich am meisten."
    extend " ....Es ist die kurze Zeit, die meinen langweiligen Alltag auflockert.”"
    show but b11warai2 at rightedge with dis
    but "“Ja, ich bin auch froh, wieder bei euch zu sein, das hat mir in den sechs Jahren am meisten gefehlt.”"
    jes "“Ich finde es super toll, dass ihr dieses Wochenende da seid."
    extend " Es ist schrecklich, nur mit meinen Eltern und meinem Großvater auf der Insel zu leben."
    extend " ....Ich muss jeden Tag ziemlich früh aufstehen, weil meine Schule nicht wirklich in der Nähe ist, sondern außerhalb der Insel.”"
    stop music fadeout 2.0
    $ songname = "-"
    "Sofort scheint die gute Atmossphäre etwas zu kippen, da Jessicas Stimmung ebenfalls am kippen ist."
    jes b22komaru1 "“Nach der Schule muss ich sofort nach Hause, so dass ich keine Zeit mit meinen Freunden verbringen kann.”"
    "Jessicas Laune bricht immer weiter in sich zusammen, je mehr sie erzählt."
    " Sie holte etwas luft und fährt mit niedergeschlagener Miene fort."
    scene black with quickgradientwipedown
    play music "audio/bgm/umib_035_Intro.ogg"
    queue music "audio/bgm/umib_035_loop.ogg" loop 
    $ songname = "Worldend"
    if persistent.showbgm == True:
        show screen showsong
    jes "“Ich hasse einfach alles an dieser verfickten Insel..."
    extend " ...Ich habe nur noch Zeit, meine Hausaufgaben zu machen und in meinem Zimmer zu bleiben." 
    extend " ....Es gibt nichts zu tun."
    extend " ...Am liebsten würde ich diese scheiss Insel für immer verlassen und auf dem Festland ein neues Leben beginnen."
    jes "........"
    extend " .....Da ich keinen direkten Kontakt zu meinen Schulfreunden habe," 
    extend " ....fühle ich mich hier ziemlich einsam."
    "Man merkt sofort, dass es Jessica sehr nahe geht, nach der Schule von der Außenwelt abgeschnitten zu sein."
    extend " Auch George und Battler sind bedrückt, aber verständnisvoll, als sie Jessicas Worte über ihren Alltag auf der Insel hörten."
    scene schr_p1b at bgani
    show jes d11warai1 at m
    with quickergradientwiperight
    "Jessicas Situation ist etwas besonders, da sie im Gegensatz zu normalen Schülern auf einer Insel lebt."
    extend " ...Normalerweise würden solche Kinder in der Schule nicht sehr beliebt sein," 
    extend " da sowas schnell mal zu Neid und Missgunst führen kann."
    "Aber Jessica konnte mit ihrem Auftreten und ihren Charakter die meisten dieser Leute ruhig halten."
    extend " Sie konnte auch Freunde während ihrer Schulzeit finden mit denen sie eine tolle Schulzeit genießt."
    window hide
    camera at grayscale
    with gradientcirclefade
    window auto
    "Nur leider begrenzt sich diese Schöne Zeit alleine auf die Schule."
    extend " ...Zuhause auf Rokkenjima ist die Welt eine ganz andere."
    scene mjes_1cf at bgani,grayscale
    show jes a11tohoho4 at m,grayscale
    camera
    with gradientwiperight
    "Ihre Mutter ist sehr streng, sie erlaubt es nicht, dass sie sich amüsiert."
    extend " Sie will, dass ihre Tochter gute Noten schreibt und einen guten Abschluss erwirbt."
    "Dabei kann Jessica die Insel nur sehr selten außerschullisch verlassen."
    extend " Sie muss entweder lernen oder alleine die Zeit totschlagen, bis sie wieder zum Schulalltag zurückkehren darf."
    "Gott bewahre," 
    extend " ....wenn sie Jungs in ihrem Alter treffen will." 
    extend " ...Gott bewahre."
    extend " ....Die Überfürsorge einer Mutter ist das gruseligste was man in einem 'normalen' Haushalt finden kann."
    scene black with gradientcirclefade
    "Onkel Hideyoshi scheint die ganze Szene mitgehört zu haben und erhebt sich von seinem bequemen Platz."
    extend " Er nähert sich langsam der in Tränen versunkenen Jessica und spricht ruhig und sanft zu ihr."
    scene ship_s3a at bgani
    show expression(CustomParticles("images/system/particle.png", 10))
    show hid a21warai1 at l
    with quickergradientwiperight
    hid "“Na, na Jessica-chan,"
    extend " ....du musst es positiv sehen!"
    extend " Eines Tages wirst du die Insel wirklich verlassen und dein eigenes Leben führen können.”"
    show jes b33naku1 at r with dis
    jes "“Aber wie lange noch?" 
    extend " .....Was wäre wenn meine Schulfreunde bis dahin nichts mehr mit mir zu tun haben wollen?”"
    "Jessicas Stimme, hatte eine tiefe trauer in sich, in diesem Moment scheint alles aus ihr heraus zu kommen."
    hid a11odayaka1 "“Auch deine Schulfreunde werden deine Situation verstehen, eines Tages wirst du zu ihnen gehen können und ab da viel Zeit mit ihnen verbringen."
    extend " Bis dahin solltest du immer dein Bestes geben, denn das wird sich am Ende des Tages definitiv auszahlen!”"
    jes a11naku3 "“.......Eines Tages?"
    extend " Aber ich warte schon so viele Jahre.....”"
    hid a21warai1 "“...Du hast dein ganzes Leben noch vor dir, glaub mir." 
    extend " Deine Zeit als Teenager auf der Insel wird später nur noch eine Erinnerung sein."
    extend " Es ist auch okay mal traurig zu sein, denn Weinen ist die aufrichtigste Emotion die es gibt."
    hid a21warai2 " Jetzt habe ich mich aber verquatscht," 
    extend " ....wahahahahaha!"
    hid "Aber lass den Kopf nicht hängen und häng dich weiter rein, ja?”"
    jes a11tereru1 "“Danke Hideyoshi, ich werde es mir zu Herzen nehmen."
    extend " ...Ich fühle mich schon besser.”"
    hid "“So ist's gut, du schaffst es!, wahahahaha”"
    if persistent.hideyoshi == False:
        $ persistent.hideyoshi = True
        play sound "audio/sfx/umise_1060.ogg"
        show screen charupdate
    hide jes
    show hid a11defo1 at m
    with quickergradientwiperight
    "Das ist Georges Vater und mein Onkel Hideyoshi." 
    extend " Er ist ein netter und sympathischer Mann und ich glaube, ich mag ihn von allen Erwachsenen am meisten."
    "Er ist der Ehemann von Tante Eva und hat seine Firma von Grund auf neu aufgebaut."
    extend " Desweiteren ist er als Präsident einer mittelgroßen Restaurantkette tätig. Die Kette scheint zu wachsen und sehr gut zu laufen."
    "Sein Name wird Ushiromiya Hideyoshi ausgesprochen, wie Kyrie ist sein Name absolut perfekt!"
    extend " Das liegt daran, dass er als Japaner in die Familie eingeheiratet hat. ..... Ich beneide jeden, der einen normalen Namen hat."
    hide hid
    show geo a11hohoemi1 at r
    with quickergradientwiperight
    geo "“Jessica-chan, allein ein Ziel zu haben, auf das man hinarbeiten kann, ist etwas, das einen jeden Tag motivieren sollte, nicht aufzugeben."
    geo "Auch ich oder Battler-kun haben unsere Sorgen und Probleme, die wir überall mit hinnehmen. Also halte noch ein bisschen durch, okay?”"
    show jes a11tohoho4 at l with dis
    jes "“Ja vielen Dank, das hilft mir wirklich sehr, danke!”"
    "Die Worte von Hideyoshi und George haben Jessica sehr gut aufgemuntert."
    extend " Man sieht deutlich, wie Jessica wieder ein wenig lächelt."
    stop music fadeout 2.0
    $ songname = "-"
    scene black with quickergradientwiperight
    "Ich saß zuhörend in unmittelbarer Nähe zur Szenerie und hab nicht darauf geachtet was in meiner Umgebung passiert."
    extend " ...Diesen Moment in der ich meine Deckung links liegen ließ, hat Tante Eva benutzt um sich an mich heranzuschleichen und mir etwas ins Ohr zu flüstern."
    $ songname = "Praise"
    play music "audio/bgm/umib_021_Intro.ogg"
    queue music "audio/bgm/umib_021_loop.ogg" loop 
    if persistent.showbgm == True:
        show screen showsong
    eva "“Wusstest du, dass deine Seekrankheit auch noch nach der Reise anhalten kann?”"
    "Battler hat sich wie erwartet erschrocken und springt auf, als hätte ihm eine Biene in den Hintern gestochen."
    scene ship_s3a at bgani
    play sound "audio/sfx/umise_047.ogg"
    show but b11kuyasigaru1 at m,jumping
    with vpunch
    but "......Wuahhhh....." 
    extend " ...Was soll das?"
    extend " .....Bitte schleich dich nie wieder an mich ran, Tante Eva!”"
    show eva b22akire2 at r with dis
    eva "“Oh... Entschuldige," 
    extend " ...ich wollte dir nur sagen, dass, wenn sich dein Körper an die Bewegungen des Bootes gewöhnt hat, er sich an Land wieder umgewöhnen muss."
    show eva b21akire1go at rightedge with dis
    eva "Aber mach dir darüber bloß keinen Kopf. Battler-kun, so etwas passiert nicht unbedingt." 
    extend " *kicher*”"
    if persistent.eva == False:
        $ persistent.eva = True
        play sound "audio/sfx/umise_1060.ogg"
        show screen charupdate
    hide but
    show eva b25defo1 at m
    with quickergradientwiperight
    "Das ist meine Tante Eva, die Mutter von George und die Ehefrau von Onkel Hideyoshi." 
    extend " Sie und der alte Bastard Dad sind so etwas wie ein Spaßvogel-Duo."
    extend " ...Wenn die beiden richtig loslegen, bleibt kein Stein auf dem anderen."
    extend " Als wir Kinder waren, war sie zu uns immer lieb und vorallem witzig."
    "Sie beherrscht auch einige chinesische Kampfsporttechniken." 
    extend " Einer ihrer Roundhousekicks soll einmal bei einem Trainingskampf getroffen haben, und ihr Gegner wurde kaltgestellt wie ein Softdrink."
    "Auf keinen Fall möchte ich von ihr einen Tritt unter die Dachlatte abbekommen...."
    extend " Ach ja!" 
    extend " Fast hätte ich ihren seltsamen Namen vergessen...." 
    extend " ....Sie wird Ushiromiya Äba ausgesprochen." 
    "mit Ä und b....."
    extend " ....Wann hört das endlich auf?"
    show but b11aseru1 at leftedge
    hide eva
    with quickergradientwiperight
    but "“.....Nein," 
    extend " du verarschst mich Tante Eva....”"
    show eva b22akire2 at r with dis
    eva "“Oh nein..." 
    extend " .....Das würde ich nie tun..." 
    extend " *kicher*"
    eva a11hohoemi1 "....Ich wollte dir nur etwas über Seekrankheiten erzählen," 
    extend " mehr nicht," 
    extend " *kicher*”"
    "Tante Eva wollte mich wahrscheinlich nicht erschrecken,"
    extend " sondern meinen Kopf auf die Probe stellen, denn wenn ich an ihre Worte denke, sobald ich an Land bin,"
    extend " dann wird mir bestimmt wieder schlecht," 
    extend " ......ganz schön raffiniert."
    "Während wir uns fröhlich über Seekrankheiten unterhalten, kommt Kyrie runter um uns zu sagen, dass wir gleich anlegen werden."
    hide but
    hide eva
    show kir a11defo1 at m
    with quickgradientwiperight
    kir "“Wir sind jetzt gleich da!" 
    extend " .....Die Insel ist ganz nah!”"
    hide kir
    show but a11defo1 at m
    with quickergradientwiperight
    but "“....Wir werden sehen, ob du Recht hast Tante Eva...”"
    show eva b22akire2 at leftedge with dis
    eva "“*kicher*"
    extend " Forder es besser nicht heraus.... Battler-kun....”"
    show hid a21warai1 at rightedge with dis
    hid "“Wahahahahaha!" 
    extend " ....Ihr zwei seid mir ja welche." 
    extend a11defo1 " ...Lasst uns lieber an Deck gehen, wir gehen gleich an Land!”"
    hide eva
    show jes a11warai1 at leftedge
    with dis
    jes "“Ja, das ist eine gute Idee!"
    extend " ...So langsam bekomme ich keine Luft mehr und das liegt nicht an meinem Asthma!"
    "Jessica leidet an Asthma, dass bedeutet bei ihr sind die Atemwege verengt und sie wird manchmal von derartigen Anfällen heimgesucht."
    "So erhoben sich alle von ihren Plätzen und bemerkten beim rausgehen, dass sich draußen die Wolken unerwartet und viel zu früh verdunkelt hatten."
    stop music
    $ songname = "-"
    play wind "audio/sfx/umilse_005.ogg"
    play ship "audio/sfx/umilse_004.ogg"
    scene sky_1c 
    with gradientwipeup
    "So wie der Himmel, hat sich auch die Gesamtatmosphäre auf dem Boot verfinstert."
    extend " Der Wind hat ordentlich an Stärke zugenommen und es sieht nach starken Regen aus."
    "Dabei kommt der angekündigte Taifun früher als berichtet."
    extend " Normalerweise sollte der Taifun um die Mittagszeit herum anfangen."
    scene ship_s2b 
    camera at boatswing,slowerboat
    show kir a11majime1 at r
    with gradientwipedown
    kir "“War der Taifun nicht für heute Mittag angekündigt?"
    extend " Vielleicht fängt es gleich an zu regnen.”"
    "Kyrie hat sofort bemerkt, dass etwas nicht stimmt."
    extend " Der Himmel hat sich in der Zwischenzeit bereits verdunkelt,"
    extend " was zu diesem Zeitpunkt noch gar nicht hätte passieren dürfen."
    show rud a13odoroki1 at l with dis
    rud "“In etwa 10 Minuten sind wir da, aber gemütlich wird es nicht mehr.”"
    kir a13majime1 "“Stimmt..." 
    extend " Der Wind hat auch schon stark zugenommen.”"
    "Der Wind, der von Minute zu Minute stärker über das Meer peitscht,"
    extend " ist kein Wind, wie ihn die meisten Menschen vom Festland kennen."
    "Der Wind kann ungehindert und mit voller Kraft über das Wasser fegen,"
    extend " während es auf dem Land immer Häuser, Berge und Gelände gibt, die den Wind abschwächen können."
    kir "“Dass die Wettervorhersage sich mal irrt?”"
    rud a13warai1 "“Ich habe einmal ein Geschäftsessen wegen eines angeblichen Taifuns abgesagt...."
    extend " Der Taifun kam erst 2 Tage später, ich habe mich noch nie so dumm gefühlt wie in dieser Situation.”"
    kir a13warai2 "“Das war sicher eine Erfahrung, so etwas am Ende erklären zu müssen..."
    extend " *kicher*”"
    rud "“Bitte erinnere mich nicht daran....”"
    "Nicht nur Rudolf und Kyrie sind beunruhigt," 
    extend " auch alle anderen sind überrascht,"
    extend " dass der Sturm einige Stunden zu früh kommt. Dabei hatte der Wetterbericht garantiert, dass es erst um die Mittagszeit losgehen würde."
    "Die Folgen könnten turbulente Flüge sein, die noch eine Starterlaubnis für Kurzflüge haben."
    "Inzwischen hat sich Maria ganz vorne auf der Brücke niedergelassen, und ihr Blick schweift nicht mehr von einer ganz bestimmten Klippe ab."
    scene black
    camera 
    with quickergradientwiperight
    scene ship_s2b 
    camera at boatswing,slowerboat
    hide rud
    hide kir  
    show mar a11defo1 at m
    with quickergradientwiperight
    mar "“..........Uu~"
    mar a11defo1_mouth_closed "......................."
    mar a11defo1 ".............Es ist weg"
    extend " ......................Uu~"
    extend " ......Uu~"
    extend " ........nicht mehr da”"
    $ songname = "Stupefaction"
    play music "audio/bgm/umib_020_Intro.ogg"
    queue music "audio/bgm/umib_020_loop.ogg" loop 
    if persistent.showbgm == True:
        show screen showsong
    show but b11warai2 at rightedge with dis
    but "“hmm?" 
    extend " .....Was ist los Maria?"
    extend " ...Wo drückt der Schuh?”"
    show jes a11atya3 at l with dis
    jes "“Etwas scheint sie sehr zu beunruhigen...”"
    mar a22sakebu1 "“Es ist weg!" 
    extend " .....Es ist weg!" 
    extend " ....Uu!"
    extend " ...Es ist weg!" 
    extend " ...Uu~...!"
    mar "Es war immer da, aber jetzt ist es weg!..." 
    extend " Uu!..”"
    "Maria fängt sich buchstäblich an in Rage zu reden nur Jessica scheint eine Idee zu haben, was Maria meinen könnte."
    jes a11majime1 "“Stimmt ja..." 
    extend " Der Schrein fehlt, er war letztes Jahr noch da...."
    jes "Es sieht auch so aus, als wäre ein Teil des Riffs mitgerissen worden....”"
    hide jes
    hide but
    hide mar
    show kum a12defo2 at m
    with quickergradientwiperight
    kum "“Ohohohoh," 
    extend " ...der Schrein wurde während eines Gewitters letztens von einem gewaltigen Blitz getroffen und zerstört.”"
    if persistent.kumasawa == False:
        $ persistent.kumasawa = True
        play sound "audio/sfx/umise_1060.ogg"
        show screen charupdate
    "Die ältere Frau heißt Kumasawa Chiyo." 
    extend " Sie ist eine Teilzeitarbeiterin, die zwar mehrmals gekündigt hat, aber insgesamt schon viele Jahre im Dienst der Familie steht."
    "Sie ist geschickt und mehr als fähig, ihre Aufgaben zu erfüllen,"
    extend " aber wegen ihrer Geschwätzigkeit und ihrer Vorliebe für Gerüchte ist sie als Angestellte nicht sehr beliebt."
    "Ihr Name auf Japanisch?" 
    extend " ...Auch bei uns Kumasawa, ihre Eltern haben ihr einen vernünftigen Namen gegeben" 
    extend " ....*seufz*"
    hide kum  
    show jes a11atya3 at m
    with quickergradientwiperight
    jes "“Ein Blitzeinschlag?..."
    extend " Ein Blitz kann so gewaltig sein?”"
    show kum a12majime1 at r with dis
    kum "“Die Fischer sagen, es sei ein Zeichen von Unglück....”"
    show mar a11defo1 at l with dis
    mar "“Ein Zeichen von Unglück....Uu~..."
    extend a11defo1_mouth_closed " ...........................”"
    scene black
    camera 
    with quickgradientwipedown
    "Kumasawas Worte haben die ohnehin schon düstere Atmosphäre auf dem Schiff in ein noch beklemmenderes Gefühl verwandelt."
    extend " Maria hat ihren Blick noch immer nicht von der Stelle abgewandt, an der der Schrein stehen sollte."
    stop wind fadeout 5
    stop ship fadeout 5
    extend " Und es scheint, als würde in genau diesem Moment der heftige Wind für einen Moment nachlassen."
    scene ship_s2b 
    camera at boatswing,slowerboat
    show mar a22defo1k
    with gradientwipeup
    pause 2
    mar "“Unglück..."
    extend " ....Unglück...Unglück...”"
    but ".....Was hast du gesagt, Maria?"
    play sound "audio/sfx/umise_021.ogg"
    mar "“....Unglück Unglück Unglück Unglück Unglück Unglück Unglück"
    extend " ....Unglück Unglück Unglück Unglück Unglück Unglück"
    extend " .....Unglück Unglück Unglück Unglück Unglück Unglück”"
    "Maria fängt plötzlich an lautstark das Wort 'Unglück' sehr oft zu wiederholen,"
    extend " was das unheimliche Gefühl bei den Anwesenden nur noch verstärkt."
    geo "“Kumasawa-san bitte gehen Sie mit ihren Witzen etwas vorsichtiger um!"
    extend " Maria-chan nimmt sowas ziemlich ernst, verstehen Sie?”"
    mar "“Unglück Unglück Unglück”"
    show but b11odoroki3 at leftedge with dis
    but "“Hey Maria!"
    extend " Wenn du so oft 'Unglück' sagst, wird es wirklich ein Unglück geben," 
    extend " also beruhige dich, ja?”"
    show geo a11majime2 at rightedge with dissolve
    geo "“Maria-chan, es wird nichts schlimmes passieren."
    extend " ....Also beruhigen wir uns wieder und warten bis wir gleich anlegen, okay?”"
    mar "“............Uu~"
    "Alle versuchen die Situation zu entschärfen, um das Thema irgendwie abzuschließen."
    extend " Aber Maria wendet den Blick vom Riff ab, dreht sich um, hebt den rechten Arm zum Himmel und öffnet langsam den Mund..."
    mar a11defo1 "“Es geschieht definitiv....."
    extend " .....Ein Unglück wird geschehen!......”"
    play sound "audio/sfx/umise_027.ogg"
    scene ship_s2b
    call rainlayer from _call_rainlayer_8
    camera at boatswing,slowerboat
    play rain "audio/sfx/umilse_012.ogg"
    play wind "audio/sfx/umilse_005.ogg"
    play ship "audio/sfx/umilse_004.ogg"
    show but b22odoroki2 behind rain at leftedge
    show geo a11komaru1 behind rain at rightedge
    show mar a11defo1 behind rain at m
    with quickflash 
    "Mit diesen Worten, als hätte Maria gerade den Befehl dazu gegeben, hörte man es donnern und sofort begann es zu regnen."
    extend " ....Nicht nur Battler lief deswegen ein kalter Schauer über den Rücken."
    but "“.......Was?"
    extend " .......Hä?”"
    "Alle haben in diesem Moment ein mulmiges Gefühl."
    extend " Es ist fast so, als ob Maria ahnt, dass dieses Familientreffen etwas ganz Besonderes sein würde."
    extend " Doch Battler scheint als einziger zu erkennen, dass mit Marias erhobener Arm und das 'Unglück' wohl nur das Wetter gemeint sein muss."
    hide but  
    hide mar  
    hide geo  
    show but b11warai3 behind rain at m
    with quickergradientwiperight
    but "“Du hast also gemerkt, dass es ein schlimmes Unwetter wird?”"
    show mar a11defo1 behind rain at rightedge with dis
    mar "“..........Uu~”"
    but "“Die Wettervorhersage sagt, dass der Taifun erst gegen Mittag kommen wird. Aber er ist schon da."
    extend b11warai2 " ....Das nenne ich wirklich ein Unglück...."
    extend " ...hihihihi"
    but "Maria, ich bin sicher, dass dieser Taifun schneller vorbei ist, als du bis zehn zählen kannst. Alles wird gut.”"
    "Battler versucht Maria zu beruhigen, dass sie keine Angst vor dem Taifun haben muss, aber Marias Gesichtsausdruck spricht eine ganz andere Sprache."
    play sound "audio/sfx/umise_011.ogg"
    show mar a22sakebu1 behind rain at rightedge,jumping
    show but b11aseru1 behind rain at m
    with vpunch
    mar "“Uu~!!"
    extend " Uu~!!Uu~!!Uu~!!Uu~!!Uu~!!Uu~!!"
    extend " Ein Unglück wird geschehen! Uu~!!”"
    "Wütend stampft Maria gefolgt von lauten 'Uus' da ihr anscheinend keiner zuhören möchte."
    hide but  
    hide mar  
    show jes a11majime1 behind rain at m
    with quickergradientwiperight
    jes "“Maria, warum sagst du sowas?”"
    show kum a12majime1 behind rain at l with dis
    kum "“Es ist klar, dass sie etwas im Blick hat, das im Alter schnell verloren geht."
    extend " Sehr junge Menschen haben einen Sinn für das Übernatürliche..."
    extend " Aber dieses Gefühl wird schwächer, je älter man wird."
    kum "Was Maria fühlen kann, kann nur sie fühlen, weil sie die Jüngste hier ist.”"
    show but b22odoroki2 behind rain at rightedge with dis
    "Battler erstarrt bei diesen Worten, ist das wirklich möglich? denkt er, das kann es doch gar nicht geben..."
    extend " Viel mehr ist es so, dass das seltsame Verhalten von Maria und die angespannte Atmospähre ihm diese Erklärung für einen kurzen Moment logisch vorkommen lässt."
    kum "“Es scheint so, dass in der Vergangenheit von Rokkenjima eine Hexe....”"
    jes "“Es reicht, Kumasawa! Darüber reden wir nicht!”"
    kum a12defo2 "“Ohohohoh," 
    extend " ich muss mich entschuldigen, ich wollte nicht unhöflich sein.”"
    "Kumasawas Geschichten sind im Moment eher ungünstig, denn es geht darum, Maria zu beruhigen und nicht darum, ihr noch mehr Dinge in den Kopf zu setzen."
    extend " Jessica hat richtig gehandelt, in dem sie Kumasawa unterbrochen hat."
    "Plötzlich konnte Hideyoshi gehört werden, der eine Kiste in der Hand hält."
    scene black
    camera 
    with quickergradientwiperight
    scene ship_s2b
    call rainlayer from _call_rainlayer_9
    camera at boatswing,slowerboat
    show hid a21warai1 behind rain at m
    with quickergradientwiperight
    hid "Huuhuu!"
    extend " ....Wir haben Regenschirme an Bord, also habe ich sie hergebracht!"
    "Jeder außer Maria nahm sich einen Regenschirm um nicht weiter nass zu werden."
    extend " Battler ist so lieb und hält seinen Schirm über Marias kopf."
    "In der Ferne konnte man Rudolf sehen, der sehr nachdenklich zu sein scheint."
    scene black
    camera 
    with quickergradientwiperight
    scene ship_s2ab
    camera at boatswing,slowerboat
    call rainlayer from _call_rainlayer_10
    show rud a11defo2 behind rain at m
    with quickergradientwiperight
    rud "“*seufz*”"
    "Rudolf stieß einen tiefen Seufzer aus, während er sich eine Zigarette anzündete, weil ihn etwas sehr beschäftigte, und niemand außer Eva schien diesen Seufzer gehört zu haben."
    show eva a11hohoemi1 behind rain at rightedge with dis
    eva "“Was ist los Rudolf?" 
    extend " ....irgendwelche Sorgen wegen heute Abend?"
    extend " ...Wir müssen uns nur genau an das halten, was wir besprochen haben, dann können wir gegen Krauss gewinnen.”"
    rud a11defo1 "“....Ja, es liegt nicht am Plan." 
    extend " Aber wenn unsere Vermutung falsch ist?...."
    extend " Wir würden wegen Hochverrats an der Ushiromiya Familie von den Klippen geworfen werden."
    if persistent.tip3 == False:
        $ persistent.tip3 = True
        play sound "audio/sfx/umise_1060.ogg"
        show screen tipupdate
    rud a13odoroki1 "Das wäre das absolute Ende meines Lebens und auch deines, {note_green}Aneki{/note_green}."
    extend " Damit würden wir unser Ziel um rund eine Quadrillion Kilometer verfehlen.”"
    "Rudolf sieht sehr angespannt aus und zieht stark an seiner Zigarette, während Eva versucht, sich ein leichtes Lächeln zu bewahren..."
    extend " Aber auch ihr ist anzumerken, dass sie so kurz vor der Familienkonferenz, bei der es um das Erbe des Familienoberhauptes geht, ein wenig weiche Knie bekommt."
    eva b21akire1go "“Keine Sorge..." 
    extend " Rudolf..." 
    extend " ....Es ist ein sehr hoher Einsatz, aber ein Treffer wird mit Vaters Erbe belohnt."
    eva "Außerdem denke ich, dass das Erbe, das man hier erhalten kann, das Risiko definitiv wert ist."
    extend b21futeki1 " Ich lasse nicht zu, dass mein hinterhältiger Bruder das ganze Erbe für sich behält!”"
    rud a13komaru1 "“Das klingt logisch... Solange du dich an die Aufteilung hältst und im Ernstfall Rede und Antwort stehst, bin ich dabei."
    extend " Trotzdem ist das so als würde ich mein ganzes Leben drauf verwetten," 
    extend " dass eine unbedeutende Fußball-Mannschaft aus Portugal dieses Jahr den Europäischen Pokal gewinnt.”"
    eva a11hohoemi1 "Wirklich jetzt?" 
    extend " Fußball?" 
    extend " Damit kenne ich mich nicht aus."
    rud "Was ich sagen kann, ist dass die Quoten schlecht für uns stehen, aber ein Treffer würde die Situation verändern."
    eva "“Risikobereitschaft kann großzügig belohnt werden und im besten Fall mit Vaters Erbe..”"
    rud "“Ich hoffe einfach auf das beste...”"
    "Sagte er, nimmt einen großen Zug von seiner Zigarre und bläst den feinen weißen Rauch wieder in die Luft."
    "Genau in diesem Moment ertönte die Stimme von Shannon, einer Bediensteten, die heute zusammen mit Chefkoch Gohda die Familienmitglieder abholen sollte."
    extend " Das Boot hat nämlich bereits die Anlegestelle auf Rokkenjima erreicht."
    scene black
    camera 
    with quickergradientwiperight
    stop ship fadeout 3
    stop music fadeout 3
    scene ship_s1ab
    call rainlayer from _call_rainlayer_11
    show sha a11defo1 behind rain at m
    with quickergradientwiperight
    sha "“Entschuldigung, liebe Gäste," 
    extend " das Schiff legt gleich an!"
    extend " ...Ich bitte um Vorsicht beim Überqueren der Planke, danke!”"
    $ songname = "Towering cloud in summer"
    play music "audio/bgm/umib_011_Intro.ogg"
    queue music "audio/bgm/umib_011_loop.ogg" loop 
    if persistent.showbgm == True:
        show screen showsong
    show geo a12warai1 behind rain at l with dis
    geo "“Das hast du gut gesagt, Shannon-chan."
    extend " Genau wie ich es von dir erwartet habe.”"
    show sha a11hajirai2 behind rain at r with dis
    sha "“George-sama...." 
    extend " D-"
    extend "Das ist zu viel des Lobes..."
    extend " ....I-"
    extend "Ich bin nur das Mobiliar der Familie, es ist meine Pflicht euch anständig zu empfangen.”"
    "Shannon errötete, als sie diese Worte von George hörte."
    extend " Dann fuhr George fort, sich mit ihr in einem angenehmen und ruhigen Ton zu unterhalten."
    geo a11hohoemi1 "“Shannon-chan..." 
    extend " Du weißt selbst nicht, was für eine tolle Bedienstete du bist, du kannst dich auch mal mehr etwas selber loben."
    extend " Und wenn ich schon dabei bin, du bist auf keinen Fall so etwas wie Mobiliar," 
    extend " du bist ein Mensch."
    geo "Ich will so etwas nicht mehr hören, ist das klar?”"
    sha a12hajirai3 "“G-"
    extend "George-sama......”"
    scene black
    camera 
    with quickergradientwiperight
    scene ship_s1ab
    call rainlayer from _call_rainlayer_12
    show sha a11defo1 behind rain at m
    with quickergradientwiperight
    if persistent.shannon == False:
        $ persistent.shannon = True
        play sound "audio/sfx/umise_1060.ogg"
        show screen charupdate
    "Diese junge Bedienstete heißt Shannon."
    extend " Sie ist zwar eine junge, aber sehr erfahrene Bedienstete."
    "Normalerweise ist sie ruhig und erledigt ihre Arbeit effizient, aber wenn sie nervös wird, macht sie Fehler."
    extend " Da sie kein Familienmitglied ist, ist ihr Name völlig in Ordnung und nicht seltsam."
    "Ich habe sie seit 6 Jahren nicht mehr gesehen und sie ist noch schöner als in meiner Erinnerung."
    scene black
    camera 
    with quickergradientwiperight
    scene ship_s1ab
    call rainlayer from _call_rainlayer_13
    show but b11warai2 behind rain at m
    with quickergradientwiperight
    but "“Sag mal Jessica-chan," 
    extend " ...kann es sein, dass die beiden sich ein bisschen nahe stehen?”"
    show jes a11tereru2 behind rain at rightedge with dis
    jes "“.....wahahahaha" 
    extend " .....wahahahaha," 
    extend " das hast du so schnell kapiert?”"
    but "“Also sind sie wirklich ein Paar?”"
    jes "“Ich weiß es nicht genau," 
    extend " ...aber ich habe den Eindruck, dass George wirklich etwas für sie empfindet.”"
    but b11aseru1 "“Wenn ich ganz ehrlich bin," 
    extend " ....glaube ich, dass ich auch ein bisschen in sie verliebt war."
    but "Ich war damals auch in so einer Phase, wo ich immer so komische Sachen mit ihr geredet habe....."
    extend " Sowas wie" 
    extend " <see you again>" 
    extend " ....oder total schnulziges Zeug wie...." 
    extend " ....Ich komme auf....." 
    extend " ....einem weißen Pferd geritten oder so.”"
    jes a11tereru1 "“wahahahahahaha!!" 
    extend " <see you again?>"
    extend " ....Du hattest wirklich einen Vogel!" 
    extend "...Ich bin mir ziemlich sicher, dass Shannon das heute sehr peinlich finden würde.”"
    but b11nayamu2 "“Das glaube ich auch," 
    extend " ....das ist mir selber maximal peinlich, also bitte behalte das für dich, okay?"
    extend " Ich bin absolut tot, wenn sie sich auch noch an dieses peinliche Zeug erinnert.”"
    jes a11aisowarai1 "“Ja, das geht klar! Ich schweige wie ein Grab!”"
    "Während alle fröhlich miteinander plauderten, hat das Boot erfolgreich angelegt und alle beginnen, das Boot nach und nach zu verlassen,"
    "Auf der anderen Seite wartet schon der Koch Gohda, um die Familie zu empfangen."
    scene black
    camera 
    with quickergradientwiperight
    scene ship_s1ab
    call rainlayer from _call_rainlayer_14
    show goh a11defo1 behind rain at m
    with quickergradientwiperight
    goh "“Meine Damen und Herren, herzlich willkommen auf der Insel Rokkenjima!”"
    extend " ...Auch wenn uns dieses Wochenende ein schlimmer Taifun erwartet..." 
    extend " ...Ich" 
    extend " ....Gohda, werde euch immer erstklassiges Essen zubereiten!”"
    goh "Wenn Sie nun so freundlich wären, mir Ihr Gepäck zu überlassen."
    extend " Wir müssen uns sputen und schnell das Gästehaus erreichen."
    "Ein freundlicher Bediensteter der Familie nimmt die angereisten Verwandten in Empfang, um sie und ihr Gepäck in das Gästehaus zu bringen."
    show jes a11defo2 behind rain at l with dis
    jes "“Vielen Dank, Gohda-san, ich glaube, die meisten von uns kommen jedes Jahr hierher, nur um deine leckeren Gerichte zu essen.”"
    goh a11hohoemi1 "“Mit solchen Worten macht das Kochen gleich viel mehr Spaß!"
    goh "Ich muss allerdings sagen, dass wir euch schon 20 Minuten früher erwartet haben, das ist nicht gut für unseren Zeitplan....."
    goh "Außerdem scheint sich dieser Taifun schon früher als angekündigt zu formieren, so dass wir uns nun schnell auf den Weg machen sollten.”"
    scene black
    camera 
    with quickergradientwiperight
    scene ship_s1ab
    call rainlayer from _call_rainlayer_15
    show goh a11defo1 behind rain at m
    with quickergradientwiperight
    if persistent.gohda == False:
        $ persistent.gohda = True
        play sound "audio/sfx/umise_1060.ogg"
        show screen charupdate
    "Gohda ist ein Bediensteter, der bei der Familie als Koch angestellt ist."
    extend " Er ist noch nicht lange bei der Familie, aber durch seine früheren Tätigkeiten und Erfahrungen hat er ein Talent dafür entwickelt, Gäste zu bewirten."
    "Aus diesem Grund wird er als Bediensteter sehr geschätzt. Da er nicht zur Familie gehört, hat er auch nicht wie Shannon einen unserer seltsamen Namen."
    scene black
    camera 
    with quickergradientwiperight
    scene ship_s1ab
    call rainlayer from _call_rainlayer_16
    show kum a12defo2 behind rain at m
    with quickergradientwiperight
    kum "“Aber vergiss nicht, dass es heute zum Mittagessen meine speziellen Spaghetti mit würziger Makrelenrahmsauce nach meinem Geheimrezept gibt, Gohda!" 
    extend " ....Ohohohohoh!"
    kum "Man muss sie einfach probieren..." 
    extend " ....Es gibt nichts Besseres als frische, saftige Makrelen." 
    extend " ....Ohohohoh!”"
    show jes a11atya3 behind rain at r with dis
    jes "“.....Ich denke, ich passe....”"
    kum a11defo2 "“Aber Jessica-sama, Ihr könnt euch doch nicht die ganze Zeit von Junkfood ernähren!"
    extend " Gebt der Makrele eine Chance!”"
    jes "“Aber...." 
    extend a11warai1 " Ich habe heute Morgen in der Küche keine Makrelen gesehen, Kumasawa...."
    extend " ...Deshalb kann es heute leider keine Makrele geben!”"
    kum a12defo2 "“Ohohohoh," 
    extend " ....Ihr habt mich erwischt, Jessica-sama.”"
    scene black
    camera 
    with quickergradientwiperight
    scene beach_1ab
    call rainlayer from _call_rainlayer_17
    show rud a11akuwarai2 behind rain at r
    with quickergradientwiperight
    rud "“Hey Battler-kun!" 
    extend " ...Wenn dir immer noch schwindelig ist und du dich gleich auf den Esstisch übergibst," 
    extend " ....kannst du nach Hause schwimmen.”"
    show but a11niramu3 behind rain at l with dis
    but "“....Lass es gut sein!" 
    extend " Es geht mir schon besser."
    extend " Danke der Nachfrage," 
    extend " ....Dad.”"
    rud "“Naaa," 
    extend " ....das hoffe ich doch!"
    extend a11defo2 " ...Ich will mich nicht vor den anderen rechtfertigen müssen, warum du Holzkopf den Esstisch ruiniert hast.”"
    but "“Keine Sorge, Dad," 
    extend a11aseru1 " ....dein schicker Anzug passt mir auch, wenn's hart auf hart kommt...." 
    extend " ...ihihihi"
    but a11niramu3 "........ahh" 
    play sound "audio/sfx/umise_003.ogg"
    show but a11niramu3 behind rain at l,run
    hide but with dissolve
    extend " .......*würg*"
    "Battler versuchte sein Schwindelgefühl herunterzuspielen, verlor aber gegen die Übelkeit und erbrach in den nächsten Busch."
    hide rud  
    show eva b22akire2 behind rain at m
    with quickergradientwiperight
    eva "“....Meine Güte, Battler-kun....." 
    extend " ....*kicher*"
    extend a11hohoemi1 " ......Wir haben doch vorhin schon einmal darüber gesprochen, oder etwa nicht?" 
    extend " *kicher*kicher*"
    extend " .....Du wolltest deiner Tante ja nicht glauben”"
    "Tante Evas fettes Grinsen war nicht zu übersehen..." 
    extend " ...Sie hatte mich mit einem einfachen psychologischen Trick ausgetrickst."
    extend " Indem ich die ganze Zeit darauf achtete, nicht auf meine Übelkeit zu achten, provozierte ich es im Grunde selbst."
    scene black
    camera 
    with quickergradientwiperight
    scene beach_1ab
    call rainlayer from _call_rainlayer_18
    show goh a11komaru1 behind rain at m
    with quickergradientwiperight
    goh "“Liebe Gäste, wir haben Verspätung und der Sturm wird immer stärker!" 
    extend " ...Wir müssen sofort ins Gästehaus!"
    "Plötzlich platzt Gohda in unsere Gespräche und tickt mehrmals mit dem Zeigefinger in kurzen Abständen auf seine Armbanduhr."
    goh "Wir müssen uns beeilen, wir haben viel Zeit verloren, und Madam wird sehr böse sein, wenn wir nicht bald ankommen.”"
    show but b22warai1 behind rain at l with dis
    but "“Beruhige dich, Gohda-san, wir sind jetzt alle da und bereit, ins Gästehaus zu gehen.”"
    hide goh   
    show jes a12ikari1 behind rain at m
    with dis
    jes "“Hättest du nicht ins Meer gekotzt und hätte ich nicht den Kapitän angefleht, langsamer zu fahren, wären wir jetzt nicht im Verzug, Freund Nase!"
    extend " .....Dafür müsste ich dir die Prügel rausschmeißen, bis mir die Puste ausgeht....”"
    but b11aseru1 "“....hihihi...."
    extend " Da scheint etwas dran zu sein, tut mir voll traurig."
    but "Das nächste Mal teleportiere ich mich einfach mit Magie hierher, du wirst schon sehen!”"
    jes b22warai1 "“Ahahahaha," 
    extend " ...das würde ich zu gerne sehen!"
    extend " ...Kannst mir ja dann verraten, wie man von der Insel weg kommt.”"
    show mar a11uuu1 behind rain at rightedge with dis
    mar "“....Uu???"
    extend " Battler kann Magie benutzen?”"
    jes "“Ganz genau Maria-chan, Battler kann Magie benutzen, aber nicht nur Battler!"
    extend " Jeder kann zaubern, denn jeder trägt etwas Magie im Herzen, auch du!”"
    mar a22warai2 "“Uu-uu!" 
    extend " ...Wir alle besitzen Magie!" 
    extend " ...Wir alle besitzen Magie! Uu-uu!"
    extend " Uu-uu!" 
    extend " Ich möchte dir meine Freundinnen vorstellen, Battler!" 
    extend " Uu~!"
    mar "Ich möchte dir Beatrice vorstellen!"
    extend " ..Uu!"
    but b11oya1 "“.....Beatrice?”"
    mar a11warai1 "“Wer Magie besitzt, kann sie sehen, also kannst auch du sie sehen! Uu-uu!”"
    "Battler war wieder nicht vorsichtig mit Maria und ließ sie versehentlich glauben, dass er magische Kräfte besaß, was natürlich Unsinn war."
    scene black
    camera 
    with quickergradientwiperight
    scene beach_1ab
    call rainlayer from _call_rainlayer_19
    show geo a11majime2 behind rain at m
    with quickergradientwiperight
    geo "“Battler-kun...." 
    extend " Jessica-chan..." 
    extend " Ihr müsst vorsichtiger sein mit euren Witzen in Marias Umgebung, wie ihr erneut seht, nimmt sie alles viel zu ernst.”"
    show but b22nayamu1 behind rain at rightedge with dis
    but "“Entschuldige... Aniki...”"
    "'Aniki' bedeutet so viel wie 'großer Bruder', was aber keinen Sinn macht, weil wir ja Cousins sind und keine Geschwister..."
    extend " Aber es hat sich bei uns so eingebürgert, also ist es in Ordnung, auch weil George älter ist als ich."
    "Außerdem gibt es noch 'Aneki', was so viel wie 'große Schwester' bedeutet."
    scene black
    camera 
    with quickergradientwiperight
    scene beach_1ab
    call rainlayer from _call_rainlayer_20
    show mar a22warai2 behind rain at l
    with quickergradientwiperight
    mar "“...uu~!" 
    extend " Battler besitzt Magie!" 
    extend " ...Battler besitzt Magie!"
    extend " ...hahaha...haha...Uu~!”"
    show geo a12warai1 behind rain at rightedge with dis
    geo "“....Du hast recht Maria-chan! Nur kann Battler-kun keine magischen Wesen sehen."
    extend " ...Das ist nämlich etwas, dass nur du sehen kannst, da du was ganz besonderes bist.”"
    mar a11uuu1 "“Battler kann Beatrice nicht sehen?"
    extend " .........Uu~”"
    "George-Aniki konnte Maria schnell beruhigen," 
    extend " solche Momente zeigen immer wieder, wie gut er mit Kindern umgehen kann, er wird eines Tages ein guter Vater sein."
    hide geo  
    show ros a11majime1 behind rain at rightedge 
    with dis
    ros ".....Maria!"
    extend " Lass den Unsinn und komm her!"
    extend a12ikari1 " ...Und ich möchte nichts mehr von Magie oder dieser Beatoriche-irgendwer hören!"
    extend " ....Hast du mich verstanden?"
    extend " ....Maria!"
    "Rosa wollte Maria dazu zwingen mit diesem Magiekram aufzuhören," 
    extend " laut ihrer Meinung ist Maria zu alt für sowas und das regt sie auf."
    "Maria wurde darauf hin still, blieb aber bei Battler und den anderen."
    scene black
    camera 
    with quickergradientwiperight
    scene beach_1ab
    call rainlayer from _call_rainlayer_21
    show but b23nayamu1 behind rain at r
    with quickergradientwiperight
    but "“.....Etwas ist anders in diesem Jahr...."
    extend " ...Ich habe das Gefühl, dass es hier an etwas fehlt..."
    extend " .....Hmmm"
    but "....Richtig!" 
    extend " ....Die Möwen sind weg," 
    extend " ...wir wurden doch immer von den Möwen begrüßt, oder irre ich mich?”"
    show jes a11majime1 behind rain at leftedge with dis
    jes "“.....Jetzt, wo du es sagst..." 
    extend " Das Schreien der Möwen war immer zu hören...”"
    show mar a11uuu1 behind rain at m with dis
    mar "“Uu~....." 
    extend " Keine Möwen?"
    mar "....Wo sind die Möwen? uu~...”"
    hide jes  
    show geo a11defo1 behind rain at leftedge
    with dis
    geo "“...Die Möwen sind längst in ihre Nester zurückgekehrt, denn der Taifun ist bereits in vollem Gange."
    extend " ....Auch für Möwen ist so ein Taifun gefährlich, weshalb sie bereits Schutz gesucht haben.”"
    but b23nayamu2  "“Darauf hätte ich auch selbst kommen können.”"
    scene black with gradientwipeup
    scene sky_1c
    call rainlayer from _call_rainlayer_22
    stop music fadeout 3 
    with gradientwipeup
    "Wir plauderten fröhlich miteinander, doch der Taifun wird von Minute zu Minute stärker und haben beschlossen nun schnell zum Gästehaus zu eilen."
    extend " aber aus irgendeinem Grund habe ich so ein beklemmendes Gefühl..."
    "Verliere ich langsam aber sicher die Nerven? Liegt es an meinen sechs Jahren der Abwesenheit?"
    extend " Oder an Marias gruseliger Show von vorhin? Ich hoffe, ich werde es nie erfahren..."
    stop audio fadeout 2.0
    scene black with dissolve
    pause(2)
    $ songname = "Ride on"
    if persistent.showbgm == True:
        show screen showsong
    play music "audio/bgm/umib_004_Intro.ogg"
    queue music "audio/bgm/umib_004_loop.ogg" loop
    pause(1)
    show op1
    call rainlayer from _call_rainlayer_23
    with dissolve
    pause(11)
    scene white with quickergradientwiperight
    show op2
    call rainlayer from _call_rainlayer_24 
    with quickergradientwiperight
    pause(11)
    scene white with quickergradientwiperight
    show op3
    call rainlayer from _call_rainlayer_25 
    with quickergradientwiperight
    pause(11)
    scene white with quickergradientwiperight
    show op4
    call rainlayer from _call_rainlayer_26 
    with quickergradientwiperight
    pause(11)
    scene white with quickergradientwiperight
    show op5
    call rainlayer from _call_rainlayer_27 
    with quickergradientwiperight
    pause(11)
    scene white with quickergradientwiperight
    show op6
    call rainlayer from _call_rainlayer_28 
    with quickergradientwiperight
    pause(11)
    scene white with quickergradientwiperight
    show op7
    call rainlayer from _call_rainlayer_29 
    with quickergradientwiperight
    pause(11)
    scene white with quickergradientwiperight
    show op8
    call rainlayer from _call_rainlayer_30 
    with quickergradientwiperight
    pause(11)
    scene white with flash
    scene op9 
    call rainlayer from _call_rainlayer_31
    with dissolve
    play sound "audio/sfx/umise_028.ogg"
    pause(11)
    scene black with longdissolve
    stop music fadeout 3.0
    stop wind fadeout 3.0
    stop rain fadeout 3.0
    pause(5)
    $ songname = "Rose"
    if persistent.showbgm == True:
        show screen showsong
    play music "audio/bgm/umib_013_Intro.ogg"
    queue music "audio/bgm/umib_013_loop.ogg" loop 
    play rain "audio/sfx/umilse_012.ogg"
    show mlib_1a_bg at bgani
    call rainlayer from _call_rainlayer_1
    show mlib_1a at bgani
    with gradientcirclefade
    show nan a1defo1 at l2 with dis
    nan "“Musste das wieder sein?..."
    extend " Du trinkst immer noch, obwohl ich dir schon so oft gesagt habe, dass du damit aufhören sollst?”"
    hide nan a1defo1
    show nan a1fumu1 at l2
    with dis
    "Als er seine Untersuchung beendet hatte, stieß der Doktor, der sich im Spätherbst seines Lebens befindet einen ärgerlichen Seufzer aus."
    "Zwei ältere Herren standen in einem dunklen, staubigen und übel riechenden Arbeitszimmer."
    scene mlib_1b_bg at bgani
    call rainlayer from _call_rainlayer_2
    show mlib_1b at bgani
    with dissolve
    "Es ist anzumerken, dass dieses Arbeitszimmer nicht wie ein gewöhnliches Arbeitszimmer aussieht."
    extend " Es ist komplett möbliert mit Schlafzimmer, Küche und eigener Toilette."
    "Es ist praktisch eine komplett eigene Wohnung."
    extend " Niemand würde auf die Idee kommen, dass es sich hier nur um ein Arbeitszimmer handelt."
    show nan a1defo1 at m with dis
    nan "“Kinzo-san...." 
    extend " ...Wenn du damit nicht sofort aufhörst, muss ich meine Berechnungen korrigieren.”"
    if persistent.nanjo == False:
        $ persistent.nanjo = True
        play sound "audio/sfx/umise_1060.ogg"
        show screen charupdate
    "Das ist Nanjo Terumasa."
    extend " Er ist der langjährige Arzt von Kinzo und sein bester Freund."
    "Jetzt, da Kinzos ständiges Misstrauen außergewöhnliche Ausmaße angenommen hat, ist Nanjo einer der wenigen Menschen, denen er vertraut." 
    "Dank Nanjos großherziger Natur konnte er die Freundschaft mit Kinzo aufrechterhalten, obwohl dieser bei der geringsten Provokation in Wut gerät."
    scene mlib_1b_bg at bgani
    call rainlayer from _call_rainlayer_3
    show mlib_1b at bgani
    show kin a11warai1 at m
    with quickergradientwiperight
    kin "“....Danke"
    extend " ....Nanjo"
    extend " ...Du bist mein bester Freund..."
    extend " ...Doch die Flasche ist es ebenfalls..." 
    extend " Und gerade deshalb kann mich nichts auf der Welt davon abbringen.”"
    kin "Außerdem gibt es etwas, dass nicht einmal deine Medizin in mir lindern kann."
    if persistent.kinzo == False:
        $ persistent.kinzo = True
        play sound "audio/sfx/umise_1060.ogg"
        show screen charupdate
    "Das ist das Familienoberhaupt Ushiromiya Kinzo."
    "Er ist sehr mürrisch und leicht zu provozieren."
    extend " Er ist stark vom Westen beeinflusst und ist sehr interessiert an dem Okkulten." 
    extend " Deswegen ist sein Arbeitszimmer vollgepackt mit geheimnisvollen Grimoires."
    "Obwohl er dem tot sehr nahe ist, strotzt er nur so vor Energie."
    extend " und obwohl er in der Vergangenheit ein großes Vermögen angehäuft hat, hat er seinen Kindern gegenüber nie etwas über das Erbe bekannt gegeben."
    kin "“Deine Medikamente halten mich zwar am Leben, aber ich würde ebenfalls sterben, wenn ich aufhören würde.”"
    "Ruhig und ohne Umschweife sprach der Mann, der sich von seinem geliebten Alkohol nicht trennen wollte."
    kin a11warai2 "“Genji..."
    extend " Noch ein Glas...."
    extend " Mach eine Mischung daraus, damit Nanjo nicht aus allen Wolken fällt.”"
    scene mlib_1c_bg at bgani
    call rainlayer from _call_rainlayer_4
    show mlib_1c at bgani
    show gen a11defo1 at m
    with quickergradientwiperight
    gen "“Herr...."
    extend " ....Seid ich Euch absolut sicher?”"
    "Der alte Butler, sah zuerst seinen Herren an, der auf sein nächstes Getränk wartete" 
    extend " und dann auf den Arzt, der die Augen verdrehte um sich danach am Schnapsschrank zu schaffen zu machen."
    hide gen a11defo1
    show gen a11komaru1 at m
    with dis
    if persistent.genji == False:
        $ persistent.genji = True
        play sound "audio/sfx/umise_1060.ogg"
        show screen charupdate
    "Der Duft des alkoholischen Getränks erfüllte den ganzen Raum, als würde sich der Gestank in der Luft buchstäblich verflüchtigen."
    extend " Dieser Duft kitzelt die Riechschleimhaut so angenehm, dass nicht nur die Seele dahinschmelzen möchte."
    "Das ist Ronoue Genji, Kinzos treuerster Butler, er steht seinem Herrn schon so viele Jahre zur seite,"
    extend " dass Kinzos Kinder denken, er sei ein Spion, der Kinzo immer auf den laufenden hält."
    "Er ist so loyal, dass er absolut jeden Befehl seines Herren ausführen würde," 
    extend " selbst dann, wenn er den Befehl erhalten würde, sein eigenes Leben herzugeben."
    scene black with gradientwipeup
    "Erneut stieß Nanjo einen tiefen Seufzer aus, als er mit ansah, wie der Butler seinen Befehl ausführte."
    "Das herrliche Aroma des giftgrünen Getränks hat mittlerweile den ganzen Raum eingenommen."
    extend " Wenn man nicht gerade Alkoholexperte ist, würde man bei der Farbe nicht daran denken, dass es sich hierbei um ein Alkoholisches Getränk handelt."
    scene mlib_1b_bg at bgani
    call rainlayer from _call_rainlayer_5
    show mlib_1b at bgani
    show kin a11warai2 at r
    with gradientwipedown
    kin "“.......Nanjo,"
    extend " ich weiß, dass du mir nur ein längeres Leben ermöglichen willst, und ich weiß das zu schätzen."
    extend " Dafür bin ich dir von Herzen dankbar.”"
    show nan a1defo1 at l with dis
    nan "“......Ach was,"
    extend " ich habe nichts gemacht," 
    extend " du hast mir nie zugehört.”"
    kin "“Hahahahaha..."
    extend " Touché”"
    show gen a11defo1 at m with dis
    gen "“.....Herr”"
    kin "“Vielen Dank.”"
    "Genji führte die Anweisung gewissenhaft aus und reichte seinem Herrn eine Mischung mit geringerem Alkoholgehalt."
    scene mlib_1c_bg at bgani
    call rainlayer from _call_rainlayer_6
    show mlib_1c at bgani
    with gradientwiperight
    show kin a11defo1 at r with dissolve
    kin "“....Nanjo," 
    extend " .....wie lange noch?”"
    show nan a2fumu1 at l with dis
    nan "“...Wenn ich ehrlich sein soll,"
    extend " ...wohl nicht mehr lange."
    nan "...Das liegt aber auch an deinem übermäßigen Alkoholkonsum."
    extend " ...Du verkürzt dir dein eigenes Leben enorm.”"
    kin "“......Nanjo,"
    extend " dass du mich am Leben hältst, gefällt hier längst nicht jedem.”"
    nan a1defo1 "“...Kinzo-san”"
    kin a11akuwarai1 "“...Die Aasgeier, die sich meine Kinder nennen, warten doch nur sehnsüchtig darauf, dass ich diese Welt verlasse."
    extend " ....Sobald mein Ende gekommen ist, stürzen sie sich auf mich und reißen mir das Fleisch von den Knochen bis nichts mehr übrig ist."
    kin "Doch sie bekommen nichts!" 
    extend " Absolut garnichts!”"
    nan "“Bitte beruhige dich doch, noch bist du nicht tot."
    extend " Wie wäre es, wenn du ein Testament aufsetzt, als letzter Wille nach dem tot?"
    extend " So kannst du selbst entscheiden, was wer bekommt.”"
    kin a11fukigen1 "“....Wie bitte?"
    extend " .....Ein Testament?"
    extend " .....Lächerlich"
    scene mlib_1e with gradientwipeup
    kin "Ich, Ushiromiya Kinzo, habe keine Verwendung für so einen Quatsch wie ein Testament!"
    extend " Geboren wurde ich mit nichts!"
    extend " Sterben werde ich mit nichts!"
    kin "Als ob es etwas geben würde, was ich meinen törichten Kindern hinterlassen möchte!”"
    nan "“...Du könntest aber auch aufschreiben, was du erledigt haben möchtest,"
    extend " ...Dinge die du zu Lebzeiten nicht selber tun konntest.”"
    kin "“Ich habe absolut nichts zum weitergeben!"
    extend " Wenn der Tod mich jetzt holen käme, würde ich ohne eine Spur von Angst mit ihm gehen!"
    extend " Mein Schicksal ist der Tod und alles, was ich je besessen habe, nehme ich mit mir!"
    kin "Ich habe alles hier geschaffen und es wird mit mir untergehen!"
    extend " Ich verlange gar nichts!"
    kin "Denn das ist der Vertrag, den ich mit der Hexe geschlossen habe!"
    extend " ....So war es von Anfang an bestimmt und so wird es auch sein!”"
    "Nach einem heftigen Wutanfall brach der alte Mann plötzlich in sich zusammen."
    extend " Sein Gesicht war völlig schlaff und kraftlos,"
    extend " Als hätte ein sehr mächtiger Dämon von ihm Besitz ergriffen und ihn dann wieder verlassen."
    kin "“..........."
    extend " Aber eines fehlt mir noch in meinem Leben."
    extend " Ich lasse nichts zurück, aber eines fehlt noch.”"
    nan "“Dann schreib es auf, für die Nachwelt."
    extend " Wenn du es jetzt aufschreibst, kann sich sicher jemand darum kümmern."
    extend " Es wäre natürlich besser, wenn du das selbst machen könntest."
    nan "Höre einmal auf meinen Rat und halte ihn fest, damit dein Bedauern auch dann noch aufgelöst werden kann, wenn du gegangen bist."
    extend " ....Dafür ist ein Testament da.”"
    "Als Nanjo versuchte, Kinzos Rücken sanft zu streicheln, bekam der Sterbende einen weiteren Wutanfall und schlug Nanjos Hand weg."
    scene mlib_1e
    play sound "audio/sfx/umise_020.ogg" 
    with vpunch
    scene black
    kin "“Es hat keinen Sinn, es hat alles keinen Sinn!"
    kin "Bevor ich sterbe, muss es vollbracht sein!"
    extend " ...Bevor mich die Dämonen des Vertrages im Augenblick meines Todes verschlingen, muss es geschehen!"
    kin "Für mich gibt es so etwas wie Frieden nicht!"
    extend " Deshalb ist ein Testament sinnlos!"
    extend " ...Selbst wenn ich etwas tun könnte."
    kin "....Dann"
    extend " ....Würde ich es nochmal sehen wollen."
    extend " .....Ich möchte dein bezauberndes Lächeln wieder sehen."
    extend " Ich will Beatrice noch einmal lächeln sehen!"
    kin "Oh Beatrice, warum hast du mich nur verlassen?"
    extend " ....War ich dir etwa nicht gut genug?"
    kin "Seit jenem Tag ist mein Herz von diesem unerträglichen Schmerz erfüllt!"
    extend " ...Ich habe es verdient, dass du mir den Rücken gekehrt hast!"
    kin " ...Oh, Beatrice,"
    extend " ....Bitte vergebe meine Sünden!"
    extend " Gib mir eine Chance für die Sünden die ich begangen habe zu sühnen!"
    kin " Ich werde dir alles zurückgeben, ich bin bereit alles zu verlieren!"
    extend " Bitte, ein letztes Mal, bevor ich sterbe..."
    extend " ....Zeig mir noch einmal dein Lächeln, ein letztes Mal!"
    kin "Beatrice!"
    extend " ....Ich flehe dich an!"
    extend " Seit dem Tag an dem du verschwunden bist, sehne ich mich nach nichts anderem mehr!"
    kin "....Du bist hier oder?"
    extend " Du bist hier irgendwo im Raum und machst dich über mich lustig, nicht wahr?"
    extend " ...Es ist doch so," 
    extend " denn das ist die Art von Frau die du bist!"
    kin "Aah, Beatrice!"
    extend " Beatrice!"
    kin "Es tut mir so leid, es tut mir alles so unendlich leid...."
    extend " Es ist alles meine Schuld gewesen!"
    extend " Ich biete dir als Wiedergutmachung mein Leben an!"
    extend " Ich biete es dir an!"
    extend " .....Beatriceeeeeee!!!”"
    stop music
    $ songname = "-"
    play sound "audio/sfx/umise_019.ogg"
    pause(1.5)
    "Plötzlich klopfte es an der Tür, dabei war es doch verboten um diese Zeit zu stören."
    "Kinzos Wutanfall war nur noch wie ein Echo, das im Raum verblieben war."
    scene mlib_1b_bg at bgani
    call rainlayer from _call_rainlayer_7
    show mlib_1b at bgani
    show kin a11fukigen1 at m
    with quickergradientwiperight
    kin "“....Wer stört?"
    extend " Es ist doch ausdrücklich verboten worden, um diese Zeit zu stören, also wer besitzt die Dreißtigkeit?”"
    "Kinzo ist außer sich, er wird von seinen gierigen Kindern gestört, denkt er."
    kin "“....Genji,"
    extend " öffne die Tür!"
    extend " ....Wer es wagt zu stören, hat bestimmt auch einen Grund dafür.”"
    show gen a11komaru1 at r with dis
    gen "“Wie Ihr wünscht, Herr.”"
    scene m_door1k with gradientwiperight
    "Sofort ging Genji zum Schreibtisch um den Knopf zu drücken, der die Tür öffnen lässt."
    extend " Die Tür öffnet sich langsam und eine seltsame Gestalt konnte erblickt werden, die dabei ist einzutreten."
    window hide
    play sound "audio/sfx/umise_017.ogg"
    stop rain fadeout 2.0
    scene white zorder 99
    with kanon_r
    pause(1.5)
    scene black with dissolve
    window show
    nan "“......."
    extend " ....Was sehen meine alten Augen?”"
    kin "“......."
    extend " ....Unmöglich!"
    extend " ......Das..." 
    extend " ....Das kann doch nicht wahr sein!”"
    pause 1
    window hide
    if persistent.musicbox == False:
        $ persistent.newelement1 = True
        play sound "audio/sfx/umise_1060.ogg"
        $ persistent.musicbox = True
        $ persistent.menustate = 4
        show screen musicupdate
        $ Achievement.add(achievement_bronze3)
    play audio "audio/sfx/umise_030.ogg"
    show text _("Ich wollte dich niemals mit reinziehen....") 
    with fastdissolve
    pause 0.5
    hide text with fastdissolve
    play audio "audio/sfx/umise_030.ogg"
    show text _("Ich bin schon zu weit gegangen....") 
    with fastdissolve
    pause 0.5
    hide text with fastdissolve
    play audio "audio/sfx/umise_030.ogg"
    show text _("Bitte halt mich auf....") 
    with fastdissolve
    pause 0.5
    hide text with fastdissolve
    play audio "audio/sfx/umise_030.ogg"
    show text _("Lass mich endlich raus....") 
    with fastdissolve
    pause 0.5
    hide text with fastdissolve
    play audio "audio/sfx/umise_030.ogg"
    show text _("Du kannst ohne mich nicht existieren....") 
    with fastdissolve
    pause 0.5
    hide text with fastdissolve
    play audio "audio/sfx/umise_030.ogg"
    show text _("So zu tun als wäre ich nicht da ist sinnlos....") 
    with fastdissolve
    pause 0.5
    hide text with fastdissolve
    pause 0.5
    play audio "audio/sfx/umise_046.ogg"
    $ Achievement.add(achievement_bronze4)
    show logo
    pause 10
    hide logo
    with kanon_rev
    jump chapter2




    


