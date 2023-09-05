label chapter2:

        $ discord.update(state = "Episode 0")
        $ discord.update(details = "Chapter 2")
        $ chapter = 2
        $ songname = "-"
        $ renpy.free_memory()
        $ save_name = _("Kapitel 2: Die Hexe auf dem Balkon")
        if persistent.showch == True:
                show screen showch
        pause 2
        scene purgatorio with dissolve
        pause 5
        scene different_spiral_1a at rotatebg with dissolve
        pause 3.0
        scene different_space_1a at bgani
        show expression(CustomParticles("images/system/particle.png", 10))
        with gradientcirclefade
        pause 1
        $ songname = "Pitiful Sneerer"
        if persistent.showbgm == True:
                show screen showsong
        play music "audio/bgm/umib_1001_intro.ogg"
        queue music "audio/bgm/umib_1001_loop.ogg" loop
        window auto
        show ber a11defo1 at l with dis
        ber "“Ja,"
        extend " ...schwarzer Tee ist wahrlich wie geschaffen für eine Hexe."
        extend " ....Besonders gut schmeckt er mit getrockneten Pflaumen."
        extend " ...Sie sind für einen Preis von 200 Yen pro Packung erhältlich."
        ber "Sie machen das ewige Leben einer tausendjährigen Hexe etwas erträglicher.”"
        play sound "audio/sfx/umise_052.ogg"
        show bea a11warai1 at r with witchfadein
        bea "“*gacker*gacker*...!"
        extend " Den heutigen Tee habe ich extra für Euch auf die Nanosekunde ziehen lassen,"
        extend " ...Großes Fräulein Bernkastel."
        bea "Ronove als mein persönlicher Butler ist besser als der talentierteste Butler in der Menschenwelt."
        extend " Seine Kekse schmecken so vollmundig, wie es kein einfacher Mensch je könnte."
        extend " ...Allein aus diesem Grund können wir einen so ausgezeichneten Tee genießen.”"
        "In einem düsteren Raum, der scheint, als würde er im ewigen nichts durch die leere schweben,"
        extend " war es möglich, zwei Hexen zu beobachten, wie sie beide an einem Tisch saßen, der elegant dekoriert war,"
        extend " köstlichen schwarzen Tee tranken und himmlische Kekse aßen."
        ber a11defo2 "“Ich bin nicht interessiert an irgendwelchen Keksen.”"
        bea a13warai1 "“Großes Fräulein Bernkastel," 
        extend " ...ich möchte nicht unhöflich sein," 
        extend " aber ich glaube nicht, dass Ihr mein Territorium nur für eine kleine Teeparty betreten habt."
        extend " ...Darf ich fragen, was der Grund für Euren Besuch ist?”"
        play sound "audio/sfx/umise_056.ogg"
        hide ber with witchfadeout
        scene black with quickergradientwipeleft
        scene g1f_s1ap at bgani
        show expression(CustomParticles("images/system/particle.png", 10)) 
        with quickergradientwipeleft
        pause 1.5
        play sound "audio/sfx/umise_052.ogg"
        show ber a21defo1 at l with witchfadein
        ber "“...Beato,"
        extend " Ich bin nur eine gelangweilte Hexe die durch den See der Fragmente wandert."
        extend " ...Es ist nicht nötig, mich als Bedrohung zu betrachten."
        ber "Ich habe nicht die Absicht die Regeln deines Territoriums zu verletzen.”"
        play sound "audio/sfx/umise_052.ogg"
        show bea a13warai1 at r with witchfadein
        bea "“...*gacker*gacker*"
        extend " Bedrohung?" 
        extend " ...Ich sehe Euch nicht im geringsten als solche an."
        extend " Ich bin nur furchtbar erstaunt, dass die legendäre Hexe Bernkastel an meiner Teeparty teilnimmt.”"
        ber a21defo2 "“Nein,"
        extend " Ich bin völlig machtlos gegen eine Hexe, die ein Individum töten kann, so oft sie will."
        extend " ...Auch wenn es mir widerstrebt, bin ich hier, um dir vor deinem nächsten Spiel mit Battler etwas über die Regeln dieser Welt zu erklären.”"
        bea a11futeki2 "“Regeln dieser Welt, die ich nicht kenne?"
        extend " ..Ich bin eine tausendjährige Hexe, die millionenfach mit Menschenleben gespielt hat, bevor ich sie in Millionen feiner Fleischklumpen verwandelt habe.”"
        ber "“Es gibt Dinge auf dieser Welt, die du noch nicht verstehst.”"
        bea a11futeki1 "“Hoh?"
        extend " ...Ich weiß also nicht alles über diese Welt?"
        extend " ...Ich bin mehr als neugierig, was eine Hexe aus dem Senat mir zu sagen hat.”"
        "Beatrice war ziemlich verwundert, als sie erfuhr, dass sie noch nicht das komplette Wissen dieser Welt besitzt."
        extend " ...Ohne lang zu zögern fing Bernkastel an die Grundlagen der Macht der Hexen zu erklären."
        scene black with quickergradientwiperight
        scene g1f_s1ap at bgani
        show expression(CustomParticles("images/system/particle.png", 10))  
        with quickergradientwiperight
        play sound "audio/sfx/umise_052.ogg"
        show ber a21defo1 at m with witchfadein
        ber "“Die Macht einer Hexe beruht ohne Einschränkung auf einer bestimmten Zahl."
        if persistent.bernkastel == False:
                $ persistent.bernkastel = True
                $ persistent.witches = True
                play sound "audio/sfx/umise_1060.ogg"
                show screen charupdate
        extend " ...Ich bin die Hexe der Wunder,"
        extend " ...Meine Macht lenkt die Wunder, die in dieser Welt geschehen."
        ber "Wenn einem Krebspatient gesagt wird, dass er mit Sicherheit nur noch drei Tage zu leben hat"
        extend " und doch gelingt es ihm, den Krebs zu besiegen, obwohl ihm der Tod gewiss war,"
        extend " ....wird dies von den Menschen als Wunder bezeichnet."
        ber "Seine Überlebenschance lag bei 1 zu 100.000.000, aber er überlebte.”"
        play sound "audio/sfx/umise_052.ogg"
        show bea a11defo2 at rightedge with witchfadein
        bea "“Wenn ich das richtig verstehe, kann ein Wunder geschehen, solange die Wahrscheinlichkeit nicht gleich Null ist?”"
        show ber a21defo2 at l with dis
        ber "“Das ist korrekt."
        extend " ...Ich kann ein Wunder geschehen lassen, solange die Chance nicht gleich Null ist."
        ber "Darum werfe ich die Würfel des Schicksals immer wieder, bis ich mit dem Ergebnis zufrieden bin, das ist meine Macht.”"
        "Wer in einem Brettspiel würfelt, möchte immer möglichst eine hohe Zahl erzielen um vorranzuschreiten," 
        extend " ...wer zu häufig nicht die gewünschten Zahlen würfelt, bleibt meistens auf der Strecke und hat geringe Gewinnchancen."
        "All das ist nur eine Sache des Glücks welche Zahl man erhält."
        extend " ...Bernkastel kann allerdings solange würfeln, bis sich das Spiel zu ihren gunsten wendet."
        extend " In anderen Worten, sie würfelt solange und das Spiel endet erst bis sie gewonnen hat."
        ber a21defo1 "“Deine Macht aber ist die Unendlichkeit."
        extend " Egal welche Zahl du würfelst, du nimmst das Ergebnis an und bist zufrieden."
        extend " Das heißt, du kannst so oft würfeln, wie du willst, es wird dir nie langweilig, weil du keine bestimmte Zahl erreichen musst."
        extend " ...Eine beängstigende Fähigkeit, gegen die ich nicht antreten möchte.”"
        bea "“Das ist richtig, für mich ist nicht wichtig, was ich bekomme, sondern was daraus wird."
        extend " ...Wenn ich würfle, ob der Krebspatient stirbt oder nicht, ist mir das Ergebnis völlig gleich."
        extend " ...Ich würfle einfach immer wieder und erfreue mich an jedem Ergebnis."
        bea a11akuwarai2 "*gacker*..!"
        extend " ...Ich spiele einfach mit dessen Leben bis in alle Ewigkeit.”"
        "Beatrice würfelt nicht um zu gewinnen, sondern sie würfelt einfach nur um zu sehen was passiert."
        extend " ...Stell dir vor dein Gegner würfelt bei einem Spiel und ist zufrieden, wenn die Zahl schlecht für ihn ist."
        "Er würfelt einfach immer weiter mit absoluter Gleichgültigkeit und spielt solange, bis in alle Ewigkeit weiter um unendlich viele Ausgänge zu sehen."
        extend " ...Ob dein Gegner gewinnt oder verliert ist nicht von Bedeutung für ihn."
        ber a21shian1 "“Und dann gibt es noch die Hexe der Gewissheit, die die Zahl 99 in der Hand hält."
        extend " Wenn sie würfelt, bekommt sie mit fast absoluter Sicherheit immer genau das, was sie braucht, man könnte sagen, wenn sie etwas garantiert, kann kein Wunder geschehen, und das macht sie zu meinem natürlichen Feind."
        ber "Wenn sie sagt, dass der Krebspatient sterben wird, dann wird er sterben," 
        extend " ...wenn sie sagt, er wird überleben, dann wird er mit absoluter Sicherheit überleben."
        ber "Eine Macht, die absolut grausam ist."
        extend " Der Nachteil ist, dass sie nur einmal würfeln kann, aber das Ergebnis ist absolut sicher."
        ber "Ich habe einmal gegen sie gewonnen, aber das war nur ein Ausdauerwettkampf.”"
        bea a11gaman4 "“Das klingt sehr grausam, es muss sehr schwer sein, gegen eine solche Macht zu gewinnen."
        extend " Der Versuch, bei einer sicheren Niederlage doch noch zu gewinnen, ist so," 
        extend " ...wie die Flucht einer Stubenfliege aus einem vollen Glas Wasser."
        bea "Mit anderen Worten, zu versuchen, in einem tiefen Gewässer nicht zu ertrinken, auch wenn man nicht in der Lage ist zu schwimmen."
        extend " ...Man erleidet das Schicksal des ertrinkens mit absoluter Gewissheit.”"
        ber a21defo1 "“Das Problem ist, dass die Wahrscheinlichkeit bei 999.999.999 zu 1.000.000.000 liegt."
        extend " ...Das würde die Möglichkeit offen lassen, dass ein Wunder geschieht,"
        extend " ...in dem beispielweise jemand zufällig mit einem Schiff die ertrinkende Person rettet."
        ber "Sollte aber garantiert werden, dass kein Wunder geschehen wird, bin ich machtlos."
        extend " ....Es würde meine Macht annulieren.”"
        "Die Macht der nahezu absoluten Gewissheit ist so, als würde man 1.000 mal hintereinander Lotto spielen und 999 mal gewinnt man den Jackpot und einmal nur den nächst höchsten Preis."
        "Man kann zwar nicht absolut immer den Jackpot holen, aber der zweite Preis ist auch nicht weniger wert."
        "Erfolg im Leben, Erfolg bei allen was man sich vornimmt, das kann die Hexe der Gewissheit garantieren."
        ber "“Dann gibt es noch die Hexe des Theaterbesuchs und der Zuschauerschaft."
        extend " ...Sie kontrolliert keine der Zahlen, aber sie duldet sie.”"
        bea a13warai1 "“Ist das nicht die mächtige Große Hexe Aurora von der ich einmal gehört habe?"
        extend " ....*gacker*..!"
        extend " ...Ich habe gehört sie ist unter allen Wesen dieser Welt sowas wie eine Gottheit.”"
        ber a21defo2 "“Für uns Hexen ist sie das definitiv, sie mischt sich aber selten ein, sie beobachtet alles nur."
        extend " ...Unsere Leben sind für sie nur wie ein Narrativ, dass man bis in alle Ewigkeit genießen kann.”"
        bea a11akuwarai5 "“Also sind all die Milliarden von Leben die existieren, für die Große Aurora nur ein paar einfache Abendlektüren?"
        extend " ....*gacker*gacker*..!"
        extend " ...Das ist in der Tat sehr amüsant!”"
        ber a21shian1 "“Auch wenn sie nur zuschaut, werden wir nur geduldet!" 
        extend " ...es macht ihr nichts aus die Seiten in einem Buch zu verbrennen, wenn sie den Inhalt überdrüssig geworden ist."
        extend " ....Die gruseligste Macht aller Hexen.”"
        "Du lebst jeden Tag deinen normalen Alltag, aber irgendjemand unsichtbares beobachtet dich Tag und Nacht,"
        extend " als wäre dein Leben nur eine Geschichte in einem Buch die von jemanden gelesen wird."
        "Nur mit dem feinen Unterschied, dass dieser Irgendjemand jederzeit ein Radiergummi benutzen kann um Details aus deinem Leben rauszulöschen oder umzuschreiben."
        extend " ...Das Narrativ für eine absurd mächtige Hexe zu sein, ist das alltäglichste für jedes Individum des Universums."
        "Der Plausch über die verschiedene Hexen dieser Welt während dem Tee trinken und Kekse essen ist zwar ganz nett,"
        extend " ...aber Beatrice wartet die ganze Zeit auf den Teil, der wirklich wichtig sein soll und wird langsam ungeduldig."
        bea a13futeki1 "“Entschuldige, dass ich Euch unterbreche, aber die meisten Dinge waren mir bereits bewusst.."
        extend " ....*gacker*"
        extend " ...Was wollt ihr mir wirklich sagen?”"
        ber "“Du hast es also bemerkt?"
        extend a21defo2 " ...Eigentlich bist du mir völlig egal, aber ich erzähle es dir trotzdem.”"
        bea a13warai1 "“*gacker*gacker*..!"
        extend " ...Ich höre Euch sehr gerne zu, Großes Fräulein Bernkastel.”"
        ber a21defo1 " ......Ich erzähl dir das nur ein einziges mal, verstanden?"
        extend " ....Du bist normalerweise nicht mal ein Zehntel meiner Zeit wert, ist das klar?"
        play sound "audio/sfx/umise_056.ogg"
        hide ber with witchfadeoutq
        scene different_space_1c
        show expression(CustomParticles("images/system/particle.png", 10)) 
        with quickgradientwipeup
        play sound "audio/sfx/umise_052.ogg"
        show ber a21defo2 at m with witchfadeinq
        ber "Die mächtigste Hexe ist definitiv die Große Hexe Auauau..."
        extend a21niramu1 " .....Wer hat sich diesen Namen ausgedacht? Ich will meine geliebten Kitties auf denjenigen loslassen...."
        extend " ...Auch nur einen Teil ihres viel zu langen Namens aussprechen zu müssen ist absolut lästig..."
        extend " ...Featherine Augustus Auauauauauaua...... hmpf...."
        ber a21warai4 "Sie mag zwar die mächtigste Hexe sein, aber das mächtigste Wesen ist sie definitiv nicht.”"
        scene black with quickgradientwipeup
        bea "“Es gibt etwas mächtigeres als Fräulein Aurora?"
        extend " ...Das hat in der Tat mein Interesse geweckt."
        extend " *gacker*gacker*...!”"
        ber "“Sei ruhig und hör zu..."
        ber "...Das komplette Universum zusammengefasst besteht aus der Domäne der Menschen und der {note_green}Metawelt{/note_green}."
        extend " ...Diese Metawelt in der wir uns befinden ist in Hierachien und Ebenen aufgeteilt."
        extend " ....Wir befinden uns auf der Hohen Ebene und somit in einer höheren Dimension, als normale Menschen."
        ber "Du hast es vollbracht, als du zur Hexe wurdest, ein komplettes Territorium zu beanspruchen."
        extend " ...Die Rede ist von deinem sogenannten Goldenen Land, dass direkt über uns liegt und mit diesem Raum verbunden ist."
        extend " ...Es ist vorher nur sehr wenigen gelungen sofort ein komplettes Territorium zu beanspruchen."
        ber "In dieser Ebene liegt deine Existenz als Territorialherr.”"
        scene different_space_2c with gradientcirclefade
        "Die Metawelt oder auch die Welt der Hexen und anderen nicht menschlichen Wesen ist in anderen Worten das Universum selber."
        extend " In diesem gibt es mehrere Ebenen wie zum Beispiel der See der Fragmente, der von Bernkastel kontrolliert wird."
        "In diesem See befinden sich mehrere Milliarden Fragmente und ein Fragment ist sowas wie eine komplett eigene Welt."
        extend " Alle Fragmente befolgen die selben Regeln, aber jedes Fragment unterscheidet sich von dem anderen."
        "In dem einen Fragment hast du dir Nudeln zum Mittagessen gemacht, in einem anderen hast du dir stattdessen was zu Essen bestellt."
        extend " ...Oder in einer Welt wurdest du von einem Auto überfahren und in der anderen, hat das Auto dich knapp verfehlt."
        extend " Jedes Fragment ist einzigartig und definitiv wert mal im See der Fragmente besucht zu werden."
        stop music fadeout 5
        $ songname = "-"
        "Bernkastels Aura fängt plötzlich an sich zu verändern, ihre Gleichgültige Aura veränderte sich plötzlich in etwas undefinierbares."
        $ songname = "Witch of the Painting"
        if persistent.showbgm == True:
                show screen showsong
        play music "audio/bgm/umib_026_intro.ogg"
        queue music "audio/bgm/umib_026_loop.ogg" loop
        extend " ...Beato ist das sofort aufgefallen, es ist plötzlich ein dezenter Hauch von Angst in der Luft."
        ber "“Ganz weit draußen auf der höchsten Ebene....." 
        extend " .....Sogar noch höher als Auauaus Territorium befinden sich die Ebene der grenzenlosen Götter und Schöpfer."
        extend " ...Es heißt zwar dort befinden sich 'die' Grenzenlosen Götter und Schöpfer, aber das ist falsch."
        scene different_space_2a with gradientcirclefade
        ber "Es gibt nicht die Götter und die Schöpfer," 
        extend " sondern es gibt nur einen einzigen."
        extend " Dieser eine Gott ist auch der Schöpfer unserer Welt."
        ber "Diese Gottheit soll sogar mal ein einfacher Mensch gewesen sein.”"
        scene black with quickgradientwipedown
        scene different_space_1a at bgani
        show expression(CustomParticles("images/system/particle.png", 10))
        show bea a11futeki2 at r 
        with quickgradientwipedown
        bea "“*gacker*gacker*...!"
        extend " ....Ihr wollt mir also erzählen, dass es einen Schöpfergott gibt, der mal ein einfacher Mensch gewesen sein soll?"
        extend a11akuwarai2 " ....Ahahaahaha,"
        extend " ...Das ist wahrhaftig amüsant," 
        extend " ....wie soll ein Schöpfergott ein Mensch gewesen sein, wenn er diese Welt erst erschaffen musste?”"
        show ber a21shian1 at l with dis
        ber "“...Das ist ganz einfach..."
        extend " ...Bevor er unser Universum erschaffen hat, gab es ein einziges Fragment, dass ziellos im ewigen nichts umher wanderte."
        extend " ...Nein, er kam aus seinem Universum hier her und fand absolut gar nichts vor." 
        extend " Er fand Null vor."
        ber "Es gab nur ihn und sein Fragment, dass in eine leere Welt geschleudert wurde." 
        extend " ....Das Urfragment."
        extend a21defo1 " ...Er hat es irgendwie geschafft als aller erstes Individum aus der Menschenwelt zu entkommen und baute diese Welt auf."
        extend " ...Er war es der vor einer Quadrillion Jahren, die Ebenen der Metawelt erschaffen hat und auch der, der Auauau erschaffen hat.”"
        ber "So lauten die Überlieferungen, die innerhalb der Hexen und Dämonen seit mehreren Milliarden Jahren weitergegeben wurden."
        extend " ...Natürlich gibt es keinen Beweis, dass diese Gottheit wirklich existiert..."
        extend " ....Ich habe in meiner Lebensspanne als Hexe im See der Fragmente auch nie ein derartiges Fragment gefunden, dass man als das Urfragment bezeichnen könnte."
        ber a21defo2 "Das Konzept eines Urfragments in einem See voller Parallelwelten entzieht sich auch jeglicher Logik."
        extend " ...Es kann nicht die eine 'Erste Welt' geben, denn so funktionieren Parallelwelten nicht."
        extend " ...Jedoch, hat Auauau mir einmal eine Antwort gegeben...."
        extend " ...Sie sagte mir einmal..."
        play sound "audio/sfx/umise_059.ogg"
        extend " ...'Für den von der Null erwählten, ist das Konzept der Existenz obsolet.'”"
        bea a11warai1 "Der von der Null erwählte?"
        extend " ...Wie überaus interessant."
        extend " ...Diese Gottheit ist trotzdem absolut beeindruckend, er scheint eine so unglaublich starke Macht zu besitzen, dass er ein nahezu unendliches Universum aus dem nichts erschaffen konnte."
        extend " ...Zu gerne würde ich diesen Gott einmal treffen, auch wenn es mir das Blut in den Adern gefrieren würde und es mich auf der Stelle vernichten würde.”"
        ber "“Sei nicht dumm..."
        extend " ...Er würde dich nicht mal bemerken, er hat nichts für unbedeutene Hexen wie dich und mich übrig.”"
        bea a11gaman4 "“Das ist hart, selbst für eine legendäre Hexe wie Ihr es seid.”"
        ber a21shian1  "“Dadurch dass er diese Welt und seine Regeln erschaffen hat, besitzt er eine unglaubliche Macht, die nicht mal Auauau besitzt."
        extend " Er hat die Macht von Null. Er kontrolliert die Null von der jede Hexe träumt sie zu kontrollieren."
        extend " ...Er ist der, der die Limits von Null durchbrochen hat.”"
        bea a11futeki2 "“Oho," 
        extend " ....ein Individum, dass alle Hexen in den Schatten stellt, klingt mehr als nur beängstigend."
        extend " ...Ein Individum, dass selbst mein Spiel mit leichtigkeit gewinnen könnte...”"
        ber a21warai4 "“Er würde dein Spiel in eine Quadrillion Stücke zerteilen, wieder zusammensetzen, die Regeln ändern, es eine Milliarde Jahre spielen und dann in die nächst gelegene Mülltonne werfen und dich auslöschen.”"
        play sound "audio/sfx/umise_056.ogg"
        hide ber with witchfadeoutq
        scene black with quickergradientwiperight
        scene g1f_s1bp at bgani
        show expression(CustomParticles("images/system/particle.png", 10))
        with quickergradientwiperight
        play sound "audio/sfx/umise_052.ogg"
        show ber a21shian1 at leftedge with witchfadeinq
        "Plötzlich teleportierte sie sich in eine andere Ecke des Raumes um sprach mit ernster und direkter Stimme."
        ber a21defo1 "“Diese Gottheit, hat keinen Namen, aber da er die Macht der Null besitzt nennt man ihn nur"
        play sound "audio/sfx/umise_021.ogg"
        extend " ....Fürst Zero die Göttliche Null."
        ber "Du kannst dir seine Macht so vorstellen, egal wie oft du mit deiner Endlosen Magie ein Individum zerteilst, es wird niemals zur Null."
        extend " ...Es ist egal, ob ich Wunder kontrolliere, Zero kann mir die Kontrolle entreißen."
        ber "Selbst wenn etwas definitiv garantiert wird, Zero kann der absoluten Gewissheit entgehen."
        extend " ...Völlig irrelevant, was Auauau duldet und sich ansieht, Zero kann das Narrativ unwiderruflich umschreiben oder für alle Zeiten ausradieren."
        ber "Es ist die gewaltige Macht ein Individum auf Null zu setzen.”"
        play sound "audio/sfx/umise_052.ogg"
        show bea a11futeki1 at r with witchfadeinq
        bea "“In anderen Worten, wenn Zero ein Individum auf Null setzt, wird nicht nur die Existenz ausgelöscht, absolut alle Erinnerungen an diese Existenz werden ebenfalls ausgelöscht."
        extend " ...So als hätte es dieses Individum niemals gegeben."
        ber a21akuwarai2 "“Das versteht doch selbst die größte Dumpfbacke mit den kleinsten Gehirnzellen."
        extend " ...Die einzige Möglichkeit gegen Zero gewinnen zu können ist es, wenn er Spielregeln befolgen muss."
        extend " ..Diese Regel gilt ebenfalls auch für alle Hexen."
        extend " Wenn alle ihre Kräfte uneingeschränkt nutzen könnten, wären alle Hexen bereits vor Langeweile gestorben..."
        extend " ...Und Hexen hassen Langeweile über alles."
        ber a21warai4 "Hexen spielen Spiele gegen andere Hexen um der Langeweile zu entkommen, denn das ist das, was Hexen töten kann.”"
        bea a11defo2 "“...Das bedeutet also, er müsste mein Spiel nach den gesetzten Regeln spielen und kann nicht einfach mit seiner Macht schummeln?”"
        play sound "audio/sfx/umise_037.ogg"
        ber a21akuwarai2 "“....Ahahahaha!! ahahahaha!!!"
        extend " ...Als hätte eine Gottheit es nötig bei deinem niederen Spiel zu schummeln!"
        extend " ...Rokkenjima wäre für ihn nur wie Mensch ärgere dich nicht zu spielen!!"
        extend " ...Er würde dich nicht mal am Spiel teilnehmen lassen, ohne dass du es überhaupt merkst!!!”"
        play sound "audio/sfx/umise_037.ogg"
        ber a21akuwarai3 "....Ahaha...."
        extend " ...Ahahahahahahahahahah!!!"
        play sound "audio/sfx/umise_037.ogg"
        bea a11akuwarai4 "“....Kyahahahahahahaahahahah!!!"
        extend " ....Kyahahah hahahahahaha!!!!"
        extend " Wie überaus unterhaltsam, das gefällt mir!"
        extend " ...Wenn er wirklich nach meinen Regeln spielen muss, würde ich es gerne mal ausprobieren."
        bea "Zu gerne würde ich sehen, wie er meine Seele mit Leichtigkeit und einem einzigen Fingerschnipsen zermalmt, bis nichts mehr übrig ist!”"
        ber a21warai4 "“*giggle*giggle*"
        play sound "audio/sfx/umise_056.ogg"
        hide ber with witchfadeout
        scene black with quickgradientwipeup
        scene different_space_1c
        show expression(CustomParticles("images/system/particle.png", 10))
        with quickgradientwipeup
        play sound "audio/sfx/umise_052.ogg"
        show ber a11defo1 at m with witchfadein
        ber "Es wird Zeit sich zu verabschieden, denn ich bin keine Hexe die lange an einem Ort bleibt."
        extend " ...Ich werde weiter durch den See der Fragmente wandern und versuchen meiner Langeweile zu entkommen.”"
        scene black with quickgradientwipedown
        scene g1f_s1ap at bgani
        show bea a11warai1 at m
        with quickgradientwipedown
        bea "“Die Freude war ganz meinerseits, Großes Fräulein Bernkastel."
        extend " ...Das nächste Spiel wird in den nächsten Tagen beginnen, schaut doch bei Gelegenheit mal vorbei.”"
        scene black with quickgradientwipeup
        scene different_space_1c
        show expression(CustomParticles("images/system/particle.png", 10))
        show ber a11defo2 at m
        with quickgradientwipeup
        pause 1.5
        play sound "audio/sfx/umise_056.ogg"
        hide ber with witchfadeoutq
        stop music fadeout 5
        $ songname = "-"
        "Ohne auf die Einladung zu reagieren verschwand Bernkastel ins nichts und zurückblieb nur Beato."
        extend " ...Plötzlich spürte Beato eine seltsam unangenehme Präsenz, sie ist zwar nicht sehr stark, aber trotzdem ziemlich unangenehm."
        scene black with quickgradientwipedown
        scene g1f_s1ap at bgani
        show bea a11akuwarai5 at m
        with quickgradientwipedown
        bea "“Hoh?"
        extend " ...Etwa noch ein Besucher aus dem See der Fragmente?"
        bea "Es ist definitiv nicht Battler oder Fräulein Lambdadelta..."
        extend " ...Es ist auch nicht die Oberinquisitorin"
        extend " ... Wer auch immer das ist, Ich hoffe, dass mein Gast schwarzen Tee mag."
        extend " *gacker*gacker*...!”"
        window hide
        pause 2.0
        play sound "audio/sfx/umise_056.ogg"
        scene black with gradientcirclefade
        pause 3
        show screen clockch2_1
        play sound "<from 0 to 2>/audio/sfx/umilse_1050.ogg"
        pause 7
        hide screen clockch2_1



        













