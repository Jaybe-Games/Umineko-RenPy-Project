## This file contains options that can be changed to customize your game.
##
## Lines beginning with two '#' marks are comments, and you shouldn't uncomment
## them. Lines beginning with a single '#' mark are commented-out code, and you
## may want to uncomment them when appropriate.


## Basics ######################################################################

## A human-readable name of the game. This is used to set the default window
## title, and shows up in the interface and error reports.
##
## The _() surrounding the string marks it as eligible for translation.

define config.name = _("Umineko When They Cry Zero ~Waltz of Reflections and Delusions~")


## Determines if the title given above is shown on the main menu screen. Set
## this to False to hide the title.

define gui.show_name = False


## The version of the game.

define config.version = "1.2"


## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.

define gui.about = _p("""Developed by Jaybe Games\n

CREATIVE DIRECTOR\n

Jaybe\n

STORY & SCRIPT\n

Jaybe\n

ANIMATIONS & EFFECTS\n

Jaybe
from original assets\n

CLOSED TESTER / PROOFREADER\n

Singularity\n
Fakuum\n
SurfingJeorn\n
AlexHD199\n
AiylaChan\n
Ararara555\n
Bucky\n

USED ASSETS\n

Gameassets from
Umineko no Naku Koro ni Saku
~Symphony of Catbox and Dreams~\n

FancyText: yukinogatari\n
RPY-VNBE Achievement System: rjscdev\n
RenPyParticles: AgentAlpha81\n
Gradient Tags: sodara9\n

MUSICBOX ORANGE\n

Black Lilliana Orchestra by Pennoink\n
fullendrecharger by Rolli B\n

Umineko ~Rose Crimson~\n

Pitiful Sneerer\n

OPENING SONG\n

Gold Dream Symphony\n
Original Performer: Kino Nei, Luck-Ganriki, dai\n
German Vocals & Lyrics: aFlowerSmiles\n
Openingvideo: Jaybe\n

ENDING SONG\n

Golden Sneers ~ Lovely Banquet\n
Composed by: Luck Ganriki\n
Arranged by: Yoshitaka Hirota\n
Lyrics by: Tomoko Shinoda\n
Vocals by: Akiko Shikata\n
All Instruments: Yoshitaka Hirota""")


## A short name for the game used for executables and directories in the built
## distribution. This must be ASCII-only, and must not contain spaces, colons,
## or semicolons.

define build.name = "whentheycry0"


## Sounds and music ############################################################

## These three variables control, among other things, which mixers are shown
## to the player by default. Setting one of these to False will hide the
## appropriate mixer.

define config.has_sound = True
define config.has_music = True
define config.has_voice = True


## To allow the user to play a test sound on the sound or voice channel,
## uncomment a line below and use it to set a sample sound to play.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Uncomment the following line to set an audio file that will be played while
## the player is at the main menu. This file will continue playing into the
## game, until it is stopped or another file is played.

define config.main_menu_music = "audio/bgm/umib_000.ogg"


## Transitions #################################################################
##
## These variables set transitions that are used when certain events occur.
## Each variable should be set to a transition, or None to indicate that no
## transition should be used.

## Entering or exiting the game menu.
define dis = { "master" : Dissolve(0.15) }
define config.enter_transition = ImageDissolve("images/masks/circle.png", 0.5, reverse=True, ramplen = 200)
define config.enter_sound = "audio/sfx/umise_1001.ogg"
define config.exit_transition = ImageDissolve("images/masks/circle.png", 0.5, reverse=True, ramplen = 200)
define config.exit_sound = "audio/sfx/umise_1006.ogg"


## Between screens of the game menu.

define config.intra_transition = ImageDissolve("images/masks/circle.png", 1.0, reverse=True, ramplen = 200)

## Used when entering the main menu after the game has ended.

define config.end_game_transition = dissolve

define config.end_splash_transition = dissolve

define config.nvl_adv_transition = dissolve

define config.adv_nvl_transition = dissolve

define config.game_main_transition = dissolve

define config.exit_yesno_transition = ImageDissolve("images/masks/circle.png", 1.0, reverse=True, ramplen = 100)

define config.enter_yesno_transition = ImageDissolve("images/backgrounds/different_spiral_1a.png",0.6,reverse=False, ramplen = 30)
define config.say_attribute_transition = dis

define config.manage_gc = True

define config.after_load_transition = MultipleTransition([
    True, Dissolve(0.0),
    "images/system/ware2.png", Pause(2.0),
    "images/system/ware2.png", dissolve,
    True])

define config.main_game_transition = MultipleTransition([
    True, Dissolve(0.0),
    "images/system/ware2.png", Pause(2.0),
    "images/system/ware2.png", dissolve,
    True])

define _scene_show_hide_transition = { "master" : Dissolve(0.25) }

define gradientwipedown = ImageDissolve("/images/masks/down.png", 0.8, ramplen = 300)
define gradientwipeup = ImageDissolve("/images/masks/up.png", 0.8, ramplen = 300)

define config.window = "auto"

define config.window_show_transition = gradientwipeup
define config.window_hide_transition = gradientwipedown


default preferences.text_cps = 50

default preferences.afm_time = 10
default preferences.fullscreen = True
default preferences.gl_powersave = False
default preferences.gl_tearing = False
default preferences.gl_framerate = None
define config.image_cache_size_mb = 1024
define config.cache_surfaces = False
define config.predict_statements = 25
define config.developer = "auto"



define config.default_music_volume = 0.7
define config.default_sfx_volume = 0.5


## Save directory ##############################################################
##
## Controls the platform-specific place Ren'Py will place the save files for
## this game. The save files will be placed in:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## This generally should not be changed, and if it is, should always be a
## literal string, not an expression.

define config.save_directory = "whentheycry0"


## Icon ########################################################################
##
## The icon displayed on the taskbar or dock.

define config.window_icon = "gui/icon.png"

## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution files.

init python:

    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##
    ## / is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## For example, "*.txt" matches txt files in the base directory, "game/
    ## **.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.archive("scripts", "all")
    build.archive("librarys", "all")
    build.archive("audio", "all")
    build.archive("fonts", "all")
    build.archive("images", "all")
    build.archive("movies", "all")
    # prepare english translation archive
    build.archive("english", "all")

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**.psd', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**.rpy', None)
    build.classify('**.rpyb', None)
    build.classify('**.rpym', None)
    build.classify('**.rpymc', None)
    build.classify('**.txt', None)
    build.classify('**.md', None)

    ## To archive files, classify them as 'archive'.

    build.classify('**.png', 'images')
    build.classify('**.rp', 'librarys')
    build.classify('**.py', 'librarys')
    build.classify('**.rpc', 'librarys')
    build.classify('**.bmp', 'images')
    build.classify('**.jpg', 'images')
    build.classify('**.ico', 'images')
    build.classify('**.icns', 'images')
    build.classify('**.ogg', 'audio')
    build.classify('**.mp3', 'audio')
    build.classify('**.wav', 'audio')
    build.classify('**.rpyc', 'scripts')
    build.classify('**.json', 'scripts')
    build.classify('**.webm', 'movies')
    build.classify('**.mov', 'movies')
    build.classify('**.otf', 'fonts')
    build.classify('**.ttf', 'fonts')

    # English translation archive
    build.classify('tl/English/**.bmp', 'english')
    build.classify('tl/English/**.jpg', 'english')
    build.classify('tl/English/**.png', 'english')
    build.classify('tl/English/**.ico', 'english')
    build.classify('tl/English/**.icns', 'english')
    build.classify('tl/English/**.rpyc', 'english')


    ## Files matching documentation patterns are duplicated in a mac app build,
    ## so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')




## A Google Play license key is required to download expansion files and perform
## in-app purchases. It can be found on the "Services & APIs" page of the Google
## Play developer console.

# define build.google_play_key = "..."


## The username and project name associated with an itch.io project, separated
## by a slash.

define build.itch_project = "jaybe-games/umineko-when-they-cry-zero"
