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


    darkhour = ost.soundtrack(
    name = "Hour of darkness", 
    path = "audio/musicbox orange/03 Hour of darkness.ogg",
    priority = 3,
    author = "pre-holder",
    cover_art = False,
    )     
    ost.manualDefineList.append(darkhour)


    death_door = ost.soundtrack(
    name = "At Death's Door", 
    path = "audio/musicbox orange/04 At Death's Door.ogg",
    priority = 4,
    author = "Pureco",
    cover_art = False,
    )     
    ost.manualDefineList.append(death_door)

    hane = ost.soundtrack(
    name = "HANE (Feathers)", 
    path = "audio/musicbox orange/05 HANE (Feathers).ogg",
    priority = 5,
    author = "Dai",
    cover_art = False,
    )     
    ost.manualDefineList.append(hane)

    doorway = ost.soundtrack(
    name = "Doorway of Summer", 
    path = "audio/musicbox orange/06 Doorway of Summer.ogg",
    priority = 6,
    author = "Dai",
    cover_art = False,
    )     
    ost.manualDefineList.append(doorway)

    worldend = ost.soundtrack(
    name = "Worldend", 
    path = "audio/musicbox orange/07 Worldend.ogg",
    priority = 7,
    author = "zts",
    cover_art = False,
    )     
    ost.manualDefineList.append(worldend)

    praise = ost.soundtrack(
    name = "Praise", 
    path = "audio/musicbox orange/08 Praise.ogg",
    priority = 8,
    author = "sumiisan",
    cover_art = False,
    )     
    ost.manualDefineList.append(praise)

    stupefaction = ost.soundtrack(
    name = "Stupefaction", 
    path = "audio/musicbox orange/09 Stupefaction.ogg",
    priority = 9,
    author = "zts",
    cover_art = False,
    )     
    ost.manualDefineList.append(stupefaction)

    towering = ost.soundtrack(
    name = "Towering cloud in summer", 
    path = "audio/musicbox orange/10 Towering cloud in summer.ogg",
    priority = 10,
    author = "dai",
    cover_art = False,
    )     
    ost.manualDefineList.append(towering)

    rideon = ost.soundtrack(
    name = "Ride on", 
    path = "audio/musicbox orange/11 Ride on.ogg",
    priority = 11,
    author = "dai",
    cover_art = False,
    )     
    ost.manualDefineList.append(rideon)

    rose = ost.soundtrack(
    name = "Rose", 
    path = "audio/musicbox orange/12 Rose.ogg",
    priority = 12,
    author = "sumiisan",
    cover_art = False,
    )     
    ost.manualDefineList.append(rose)

    pitiful = ost.soundtrack(
    name = "Pitiful Sneerer", 
    path = "audio/musicbox orange/13 Pitiful Sneerer.ogg",
    priority = 13,
    author = "GranMusik",
    cover_art = False,
    unlocked = renpy.seen_audio("audio/bgm/umib_1001_intro.ogg")
    )     
    ost.manualDefineList.append(pitiful)

    painting = ost.soundtrack(
    name = "Witch of the Painting", 
    path = "audio/musicbox orange/14 Witch of the Painting.ogg",
    priority = 14,
    author = "pre-holder",
    cover_art = False,
    unlocked = renpy.seen_audio("audio/bgm/umib_026_intro.ogg")
    )     
    ost.manualDefineList.append(painting)