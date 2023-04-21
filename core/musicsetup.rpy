
default persistent.visual_text_help = _preferences.self_voicing

default persistent.audio_cues = True

default persistent.screenshake = True

default persistent.say_window_alpha = 0.75

default persistent.pref_text_scale = "regular"

default persistent.say_dialogue_kerning = 0

default persistent.pref_text_font = "DejaVuSans.ttf"

default persistent.pref_text_size = 32

default persistent.pref_text_color = "#333333"

default persistent.pref_text_spacing = 0



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


    # alias : "Song Title",
    music_dictionary = {
        deaths_door : "At Death's Door",
        hane : "HANE (Feathers)",
        ride_on : "Ride on",
        summer : "Door of Summer",
        pitiful : "Pitiful Sneerer"
    }

