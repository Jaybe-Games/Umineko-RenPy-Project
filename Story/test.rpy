label test:
    $ st = 0.0
    pause (3)
    scene different_spiral_1a with dissolve
    pause (2)
    scene different_space_1a with gradientcirclefade
    pause (1)
    play sound "audio/sfx/umise_052.ogg"
    $ play_music(pitiful)
    show ber_a21_warai1 at l,ah('ber') with witchfadein
    pause 1
    ber "Yes..."
    extend " Black tea is indeed the best tea for a witch..."
    extend " especially with dried plums..."
    play sound "audio/sfx/umise_052.ogg"
    show bea_a11_defo2 at r, ah('bea') with witchfadein
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
    scene black with gradientcirclefade
    stop music fadeout 2.0
    pause (3)
    jump test
