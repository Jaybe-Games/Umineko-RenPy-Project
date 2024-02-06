label test:
    $ discord.update(state = "testscene")
    $ discord.update(details = "testing something")
    $ chaptername = "“testscene”"
    $ chapternumber = "none"
    window auto
    pause (3)
    scene different_spiral_1a with dissolve
    pause (2)
    scene cha_i1ip at bgani with gradientcirclefade
    pause (1)
    play sound "audio/sfx/umise_052.ogg"
    $ songname = "goldenslaughterer"
    $ play_music(goldenkiller)
    queue music "audio/bgm/umib_024_loop.ogg" loop 
    show ber_a21_warai1 behind rain4 at l,ah('ber') with witchfadein
    pause 1
    ber "“Yes..."
    extend " Black tea is indeed the best tea for a witch..."
    extend " especially with dried plums...”"
    window hide
    call butterfly1 from _call_butterfly1_1
    play sound "audio/sfx/umise_052.ogg"
    show bea_a11_defo2 behind rain4 at r, ah('bea') with witchfadein
    pause 1
    window show
    bea "“...Indeed"
    extend " ...This black tea is simply a delicacy to enjoy."
    extend " .....I bought the best black tea in Japan to please you...”"
    ber "“...You just bought the one that goes for 200 yen a pack."
    extend " ...But that's fine..." 
    extend " {red_truth}It's my favorite kind of tea.{/red_truth}”"
    bea "“I am very comforted by this Great Lady Bernkastel”"
    window hide
    play sound "audio/sfx/umise_052.ogg"
    hide bea_a11_defo2 with witchfadeout
    pause 1
    call hidebf1 from _call_hidebf1_1
    window show
    $ play_music(kuina)
    ber "“...*giggle*giggle*"
    extend "....Whatever you say...”"
    play sound "audio/sfx/umise_052.ogg"
    window hide
    hide ber_a21_warai1 with witchfadeout
    pause 1
    play sound "audio/sfx/umise_057.ogg"
    #stop music
    scene black with flash
    jump gameresult
