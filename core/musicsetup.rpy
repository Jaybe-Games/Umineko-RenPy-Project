default persistent.audio_cues = True

init python:


    size_dict = {

        "OpenDyslexic.otf" : {
            "regular" : 31,
            "large" : 34,
            "line_spacing" : -15,
            },

        "DejaVuSans.ttf" : {
            "regular" : 32,
            "large" : 35,
            "line_spacing" : 0,
            },
        }


    ###Initial Audio Cues Setup

    mainmenu = "audio/bgm/umib_000.ogg"
    deaths_door = "audio/bgm/umib_014_Intro.ogg"
    deaths_door_loop = "audio/bgm/umib_014_loop.ogg"
    hane = "audio/bgm/umib_003.ogg"
    ride_on = "audio/bgm/umib_004.ogg"
    summer = "audio/bgm/umib_002.ogg"
    pitiful = "audio/bgm/umib_1000.ogg"
    face = "audio/bgm/umib_110.ogg"
    ending = "audio/bgm/umib_0000.ogg"
    endroll = "audio/bgm/bgm_final.ogg"
    kuina = "audio/bgm/umib_121.ogg"
    goldenkiller = "audio/bgm/umib_024_intro.ogg"


    # alias : "Song Title",
    music_dictionary = {
        mainmenu : "Black Lilliana Orchestra",
        deaths_door : "At Death's Door",
        deaths_door_loop : "At Death's Door",
        hane : "HANE (Feathers)",
        ride_on : "Ride on",
        summer : "Door of Summer",
        pitiful : "Pitiful Sneerer",
        face : "About Face",
        ending : "Golden Sneers - Lovely Banquet",
        endroll : "Bring the Fate",
        kuina : "Kuina",
        goldenkiller : "goldenslaughterer"
    }

