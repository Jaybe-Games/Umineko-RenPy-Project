screen showsong():
    zorder 999999

    ## Shows current song on screen
    $ current_music = renpy.music.get_playing('music')
    if current_music is not None and current_music in music_dictionary:
        text "♪" + music_dictionary[current_music] size 40 xalign 0.05 yalign 0.01 font "fonts/AOTFShinGoProMedium.otf" outlines [ (absolute(3), "#000", absolute(0), absolute(0)) ] at songflyin, bgm_gradient
    else:
        text "" size 40 xalign 0.05 yalign 0.01 font "fonts/AOTFShinGoProMedium.otf" outlines [ (absolute(3), "#000", absolute(0), absolute(0)) ] at songflyin, bgm_gradient

    timer 8 action Hide('showsong')

default persistent.audio_cues = True

init python:

    thunberg_lily = "audio/bgm/umib_001.ogg"
    door_of_summer = "audio/bgm/umib_002.ogg"
    hane = "audio/bgm/umib_003.ogg"
    ride_on = "audio/bgm/umib_004.ogg"
    sea = "audio/bgm/umib_005.ogg"
    hour_of_darkness = "audio/bgm/umib_006.ogg"
    novelette = "audio/bgm/umib_007.ogg"
    hope = "audio/bgm/umib_008.ogg"
    white_shadow = "audio/bgm/umib_009.ogg"
    steady_pace = "audio/bgm/umib_010.ogg"
    towering_cloud_in_summer = "audio/bgm/umib_011.ogg"
    moonlit_night = "audio/bgm/umib_012.ogg"
    rose = "audio/bgm/umib_013.ogg"
    at_deaths_door = "audio/bgm/umib_014.ogg"
    hells_halls = "audio/bgm/umib_015.ogg"
    fortitude = "audio/bgm/umib_016.ogg"
    witch_in_gold_cembalo = "audio/bgm/umib_017.ogg"
    beckoning = "audio/bgm/umib_018.ogg"
    fishy_aroma = "audio/bgm/umib_019.ogg"
    stupefaction = "audio/bgm/umib_020.ogg"
    praise = "audio/bgm/umib_021.ogg"
    bgm_pass = "audio/bgm/umib_022.ogg"
    butterfly = "audio/bgm/umib_023.ogg"
    goldenslaughterer = "audio/bgm/umib_024.ogg"
    worldend_bp = "audio/bgm/umib_025.ogg"
    the_witch_of_the_painting = "audio/bgm/umib_026.ogg"
    suspicion = "audio/bgm/umib_027.ogg"
    scar_in_the_score = "audio/bgm/umib_028.ogg"
    core = "audio/bgm/umib_029.ogg"
    minute_darkness = "audio/bgm/umib_030.ogg"
    nighteyes = "audio/bgm/umib_031.ogg"
    closed_my_heart = "audio/bgm/umib_032.ogg"
    requiem = "audio/bgm/umib_033.ogg"
    mind = "audio/bgm/umib_034.ogg"
    worldend = "audio/bgm/umib_035.ogg"
    _play = "audio/bgm/umib_036.ogg"
    system0 = "audio/bgm/umib_037.ogg"
    voiceless = "audio/bgm/umib_038.ogg"
    dead_angle = "audio/bgm/umib_039.ogg"
    organ_short_600_million_in_c_minor = "audio/bgm/umib_040.ogg"
    prison_strip = "audio/bgm/umib_041.ogg"
    string_quartet_1_in_g_major_allegro = "audio/bgm/umib_042.ogg"
    cage = "audio/bgm/umib_043.ogg"
    golden_sneer = "audio/bgm/umib_044.ogg"
    scorpion_guts = "audio/bgm/umib_045.ogg"
    lifes_end_verc = "audio/bgm/umib_046.ogg"
    answer = "audio/bgm/umib_047.ogg"
    answer_short = "audio/bgm/umib_048.ogg"
    melody_inst_ver = "audio/bgm/umib_049.ogg"
    red_dread = "audio/bgm/umib_050.ogg"
    moon = "audio/bgm/umib_051.ogg"
    where = "audio/bgm/umib_052.ogg"
    dread_of_the_grave = "audio/bgm/umib_053.ogg"
    worldend_dominator = "audio/bgm/umib_054.ogg"
    black_liliana = "audio/bgm/umib_055.ogg"
    rest = "audio/bgm/umib_056.ogg"
    end_of_a_daydream = "audio/bgm/umib_057.ogg"
    melody = "audio/bgm/umib_058.ogg"
    over_the_sky = "audio/bgm/umib_059.ogg"
    sunny_spot = "audio/bgm/umib_060.ogg"
    the_candles_dance = "audio/bgm/umib_061.ogg"
    distant = "audio/bgm/umib_062.ogg"
    psy_chorus = "audio/bgm/umib_063.ogg"
    far = "audio/bgm/umib_064.ogg"
    red_shoes_fake = "audio/bgm/umib_065.ogg"
    mother = "audio/bgm/umib_066.ogg"
    haze = "audio/bgm/umib_067.ogg"
    dancing_pipe = "audio/bgm/umib_068.ogg"
    dread_of_the_grave_more_fear = "audio/bgm/umib_069.ogg"
    organ_short_200_million_in_c_minor = "audio/bgm/umib_070.ogg"
    rhythm_changer = "audio/bgm/umib_071.ogg"
    happiness_of_marionette_bonus = "audio/bgm/umib_072.ogg"
    happiness_of_marionette = "audio/bgm/umib_073.ogg"
    dance_of_the_moon_rabbits = "audio/bgm/umib_074.ogg"
    melting_away = "audio/bgm/umib_075.ogg"
    soul_of_soul = "audio/bgm/umib_076.ogg"
    miragecoordinator = "audio/bgm/umib_077.ogg"
    prison = "audio/bgm/umib_078.ogg"
    thanks_for_being_born = "audio/bgm/umib_079.ogg"
    wings = "audio/bgm/umib_080.ogg"
    paradise_lost = "audio/bgm/umib_081.ogg"
    wingless = "audio/bgm/umib_082.ogg"
    activepain = "audio/bgm/umib_083.ogg"
    dread_of_the_grave_rhythm_ver = "audio/bgm/umib_084.ogg"
    eternity = "audio/bgm/umib_085.ogg"
    over = "audio/bgm/umib_086.ogg"
    like_the_gale = "audio/bgm/umib_087.ogg"
    f_style = "audio/bgm/umib_088.ogg"
    monochrome_clock = "audio/bgm/umib_089.ogg"
    apathy = "audio/bgm/umib_090.ogg"
    mystic_forest = "audio/bgm/umib_091.ogg"
    sakutarous_adventure = "audio/bgm/umib_092.ogg"
    parallel = "audio/bgm/umib_093.ogg"
    five_hundred_ninety_nine_million_ruins = "audio/bgm/umib_095.ogg"
    happy_maria_instrumental = "audio/bgm/umib_096.ogg"
    surrounding = "audio/bgm/umib_097.ogg"
    open_fire = "audio/bgm/umib_098.ogg"
    death_from_stupefaction = "audio/bgm/umib_099.ogg"
    mortal_stampede = "audio/bgm/umib_100.ogg"
    victima_propiciatoria = "audio/bgm/umib_101.ogg"
    revolt = "audio/bgm/umib_102",
    purgatory_catastrophe_rhapsodie = "audio/bgm/umib_103.ogg"
    happy_maria = "audio/bgm/umib_104.ogg"
    dive_to_emergency = "audio/bgm/umib_105.ogg"
    _dir = "audio/bgm/umib_106.ogg"
    endless_nine = "audio/bgm/umib_107.ogg"
    dreamenddischarger = "audio/bgm/umib_108.ogg"
    discotheque = "audio/bgm/umib_109.ogg"
    twirl = "audio/bgm/umib_110.ogg"
    future = "audio/bgm/umib_111.ogg"
    deep_blue_jeer = "audio/bgm/umib_112.ogg"
    the_great_detective_knows = "audio/bgm/umib_113.ogg"
    smileless_soiree = "audio/bgm/umib_114.ogg"
    one = "audio/bgm/umib_115.ogg"
    spiral = "audio/bgm/umib_116.ogg"
    string_trio_600_million_in_f_sharp_minor = "audio/bgm/umib_117.ogg"
    totenblume = "audio/bgm/umib_118.ogg"
    justice = "audio/bgm/umib_119.ogg"
    aci_l = "audio/bgm/umib_120.ogg"
    predator = "audio/bgm/umib_121.ogg"
    proud_dust = "audio/bgm/umib_122.ogg"
    hello_your_dream = "audio/bgm/umib_123.ogg"
    a_lonely_deep_sea_fish = "audio/bgm/umib_124.ogg"
    the_girls_witch_hunt = "audio/bgm/umib_125.ogg"
    patchwork_chimera = "audio/bgm/umib_126.ogg"
    discolor = "audio/bgm/umib_127.ogg"
    resurrectedreplayer = "audio/bgm/umib_128.ogg"
    final_answer = "audio/bgm/umib_129.ogg"
    light = "audio/bgm/umib_130.ogg"
    bread_of_life = "audio/bgm/umib_131.ogg"
    promise = "audio/bgm/umib_132.ogg"
    tomorrow = "audio/bgm/umib_133.ogg"
    wings_ver_hope = "audio/bgm/umib_134.ogg"
    fake_gray_smile = "audio/bgm/umib_135.ogg"
    eternal_chains = "audio/bgm/umib_136.ogg"
    love_examination = "audio/bgm/umib_137.ogg"
    instant = "audio/bgm/umib_138.ogg"
    look_back = "audio/bgm/umib_139.ogg"
    blue_butterfly = "audio/bgm/umib_140.ogg"
    my_dear = "audio/bgm/umib_141.ogg"
    somethings_up_going_down = "audio/bgm/umib_142.ogg"
    rog_limitation = "audio/bgm/umib_143.ogg"
    waltz_op34 = "audio/bgm/umib_144.ogg"
    alive = "audio/bgm/umib_145.ogg"
    birth_of_new_witch_inst = "audio/bgm/umib_146.ogg"
    ruriair = "audio/bgm/umib_147.ogg"
    engage_of_marionette = "audio/bgm/umib_148.ogg"
    life = "audio/bgm/umib_149.ogg"
    loreley = "audio/bgm/umib_150.ogg"
    the_sin = "audio/bgm/umib_151.ogg"
    the_first_and_the_last = "audio/bgm/umib_152.ogg"
    anti_demon_sequentia = "audio/bgm/umib_153.ogg"
    battle_field = "audio/bgm/umib_154.ogg"
    rebirth = "audio/bgm/umib_155.ogg"
    the_way = "audio/bgm/umib_156.ogg"
    liberatedliberator = "audio/bgm/umib_157.ogg"
    thanks_for_all_people = "audio/bgm/umib_158.ogg"
    infant_queen_bee = "audio/bgm/umib_159.ogg"
    birth_of_new_witch_short_ver = "audio/bgm/umib_160.ogg"
    fishyaroma = "audio/bgm/umib_161.ogg"
    le4_octobre = "audio/bgm/umib_162.ogg"
    ld_circulation = "audio/bgm/umib_163.ogg"
    reflection_call = "audio/bgm/umib_164.ogg"
    rain = "audio/bgm/umib_165.ogg"
    _7_weights = "audio/bgm/umib_166.ogg"
    fall = "audio/bgm/umib_167.ogg"
    bore_ral = "audio/bgm/umib_168.ogg"
    ballade_continuer = "audio/bgm/umib_169.ogg"
    song_without_a_name_ver2007_inst = "audio/bgm/umib_170.ogg"
    lie_alaia = "audio/bgm/umib_171.ogg"
    golden_nocturne_inst = "audio/bgm/umib_172.ogg"
    far_flat = "audio/bgm/umib_173.ogg"
    toybox = "audio/bgm/umib_174.ogg"
    terminal_entrance = "audio/bgm/umib_175.ogg"
    puppet_show = "audio/bgm/umib_176.ogg"
    s_he_end = "audio/bgm/umib_177.ogg"
    song_without_a_name_full_inst = "audio/bgm/umib_179.ogg"
    the_end_of_the_world = "audio/bgm/umib_180.ogg"
    goddess_gardena = "audio/bgm/umib_181.ogg"
    ridicule = "audio/bgm/umib_183.ogg"
    yomotsu_hirasaka_corruption = "audio/bgm/umib_184.ogg"
    the_executioner = "audio/bgm/umib_185.ogg"
    song_without_a_name_ver_sakura_ed_size = "audio/bgm/umib_186.ogg"
    stuffed_animal = "audio/bgm/umib_187.ogg"
    bizarre_divertimento = "audio/bgm/umib_188.ogg"
    en_counse = "audio/bgm/umib_190.ogg"
    lixAxil = "audio/bgm/umib_191.ogg"
    revelations_inst = "audio/bgm/umib_192.ogg"
    flying = "audio/bgm/umib_193.ogg"
    lastendconductor = "audio/bgm/umib_194.ogg"
    revelations = "audio/bgm/umib_195.ogg"
    cocoon_of_white_dreams = "audio/bgm/umib_240.ogg"
    when_the_seagulls_cry = "audio/bgm/umib_241.ogg"
    suisui_sweets = "audio/bgm/umib_1000.ogg"
    bring_the_fate = "audio/bgm/umib_1010.ogg"
    bring_the_fate_ver_chiru = "audio/bgm/umib_1013.ogg"
    tsurupettan = "audio/bgm/umib_94.ogg"
    system0_original_version = "audio/bgm/umib_1011.ogg"
    igreja_of_echoing_vows = "audio/bgm/umib_1012.ogg"
    inannas_dream = "audio/bgm/umib_1014.ogg"
    the_witch_of_occultics = "audio/bgm/umib_1017.ogg"
    the_pithos_in_the_fog = "audio/bgm/umib_1018.ogg"


    ## Add them to the dictionary
    music_dictionary = {
        thunberg_lily : "Thunberg Lily",
        door_of_summer : "Door of Summer",
        hane : "HANE Feathers",
        ride_on : "Ride on",
        sea : "sea",
        hour_of_darkness : "Hour of Darkness",
        novelette : "Novelette",
        hope : "hope",
        white_shadow : "White Shadow",
        steady_pace : "steady pace",
        towering_cloud_in_summer : "Towering cloud in summer",
        moonlit_night : "Moonlit Night",
        rose : "Rose",
        at_deaths_door : "At Death’s Door",
        hells_halls : "Hell’s Halls",
        fortitude : "Fortitude",
        witch_in_gold_cembalo : "witch in gold(cembalo)",
        beckoning : "Beckoning",
        fishy_aroma : "Fishy Aroma",
        stupefaction : "stupefaction",
        praise : "praise",
        bgm_pass : "Pass",
        butterfly : "butterfly",
        goldenslaughterer : "goldenslaughterer",
        worldend_bp : "Worldend(bp)",
        the_witch_of_the_painting : "The Witch of the Painting",
        suspicion : "suspicion",
        scar_in_the_score : "Scar in the Score",
        core : "Core",
        minute_darkness : "minute darkness",
        nighteyes : "nighteyes",
        closed_my_heart : "Closed My Heart",
        requiem : "Requiem",
        mind : "mind",
        worldend : "Worldend",
        _play : "play",
        system0 : "system0",
        voiceless : "Voiceless",
        dead_angle : "dead angle",
        organ_short_600_million_in_c_minor : "Organ Short #600 Million in C Minor",
        prison_strip : "Prison STRIP",
        string_quartet_1_in_g_major_allegro : "String Quartet #1 in G Major — I.Allegro",
        cage : "cage",
        golden_sneer : "Golden Sneer",
        scorpion_guts : "Scorpion Guts",
        lifes_end_verc : "Life's End (VerC)",
        answer : "Answer",
        answer_short : "Answer short",
        melody_inst_ver : "Melody inst.ver",
        red_dread : "Red Dread",
        moon : "moon",
        where : "where",
        dread_of_the_grave : "Dread of the grave",
        worldend_dominator : "Worldend dominator",
        black_liliana : "Black Liliana",
        rest : "Rest",
        end_of_a_daydream : "End of a Daydream",
        melody : "Melody",
        over_the_sky : "Over the sky",
        sunny_spot : "sunny spot",
        the_candles_dance : "The Candles Dance",
        distant : "Distant",
        psy_chorus : "psy-chorus",
        far : "far",
        red_shoes_fake : "red shoes FAKE",
        mother : "mother",
        haze : "haze",
        dancing_pipe : "Dancing Pipe",
        dread_of_the_grave_more_fear : "Dread of the grave -More fear-",
        organ_short_200_million_in_c_minor : "Organ Short #200 Million in C Minor",
        rhythm_changer : "rhythm-changer",
        happiness_of_marionette_bonus : "happiness of marionette bonus",
        happiness_of_marionette : "happiness of marionette",
        dance_of_the_moon_rabbits : "Dance of the Moon Rabbits",
        melting_away : "Melting Away",
        soul_of_soul : "Soul of Soul",
        miragecoordinator : "Miragecoordinator",
        prison : "Prison",
        thanks_for_being_born : "Thanks for Being Born",
        wings : "Wings",
        paradise_lost : "Paradise Lost",
        wingless : "Wingless",
        activepain : "Activepain",
        dread_of_the_grave_rhythm_ver : "Dread of the Grave -Rhythm Ver-",
        eternity : "Eternity",
        over : "Over",
        like_the_gale : "Like the Gale",
        f_style : "F Style",
        monochrome_clock : "Monochrome Clock",
        apathy : "Apathy",
        mystic_forest : "Mystic Forest",
        sakutarous_adventure : "Sakutarou's Adventure",
        parallel : "Parallel",
        five_hundred_ninety_nine_million_ruins : "599 Million Ruins",
        happy_maria_instrumental : "Happy Maria (Instrumental)",
        surrounding : "Surrounding",
        open_fire : "Open Fire",
        death_from_stupefaction : "Death from Stupefaction",
        mortal_stampede : "Mortal Stampede",
        victima_propiciatoria : "Victima Propiciatoria",
        revolt : "Revolt",
        purgatory_catastrophe_rhapsodie : "Purgatory Catastrophe Rhapsodie",
        happy_maria : "Happy Maria",
        dive_to_emergency : "Dive to Emergency",
        _dir : "dir",
        endless_nine : "Endless Nine",
        dreamenddischarger : "Dreamenddischarger",
        discotheque : "Discotheque",
        twirl : "Twirl",
        future : "Future",
        deep_blue_jeer : "Deep Blue Jeer",
        the_great_detective_knows : "The Great Detective Knows",
        smileless_soiree : "Smileless Soiree",
        one : "One",
        spiral : "Spiral",
        string_trio_600_million_in_f_sharp_minor : "String Trio #600 Million in F-Sharp Minor",
        totenblume : "Totenblume",
        justice : "Justice",
        aci_l : "ACI-L",
        predator : "Predator",
        proud_dust : "Proud-dust",
        hello_your_dream : "hello your dream",
        a_lonely_deep_sea_fish : "A Lonely Deep-Sea Fish",
        the_girls_witch_hunt : "The Girls's Witch Hunt",
        patchwork_chimera : "Patchwork Chimera",
        discolor : "Discolor",
        resurrectedreplayer : "Resurrectedreplayer",
        final_answer : "Final Answer",
        light : "Light",
        bread_of_life : "Bread of Life",
        promise : "Promise",
        tomorrow : "Tomorrow",
        wings_ver_hope : "WINGS(Ver.Hope)",
        fake_gray_smile : "Fake Gray Smile",
        eternal_chains : "Eternal Chains",
        love_examination : "Love Examination",
        instant : "Instant",
        look_back : "Look Back",
        blue_butterfly : "Blue Butterfly",
        my_dear : "my dear",
        somethings_up_going_down : "Something’s Up & Going Down",
        rog_limitation : "rog-limitation",
        waltz_op34 : "Waltz Op.34",
        alive : "ALIVE",
        birth_of_new_witch_inst : "birth of new witch(inst)",
        ruriair : "ruriair",
        engage_of_marionette : "Engage of marionette",
        life : "Life",
        loreley : "Loreley",
        the_sin : "The Sin",
        the_first_and_the_last : "The first and The last",
        anti_demon_sequentia : "Anti-Demon Sequentia",
        battle_field : "battle field",
        rebirth : "Rebirth",
        the_way : "The Way",
        liberatedliberator : "liberatedliberator",
        thanks_for_all_people : "Thanks for all people",
        infant_queen_bee : "Infant Queen Bee",
        birth_of_new_witch_short_ver : "birth of new witch(Short Ver)",
        fishyaroma : "FISHYAROMA",
        le4_octobre : "le4-octobre",
        ld_circulation : "l&d-circulation",
        reflection_call : "reflection-call",
        rain : "rain",
        _7_weights : "7-weights",
        fall : "fall",
        bore_ral : "bore-ral",
        ballade_continuer : "ballade-continuer",
        song_without_a_name_ver2007_inst : "Song without a name ver.2007 inst",
        lie_alaia : "lie-alaia",
        golden_nocturne_inst : "Golden Nocturne(inst)",
        far_flat : "far(flat)",
        toybox : "Toybox",
        terminal_entrance : "terminal entrance",
        puppet_show : "Puppet Show",
        s_he_end : "s/he-end",
        song_without_a_name_full_inst : "Song without a name full-inst",
        the_end_of_the_world : "The End Of The World",
        goddess_gardena : "goddess-gardena",
        ridicule : "ridicule",
        yomotsu_hirasaka_corruption : "Yomotsu Hirasaka Corruption",
        the_executioner : "the executioner",
        song_without_a_name_ver_sakura_ed_size : "Song without a name ver.sakura ED-size",
        stuffed_animal : "Stuffed Animal",
        bizarre_divertimento : "Bizarre Divertimento",
        en_counse : "en-counse",
        lixAxil : "lixAxil",
        revelations_inst : "Revelations(inst)",
        flying : "Flying",
        lastendconductor : "lastendconductor",
        revelations : "Revelations",
        cocoon_of_white_dreams : "Cocoon of White Dreams -Ricordando il passato-",
        when_the_seagulls_cry : "When the Seagulls Cry",
        suisui_sweets : "SuiSui☆SWEETS(^-^)",
        bring_the_fate : "Bring The Fate",
        bring_the_fate_ver_chiru : "Bring The Fate(Ver chiru)",
        tsurupettan : "Tsurupettan",
        system0_original_version : "system0(Original Version)",
        igreja_of_echoing_vows : "Igreja of Echoing Vows",
        inannas_dream : "Inanna's Dream",
        the_witch_of_occultics : "The Witch of Occultics",
        the_pithos_in_the_fog : "The Pithos in the Fog"
}


init python:
    ## It should show a screen when a song is playing.
    def play_music(music_alias,fade=0):
        renpy.music.play(music_alias,fadein=fade)
        renpy.show_screen("showsong")
