init -3 python:
    persistent.patch_installed = False
init -1 python:
    if persistent.patch_installed and not persistent.patch_first_time:
        persistent.patch_enabled = True
        persistent.patch_first_time = True
    elif not persistent.patch_installed:
        persistent.patch_first_time = False
        persistent.patch_enabled = False

default persistent.alreadystarted = False
default persistent.mainstorycleared = False
default persistent.teapartycleared = False
default persistent.gamecleared = False

default persistent.rudolf = False
default persistent.kyrie = False
default persistent.maria = False
default persistent.battler = False
default persistent.rosa = False
default persistent.jessica = False
default persistent.george = False
default persistent.hideyoshi = False
default persistent.eva = False
default persistent.kumasawa = False
default persistent.gohda = False
default persistent.shannon = False
default persistent.krauss = False
default persistent.natsuhi = False
default persistent.beatrice = False
default persistent.kinzo = False
default persistent.nanjo = False
default persistent.genji = False
default persistent.kanon = False
default persistent.goldenwitch = False

default persistent.tip1 = False
default persistent.tip2 = False
default persistent.tip3 = False
default persistent.musicbox = False

default persistent.textbox = 0
default persistent.textboxswitch = 0