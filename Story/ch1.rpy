label chapter1:

    $ discord.update(state = "Boat trip to Rokkenjima")
    $ discord.update(details = "Reading Chapter 1")
    $ chaptername = "“Bootsfahrt nach Rokkenjima”\nSam. 04. Oktober 1986 09:30 Uhr"
    $ chapternumber = "Kapitel 1"
    $ songname = "-"
    $ persistent.openingplayed = True
    call showch1 from _call_showch1
    play sound "audio/sfx/umise_028.ogg"
    show oct_4_1986 with dissolve
    pause (7)
    play ship "audio/sfx/umilse_004.ogg"
    $ songname = "HANE (Feathers)"
    $ play_music(hane)
    show white with m1trans
    camera at Shake(None, float('inf'), dist=4)
    scene ship_s2a with m1trans1
    window auto
    "In der Luft liegt der typische Meeresgeruch von Salz und auch ein wenig von Algen."
    extend " Ein Duft, der den Geruchssinn sofort in Ekstase versetzt, wenn nicht sogar die Seele selbst begeistert."
    "Denn auch ein taubstummer und sehbehinderter Mensch weiß sofort, dass das Meer in der Nähe ist, und kommt so in die richtige Stimmung."
    "Die Familie Ushiromiya ist mit dem Boot von der Insel Niijima unterwegs zur Familienkonferenz auf der Insel Rokkenjima."
    extend " Aber ein Familienmitglied scheint die Fahrt gar nicht gut zu tun, er schreit herum, dass er vom Boot fällt und so." 
    play sound "audio/sfx/umise_003.ogg"
    show but_b23_kuyasigaru1 at m with fastdissolve
    but "“whaoooo!!!!" 
    extend " ....Ich falle runter, ....ich falle runteeeeeer!!!...."
    extend " ....Ich hasse Boote! ...Gleich muss ich kotzen, ich falleeeee!!!"
    extend " ...Warum muss das verfluchte Ding auch so stark schaukeln?...."
    but "Das wars!..." 
    extend " Ich werde diese Insel nicht mehr erreichen, eher sterbe ich hier...”"
    show but_b23_kuyasigaru1 at l with fastdissolve
    play sound "audio/sfx/umise_047.ogg"
    show mar_a11_warai1 at r,jump_shake with dissolve
    mar "“*kicher*kicher*" 
    extend " ....Battler fällt runter, Battler fällt runter!" 
    extend " uu-uu~!!"
    hide but_b23_kuyasigaru1
    show but_b23_nayamu1 at l
    but "“Bitte..." 
    extend " Maria-chan..." 
    extend " Bitte etwas ruhiger..." 
    extend " Das macht alles mein Magen nicht mit.”"
    show mar_a11_uuu1 at r
    mar "“Uu~...?" 
    extend " du findest das nicht lustig?...."
    hide mar_a11_uuu1
    play sound "audio/sfx/umise_047.ogg"
    show mar_a11_warai1 at r,jump_shake
    extend " .....Ich finde das super lustig!" 
    extend " *kicher*kicher*" 
    extend " uu~!”"
    scene ship_s2a with quickergradientwiperight
    show but_b11_warai2 at m with quickgradientwiperight
    if persistent.battler == False:
        $ persistent.battler = True
        $ Achievement.add(achievement_bronze2)
        play sound "audio/sfx/umise_1060.ogg"
        $ renpy.notify("Ein neuer Charakter wurde im Charaktermenü freigeschaltet.")
    "Mein Name ist Ushiromiya Battler."
    extend " Ich bin der Sohn von Rudolf und Asumu, Asumu ist vor ungefähr 6 Jahren gestorben."
    "Danach habe ich die Familie wegen eines Konflikts mit Dad für 6 lange Jahre verlassen und habe bei meinen Großeltern mütterlicherseits gelebt."
    "Mein Name wird im Japanischen übrigens so geschrieben: Ushiromiya Batora."
    extend " Ja, man spricht mich nicht Battler aus, sondern 'Batora', klingt echt komisch."
    "Meine Japanischen Schriftzeichen machen mich wütend. Ich werde mit den Zeichen von 'Person' und 'Kampf' geschrieben"
    extend " Deswegen denkt ein typischer Japaner ich heiße Sento-kun. Niemand würde auch nur im Traum daran denken, dass es 'Battler' ausgesprochen wird."
    "Aber der Spaß hört bei mir noch lange nicht auf..."
    extend " Hier sind einige, die ihren Namensgeber am liebsten in dunkle Kammern sperren würden."
    scene sea_1af with gradientwipeup
    "Als die Familie Ushiromiya zur jährlichen Familienkonferenz fahren will,"
    extend " hat Battler, wie schon bei früheren Konferenzen, mit Angstzuständen zu kämpfen."
    "Battler hat eine Art Reiseangst. Wenn das Flugzeug zu sehr schaukelt, könnte es abstürzen,"
    extend " und wenn er auf einem Schiff ist, dann...... Na ja, das sehen wir ja gerade."
    "Maria, die überhaupt nicht seekrank ist, beginnt laut zu kichern,"
    extend " weil es so lustig ist, einem zu Tode erschrockenen Battler zuzusehen."
    "Aber die beiden scheinen von jemandem beobachtet zu werden, und auch der kann sich das Lachen nicht verkneifen."
    scene ship_s2bf with quickergradientwiperight
    show rud_a11_akuwarai1 at m with quickergradientwiperight  
    rud "“...Hey Battler-kun!" 
    extend " Wenn du kotzen musst, dann bitte in einen Eimer!"
    extend " .....Bei dem, was du dir in den Hals schaufelst, würdest du eine Menge Fische auf dem Gewissen haben..." 
    extend " hehe..."
    rud "....Unglaublich, dass du schon im Flugzeug so durchgedreht bist," 
    extend " du konntest ja nicht mal im Auto still sitzen.”"
    hide rud_a11_akuwarai1 with fastdissolve
    show rud_a11_defo1 at r with fastdissolve
    show but_b22_odoroki2_mouth_closed at l with fastdissolve
    but "“..........."
    hide but_b22_odoroki2_mouth_closed
    show but_b22_odoroki2 at l
    extend " ...Lass mich in Ruhe!"
    extend " ....Das ist echt kein guter Zeitpunkt!”"
    rud "“Es ist nie ein guter Zeitpunkt, wenn du mit irgendetwas fahren musst." 
    extend " .....Wag es nicht, ins Meer zu kotzen!”"
    hide but_b22_odoroki2
    show but_b22_nayamu2 at l
    but "“Ich gebe mir hier die größte Mühe...”"
    scene ship_s2bf with quickergradientwiperight
    show rud_a11_warai1 at m with quickergradientwiperight  
    pause (0.3)
    if persistent.rudolf == False:
        $ persistent.rudolf = True
        play sound "audio/sfx/umise_1060.ogg"
        $ renpy.notify("Das Charaktermenü wurde unter 'Extras' freigeschaltet.")
    "Das ist mein Vater Rudolf. Der alte Bastard ist so groß wie ich und macht sich bei Gelegenheit gerne über mich lustig."
    extend " Sein Name wird auf Japanisch Ushiromiya Rudorfu ausgesprochen, fast die ganze Familie hat diese seltsame Namenstradition."
    "Seit meine Mutter Asumu gestorben ist, hat sich unser Verhältnis sehr verschlechtert,"
    extend " aber ich bin sicher, dass es mit der Zeit wieder funktionieren kann."
    scene black with quickgradientwipedown
    camera at Shake(None, float('inf'), dist=0)
    "Vor sechs Jahren, kurz nach dem Tod meiner Mutter, hat mein Vater seine Arbeitskollegin geheiratet."
    extend " Das hat mich gebrochen, weil es einfach viel zu schnell ging, kaum war meine Mutter gestorben, hat er wieder geheiratet."
    "Das nächste Problem war, dass Dad schon eine Affäre mit ihr gehabt hatte."
    extend " Beide haben ein Kind meine Stiefschwester Ange, die heute leider Krank ist und Zuhause geblieben ist."
    "Wenn man sich ausrechnet, wann Ange geboren wurde und wann meine Mutter gestorben ist, wird mir immer ganz übel."
    extend " und da ich mit solchen Leuten nicht in einem Haushalt leben wollte, bin ich zu meinen Großeltern mütterlicherseits gezogen und habe die Ushiromiya-Familie verlassen."
    "Leider sind meine Großeltern vor kurzem gestorben, und ich hatte die Gelegenheit, mit meinem Vater und meiner Stiefmutter zu sprechen, und wir konnten irgendwie einen gemeinsamen Nenner finden."
    "Ich bin also wieder Teil der Familie und nehme nach sechs Jahren zum ersten Mal wieder an der Konferenz teil."
    camera at Shake(None, float('inf'), dist=4)
    scene ship_s2bf with quickergradientwiperight
    show kir_a11_defo1 at l with dissolve
    kyr "“Ist es nicht schön, dass Battler-kun wieder da ist?...."
    extend " Ich meine, nach 6 Jahren Abwesenheit immer noch ein Theater bei der Ankunft? *kicher*”"
    show rud_a11_warai1 at r with dissolve
    rud "“Ja...."
    extend " Aber das war viel schlimmer, als er noch jünger war...." 
    extend " Da hatte man die ganze Anreise keine Ruhe.”"
    hide kir_a11_defo1
    show kir_a11_majime1 at l
    kyr "“Aber er ist selbst schuld, wenn er da rumturnt, obwohl er weiß, dass er seekrank wird.”"
    scene ship_s2bf with quickergradientwiperight
    show kir_a11_defo1 at m with quickgradientwiperight
    if persistent.kyrie == False:
        $ persistent.kyrie = True
        play sound "audio/sfx/umise_1060.ogg"
        $ renpy.notify("Ein neuer Charakter wurde im Charaktermenü freigeschaltet.")
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
    camera at Shake(None, float('inf'), dist=10)
    hide kir_a11_defo1 with dissolve
    show but_b23_kuyasigaru1 at m with dissolve
    but "“Ich finde das gar nicht lustig..." 
    extend " Ich kämpfe hier schließlich um....."
    extend " mein..."
    extend " ....Leben..." 
    extend " ...*würg*”"
    play sound "audio/sfx/umise_003.ogg"
    show but_b23_kuyasigaru1 at m,run
    hide but_b23_kuyasigaru1 with dissolve
    "Battler wurde so übel, dass er sich nicht zurückhalten konnte und den ganzen gekochten Reis vom Vormittag ins Wasser schleuderte."
    show rud_a11_akuwarai1 at r with dissolve
    rud "“.....Jetzt hat dieser Kasper tatsächlich die Fische gefüttert, ach herrje..." 
    extend " ....ahahaha”"
    camera at Shake(None, float('inf'), dist=4)
    show mar_a22_warai2 at l with dissolve
    mar "“uu-uu~!" 
    extend " Battler hat sich übergeben!" 
    extend " Battler hat sich übergeben!" 
    extend " *kicher*kicher*”"
    scene ship_s2a with quickergradientwiperight
    show mar_a11_niyari1 at m with quickgradientwiperight
    if persistent.maria == False:
        $ persistent.maria = True
        play sound "audio/sfx/umise_1060.ogg"
        $ renpy.notify("Ein neuer Charakter wurde im Charaktermenü freigeschaltet.")
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
    scene ship_s2a with quickergradientwiperight
    show ros_a11_ikari1 at r with dissolve
    ros "“Maria!"
    extend " ....Es reicht jetzt," 
    extend " .....lass Battler-kun in Ruhe!”"
    show mar_a11_defo1 at l with dissolve
    mar "“...uu~.....”"
    hide ros_a11_ikari1
    show ros_a11_ikari2 at r
    ros "“und hör auf mit diesem 'uu-uu'!"
    extend " .....Du bist kein kleines Kind mehr!”"
    "Maria war nicht begeistert, dass ihre Mama ihre Freude unterbrach."
    extend " Rosa ist eine sehr strenge Mutter."
    extend " Sie nimmt Marias eher kindliches Verhalten sehr ernst,"
    extend " was schon zu unangenehm anzusehenden Szenen mit den beiden geführt hat."
    hide mar_a11_defo1 with fastdissolve
    show but_b11_odoroki3 at l with fastdissolve
    show ros_a11_komaru4 at r
    hide ros_a11_ikari2
    ros "“....Tut mir leid," 
    extend " ......Battler-kun," 
    extend " .....ich kriege es einfach nicht aus ihr raus.”"
    hide but_b11_odoroki3
    show ros_a11_komaru4 at r
    show but_b22_warai1 at l
    but "“Schon gut, Tante Rosa," 
    extend " ....sie meint es nicht böse, also bin ich es auch nicht.”"
    hide ros_a11_komaru4
    show ros_a11_majime1 at r
    ros "“.....aber dass dein größter Feind das Fahrzeugfahren ist, verstehe ich nicht..."
    extend " .....Du wirkst so erwachsen und reif und jetzt das?”"
    scene ship_s2a with quickergradientwiperight
    show ros_a11_warai1 at m with quickgradientwiperight
    if persistent.rosa == False:
        $ persistent.rosa = True
        play sound "audio/sfx/umise_1060.ogg"
        $ renpy.notify("Ein neuer Charakter wurde im Charaktermenü freigeschaltet.")
    "Das ist Tante Rosa," 
    extend " sie ist die Mutter von Maria die sie sehr streng erzieht."
    "Trotzdem kenne ich Tante Rosa als sehr liebe Person,"
    extend " auch wenn das Taschengeld, dass sie uns Kindern gibt, nicht so hoch ist wie bei den anderen Erwachsenen."
    "Trotz ihres blöden Namens ist ihre Aussprache nur Ushiromiya Rooza,"
    extend " was nur halb so schlimm ist wie der Name meines Vaters."
    "Trotzdem ist der Name in jeder Hinsicht lächerlich...." 
    extend " Danke Großvater nochmal dafür."
    scene ship_s2a with quickergradientwiperight
    show rud_a11_akuwarai1 at r with dissolve
    rud "“Er kann einfach nicht still sitzen, aus irgendeinem Grund."
    extend " ...Das ist wirklich peinlich, das darfst du niemandem erzählen.”"
    show but_b23_nayamu1 at l with fastdissolve
    but "“.......Ey, .....halt den Mund!”"
    hide rud_a11_akuwarai1
    show rud_a11_akuwarai2 at r
    rud "“Ja Battler-kun, das Frühstück, dass gerade im Meer gelandet ist, hat Geld gekostet und Lebensmittel werden nicht billiger...”"
    hide but_b23_nayamu1
    show but_b22_nayamu1 at l
    but "“.....ähm..... "
    hide but_b22_nayamu1
    show but_b22_nayamu2 at l
    extend " ...Also wenn du es unbedingt wiederhaben willst, kannst du ja ins Meer springen und es wieder rausfischen... hihihihi..."
    extend " ....Aber mal ernsthaft, das Schaukeln wurde gerade richtig schlimm...”"
    hide rud_a11_akuwarai2
    show rud_a11_defo2 at r
    rud "“........Battler...”"
    show rud_a11_defo2 at l2
    hide rud_a11_defo2
    show rud_a11_defo1 at l2
    play sound "audio/sfx/umise_047.ogg"
    hide but_b22_nayamu2
    show but_b11_kuyasigaru1 at l
    but "“....owowowowowow......"
    extend " Du alter Bastard!" 
    extend " Scheiße......" 
    extend " owowowow......”"
    "Einen Moment hat Battler nicht aufgepasst und schon hat Rudolf sein Ohrläppchen gepackt und behandelt es nicht gerade zimperlich."
    but "“owowowowowowowow...." 
    extend " lass los! owowowowowowow"
    extend " .......Das tut richtig weh," 
    extend " hör auf damit," 
    extend " .....owowowow”"
    rud "“Du...." 
    extend " willst...." 
    extend " also....," 
    extend " dass ich es mir zu..."
    extend " rück...."
    extend " ho..."
    extend " le..."
    extend " jaaaa~?”"
    "Rudolf hat einen sehr starken Griff, besonders wenn es um Battlers Ohrläppchen geht, man hat das Gefühl, er reißt es jeden Moment ab."
    hide but_b11_kuyasigaru1
    show but_a11_aseru5 at l
    but "“....Ich hoffe, du springst vom Boot und ertrinkst du alter Bastard.... Owowowow, lass los!"
    but "...Ich...."
    extend " gebe....."
    extend " nicht....."
    extend " auuuuuuffffff!!!"
    extend " .....owowowow..... lass doch endlich los owowowowow... es tut weh....”"
    hide rud_a11_defo1
    show rud_a11_akuwarai1 at l2
    rud "“....Das ist deine Strafe, wenn du frech wirst, Battler-kun.”"
    hide but_a11_aseru5 with fastdissolve
    hide rud_a11_akuwarai1 with fastdissolve
    show kir_a11_majime1 at m with fastdissolve
    kyr "“Lasst es für heute gut sein, ihr beiden."
    extend " Das könnt ihr später auf der Insel austragen.”"
    "Nachdem Kyrie den kleinen Konflikt erfolgreich beendet hatte, hörte man jemanden von unter Deck nach draußen gehen."
    hide kir_a11_majime1 with fastdissolve
    show jes_a11_atya2 at m with fastdissolve
    jes "“...B-Battler-kun?" 
    extend " hast du gerade eben vom Deck gekotzt? Ich schaue nach draußen und plötzlich kommt so eine widerliche Suppe von oben runter, das war eklig!"
    extend " Nächstes Mal nimm einen Eimer mit!”"
    show jes_a11_aisowarai1 at m with fastdissolve
    hide jes_a11_atya2
    jes "Ach ja, und was war das für ein 'Ich falle, ich falle' -Geschrei?"
    $ persistent.wiki_unlocked.add("wiki_crazy")
    $ persistent.tip = 2
    extend " ...Bist du ein bisschen {note_green}meschugge{/note_green}?"
    extend " ...wahahahaha!"
    jes ".....Das war die eine Sache,"
    extend " .....und dann war da noch die Kotze, die vom Deck segelte."
    extend " ....pahahahaha.”"
    scene ship_s2a with quickergradientwiperight
    show but_a11_defo1 at r with fastdissolve
    but "“......Entschuldigung...."
    extend " Das verfluchte Boot schaukelt so viel....."
    extend " ....Das Schiff schaukelt und schaukelt und schaukelt....."
    show but_a21_kuyasigaru1 at r
    hide but_a11_defo1
    but "....ahhhhhh!!!"
    extend " Mach, dass es aufhört, sonst falle ich wieder!”"
    show jes_a11_atya3 at l with fastdissolve
    hide jes_a11_defo2
    jes "“....Vielleicht sollte der Kapitän etwas langsamer fahren, sonst geht es dir gleich noch schlechter..."
    extend " Ich werde sofort den Kapitän bitten, etwas langsamer zu fahren, aber bitte nicht mehr ins Meer kotzen....”"
    show but_b11_odoroki3 at r
    hide but_a21_kuyasigaru1
    but "“Ja..." 
    extend " ....Vielen Dank, Jessica-chan.”"
    hide but_b11_odoroki3 with fastdissolve
    hide jes_a11_atya3 with fastdissolve
    show jes_a11_warai1 at m with quickgradientwiperight
    if persistent.jessica == False:
        $ persistent.jessica = True
        play sound "audio/sfx/umise_1060.ogg"
        $ renpy.notify("Ein neuer Charakter wurde im Charaktermenü freigeschaltet.")
    "Das war meine Cousine Ushiromiya Jessica." 
    extend " Sie ist echt cool drauf und ist wohl aktuell in dieser Phase, wo man gegen seine Eltern rebelliert."
    "Sie ist aber auch in dieser Phase, wo die Mädchen so große Brüste bekommen."
    extend " hihihihih... ich würde sie mal gerne in die Hand nehmen...."
    "Aber dann würde sie mich windelweich schlagen, denn mit ihr ist es nicht gut Kirschen zu essen, wenn man es sich mit ihr verscherzt."
    "Jessica klingt sehr nach englischer Herkunft und wird bei uns Ushiromiya Jeshka ausgesprochen," 
    extend " sie muss richtig unzufrieden mit ihrem Namen sein."
    "Sie hat außerdem so eine 'Verrückte Art zu reden'." 
    extend " Sie flucht viel und ihre Wortwahl ist gewöhnungsbedürftig."
    "Früher waren wir das Chaotenduo, haben viel Unsinn gemacht und waren uns auch nicht zu fein, gegenüber der Hauptfamilie einen sehr rauen Ton anzuwenden"
    extend " Die Vorträge der Erwachsenen über gutes Benehmen nervten uns zwar jedes Mal, aber es war auch einfach zu lustig zu sehen, wie sich die vorbildlichen Erwachsenen aufregten."
    camera at Shake(None, float('inf'), dist=0)
    "Der Kapitän hat zugestimmt langsamer zu fahren und jetzt schaukelt das Boot nicht mehr so stark."
    jes "“....Verdammte Scheiße Battler-kun, jetzt werden wir uns wegen dir verspäten....”"
    hide jes_a11_warai1 with fastdissolve
    show but_b22_warai1 at r2 with quickergradientwiperight
    but "“.....Halt doch mal dein Maul, immerhin kann ich jetzt ein wenig chillen....”"
    show jes_a11_defo2 at l with quickergradientwipeupright
    jes "“.....Wir sollten besser runter gehen zum 'chillen', wir sind gleich auf der Insel.”"
    but "“....Ja, das kann ich versuchen, jetzt, wo das Boot etwas langsamer fährt."
    show but_b22_nayamu2 at r2
    extend " ....Aber ich kann trotzdem nicht garantieren, dass ich den Rest meines Frühstücks bei mir behalte.... Ihihihi....' "
    stop ship
    $ songname = "Door of Summer"
    $ play_music(summer)
    scene ship_s3a with gradientwiperight
    show eva_b22_akire2 at r behind ship_s3a
    show hid_a21_warai1 at m behind ship_s3a
    show kum_a12_defo2 at l behind ship_s3a
    show ship_s3ab behind eva_b22_akire2
    "Dann gingen Battler und Jessica unter Deck zu den anderen, die im Gegensatz zu Battler ruhig warten, bis sie endlich die Insel erreichen."
    hide ship_s3a with quickergradientwiperight
    extend " ....Moment mal, dieses 'ruhig' sein ist falsch! Ich sehe es klar und deutlich! Die anderen Erwachsenen verkneifen sich doch alle gerade das Lachen...."
    scene ship_s3a with quickergradientwiperight
    show geo_a11_defo1 at m with fastdissolve
    geo "“Wie geht es dir Battler-kun?"
    extend " Wir alle wissen bereits, dass es dich schon erwischt hat.”"
    scene ship_s3a with quickergradientwiperight
    show but_b22_nayamu1 at l,nod with fastdissolve
    "Mit einem leichten, aber nicht ganz ernstgemeinten Nicken stimmt Battler zu."
    but "“Mir geht es gut, den Umständen entsprechend...."
    hide but_b22_nayamu1
    show but_b23_kuyasigaru1 at l
    extend " Der Kapitän hat das Schiff doch absichtlich so schaukeln lassen.”"
    show geo_a11_majime2 at r with fastdissolve
    geo "“Ja gut...." 
    extend " ...eigentlich nicht..."
    extend " Leg dich am besten hin, du hast es gleich geschafft."
    show geo_a11_warai1 at r
    hide geo_a11_majime2
    geo "Erinnert an alte Zeiten, nicht wahr, Jessica-chan?”"
    hide but_b23_kuyasigaru1 with fastdissolve
    show jes_b22_warai1 at l with fastdissolve
    jes "“Ja,"
    extend " .....es ist, als wäre er nie weg gewesen......"
    extend " Mit dem Unterschied, dass er sich heute zum ersten Mal übergeben hat.”"
    show geo_a11_komaru3 at r
    hide geo_a11_warai1
    geo "“Ahahahahaha, ....ja,"
    extend " ....manche Dinge ändern sich, andere nie.”"
    scene ship_s3a with quickergradientwiperight
    show geo_a11_defo1 at m with quickergradientwiperight
    if persistent.george == False:
        $ persistent.george = True
        play sound "audio/sfx/umise_1060.ogg"
        $ renpy.notify("Ein neuer Charakter wurde im Charaktermenü freigeschaltet.")
    "Das ist mein Cousin George." 
    extend " er wird von Tante Eva und Onkel Hideyoshi zu einem echten Gentleman erzogen."
    "Er arbeitet sehr hart und will schon sein eigenes Unternehmen gründen, was ich sehr beeindruckend finde."
    "Er wird von den anderen Familienmitgliedern sehr geschätzt."
    extend " Außerdem ist für sein Alter sehr reif und kennt sich gut aus."
    "Ushiromiya Joji..."
    "So spricht man ihn bei uns aus, und ich bin fest davon überzeugt,"
    extend " dass er heute einen Massenmord begehen wird."
    "Am liebsten würde ich auch diejenigen umbringen, die für diese schreckliche Namenstradition verantwortlich sind."
    scene ship_s3a with quickergradientwiperight
    show but_b22_warai1 at r with quickergradientwiperight
    but "“Ich finde, heute ist auch ein besonderer Tag...."
    extend " Denn um die Mittagszeit soll ein Sturm aufziehen, der sich erst am Montag wieder legen soll."
    hide but_b22_warai1
    show but_b11_warai3 at r
    extend " Es ist das erste Mal, dass wir länger als einen Tag auf der Insel bleiben.”"
    show geo_a11_hohoemi1 at l with quickergradientwiperight
    geo "“...Ja, aber wir haben auch immer ein wenig Glück gehabt, dass so ein starker Sturm nie über unsere Familienkonferenz hereingebrochen ist."
    extend " Wie heißt es so schön?" 
    extend " Es gibt immer ein erstes Mal.”"
    "Für Battler war die entspannte Atmosphäre eine sehr gute Ablenkung, um nicht mehr an das schaukelnde Boot denken zu müssen."
    show geo_a11_majime2 at l with fastdissolve
    hide geo_a11_hohoemi1
    geo "“...ähm" 
    extend " .....Battler-kun?" 
    extend " Wusstest du, dass es so genannte Sturmgötter gibt?”"
    show but_b11_aseru1 at r
    hide but_b11_warai3
    but "“....Ähhhhm...." 
    extend " ...Meinst du Zeus...?”"
    show geo_a11_warai1 at l
    hide geo_a11_majime2
    geo "“Auch richtig, aber nein, " 
    extend " ....ich spreche vom Sturmgott in einem selbst.”"
    show but_b11_oya1 at r
    hide but_b11_aseru1
    but "“.........." 
    extend " Was?”"
    geo "“Okay, es geht um folgendes:"
    geo "In der tantrischen Spiritualität gibt es intensivere Gefühle und auch bei den Griechen gab es die dionysische Spiritualität, "
    extend " die auch besonders heftige Gefühle beinhaltet. In diesem Sinne hat jeder Mensch auch Sturmgötter in sich."
    geo ".....diese können auch in einem selbst aktiviert werden."
    show geo_a11_majime2 at l
    extend " ....Diese Sturmgötter können aber auch zu schlimmen Taten, zu Verbrechen und Gewalt verleiten."
    geo "Man kann ihn aber auch dazu bringen, sich intensiv vorwärts zu bewegen und aus der Bequemlichkeit des Alltags auszubrechen.”"
    scene ship_s3a with quickergradientwiperight
    show jes_a11_tereru1 at m with quickergradientwiperight
    jes "....Wahahahahahaha "
    extend "Was höre ich da, was laberst du da für einen Scheiß?"
    jes "Ich habe kein Wort verstanden...."
    show jes_a11_atya3 at m
    hide jes_a11_tereru1 
    extend " ...Ich kenne nicht einmal die Bedeutung von {note_green}tantrisch oder dionysisch{/note_green}...."
    extend " Es klingt einfach unironisch, als hätte jemand einfach Wörter erfunden."
    scene ship_s3a with quickergradientwiperight
    show but_b23_nayamu1 at r with quickergradientwiperight
    but "............."
    "Battler war ein auch wenig überwältigt von diesem Input, im Leben nicht hätte er jetzt einen Vortrag über Gefühle und Spiritualität erwartet."
    but "“Ähm......"
    extend " .....ähm"
    extend " .......Tantrisch?..... Gefühlsregungen?..... Dionysische Spiritualität?"
    show but_b23_nayamu2 at r
    hide but_b23_nayamu1
    extend " ....Das hast du aus dieser einen Yoga-Zeitschrift.....' "
    show geo_a11_komaru1 at l with quickergradientwiperight
    geo "“Ähm......."
    show geo_a11_komaru3 at l
    hide geo_a11_komaru1
    extend " ....Oh...."
    extend " ....Hahahaha, aber ich habe dich zum Nachdenken gebracht."
    show geo_a11_hohoemi1 at l
    hide geo_a11_komaru3
    geo "Meine Mutter hat so eine Zeitschrift, und ab und zu schaue ich auch mal rein.”"
    show but_b11_warai2 at r
    hide but_b23_nayamu2
    but "“ ....Hihihi...." 
    extend " ....Du hast nur Pech gehabt, dass ich vor der Abreise auf der Toilette so ein Yoga-Magazin in der Hand hatte, weil ich mich vergriffen habe.”"
    geo "“Was es manchmal für Zufälle gibt.”"
    show geo_a11_defo1 at l
    hide geo_a11_hohoemi1
    geo "Eine kurze Erklärung für dionysisch wäre, dass es eine Spiritualität der Ekstaze, Musik und des Tanzes ist.”"
    but "“Mehr nicht?"
    extend " Klingt ja nicht sehr originell.”"
    geo "“Da kommt noch was und zwar....."
    extend " uhmmmm na ja...."
    extend " hehe, wie soll ich sagen?"
    geo "Es ist auch eine Spiritualität der...."
    extend " uhmm...."
    extend " ....Sexualität”"
    but "“Sehr stark, das muss ich mal ausprobieren!"
    extend " ...Ihihihi.....”"
    jes "“...Trottel!"
    extend " ....Du Holzkopf!"
    extend " ......War ja zu erwarten, dass das deine einzige Motivation ist, Trottel-Battler."
    jes "Perverser Battler!"
    extend " ...Du bist sofort Feuer und Flamme, sobald es auch nur im Entferntesten in diese Richtung geht....”"
    but "“.....Ihihihihi...."
    extend " Tut mir leid....”"
    geo "“Tantrisch ist das Tantra."
    extend " ....Es ist ein Begriff ursprünglich aus Indien, und wird mit 'Zusammenhang' oder auch 'Gefüge' übersetzt."
    extend " ....Berührungen des Körpers sollen also auch die Seele berühren, sie nähren."
    geo "Es ist ein sehr breites Thema..."
    extend " .........Ja....."
    jes "Das klingt für mich so, als hätte jemand einen Vorwand gesucht mit einem anderen Menschen engen Kontakt zu haben...."
    but "Ja, " 
    extend " .....letztlich läuft alles darauf hinaus, dass man in gewisser Weise seine Lust wiederbelebt...."
    extend " Wenn wir so darüber reden, klingt es absolut lächerlich..."
    geo "Ahahahaha...."
    extend " Ich denke da hast du Recht..."
    extend " Ach ja.... Wusstest du?...."
    extend " ....Ein echter Sturmgott aus der griechischen Mythologie. ist jedoch Aigaion.”"
    show but_b24_futeki3 at r
    hide but_b11_warai2
    but "“....Ein leckerer Teller Gyros-Geschnetzeltes ist das einzige Griechische, das ich schätze....."
    show but_b24_warai1 at r
    hide but_b24_futeki3
    extend " Yumyumyumyum....”"
    geo "“.........."
    extend " ...Jedenfalls kann dieser Gott Meeresstürme auslösen, ähnlich wie wir ihn heute erleben.”"
    but "“Du willst mir also sagen, dass irgendeine Gottheit, auf die wir keinen Einfluss haben, diesen Sturm ausgelöst hat?”"
    geo "“......Hmm"
    extend " ....So könnte man es ausdrücken ja!”"
    but "“....Auf jeden Fall können wir die Zeit, die uns Aigaion jetzt schenkt, nutzen, um wieder mehr Zeit miteinander zu verbringen.”"
    jes "“Ja, das hast du wirklich nötig, Battler-kun!”"
    extend " ...Es war ja auch notwendig, dass du deine Familie für sechs Jahre verlässt.....”"
    but "“.....Ach man”"
    jes "“Auf die Familienkonferenz freue ich mich am meisten...."
    extend "Es ist die kurze Zeit, die meinen langweiligen Alltag auflockert.”"
    but "“Ja, ich bin auch froh, wieder bei euch zu sein, das hat mir in den 6 Jahren am meisten gefehlt.”"
    jes "“Es ist schrecklich, nur mit meinen Eltern und meinem Großvater auf der Insel zu leben."
    extend " Ich muss jeden Tag ziemlich früh aufstehen, weil meine Schule nicht wirklich in der Nähe ist, sondern auf Niijima."
    jes "Nach der Schule muss ich sofort nach Hause, so dass ich keine Zeit mit meinen Freunden verbringen kann.”"
    "Jessica wird immer wütender und die Wut steht ihr ins Gesicht geschrieben."
    jes "“Danach habe ich nur noch Zeit, meine Hausaufgaben zu machen und in meinem Zimmer zu bleiben.... Es gibt nichts zu tun."
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
    hid "“...Du hast dein ganzes Leben noch vor dir, glaub mir, deine Zeit als Teenager auf der Insel wird später nur noch eine Erinnerung sein...."
    extend " Jetzt habe ich mich aber verquatscht," 
    extend " wahahahahaha!"
    hid "Aber lass den Kopf nicht hängen und häng dich weiter rein, ja?”"
    jes "“Danke Hideyoshi, ich denke der Plan ist gut, ich werde ihn mir zu Herzen nehmen."
    extend " Ich fühle mich schon besser.”"
    hid "“So ist's gut, du schaffst es!, wahahahaha”"
    if persistent.hideyoshi == False:
        $ persistent.hideyoshi = True
        play sound "audio/sfx/umise_1060.ogg"
        $ renpy.notify("Ein neuer Charakter wurde im Charaktermenü freigeschaltet.")
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
    eva "“Hey, sieht so aus, als wären wir gleich da, Battler-kun..."
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
    extend " Ach ja! Fast hätte ich ihren Namen vergessen.... Sie heißt hier Ushiromiya Eba......" 
    extend " mit b....."
    but "“.....Nein, du verarschst mich Tante Eva....”"
    eva "“Oh nein..." 
    extend " .....Das würde ich nie tun... *kicher*"
    eva "....Ich wollte dir nur etwas über die Seekrankheit erzählen... mehr nicht... *kicher*”"
    "Tante Eva wollte mich wahrscheinlich nicht erschrecken,"
    extend " sondern meinen Kopf auf die Probe stellen, denn wenn ich an ihre Worte denke, sobald ich an Land bin,"
    extend " dann wird mir bestimmt wieder schlecht," 
    extend " ......ganz schön raffiniert."
    kyr "“Wir sind jetzt gleich da!" 
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
    kyr "“War der Taifun nicht für heute Mittag angekündigt?"
    extend " Vielleicht fängt es gleich an zu regnen.”"
    "Kyrie hat sofort bemerkt, dass etwas nicht stimmt."
    extend " Der Himmel hat sich in der Zwischenzeit bereits verdunkelt,"
    extend " was zu diesem Zeitpunkt noch gar nicht hätte passieren dürfen."
    rud "“In etwa 10 Minuten sind wir da, aber gemütlich wird es nicht mehr.”"
    kyr "“Stimmt..." 
    extend " Der Wind hat auch schon stark zugenommen.”"
    "Der Wind, der von Minute zu Minute stärker über das Meer peitscht,"
    extend " ist kein Wind, wie ihn die meisten Menschen vom Festland kennen."
    "Der Wind kann ungehindert und mit voller Kraft über das Wasser fegen,"
    extend " während es auf dem Land immer Häuser, Berge und Gelände gibt, die den Wind abschwächen können."
    kyr "“Dass die Wettervorhersage sich mal irrt?”"
    rud "“Ich habe einmal ein Geschäftsessen wegen eines angeblichen Taifuns abgesagt...."
    extend " Der Taifun kam erst 2 Tage später, ich habe mich noch nie so dumm gefühlt wie in dieser Situation.”"
    kyr "“Das war sicher eine Erfahrung, so etwas am Ende erklären zu müssen....”"
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
        $ renpy.notify("Ein neuer Charakter wurde im Charaktermenü freigeschaltet.")
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
        $ renpy.notify("Ein neuer Charakter wurde im Charaktermenü freigeschaltet.")
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
    if persistent.musicbox == False:
        play sound "audio/sfx/umise_1060.ogg"
        $ persistent.musicbox = True
        $ renpy.notify("Die Musikbox wurde unter 'Extras' freigeschaltet.")
        $ Achievement.add(achievement_bronze3)
        $ Achievement.add(achievement_bronze4)
    stop audio fadeout 2.0
    stop music fadeout 2.0
    scene black with dissolve
    pause(2)
    $ songname = "Ride on"
    $ play_music(ride_on)
    pause (1)
    show op1 with dissolve
    pause (11)
    scene white with quickergradientwiperight
    show op2 with quickergradientwiperight
    pause (11)
    scene white with quickergradientwiperight
    show op3 with quickergradientwiperight
    pause (11)
    scene white with quickergradientwiperight
    show op4 with quickergradientwiperight
    pause (11)
    scene white with quickergradientwiperight
    show op5 with quickergradientwiperight
    pause (11)
    scene white with quickergradientwiperight
    show op6 with quickergradientwiperight
    pause (11)
    scene white with quickergradientwiperight
    show op7 with quickergradientwiperight
    pause (11)
    scene white with quickergradientwiperight
    show op8 with quickergradientwiperight
    pause (11)
    scene white with flash
    scene op9 with dissolve
    play sound "audio/sfx/umise_028.ogg"
    pause (11)
    scene black with longdissolve
    stop music fadeout 3.0
    pause (5)
    jump chapter2
