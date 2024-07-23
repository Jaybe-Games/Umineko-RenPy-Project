init:
    python:

        # RainBlur is how much to blur rain.
        RainBlur = 0

        # RainAlpha is the total alpha level of the entire rain sheet.
        RainAlpha = 0.7

        # RainY is rain speed, basically how long does it take
        # for the rain sheet to fall down by one tile
        RainY = 0.30

        # RainX is the same for horizontal movement,
        # and needs to be manually adjusted to fit the chosen raindrop angle
        # for the rain to fall naturally.
        RainX = RainY * 80
        
        # Total alpha of the rain is the sum of the alpha of all three layers,
        # so each sheet has a third of it.
        RainLayerAlpha = RainAlpha / 4

        # Speed of the medium sheet of rain is two times faster than the front sheet.
        RainYM = RainY / 2
        RainXM = RainX / 2

        # Speed of the futhest sheet of rain is two times faster than that.
        RainYF = RainYM 
        RainXF = RainXM

        ######################################

        # Automatically find our rain files, which are assumed to live in the module directory:
        RainFiles = renpy.os.path.dirname(renpy.get_filename_line()[0]).split("game/")[-1]

        # We're making three displayables, each bigger than the screen by the size of one rain 
        # tile, in both directions.
        #
        # Check generate-rain.py for how the raindrops are made.

        RainTileSizeX, RainTileSizeY = renpy.image_size(RainFiles+"/_rain-long.png")
        
        # Amazingly, using ATLs xtile/ytile to tile the rain images actually results
        # in a lot more CPU usage.
        RainsheetLong = Composite(
            (config.screen_width + RainTileSizeX, config.screen_height + RainTileSizeY),
            (0, 0), Tile(RainFiles+"/_rain-long.png"))
        RainsheetMedium = Composite(
            (config.screen_width + RainTileSizeX, config.screen_height + RainTileSizeY),
            (0,0), Tile(RainFiles+"/_rain-medium.png"))
        RainsheetShort = Composite(
            (config.screen_width + RainTileSizeX, config.screen_height + RainTileSizeY),
            (0,0), Tile(RainFiles+"/_rain-short.png"))
    
    # This defines the far sheet of the rain.
    # You show this one /behind/ character sprites.
    # It has the shortest (more distant) and fastest moving raindrops.
    # In theory you can split it and put sprites between each of the three sheets,
    # but I didn't need that.

    image rain:
        # Distant drops
        contains:
            RainsheetShort
            blur RainBlur
            alpha RainLayerAlpha
            subpixel True
            parallel:
                ypos -RainTileSizeY
                ease RainYF ypos 0
                repeat
            parallel:
                xpos 0
                ease RainXF xpos -RainTileSizeX
                repeat
        #Medium drops
        contains:
            RainsheetMedium
            blur RainBlur
            alpha RainLayerAlpha
            subpixel True
            parallel:
                ypos -RainTileSizeY
                ease RainYM ypos 0
                repeat
            parallel:
                xpos 0
                ease RainXM xpos -RainTileSizeX
                repeat
        #long drops
        contains:
            RainsheetLong
            blur RainBlur
            alpha RainLayerAlpha
            subpixel True
            parallel:
                ypos -RainTileSizeY
                ease RainY ypos 0
                repeat
            parallel:
                xpos 0
                ease RainX xpos -RainTileSizeX
                repeat


    image rainback:
        # Distant drops
        contains:
            RainsheetShort
            blur RainBlur
            alpha RainLayerAlpha
            subpixel True
            parallel:
                ypos -RainTileSizeY
                ease RainYF ypos 0
                repeat
            parallel:
                xpos 0
                ease RainXF xpos -RainTileSizeX
                repeat
        #Medium drops
        contains:
            RainsheetMedium
            blur RainBlur
            alpha RainLayerAlpha
            subpixel True
            parallel:
                ypos -RainTileSizeY
                ease RainYM ypos 0
                repeat
            parallel:
                xpos 0
                ease RainXM xpos -RainTileSizeX
                repeat

    # This is the front sheet of the rain, it goes /above/ the 
    # character sprites.
    image rainfront:    
        contains:
            RainsheetLong
            blur RainBlur
            alpha RainLayerAlpha
            subpixel True
            parallel:
                ypos -RainTileSizeY
                ease RainY ypos 0
                repeat
            parallel:
                xpos 0
                ease RainX xpos -RainTileSizeX
                repeat

    # Static sheets of rain for use when the rain does not need to animate,
    # e.g. when the time has stopped.
    image rainbackstatic:
        contains:
            RainsheetShort
            alpha RainLayerAlpha
            blur RainBlur
        contains:
            RainsheetMedium
            alpha RainLayerAlpha
            blur RainBlur

    image rainfrontstatic:        
        contains:
            RainsheetLong
            alpha RainLayerAlpha
            blur RainBlur

init -50 python hide:
    # We also need to forbid build code from picking up our generator script,
    # which I like to keep with my project.
    build.classify("**/generate-rain.py", None)

