# This RPY is a base template on defining songs manually that aren't located in
# the track folder. Use the commented sample below as a base to manually
# add songs from your projects to here.

init python:
    # imports the OST library. Leave this as-is.
    import ost 

    ## Base Template
    ######################################

    zeroopfull = ost.soundtrack(
    name = "Gold Dream Symphony", 
    path = "audio/bgm/op.ogg",
    priority = 0,
    author = "aFlowerSmiles",
    cover_art = False,
    )     
    ost.manualDefineList.append(zeroopfull)


    mmtheme = ost.soundtrack(
    name = "Black Lilliana Orchestra", 
    path = "audio/bgm/umib_000.ogg",
    priority = 1,
    author = "Pennoink",
    cover_art = False,
    )     
    ost.manualDefineList.append(mmtheme)


    death_door = ost.soundtrack(
    name = "At Death's Door", 
    path = "audio/bgm/umib_014.ogg",
    priority = 2,
    author = "Pureco",
    cover_art = False,
    )     
    ost.manualDefineList.append(death_door)

    hane = ost.soundtrack(
    name = "HANE (Feathers)", 
    path = "audio/bgm/umib_003.ogg",
    priority = 3,
    author = "Dai",
    cover_art = False,
    )     
    ost.manualDefineList.append(hane)

    doorway = ost.soundtrack(
    name = "Doorway of Summer", 
    path = "audio/bgm/umib_002.ogg",
    priority = 4,
    author = "Dai",
    cover_art = False,
    #unlocked = renpy.seen_audio("bgm/09 Easy.mp3")
    )     
    ost.manualDefineList.append(doorway)
