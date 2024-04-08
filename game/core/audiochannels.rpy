init -1 python:
    renpy.music.register_channel("ship", mixer= "sfx", loop=True, stop_on_mute=True)
    renpy.music.register_channel("wind", mixer= "sfx", loop=True, stop_on_mute=True)
    renpy.music.register_channel("rain", mixer= "sfx", loop=True, stop_on_mute=True)
    renpy.music.register_channel("clocktick", mixer= "sfx", loop=True, stop_on_mute=True)
    renpy.music.register_channel("effect", mixer= "sfx", loop=False, stop_on_mute=True)
