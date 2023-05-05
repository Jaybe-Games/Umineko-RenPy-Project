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

    deaths_door = "audio/bgm/umib_014.ogg"
    hane = "audio/bgm/umib_003.ogg"
    ride_on = "audio/bgm/umib_004.ogg"
    summer = "audio/bgm/umib_002.ogg"
    pitiful = "audio/bgm/umib_1000.ogg"
    face = "audio/bgm/umib_110.ogg"
    credits = "audio/bgm/umib_0000.ogg"
    endroll = "audio/bgm/bgm_final.ogg"
    kuina = "audio/bgm/umib_121.ogg"


    # alias : "Song Title",
    music_dictionary = {
        deaths_door : "At Death's Door",
        hane : "HANE (Feathers)",
        ride_on : "Ride on",
        summer : "Door of Summer",
        pitiful : "Pitiful Sneerer",
        face : "About Face",
        credits : "Golden Sneers - Lovely Banquet",
        endroll : "Bring the Fate",
        kuina : "Kuina"
    }

