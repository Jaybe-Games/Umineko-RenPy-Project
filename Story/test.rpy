label test:
    $ discord.update(state = "testscene")
    $ discord.update(details = "testing something")
    $ chaptername = "\"testscene\""
    $ chapternumber = "none"
    pause (3)
    scene different_spiral_1a with dissolve
    pause (2)
    scene different_space_1a with gradientcirclefade
    play rain "audio/sfx/umilse_012.ogg" fadein 1.0
    show rain
    pause (1)
    play sound "audio/sfx/umise_052.ogg"
    $ songname = "Pitiful Sneerer"
    $ play_music(pitiful)
    show ber_a21_warai1 behind rain at l,ah('ber') with witchfadein
    pause 1
    ber "Yes..."
    extend " Black tea is indeed the best tea for a witch..."
    extend " especially with dried plums..."
    play sound "audio/sfx/umise_052.ogg"
    show bea_a11_defo2 behind rain at r, ah('bea') with witchfadein
    pause 1
    bea "...Indeed"
    extend " ...This black tea is simply a delicacy to enjoy."
    extend " .....I bought the best black tea in Japan to please you..."
    ber "...You just bought the one that goes for 200 yen a pack."
    extend " ...But that's fine..." 
    extend " It's my favorite kind of tea."
    bea "I am very comforted by this Great Lady Bernkastel"
    play sound "audio/sfx/umise_052.ogg"
    hide bea_a11_defo2 with witchfadeout
    pause 1
    ber "...*giggle*giggle*"
    extend "....Whatever you say..."
    play sound "audio/sfx/umise_052.ogg"
    hide ber_a21_warai1 with witchfadeout
    pause 1
    call chapterendb
    call clockch2
    jump test
