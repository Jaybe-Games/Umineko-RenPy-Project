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
    ## declare bgm
    ## Sorted after first appearance
    rose = "audio/bgm/umib_001.ogg"

    ## Add them to the dictionary
    music_dictionary = {
        ## I want to use song names, because I can only remember a few umib soundtrack names
        ## Sorted after first appearance
        rose : "Rose"
        }

init python:
    ## It should show a screen when a song is playing.
    def play_music(music_alias,fade=0):
        renpy.music.play(music_alias,fadein=fade)
        renpy.show_screen("showsong")
