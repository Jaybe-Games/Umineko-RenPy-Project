label umi1_1:
    $ chapter = _("Rokkenjima")
    $ menuchapter = _("""Episode1 Chapter1
Rokkenjima""")
    $ save_name = _("Episode1 Legend of the Golden Witch\nRokkenjima")
    $ show_chapter = _("""Episode1 Legend of the Golden Witch
Chapter 1: Rokkenjima""")
    $ _game_menu_screen = "cleanmenu"
    $ persistent.ep1started = True
    $ persistent.new = False
    show mlib_1b_bg at bgani
    show rainbackscroll
    show mlib_1b at bgani
    with gradientcirclefade
    $ play_music(thunberg_lily)
    window show
    "Watch her breakup with terrible performance"
    window hide
    play sound umise_052
    show bea_bri at m
    pause 5
    hide bea_bri
    show bea at m
    window show
    voice "audio/voice/bea_01.ogg"
    bea v001 "Try to solve Kinzo's Epitaph, you god damn idiots!"
    window hide
    hide bea
    show bea_bro at m
    pause 5
    "Two older men could be observed in a darkened and foul-smelling study."
    extend " While one of them examined his magnificent glass with a poisonous green alcoholic drink, he began to speak with a grim expression."
    $ kin_pose = "a11"
    $ kin_face = "badmood1"
    show kin at m
    kin "....Nanjo..."
    extend " ....how much longer do I have to live?"
    window hide
    pause 0.2
    scene mlib_1a_bg at bgani
    show rainbackscroll
    show mlib_1a at bgani
    $ nan_pose = "a1"
    $ nan_face = "hmm1"
    with quickergradientwipeleft
    show nan at l
    pause 0.2
    window show
    nan "............"
    "Nanjo, couldn't get a word out, but the man who wanted to know how long he had to live still got his answer."
    $ kin_pose = "a11"
    $ kin_face = "default1"
    show kin at r
    kin "...Hmpf."
    extend " Not long, then..."
    window hide
    play audio umise_020
    camera at vpunch
    pause 0.25
    scene black with instant
    play audio umise_1006
    "Suddenly he dropped his glass and began to throw a sorrowful tantrum."
    scene mlib_1b_bg at bgani
    show rainbackscroll
    show mlib_1b at bgani
    $ kin_pose = "a13"
    $ kin_face = "cry2"
    show kin at m
    camera at zoomin
    with quickergradientwipeleft
    pause 0.2
    window show
    kin "But this cannot be my death..."
    extend " I'll not allow death to claim me until I have seen her smile once again!!"
    $ kin_pose = "a23"
    $ kin_face = "cry1"
    kin "Come to me again..."
    extend " Come to me and smile...!!"
    window hide
    play audio umise_027
    pause 0.8
    scene beato at bgani with flash
    show screen show_chapter
    pause 0.2
    window show
    kin "BEATRICE!!!"
    window hide
    pause 2
    stop music fadeout 2
    pause 2
    hide screen show_chapter
    scene black 
    with dissolve
    $ renpy.movie_cutscene("videos/pc_op.mkv")
    "This boat is charting a course..."
    extend " ...For Rokkenjima, an island in the Izu archipelago, south of Tokyo."
    extend " It's a small island six miles across, owned by the wealthy Ushiromiya Family."
    "The traditional annual family gathering is nearly upon us."
    extend " And it is for this purpose that the ten of us enjoy our pleasant cruise..."
    extend " Our pleasant..."
    but "...Wai-"
    extend " This is too fast!"
    but "Is it just me, or are we going dangerously fast?"
    but "I AM GONNA FALL OVEEERRRRRRRRR!!!!!!!!"
    "For personal reasons, I've been largely estranged from the rest of the family for some time."
    "...I never actually dreamed that my first family gathering in six years would involve a baptism..."
    jes "Consider yourself lucky, Battler! The captain bumped down the speed just for you!"
    extend " Still, you should see yourself! Hee-Hee-Ha-Ha-Ha!!"
    jes "Six years later, you're about twice the size you used to be, but as helpless as ever on a moving vehicle!"
    extend " Bwa-ha-ha-ha-ha!"
    but "Shut up, Jessica!"
    jes "And you're supposed to be an eighteen-year-old man?"
    extend " Pathetic!"
    jes "I guess your courage and your twig and berries are the same size they were when you were a kid!, pfff!"
    "This girl who seems entirely unsuited to her role as the lofty daughter of a proud and powerful family is Jessica."
    "She's my cousin, born the same year as me."
    but "Damn you, Jessica..."
    extend " So you think you're the only one who's a grownup now...?"
    but "How about I perform a little exermination..."
    extend " ...to see how much you've grown?"
    jes "....Nh!!"
    "Battler managed to touch her breasts with his fingertips but after he did, Jessica smacked him on the head"
    jes "Dammit! You brushed my chest."
    extend " I miscalculated how much your reach would have grown in six years...!"
    mar "Uuu."
    extend " Battler wiped out."
    "While Battler was lying on the floor because of Jessica's smack, a little girl knelt in front of him and stroked his head."
    but "Hey, Maria."
    extend " You're right... Battler's all wiped out."
    extend " Thanks for caring, kid."
    mar "uuu."
    "Maria's another cousin I haven't seen in six years. She's an adorable little sweetheart!"
    but "Here we go! Princess gets a piggyback ride!"
    extend " hmpff...hnn..."
    mar "uuu!!"
    extend " Battler, Battler!! Uuu, Uuu!!"
    but "You said it!"
    extend " Maria, Maria!! Uuu, Uuu!!"
    but "Make sure you don't grow into a tomboy like Jessica, Maria!"
    extend " You'll be a graceful lady and let me touch your boobs whenever I want! Got that? It's a promise!"
    mar "Uuu! I'll let you! I promise!"
    extend " uuuu!!"
    "Suddenly there is another smack, Jessica has hit Battler over the head again with great vigour."
    jes "You sick bastard!"
    extend " Don't fill her head with that nonsense! You know Maria will take it seriously!"
    mar "Uuu! He can touch them! I promised"
    extend " Maria always keeps promises! Uuuu!"
    jes "And I'm telling you not to make promises like that, Maria! The deal's off!"
    geo "You shouldn't make promises like that."
    extend " And don't tease her with that nonsense, Battler-kun."
    but "George-aniki!"
    "Suddenly George-aniki came to explain the situation to Maria in a way she could understand and at the same time put a verbal blow to me."
    jes "You should follow George-niisan's example and be more of an intellectual."
    geo "Me?"
    extend "Ha-ha-ha! Oh I'm not that special."
    "George is an oler cousin. Very smart, with a top-class education and a good head for business."
    extend " He's a far cry from me, A guy with not future and no dreams."
    but "You and I should try to bottle some of Aniki's magic later, Jessica."
    extend " yeah, yeah."
    jes "Shut the hell up!"
    extend " Whaaat? were you just subtly insulting me?"
    jes "With Battler-kun around, it finally feels like we've got all the cousins together! Nice and lively."
    geo "He provides that extra measure of comedy."
    mar "Uuu! This year will be the most fun of all! Uuu!"
    but "I agree with you there! Hee Hee!"
    "It's like that six-year gap never happened."
    but "Maria, when you dry out jellyfish, they turn into mushrooms."
    jes "Don't listen to him!"
    "This kind of contact with distant family members is different from interacting with friends."
    extend " All in all ...I kinda like it."
    mar "Uuu! Battler, I see the dock! I see the dock!"
    but "Ohh, where, where?"
    "The boat has reached the island and is heading straight into the bay, with huge cliffs to the left and right - a fall from these cliffs would probably be fatal."
    mar "......."
    but "What's wrong Maria?"
    "Maria, who was just having a lot of fun with her cousins, has suddenly gone eerily quiet and her gaze is nailed to a cliff."
    mar "Uuu..."
    extend "It's gone."
    but "..Hmm?"
    mar "It's gone, It's gone!!"
    extend " Uuu!! Uuu, uuu!!"
    "Suddenly Maria threw her arm up, pointed in the air and started shouting loudly"
    but "What's wrong, Maria? Did you lose something?"
    extend " I'll help you look for it. What's missing?"
    extend " .....?"
    but "......Wait..."
    extend " Wasn't there a little Torii gate over that small outcropping there..?"
    but "Yeah, there was. I remember it because it was the first landmark you saw on the island."
    geo "Yes, I remember too. The island's Shinto Shrine and the Torii archway over it."
    extend " It's not there anymore... I'm pretty sure I saw it last year..."
    mar "Gone!! Gone!!"
    extend "Uuu, uuu!"
    but "Probably got swept away by waves or something, right? Maybe it had been weakened by exposure to elements."
    extend " It must have disappeared this summer. I'm also guessing the waves must have knocked it into the water..."
    kum "Ho ho ho..."
    extend "I wish it had been just that..."
    but "Kumasawa-baachan... Do you know what happened?"
    kum "Indeed..."
    kum "A great Bolt of lightning struck the shrine one night and blasted it to pieces..."
    extend " The fishermen wisper and tremble, calling this an omen of disaster..."
    extend " Heaven be merciful..."
    mar "An omen of disaster..."
    extend " Uuu..." # Ab 023
