# This RPY is a base template on defining songs manually that aren't located in
# the track folder. Use the commented sample below as a base to manually
# add songs from your projects to here.

init python:
    # imports the OST library. Leave this as-is.
    import ost 

    ## Base Template
    ######################################

    op = ost.soundtrack(
    name = "Umineko no Naku Koro ni", 
    path = "audio/musicbox orange/01 Umineko no Naku Koro ni.ogg",
    priority = 1,
    author = "Hachimitsu Summer",
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


    purgatory = ost.soundtrack(
    name = "Corridor of Purgatory's Sands", 
    path = "audio/musicbox orange/03 Corridor of Purgatory's Sands.ogg",
    priority = 3,
    author = "Pureco",
    cover_art = False,
    )     
    ost.manualDefineList.append(purgatory)

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
    )     
    ost.manualDefineList.append(doorway)

    worldend = ost.soundtrack(
    name = "Worldend", 
    path = "audio/musicbox orange/06 Worldend.ogg",
    priority = 6,
    author = "zts",
    cover_art = False,
    )     
    ost.manualDefineList.append(worldend)

    praise = ost.soundtrack(
    name = "Praise", 
    path = "audio/musicbox orange/07 Praise.ogg",
    priority = 7,
    author = "sumiisan",
    cover_art = False,
    )     
    ost.manualDefineList.append(praise)

    stupefaction = ost.soundtrack(
    name = "Stupefaction", 
    path = "audio/musicbox orange/08 Stupefaction.ogg",
    priority = 8,
    author = "zts",
    cover_art = False,
    )     
    ost.manualDefineList.append(stupefaction)

    towering = ost.soundtrack(
    name = "Towering cloud in summer", 
    path = "audio/musicbox orange/09 Towering cloud in summer.ogg",
    priority = 9,
    author = "dai",
    cover_art = False,
    )     
    ost.manualDefineList.append(towering)

    rideon = ost.soundtrack(
    name = "Ride on", 
    path = "audio/musicbox orange/10 Ride on.ogg",
    priority = 10,
    author = "dai",
    cover_art = False,
    )     
    ost.manualDefineList.append(rideon)

    rose = ost.soundtrack(
    name = "Rose", 
    path = "audio/musicbox orange/11 Rose.ogg",
    priority = 11,
    author = "sumiisan",
    cover_art = False,
    )     
    ost.manualDefineList.append(rose)

    pitiful = ost.soundtrack(
    name = "Pitiful Sneerer", 
    path = "audio/musicbox orange/12 Pitiful Sneerer.ogg",
    priority = 12,
    author = "GranMusik",
    cover_art = False,
    unlocked = renpy.seen_audio("audio/bgm/umib_1001_intro.ogg")
    )     
    ost.manualDefineList.append(pitiful)

    painting = ost.soundtrack(
    name = "Witch of the Painting", 
    path = "audio/musicbox orange/13 Witch of the Painting.ogg",
    priority = 13,
    author = "pre-holder",
    cover_art = False,
    unlocked = renpy.seen_audio("audio/bgm/umib_026_intro.ogg")
    )     
    ost.manualDefineList.append(painting)