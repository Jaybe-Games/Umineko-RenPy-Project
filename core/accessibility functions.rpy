init python:
    ###Button Actions
    # These are the button actions found in screens replacements.rpy

    def changeFont(newFont):
        return SetField(persistent,"pref_text_font",newFont),SetField(persistent,"pref_text_size", size_dict[newFont][persistent.pref_text_scale]),SetField(persistent,"pref_text_spacing",size_dict[newFont]['line_spacing']),SelectedIf(persistent.pref_text_font == newFont)
        ###

    def changeScale(newScale):
        return SetField(persistent,"pref_text_scale",newScale),SetField(persistent,"pref_text_size", size_dict[persistent.pref_text_font][newScale])

    def changeColor(newColor):
        return SetField(persistent,"pref_text_color",newColor)

    #A quick way to toggle True/False on persistent variables.

    def persistentToggle(persistentfield):
        return ToggleField(persistent,persistentfield,true_value=True,false_value=False)

    ### Audio Cues

    def play_music(music_alias,fade=0):
        renpy.music.play(music_alias,fadein=fade)
        if persistent.audio_cues:
            renpy.notify("♪ " + music_dictionary[renpy.music.get_playing('music')])
    ###

    ###Screenshake
    # Shakes the screen. To use, put
    # $ shake()
    # inline. For other uses, simply do a check inline for ATL statements, or a ConditionSwitch for shaky images.

    def shake():
        if persistent.screenshake:
            renpy.with_statement(hpunch)
        else:
            renpy.with_statement(fade) ###OPTIONAL: Show a different effect if screenshake is turned off.

define vt = Character(None,condition="persistent.visual_text_help or _preferences.self_voicing",what_italic=True)
