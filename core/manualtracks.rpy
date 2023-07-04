# This RPY is a base template on defining songs manually that aren't located in
# the track folder. Use the commented sample below as a base to manually
# add songs from your projects to here.

init python:
    # imports the OST library. Leave this as-is.
    import ost 

    ## Base Template
    ######################################

    op = ost.soundtrack(
    name = "Gold Dream Symphony", 
    path = "audio/musicbox orange/01 Gold Dream Symphony.ogg",
    priority = 1,
    author = "aFlowerSmiles",
    cover_art = False,
    )     
    ost.manualDefineList.append(op)


    mmtheme = ost.soundtrack(
    name = "Black Lilliana Orchestra", 
    path = "audio/musicbox orange/02 Black Lilliana Orchestra.ogg",
    priority = 2,
    author = "Pennoink",
    cover_art = False,
    )     
    ost.manualDefineList.append(mmtheme)


    death_door = ost.soundtrack(
    name = "At Death's Door", 
    path = "audio/musicbox orange/03 At Death's Door.ogg",
    priority = 3,
    author = "Pureco",
    cover_art = False,
    )     
    ost.manualDefineList.append(death_door)

    hane = ost.soundtrack(
    name = "HANE (Feathers)", 
    path = "audio/musicbox orange/04 HANE (Feathers).ogg",
    priority = 4,
    author = "Dai",
    cover_art = False,
    )     
    ost.manualDefineList.append(hane)

    doorway = ost.soundtrack(
    name = "Doorway of Summer", 
    path = "audio/musicbox orange/05 Doorway of Summer.ogg",
    priority = 5,
    author = "Dai",
    cover_art = False,
    #unlocked = renpy.seen_audio("musicbox orange/09 Easy.mp3")
    )     
    ost.manualDefineList.append(doorway)

    worldend = ost.soundtrack(
    name = "Worldend", 
    path = "audio/musicbox orange/06 Worldend.ogg",
    priority = 6,
    author = "zts",
    cover_art = False,
    #unlocked = renpy.seen_audio("musicbox orange/09 Easy.mp3")
    )     
    ost.manualDefineList.append(worldend)

    praise = ost.soundtrack(
    name = "Praise", 
    path = "audio/musicbox orange/07 Praise.ogg",
    priority = 7,
    author = "sumiisan",
    cover_art = False,
    #unlocked = renpy.seen_audio("musicbox orange/09 Easy.mp3")
    )     
    ost.manualDefineList.append(praise)

    stupefaction = ost.soundtrack(
    name = "Stupefaction", 
    path = "audio/musicbox orange/08 Stupefaction.ogg",
    priority = 8,
    author = "zts",
    cover_art = False,
    #unlocked = renpy.seen_audio("musicbox orange/09 Easy.mp3")
    )     
    ost.manualDefineList.append(praise)
