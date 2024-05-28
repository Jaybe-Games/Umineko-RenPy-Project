define config.name = _("Umineko When They Cry")
define gui.show_name = False
define config.version = "1.1.1 Alpha"
define build.name = "whentheycry"


## Sounds and music ############################################################

define config.has_sound = True
define config.has_music = True
define config.has_voice = True

## Transitions #################################################################
##
## These variables set transitions that are used when certain events occur.
## Each variable should be set to a transition, or None to indicate that no
## transition should be used.

## Entering or exiting the game menu.
define dis = { "master" : Dissolve(0.25) }
define window_dissolve = { "screens" : Dissolve(0.5) }
define config.enter_transition = ImageDissolve("images/masks/circle.png", 0.5, reverse=True, ramplen = 200)
define config.enter_sound = "audio/sfx/umise_1001.ogg"
define config.exit_transition = ImageDissolve("images/masks/circle.png", 0.5, reverse=True, ramplen = 200)
define config.exit_sound = "audio/sfx/umise_1006.ogg"

define config.check_conflicting_properties = True
## Between screens of the game menu.

define config.intra_transition = ImageDissolve("images/masks/circle.png", 1.0, reverse=True, ramplen = 200)

## Used when entering the main menu after the game has ended.

define config.end_game_transition = dissolve

define config.end_splash_transition = dissolve

define config.nvl_adv_transition = dissolve

define config.adv_nvl_transition = dissolve

define config.game_main_transition = dissolve

define config.exit_yesno_transition = ImageDissolve("images/masks/circle.png", 1.0, reverse=True, ramplen = 100)

define config.enter_yesno_transition = ImageDissolve("images/system/different_spiral_1a.png", 0.6, reverse=False, ramplen = 30)
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


define config.window_show_transition = dissolve
define config.window_hide_transition = dissolve


default preferences.text_cps = 50

default preferences.afm_time = 10
default preferences.fullscreen = True
default preferences.gl_powersave = False
default preferences.gl_tearing = False
default preferences.gl_framerate = 60
define config.image_cache_size_mb = 1024
define config.cache_surfaces = False
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

define config.save_directory = "whentheycry"


## Icon ########################################################################
##
## The icon displayed on the taskbar or dock.

define config.window_icon = "gui/icon.png"

## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution files.

init python:

    build.archive("scripts", "all")
    build.archive("librarys", "all")
    build.archive("audio", "all")
    build.archive("fonts", "all")
    build.archive("images", "all")
    build.archive("movies", "all")
    # prepare other translation archive
    # build.archive("english", "all")

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

    # Other translation archive
    # build.classify('tl/English/**.bmp', 'english')
    # build.classify('tl/English/**.jpg', 'english')
    # build.classify('tl/English/**.png', 'english')
    # build.classify('tl/English/**.ico', 'english')
    # build.classify('tl/English/**.icns', 'english')
    # build.classify('tl/English/**.rpyc', 'english')


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

define build.itch_project = "jaybe-games/umineko-when-they-cry"

init -1 python:

    config.has_quicksave = False

    config.autosave_on_quit = True
