label chapter1:

    $ discord.update(state = "Episode 0 - DEBUGMODE")
    $ discord.update(details = "Editing Chapter 1")
    $ chapter = 1
    $ songname = "-"
    $ persistent.openingplayed = True
    $ renpy.free_memory()
    if persistent.showch == True:
        call showch1 from _call_showch1
    play sound "audio/sfx/umise_028.ogg"
    show oct_4_1986 with dissolve
    pause (7)
    play ship "audio/sfx/umilse_004.ogg"
    $ songname = "HANE (Feathers)"
    if persistent.showbgm == True:
        $ renpy.notify("♪HANE (Feathers)")
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
        $ renpy.notify("Die Charakterbox wurde freigeschaltet.")
    "Mein Name ist Ushiromiya Battler."
    extend " Ich bin der Sohn von Rudolf und Asumu, Asumu ist vor ungefähr 6 Jahren gestorben."
    "Danach habe ich die Familie wegen eines Konflikts mit Dad für 6 lange Jahre verlassen und habe bei meinen Großeltern mütterlicherseits gelebt."
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
        $ renpy.notify("Die Charaktere wurden geupdated.")
    $ renpy.start_predict("kir *")
    "Das ist mein Vater Rudolf. Der alte Bastard ist so groß wie ich und macht sich bei Gelegenheit gerne über mich lustig."
    extend " Sein Name wird auf Japanisch Ushiromiya Rudorfu ausgesprochen, fast die ganze Familie hat diese seltsame Namenstradition."
    "Seit meine Mutter Asumu gestorben ist, hat sich unser Verhältnis sehr verschlechtert,"
    extend " aber ich bin sicher, dass es mit der Zeit wieder funktionieren kann."
    scene black
    camera
    with quickgradientwipedown
    "Vor sechs Jahren, kurz nach dem Tod meiner Mutter, hat mein Vater seine Arbeitskollegin geheiratet."
    extend " Das hat mich gebrochen, weil es einfach viel zu schnell ging, kaum war meine Mutter gestorben, hat er wieder geheiratet."
    "Das nächste Problem war, dass Dad schon eine Affäre mit ihr gehabt hatte."
    extend " Beide haben ein Kind meine Stiefschwester Ange, die heute leider Krank ist und Zuhause geblieben ist."
    "Wenn man sich ausrechnet, wann Ange geboren wurde und wann meine Mutter gestorben ist, wird mir immer ganz übel."
    extend " und da ich mit solchen Leuten nicht in einem Haushalt leben wollte, bin ich zu meinen Großeltern mütterlicherseits gezogen und habe die Ushiromiya-Familie verlassen."
    "Leider sind meine Großeltern vor kurzem gestorben, und ich hatte die Gelegenheit, mit meinem Vater und meiner Stiefmutter zu sprechen, und wir konnten irgendwie einen gemeinsamen Nenner finden."
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
        $ renpy.notify("Die Charaktere wurden geupdated.")
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
    hide but b23kuyasigaru1 with dissolve
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
        $ renpy.notify("Die Charaktere wurden geupdated.")
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
    hide mar a11defo1
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
    but b11warai2 "....Ihihihi"
    extend " Entschuldigung, dass ich einen falschen Eindruck erweckt habe."
    scene ship_s2a
    show ros a11warai1 at m
    with quickgradientwiperight
    if persistent.rosa == False:
        $ persistent.rosa = True
        play sound "audio/sfx/umise_1060.ogg"
        $ renpy.notify("Die Charaktere wurden geupdated.")
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
    hide kir a11majime1
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
        $ renpy.notify("Die Tipps wurden geupdated.")
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
        $ renpy.notify("Die Charaktere wurden geupdated.")
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
    camera at slowerboat
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
    stop ship
    $ songname = "Door of Summer"
    if persistent.showbgm == True:
        $ renpy.notify("♪Door of Summer")
    play music "audio/bgm/umib_002_intro.ogg"
    queue music "audio/bgm/umib_002_loop.ogg" loop 
    scene ship_s3a at bgani
    camera
    show expression(CustomParticles("images/system/particle.png", 10))
    with gradientwiperight
    "Dann gingen Battler und Jessica unter Deck zu den anderen, die im Gegensatz zu Battler ruhig warten, bis sie endlich die Insel erreichen."
    show eva_b22_akire2 at rightedge
    show hid_a21_warai1 at m
    show kum_a12_defo2 at leftedge
    with quickergradientwiperight
    " ....Moment mal, dieses 'ruhig' sein ist falsch! Ich sehe es klar und deutlich! Die anderen Erwachsenen verkneifen sich doch alle gerade das Lachen."
    hide eva_b22_akire2
    hide hid_a21_warai1
    hide kum_a12_defo2
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
    hide but b23kuyasigaru1
    show jes b22warai1 at leftedge
    with dis
    jes "“Ja,"
    extend " .....es ist, als wäre er nie weg gewesen,"
    extend " ....nur mit dem Unterschied, dass er sich heute zum ersten Mal auf dem Boot übergeben hat.”"
    geo a11komaru3 "“Ahahahahaha," 
    extend " ....ja,"
    extend " ....manche Dinge ändern sich, andere nie.”"
    show geo a11defo1 at m
    hide jes b22warai1
    with quickergradientwiperight
    if persistent.george == False:
        $ persistent.george = True
        play sound "audio/sfx/umise_1060.ogg"
        $ renpy.notify("Die Charaktere wurden geupdated.")
    "Das ist mein Cousin George." 
    extend " er wird von Tante Eva und Onkel Hideyoshi zu einem echten Gentleman erzogen."
    "Er arbeitet sehr hart und will schon sein eigenes Unternehmen gründen, was ich sehr beeindruckend finde."
    "Er wird von den anderen Familienmitgliedern sehr geschätzt."
    extend " Außerdem ist für sein Alter sehr reif und kennt sich gut aus."
    "Ushiromiya Joji..."
    extend " So spricht man ihn bei uns aus, und ich bin fest davon überzeugt,"
    extend " dass er heute einen Massenmord begehen wird."
    "Am liebsten würde ich auch diejenigen umbringen, die für diese schreckliche Namenstradition verantwortlich sind."
    hide geo a11defo1
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
    hide geo a11majime2
    hide but b11oya1
    show jes a11tereru1 at m
    with quickergradientwiperight
    jes "....Wahahahahahaha "
    extend "Was höre ich da, was laberst du da für einen Scheiß?"
    jes "Ich habe kein Wort verstanden...."
    extend a11atya3 " ...Ich wusste nicht mal, dass Wörter wie tantrisch oder dionysisch existieren."
    extend " Es klingt einfach unironisch, als hätte jemand einfach Wörter erfunden."
    hide jes a11atya3
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
    hide geo a11komaru3
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
    "Von außen betrachtet sieht es nicht anders aus, als zwei Blagen die sich zanken und sich gegenseitig Sachen an den Kopf werfen."
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
    hide geo a11hohoemi1
    hide but a11niramu1
    hide jes a11tereru1
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
    jes  "“Auf die Familienkonferenz freue ich mich am meisten."
    extend " ....Es ist die kurze Zeit, die meinen langweiligen Alltag auflockert.”"
    but "“Ja, ich bin auch froh, wieder bei euch zu sein, das hat mir in den sechs Jahren am meisten gefehlt.”"
    jes "“Es ist schrecklich, nur mit meinen Eltern und meinem Großvater auf der Insel zu leben."
    extend " ....Ich muss jeden Tag ziemlich früh aufstehen, weil meine Schule nicht wirklich in der Nähe ist, sondern auf Niijima."
    jes "Nach der Schule muss ich sofort nach Hause, so dass ich keine Zeit mit meinen Freunden verbringen kann.”"
    "Jessica wird immer wütender und die Wut steht ihr ins Gesicht geschrieben."
    jes "“Danach habe ich nur noch Zeit, meine Hausaufgaben zu machen und in meinem Zimmer zu bleiben." 
    extend " ....Es gibt nichts zu tun."
    extend " ...Am liebsten würde ich diese blöde Insel für immer verlassen und auf dem Festland ein neues Leben beginnen."
    jes "........"
    extend " .....Da ich keinen direkten Kontakt zu meinen Schulfreunden habe," 
    extend " ....fühle ich mich hier ziemlich einsam."
    "Man merkt sofort, dass es Jessica sehr nahe geht, nach der Schule von der Außenwelt abgeschnitten zu sein."
    extend " Auch George und Battler sind bedrückt, aber verständnisvoll, als sie Jessicas Worte über ihren Alltag auf der Insel hören."
    "Onkel Hideyoshi scheint das Gespräch mitgehört zu haben und erhebt sich von seinem bequemen Platz."
    hid "“Na, na Jessica-chan, du musst es positiv sehen!"
    extend " Eines Tages wirst du die Insel wirklich verlassen und dein eigenes Leben führen können.”"
    jes "“Aber wie lange noch?" 
    extend " .....Was wäre wenn meine Schulfreunde nichts mehr mit mir zu tun haben wollen?”"
    hid "“Auch deine Schulfreunde werden deine Situation verstehen, eines Tages wirst du zu ihnen gehen können und ab da viel Zeit mit ihnen verbringen."
    extend " Bis dahin solltest du immer dein Bestes geben, denn das wird sich am Ende des Tages definitiv auszahlen!”"
    jes "“.......Eines Tages?"
    extend " Aber ich warte schon so viele Jahre.....”"
    hid "“...Du hast dein ganzes Leben noch vor dir, glaub mir, deine Zeit als Teenager auf der Insel wird später nur noch eine Erinnerung sein."
    extend " Jetzt habe ich mich aber verquatscht," 
    extend " wahahahahaha!"
    hid "Aber lass den Kopf nicht hängen und häng dich weiter rein, ja?”"
    jes "“Danke Hideyoshi, ich denke der Plan ist gut, ich werde ihn mir zu Herzen nehmen."
    extend " Ich fühle mich schon besser.”"
    hid "“So ist's gut, du schaffst es!, wahahahaha”"
    if persistent.hideyoshi == False:
        $ persistent.hideyoshi = True
        play sound "audio/sfx/umise_1060.ogg"
        $ renpy.notify("Die Charaktere wurden geupdated.")
    "Das ist Georges Vater und mein Onkel Hideyoshi." 
    extend " Er ist ein netter und sympathischer Mann und ich glaube, ich mag ihn von allen Erwachsenen am meisten."
    "Er ist der Ehemann von Tante Eva und hat seine Firma von Grund auf neu aufgebaut."
    extend " Desweiteren ist er als Präsident einer mittelgroßen Restaurantkette tätig. Die Kette scheint zu wachsen und sehr gut zu laufen."
    "Sein Name wird Ushiromiya Hideyoshi ausgesprochen, wie Kyrie ist sein Name absolut perfekt!"
    extend " Das liegt daran, dass er als Japaner in die Familie eingeheiratet hat. ..... Ich beneide jeden, der einen normalen Namen hat."
    geo "“Jessica-chan, allein ein Ziel zu haben, auf das man hinarbeiten kann, ist etwas, das einen jeden Tag motivieren sollte, nicht aufzugeben."
    geo "Auch ich oder Battler-kun haben unsere Sorgen und Probleme, die wir überall mit hinnehmen. Also halte noch ein bisschen durch, okay?”"
    jes "“Ja vielen Dank, das hilft mir wirklich sehr, danke!”"
    "Die Worte von Hideyoshi und George haben Jessica sehr gut aufgemuntert."
    extend " Man sieht deutlich, wie Jessica wieder ein wenig lächelt."
    eva "“Hey, sieht so aus, als wären wir gleich da, Battler-kun."
    eva "Wusstest du, dass die Seekrankheit auch noch nach der Reise anhalten kann?”"
    but "............."
    but "“Bitte mach mir keine Angst, Tante Eva!”"
    eva "“Oh... Entschuldige, ich wollte dir nur sagen, dass, wenn sich dein Körper an die Bewegungen des Bootes gewöhnt hat, er sich an Land wieder umgewöhnen muss."
    eva "Aber mach dir darüber keinen Kopf. Battler-kun, das passiert nicht unbedingt. *kicher*”"
    if persistent.eva == False:
        $ persistent.eva = True
        play sound "audio/sfx/umise_1060.ogg"
        $ renpy.notify("Ein neuer Charakter wurde im Charaktermenü freigeschaltet.")
    "Das ist meine Tante Eva, die Mutter von George." 
    extend " Sie und der alte Bastard Papa sind so etwas wie ein Spaßvogel-Duo."
    extend " ...Wenn die beiden richtig loslegen, bleibt kein Stein auf dem anderen."
    "Sie beherrscht auch einige chinesische Kampfsporttechniken." 
    extend " Einer ihrer Roundhousekicks soll einmal bei einem Trainingskampf getroffen haben, und ihr Gegner wurde kaltgestellt wie ein Softdrink."
    "Auf keinen Fall möchte ich von ihr unter die Dachlatte getreten werden."
    extend " Ach ja! Fast hätte ich ihren Namen vergessen.... Sie heißt hier Ushiromiya Eba." 
    extend " mit b....."
    but "“.....Nein, du verarschst mich Tante Eva....”"
    eva "“Oh nein..." 
    extend " .....Das würde ich nie tun... *kicher*"
    eva "....Ich wollte dir nur etwas über die Seekrankheit erzählen," 
    extend " mehr nicht," 
    extend " *kicher*”"
    "Tante Eva wollte mich wahrscheinlich nicht erschrecken,"
    extend " sondern meinen Kopf auf die Probe stellen, denn wenn ich an ihre Worte denke, sobald ich an Land bin,"
    extend " dann wird mir bestimmt wieder schlecht," 
    extend " ......ganz schön raffiniert."
    kir "“Wir sind jetzt gleich da!" 
    extend " .....Die Insel ist ganz nah!”"
    "Unser Gespräch wird jäh unterbrochen durch die erfreuliche Nachricht, dass wir bald an Land gehen werden!"
    but "“....Wir werden sehen, ob du Recht hast Tante Eva...”"
    eva "“*kicher*"
    extend " Forder es besser nicht heraus.... Battler-kun....”"
    hid "“Wahahahahaha!" 
    extend " ....Ihr zwei seid mir ja welche." 
    extend " ...Lasst uns lieber an Deck gehen, wir gehen gleich an Land!”"
    jes "“Ja, das ist eine gute Idee!”"
    "So erhoben sich alle von ihren Plätzen und bemerkten, dass sich draußen die Wolken unerwartet und viel zu früh verdunkelt hatten."
    kir "“War der Taifun nicht für heute Mittag angekündigt?"
    extend " Vielleicht fängt es gleich an zu regnen.”"
    "Kyrie hat sofort bemerkt, dass etwas nicht stimmt."
    extend " Der Himmel hat sich in der Zwischenzeit bereits verdunkelt,"
    extend " was zu diesem Zeitpunkt noch gar nicht hätte passieren dürfen."
    rud "“In etwa 10 Minuten sind wir da, aber gemütlich wird es nicht mehr.”"
    kir "“Stimmt..." 
    extend " Der Wind hat auch schon stark zugenommen.”"
    "Der Wind, der von Minute zu Minute stärker über das Meer peitscht,"
    extend " ist kein Wind, wie ihn die meisten Menschen vom Festland kennen."
    "Der Wind kann ungehindert und mit voller Kraft über das Wasser fegen,"
    extend " während es auf dem Land immer Häuser, Berge und Gelände gibt, die den Wind abschwächen können."
    kir "“Dass die Wettervorhersage sich mal irrt?”"
    rud "“Ich habe einmal ein Geschäftsessen wegen eines angeblichen Taifuns abgesagt...."
    extend " Der Taifun kam erst 2 Tage später, ich habe mich noch nie so dumm gefühlt wie in dieser Situation.”"
    kir "“Das war sicher eine Erfahrung, so etwas am Ende erklären zu müssen....”"
    rud "“Bitte erinnere mich nicht daran....”"
    "Nicht nur Rudolf und Kyrie sind beunruhigt," 
    extend " auch alle anderen sind überrascht,"
    "dass der Sturm einige Stunden zu früh kommt. Dabei hatte der Wetterbericht garantiert, dass es erst um die Mittagszeit losgehen würde."
    extend " ...Die Folge könnten turbulente Flüge sein, die noch eine Starterlaubnis für Kurzflüge haben."
    "Inzwischen hat sich Maria ganz vorne auf der Brücke niedergelassen, und ihr Blick schweift nicht mehr von einer ganz bestimmten Klippe ab."
    mar "“......................Uu~..........."
    mar "..................................."
    mar "......................Es ist weg................."
    extend " ......................Uu~.............."
    extend " ......Uu~........nicht mehr da......”"
    but "“hmm?" 
    extend " .....Was ist los Maria?”"
    jes "“Etwas scheint sie sehr zu beunruhigen...”"
    mar "“Der Schrein ist weg! Es ist weg!.... Uu!"
    extend " Es ist weg!... Uu~...!"
    mar "Es war immer da, aber jetzt ist es weg!..." 
    extend " Uu!..”"
    jes "“Stimmt ja..." 
    extend " Der Schrein fehlt, er war letztes Jahr noch da...."
    jes "Es sieht auch so aus, als wäre ein Teil des Riffs mitgerissen worden....”"
    kum "“Ohohohoh, der Schrein wurde während eines Gewitters von einem gewaltigen Blitz getroffen und zerstört.”"
    if persistent.kumasawa == False:
        $ persistent.kumasawa = True
        play sound "audio/sfx/umise_1060.ogg"
        $ renpy.notify("Die Charaktere wurden geupdated.")
    "Die ältere Frau heißt Kumasawa Chiyo." 
    extend " Sie ist eine Teilzeitarbeiterin, die zwar mehrmals gekündigt hat, aber insgesamt schon viele Jahre im Dienst der Familie steht."
    "Sie ist geschickt und mehr als fähig, ihre Aufgaben zu erfüllen,"
    extend " aber wegen ihrer Geschwätzigkeit und ihrer Vorliebe für Gerüchte ist sie als Angestellte nicht sehr beliebt."
    "Ihr Name auf Japanisch?" 
    extend " ...Auch bei uns Kumasawa, ihre Eltern haben ihr einen vernünftigen Namen gegeben" 
    extend " ....*seufz*...."
    jes "“Ein Blitzeinschlag?..."
    extend " Ein Blitz kann so gewaltig sein?”"
    kum "“Die Fischer sagen, es sei ein Zeichen von Unglück....”"
    mar "“Ein Zeichen von Unglück....Uu~..."
    extend " ...........................”"
    "Kumasawas Worte haben die sonst so entspannte Atmosphäre auf dem Schiff in ein beklemmendes Gefühl verwandelt."
    extend " Maria hat ihren Blick noch immer nicht von der Stelle abgewandt, an der der Schrein stehen sollte..."
    extend " Und es scheint, als würde in genau diesem Moment der heftige Wind für einen Moment nachlassen."
    mar "“Unglück..."
    mar "Unglück...Unglück...”"
    but ".....Was hast du gesagt, Maria?"
    mar "“UnglückUnglückUnglückUnglückUnglückUnglückUnglück"
    extend " UnglückUnglückUnglückUnglückUnglückUnglückUng”"
    "Maria fängt plötzlich an lautstark das Wort 'Unglück' sehr oft zu wiederholen,"
    extend " was das unheimliche Gefühl bei den Anwesenden nur noch verstärkt."
    "Es dürfte ein Ding der Unmöglichkeit sein, Maria jetzt noch zu beruhigen."
    geo "“Kumasawa-san bitte gehen Sie mit ihren Witzen etwas vorsichtiger um!"
    extend " Maria-chan nimmt sowas ziemlich ernst, verstehen Sie?”"
    mar "“UnglückUnglückUnglück”"
    but "“Hey Maria!"
    extend " Wenn du so oft 'Unglück' sagst, wird es wirklich ein Unglück geben, also beruhige dich, ja?”"
    geo "“Maria-chan, es wird nichts schlimmes passieren.”"
    mar "“............Uu~.............."
    extend " ............................”"
    "Die anderen versuchen Maria zu beruhigen, um das Thema irgendwie abzuschließen."
    extend " Aber Maria wendet den Blick vom Riff ab, dreht sich um, hebt den rechten Arm zum Himmel und öffnet langsam den Mund..."
    mar "“Es geschieht definitiv....."
    extend " .....Ein Unglück wird geschehen!......”"
    "Mit diesen Worten, als hätte Maria gerade den Befehl dazu gegeben, hörte man es donnern und sofort begann es zu regnen."
    extend " ....Nicht nur Battler lief deswegen ein kalter Schauer über den Rücken."
    but "“............................"
    extend " .......Hä?.........................”"
    "Alle haben in diesem Moment ein mulmiges Gefühl."
    extend " Es ist fast so, als ob Maria ahnt, dass dieses Familientreffen etwas ganz Besonderes sein würde."
    extend " Doch Battler scheint als einziger zu erkennen, dass mit Marias erhobener Arm und das 'Unglück' wohl nur das Wetter gemeint sein muss."
    but "“Du hast also gemerkt, dass es ein schlimmes Unwetter wird?”"
    mar "“..........Uu~.....”"
    but "“Die Wettervorhersage sagt, dass der Sturm erst gegen Mittag kommen wird. Aber er ist schon da...."
    extend " ....Das nenne ich wirklich ein Unglück...."
    extend " ...hihihihi"
    but "Maria, ich bin sicher, dass dieser Taifun schneller vorbei ist, als du bis zehn zählen kannst. Alles wird gut.”"
    "Battler versucht Maria zu beruhigen, dass sie keine Angst vor dem Taifun haben muss, aber Marias Gesichtsausdruck spricht eine ganz andere Sprache."
    mar "“Uu~!!"
    extend " Uu~!!Uu~!!Uu~!!Uu~!!Uu~!!Uu~!!"
    extend " Ein Unglück wird geschehen! Uu~!!”"
    jes "“Maria, warum sagst du sowas?”"
    kum "“Es ist klar, dass sie etwas im Blick hat, das im Alter schnell verloren geht."
    extend " Sehr junge Menschen haben einen Sinn für das Übernatürliche..."
    extend " Aber dieses Gefühl wird schwächer, je älter man wird."
    kum "Was Maria fühlen kann, kann nur sie fühlen, weil sie die Jüngste hier ist.”"
    "Battler erstarrt bei diesen Worten, ist das wirklich möglich? denkt er, das kann es doch gar nicht geben..."
    extend " Viel mehr ist es so, dass das seltsame Verhalten von Maria und die angespannte Atmospähre ihm diese Erklärung für einen kurzen Moment logisch vorkommen lässt."
    kum "“Es scheint so, dass in der Vergangenheit von Rokkenjima eine Hexe....”"
    jes "“Es reicht, Kumasawa! Darüber reden wir nicht!”"
    kum "“Ohohohoh, ich muss mich entschuldigen, ich wollte nicht unhöflich sein.”"
    "Kumasawas Geschichten sind im Moment eher ungünstig, denn es geht darum, Maria zu beruhigen und nicht darum, ihr noch mehr Dinge in den Kopf zu setzen."
    extend " Jessica hat richtig gehandelt, in dem sie Kumasawa unterbrochen hat."
    but "“Eine......." 
    extend " .......Hexe?"
    but "....Hat Kumasawa Hexe gesagt?"
    extend " ....Weiß Jessica irgendwas?"
    but "Hexe.........."
    but "...........”"
    "Weit weg vom Geschehen konnte man Rudolf sehen, der sehr nachdenklich wirkte."
    rud "“*seufz*”"
    "Nach etwa fünf Minuten stieß er einen tiefen Seufzer aus, während er sich eine Zigarette anzündete, weil ihn etwas sehr beschäftigte, und niemand außer Eva schien diesen Seufzer gehört zu haben."
    eva "“Was ist los Rudolf?.... irgendwelche Sorgen wegen heute Abend?"
    extend " Wir müssen uns nur genau an das halten, was wir besprochen haben, dann können wir gegen Krauss gewinnen.”"
    rud "“....Ja, es liegt nicht am Plan..... Aber wenn unsere Vermutung falsch ist?...."
    extend " Wir würden wegen Hochverrats an der Familie Ushiromiya den Haien zum Fraß vorgeworfen."
    rud "Das wäre das absolute Ende meines Lebens und auch deines, Aneki."
    extend " Damit würden wir unser Ziel um rund eine Quadrillion Kilometer verfehlen.”"
    "Rudolf sieht sehr angespannt aus, während Eva versucht, sich ein leichtes Lächeln zu bewahren..."
    extend " Aber auch ihr ist anzumerken, dass sie so kurz vor der Familienkonferenz, bei der es um das Erbe des Familienoberhauptes geht, ein wenig weiche Knie bekommt."
    eva "“Keine Sorge..." 
    extend " Rudolf..." 
    extend " Es ist ein sehr hoher Einsatz, aber ein Treffer wird mit Vaters Erbe belohnt."
    eva "Außerdem denke ich, dass das Erbe, das man hier erhalten kann, das Risiko definitiv wert ist."
    extend " Ich lasse nicht zu, dass mein hinterhältiger Bruder das ganze Erbe für sich behält!”"
    rud "“Das klingt logisch... Solange du dich an die Aufteilung hältst und im Ernstfall Rede und Antwort stehst, bin ich dabei.”"
    extend " Trotzdem ist das so als würde ich mein ganzes Leben drauf verwetten," 
    extend " dass eine unbedeutende Fußball-Mannschaft aus Portugal dieses Jahr den Europäischen Pokal gewinnt."
    eva "Wirklich jetzt?" 
    extend " Fußball?" 
    extend " Damit kenne ich mich nicht aus."
    rud "Was ich sagen kann, ist dass die Quoten schlecht für uns stehen, aber ein Treffer würde die Situation verändern."
    eva "“Risikobereitschaft kann großzügig belohnt werden und im besten Fall mit Vaters Erbe..”"
    rud "“Ich hoffe einfach auf das beste...”"
    "Sagte er, nimmt einen großen Zug von seiner Zigarre und bläst den feinen weißen Rauch wieder in die Luft."
    "Genau in diesem Moment ertönte die Stimme von Shannon, einer Bediensteten, die heute zusammen mit Chefkoch Gohda die Familienmitglieder abholen sollte."
    extend " Das Boot hat nämlich bereits die Anlegestelle auf Rokkenjima erreicht."
    sha "“Entschuldigung, liebe Gäste, das Schiff legt gleich an!"
    extend " Vorsicht beim Überqueren der Planke, danke!”"
    geo "“Das hast du gut gesagt, Shannon-chan."
    extend " Genau wie ich es von dir erwartet habe.”"
    sha "“George-sama...." 
    extend " D-Das ist zu viel des Lobes..."
    extend " ....I-Ich bin nur das Mobiliar der Familie, das musste ich sagen.....”"
    "Shannon errötete, als sie diese Worte von George hörte."
    extend " Dann fuhr George fort, sich mit ihr in einem angenehmen und ruhigen Ton zu unterhalten."
    geo "“Shannon-chan..." 
    extend " Du weißt selbst nicht, was für eine tolle Bedienstete du bist, du kannst auch mal mehr mit deiner Leistung zufrieden sein."
    extend " Und wenn ich schon dabei bin, du bist auf keinen Fall so etwas wie Mobiliar," 
    extend " du bist ein Mensch."
    geo "Ich will so etwas nicht mehr hören, ist das klar?”"
    sha "“G-George-sama......”"
    if persistent.shannon == False:
        $ persistent.shannon = True
        play sound "audio/sfx/umise_1060.ogg"
        $ renpy.notify("Die Charaktere wurden geupdated.")
    "Diese junge Bedienstete heißt Shannon."
    extend " Sie ist zwar eine junge, aber sehr erfahrene Bedienstete."
    "Normalerweise ist sie ruhig und erledigt ihre Arbeit effizient, aber wenn sie nervös wird, macht sie Fehler."
    extend " Da sie kein Familienmitglied ist, ist ihr Name völlig in Ordnung und nicht seltsam."
    "Ich habe sie seit 6 Jahren nicht mehr gesehen und sie ist noch schöner als in meiner Erinnerung."
    but "“Sag mal Jessica-chan... kann es sein, dass die beiden sich ein bisschen nahe stehen?”"
    jes "“.....wahahahaha.." 
    extend " ..wahahahaha..... das hast du so schnell kapiert?”"
    but "“Also sind sie wirklich ein Paar?”"
    jes "“Ich weiß es nicht genau, aber ich habe den Eindruck, dass George wirklich etwas für sie empfindet.”"
    but "“Wenn ich ganz ehrlich bin, glaube ich, dass ich auch ein bisschen in sie verliebt war."
    but "Ich war damals auch in so einer Phase, wo ich immer so komische Sachen mit ihr geredet habe....."
    extend " Sowas wie <see you again> oder total schnulziges Zeug wie...." 
    extend " ....Ich komme auf..... einem weißen Pferd geritten oder so.”"
    jes "“wahahahahahaha <see you again?> Du hattest wirklich einen Vogel! Ich bin mir ziemlich sicher, dass Shannon das heute sehr peinlich finden würde.”"
    but "“Das glaube ich auch, das ist mir selbst maximal peinlich, also bitte behalte das für dich, okay?"
    extend " Ich bin absolut tot, wenn sie sich auch noch an dieses peinliche Zeug erinnert.”"
    jes "“Ja, das geht klar! Ich schweige wie ein Grab!”"
    "Während alle fröhlich miteinander plauderten, hat das Boot erfolgreich angelegt und alle beginnen, das Boot nach und nach zu verlassen,"
    "Auf der anderen Seite wartet schon der Koch Gohda, um die Familie zu empfangen."
    goh "Meine Damen und Herren, herzlich willkommen auf der Insel Rokkenjima!”"
    "Ein freundlicher Bediensteter der Familie nimmt die angereisten Verwandten in Empfang, um sie und ihr Gepäck in das Gästehaus zu bringen."
    goh "“Auch wenn uns heute nachmittag ein schlimmer Taifun erwartet..." 
    extend " Ich..." 
    extend " Gohda, werde euch immer erstklassiges Essen zubereiten!”"
    jes "“Vielen Dank, Gohda-san, ich glaube, die meisten von uns kommen jedes Jahr hierher, nur um deine leckeren Gerichte zu essen.”"
    goh "“Mit solchen Worten macht das Kochen gleich viel mehr Spaß!"
    goh "Ich muss allerdings sagen, dass wir euch schon 20 Minuten früher erwartet haben, das ist nicht gut für unseren Zeitplan....."
    goh "Außerdem scheint sich dieser Taifun schon früher als angekündigt zu formieren, so dass wir uns schnell auf den Weg zur Villa machen sollten.”"
    if persistent.gohda == False:
        $ persistent.gohda = True
        play sound "audio/sfx/umise_1060.ogg"
        $ renpy.notify("Ein neuer Charakter wurde im Charaktermenü freigeschaltet.")
    "Gohda ist ein Bediensteter, der bei der Familie als Koch angestellt ist."
    extend " Er ist noch nicht lange bei der Familie, aber durch seine früheren Tätigkeiten und Erfahrungen hat er ein Talent dafür entwickelt, Gäste zu bewirten."
    "Aus diesem Grund wird er als Bediensteter sehr geschätzt. Da er nicht zur Familie gehört, hat er auch nicht wie Shannon einen unserer seltsamen Namen."
    kum "“Aber vergiss nicht, dass es heute zum Mittagessen meine speziellen Spaghetti mit würziger Makrelenrahmsauce nach meinem Geheimrezept gibt, Gohda!" 
    extend " Ohohohohoh!"
    kum "Man muss sie einfach probieren..." 
    extend " ....Es gibt nichts Besseres als frische, saftige Makrelen. Ohohohoh!”"
    jes "“.....Ich denke, ich passe....”"
    kum "“Aber Jessica-sama, ihr könnt euch doch nicht die ganze Zeit von Junkfood ernähren!"
    extend " Gib der Makrele eine Chance!”"
    jes "“Aber...." 
    extend " Ich habe heute Morgen in der Küche keine Makrele gesehen, Kumasawa...."
    extend " ...Deshalb kann es heute leider keine Makrele geben!”"
    kum "“Ohohohoh, ihr habt mich erwischt, Jessica-sama.”"
    rud "“Hey Battler-kun! Wenn dir immer noch schwindelig ist und du dich gleich auf den Esstisch übergibst, kannst du nach Hause schwimmen.”"
    but "“Lass es gut sein!...." 
    extend " Es geht mir schon besser.”"
    extend " Danke der Nachfrage.... Dad...."
    rud "“Naaa.... das hoffe ich doch....."
    extend " Ich will mich nicht vor den anderen rechtfertigen müssen, warum du Holzkopf den Esstisch ruinierst.”"
    but "“Keine Sorge, Dad," 
    extend " dein schicker Anzug passt mir auch, wenn's hart auf hart kommt...." 
    extend " ...ihihihi"
    but "........ahh......." 
    extend " *würg*.............hmpf......”"
    "Battler versuchte sein Schwindelgefühl herunterzuspielen, verlor aber gegen die Übelkeit und erbrach in den nächsten Busch."
    eva "“....Meine Güte, Battler-kun..... *kicher*"
    extend " ......Wir haben doch vorhin schon einmal darüber gesprochen, oder etwa nicht? *kicher*kicher*"
    extend " .....Du wolltest deiner Tante nicht glauben... *kicher*”"
    "Tante Evas fettes Grinsen war nicht zu übersehen..." 
    "sie hatte mich mit einem einfachen psychologischen Trick ausgetrickst."
    extend " Indem ich die ganze Zeit darauf achtete, nicht auf meine Übelkeit zu achten, provozierte ich es im Grunde selbst."
    goh "“Liebe Gäste, wir haben Verspätung und der Sturm wird immer stärker! Wir müssen sofort ins Gästehaus!"
    "Plötzlich platzt Gohda herein und tickt mit dem Zeigefinger in kurzen Abständen mehrmals auf seine Armbanduhr."
    goh "Wir müssen uns beeilen, wir haben viel Zeit verloren, und Madam wird sehr böse sein, wenn wir nicht bald ankommen.”"
    but "“Beruhige dich, Gohda-san, wir sind jetzt alle da und bereit, ins Gästehaus zu gehen.”"
    jes "“Hättest du nicht ins Meer gekotzt und hätte ich nicht den Kapitän angefleht, langsamer zu fahren, wären wir jetzt nicht im Verzug, Freund Nase!"
    extend " Dafür müsste ich dich über die ganze Insel jagen, bis dir die Puste ausgeht....”"
    but "“....hihihi...."
    extend " Da scheint etwas dran zu sein, tut mir voll traurig."
    but "Das nächste Mal teleportiere ich mich einfach mit Magie hierher, du wirst schon sehen!”"
    jes "“Ahahahaha, das würde ich zu gerne sehen!”"
    mar "“Uu???......"
    extend " Battler kann Magie benutzen?”"
    jes "“Ganz genau Maria-chan, Battler kann Magie benutzen, aber nicht nur Battler!"
    extend " Jeder kann zaubern, denn jeder trägt etwas Magie im Herzen, auch du!”"
    mar "“Uu-uu! Wir alle haben Magie! Wir alle haben Magie! Uu-uu!"
    extend " Uu-uu! Ich möchte dir Beatrice vorstellen, Battler! Uu!”"
    but "“Beatrice?.....”"
    mar "“Wer Magie hat, kann sie sehen, also kannst auch du sie sehen! Uu-uu!”"
    "Battler war wieder nicht vorsichtig mit Maria und ließ sie versehentlich glauben, dass er magische Kräfte besaß, was natürlich Unsinn war."
    geo "“Battler-kun...." 
    extend " Jessica-chan..." 
    extend " Ihr müsst vorsichtiger sein mit euren Witzen in Marias Umgebung, wie ihr erneut seht, nimmt sie alles viel zu ernst.”"
    but "“Entschuldige... Aniki...”"
    "“Aniki' bedeutet so viel wie 'großer Bruder', was aber keinen Sinn macht, weil wir ja Cousins sind und keine Geschwister..."
    extend " Aber es hat sich bei uns so eingebürgert, also ist es in Ordnung, auch weil George älter ist als ich."
    "Außerdem gibt es noch 'Aneki', was so viel wie 'große Schwester' bedeutet."
    mar "“...uu~!..." 
    extend " Battler hat Magie! Battler hat Magie!”"
    geo "“....Du hast recht Maria-chan! Nur kann Battler-kun keine Hexen sehen."
    extend " ...Das ist nämlich etwas, dass nur du sehen kannst, da du was ganz besonderes bist.”"
    mar "“Battler kann Beatrice nicht sehen?......."
    mar "..........."
    extend " .........Uu~..........”"
    "George-Aniki konnte Maria schnell beruhigen, solche Momente zeigen immer wieder, wie gut er mit Kindern umgehen kann, er wird eines Tages ein guter Vater sein."
    but "“.....Etwas ist anders in diesem Jahr...."
    extend " ...Ich habe das Gefühl, dass es hier an etwas fehlt..."
    extend " ...Hmmm........."
    but "....Richtig ...... Die Möwen sind weg, wir wurden doch immer von den Möwen begrüßt, oder irre ich mich?”"
    jes "“.....Jetzt, wo du es sagst..." 
    extend " Das Schreien der Möwen war immer zu hören...”"
    mar "“..Uu~....." 
    extend " Keine Möwen?"
    mar "....Wo sind die Möwen? uu~...”"
    geo "“...Die Möwen sind längst in ihre Nester zurückgekehrt, denn der Taifun ist bereits in vollem Gange."
    extend " ....Auch für Möwen ist so ein Taifun gefährlich, weshalb sie bereits Schutz gesucht haben.”"
    but "“Darauf hätte ich auch selbst kommen können.”"
    "George, Battler, Jessica und Maria plaudern fröhlich miteinander, doch der Sturm wird von Minute zu Minute stärker und so werden sie erneut von Gohda unterbrochen."
    goh "“Entschuldigt, aber wir müssen zur Villa, denn der Typhoon wird immer stärker und wir wollen auf keinen Fall, dass ihr nass ankommt.”"
    "Dann gingen alle den Waldweg entlang zur Villa."
    extend " aber aus irgendeinem Grund habe ich so ein beklemmendes Gefühl..."
    "Verliere ich langsam aber sicher die Nerven? Liegt es an meiner 6-jährigen Abwesenheit?"
    extend " Oder an Marias gruseliger Show von vorhin? Ich hoffe, ich werde es nie erfahren..."
    stop audio fadeout 2.0
    stop music fadeout 2.0
    scene black with dissolve
    pause(2)
    $ songname = "Ride on"
    $ renpy.notify("♪Ride on")
    play music "audio/bgm/umib_004.ogg"
    pause(1)
    show op1 with dissolve
    pause(11)
    scene white with quickergradientwiperight
    show op2 with quickergradientwiperight
    pause(11)
    scene white with quickergradientwiperight
    show op3 with quickergradientwiperight
    pause(11)
    scene white with quickergradientwiperight
    show op4 with quickergradientwiperight
    pause(11)
    scene white with quickergradientwiperight
    show op5 with quickergradientwiperight
    pause(11)
    scene white with quickergradientwiperight
    show op6 with quickergradientwiperight
    pause(11)
    scene white with quickergradientwiperight
    show op7 with quickergradientwiperight
    pause(11)
    scene white with quickergradientwiperight
    show op8 with quickergradientwiperight
    pause(11)
    scene white with flash
    scene op9 with dissolve
    play sound "audio/sfx/umise_028.ogg"
    pause(11)
    scene black with longdissolve
    stop music fadeout 3.0
    pause(5)
    $ songname = "Rose"
    if persistent.showbgm == True:
        $ renpy.notify("♪Rose")
    play music "audio/bgm/umib_013.ogg"
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
    "Als er seine Untersuchung beendet hatte, stieß der Doktor im Spätherbst seines Lebens einen ärgerlichen Seufzer aus."
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
        $ renpy.notify("Die Charaktere wurden geupdated.")
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
        $ renpy.notify("Die Charaktere wurden geupdated.")
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
    "Der alte Butler, der zuerst seinen Herrn ansah, der auf sein nächstes Getränk wartete" 
    extend " und dann auf den Arzt, der die Augen verdrehte um sich danach dann am Schnapsschrank zu schaffen zu machen."
    hide gen a11defo1
    show gen a11komaru1 at m
    with dis
    "Der Duft des alkoholischen Getränks erfüllte den ganzen Raum, als würde sich der Gestank in der Luft buchstäblich verflüchtigen."
    extend " Dieser Duft kitzelt die Riechschleimhaut so angenehm, dass nicht nur die Seele dahinschmelzen möchte."
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
    extend " öffne die Tür!”"
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
    extend " ....Das kann doch nicht wahr sein!"
    window hide
    if persistent.musicbox == False:
        $ persistent.newelement1 = True
        play sound "audio/sfx/umise_1060.ogg"
        $ persistent.musicbox = True
        $ persistent.menustate = 4
        $ renpy.notify("Die Musikbox wurde freigeschaltet.")
        $ Achievement.add(achievement_bronze3)
        $ Achievement.add(achievement_bronze4)
    call chapterendb from _call_chapterendb
    pause(2)
    hide screen cinemalogo with dissolve
    pause(2)
    jump chapter2




    


