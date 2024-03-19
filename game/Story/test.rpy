label test:
    window auto
    $ _game_menu_screen = "cleanmenu"
    scene cha_i1ip at bgani
    pause (1)
    show bea at m
    pause 3
    "Look at Beato she can move her lips I guess lol..."
    ## Plays the voice
    voice "audio/voice/bea/bea_01.ogg"
    ## Shows the Animation
    bea bea_01 "Hi, I am Justin and I am voicing BEAT-RICE!"
    $ bea_face = "akuwarai5"
    voice "audio/voice/bea/bea_02.ogg"
    extend bea_02 " Hahahahahahahaha!!!"
    show bea bea_idle
    "Just in case something weird happens"
    "Hope it's not broken lol"
    jump test

