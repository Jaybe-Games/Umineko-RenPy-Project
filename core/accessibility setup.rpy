###Image Description
# For users who are visually impaired or otherwise use self-voicing, many times it's useful to have additional
# on screen text to compensate for effects, subtle visual changes, etc. Ren'Py has a built in character, but
# since we want the ability to see the additional text *without* activating self-voicing, we have to make our own.
# Replace all instances of "sv" (The Character) in your script with "vt".

##Whether or not to display additional text for visual effects, etc
default persistent.visual_text_help = _preferences.self_voicing

###Initial GUI preferences
#Here, we'll keep all our gui preferences, along with our persistent variables regarding accessibility.

#Audio cues
default persistent.audio_cues = True

#Can we shake the screen/display shaking images?
default persistent.screenshake = True

##Default alpha of the say window. Append to your say screen.
default persistent.say_window_alpha = 0.75

#Used to determine what size font to use when changing font/size.
default persistent.pref_text_scale = "regular"

#Default spacing/kerning of say dialogue text. Append to your say screen.
default persistent.say_dialogue_kerning = 0

#Set your default font
#Replace all instances of gui.text_font with persistent.pref_text_font. Append to your say screen.
default persistent.pref_text_font = "DejaVuSans.ttf"

#Set your default text size
#Replace all instances of gui.text_size with persistent.pref_text_size. Append to your say screen.
default persistent.pref_text_size = 32

#Default text color
#Replace all instances of gui.text_color with persistent.pref_text_color. Append to your say screen.
default persistent.pref_text_color = "#333333"

#Default line_spacing for your text.
#Append to to your say screen.
default persistent.pref_text_spacing = 0

###

###
#This is all the functions for accessibility.

init python:
    ###Size Dictionary
    # Organized in dicts, follow the order below to create your font:size pairings.
    # Since lots of fonts use different vertical heights, it's highly recommended you include a "line_spacing" key for
    # each entry.
    # For advanced usage, if you do a font size slider you can make these minimum and maximum sizes!

    size_dict = {
        # "filepath" : {"size_scale1" : size in pixels, "size_scale2" : size in pixels...},
        # For advanced usage, you can make these dicts hold any optional arguments you want per font.
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
    # Define every song with an alias

    deaths_door = "audio/bgm/umib_014.ogg"
    hane = "audio/bgm/umib_003.ogg"

    # alias : "Song Title",
    music_dictionary = {
         deaths_door : "At Death's Door",
         hane : "HANE",
    }

    # Define every sound with an alias
    # door_close = "door closing sfx.wav"

    # alias : "Sound description."
    sfx_dictionary = {
         # door_close : "Door closes shut.",
    }
