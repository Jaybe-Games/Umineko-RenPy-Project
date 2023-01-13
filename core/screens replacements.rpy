# ### Things to replace in your screens.rpy
# # For our game, we've styled our own GUI, to show that these options can work with any kind of UI. That said, we want
# # you to be able to replace *easily*, without having to scour our screens.rpy for comments. Look for IMPORTANT in this file for
# # changes!
#
# ### Say Window
# screen say(who, what, namebox_type=None):
#     style_prefix "say"
#
#     window:
#         background Transform(style.window.background, alpha=persistent.say_window_alpha)
#         ### IMPORTANT: The Transform() is holding the window background, and the alpha variable ties to our say window alpha found in functions.rpy and screens replacements.rpy
#         id "window"
#         text what id "what" kerning persistent.say_dialogue_kerning font persistent.pref_text_font size persistent.pref_text_size
#         ### IMPORTANT: We adjust the kerning, color, font, and size inline here!
#

#
#
# ### Textbuttons
# #Change Font
# textbutton "{font=FontChoice}Font Name" action [changeFont("FontChoice"),SelectedIf(persistent.pref_text_font == "FontChoice")]
#
# #Change Font Size
# textbutton "Size" action [changeScale(newScale="SizeChoice"),SelectedIf(persistent.pref_text_scale == "SizeChoice") ]
#
# ### Toggles
# #You can also create SetField() buttons with on/off variables if you prefer that look.
#
# #Toggle Audio Cues
# textbutton "Audio Cues" action ToggleField(persistent,"audio_cues",true_value=True,false_value=False)
#
# #Toggle Screenshake
# textbutton "Screenshake" action ToggleField(persistent,"screenshake",true_value=True,false_value=False)
#
# #Set Textbox Opacity
# bar value FieldValue(persistent, 'say_window_alpha', 1.0, max_is_zero=False, offset=0, step=.2)
