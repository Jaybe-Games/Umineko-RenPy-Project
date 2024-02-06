init python:
  
    # This is set to the name of the character that is speaking, or
    # None if no character is currently speaking.
    speaking = None
  
    # This returns speaking if the character is speaking, and done if the
    # character is not.
    def while_speaking(name, speak_d, done_d, st, at):
        if speaking == name:
            return speak_d, .1
        else:
            return done_d, None
  
    # Curried form of the above.
    curried_while_speaking = renpy.curry(while_speaking)
  
    # Displays speaking when the named character is speaking, and done otherwise.
    def WhileSpeaking(name, speaking_d, done_d=Null()):
        return DynamicDisplayable(curried_while_speaking(name, speaking_d, done_d))
  
    # This callback maintains the speaking variable.
    def speaker_callback(name, event, **kwargs):
        global speaking
       
        if event == "show":
            speaking = name
        elif event == "slow_done":
            speaking = None
        elif event == "end":
            speaking = None
  
    # Curried form of the same.
    speaker = renpy.curry(speaker_callback)

define bea = Character('BEATRICE', what_prefix="{dialogue}\"", what_suffix="\"{/dialogue}", who_prefix="{dialogue}", who_suffix="{/dialogue}", image="bea", ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="bea", callback=speaker("bea"))
define kin = Character('Kinzo', what_prefix="{dialogue}\"", what_suffix="\"{/dialogue}", who_prefix="{dialogue}", who_suffix="{/dialogue}", image="kin", ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="kin", callback=speaker("kin"))
define cla = Character('Krauss', what_prefix="{dialogue}\"", what_suffix="\"{/dialogue}", who_prefix="{dialogue}", who_suffix="{/dialogue}", image="cla", ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="cla", callback=speaker("cla"))
define nat = Character('Natsuhi', what_prefix="{dialogue}\"", what_suffix="\"{/dialogue}", who_prefix="{dialogue}", who_suffix="{/dialogue}", image="nat", ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="nat", callback=speaker("nat"))
define jes = Character('Jessica', what_prefix="{dialogue}\"", what_suffix="\"{/dialogue}", who_prefix="{dialogue}", who_suffix="{/dialogue}", image="jes", ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="jes", callback=speaker("jes"))
define eva = Character('Eva', what_prefix="{dialogue}\"", what_suffix="\"{/dialogue}", who_prefix="{dialogue}", who_suffix="{/dialogue}", image="eva", ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="eva", callback=speaker("eva"))
define hid = Character('Hideyoshi', what_prefix="{dialogue}\"", what_suffix="\"{/dialogue}", who_prefix="{dialogue}", who_suffix="{/dialogue}", image="hid", ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="hid", callback=speaker("hid"))
define geo = Character('George', what_prefix="{dialogue}\"", what_suffix="\"{/dialogue}", who_prefix="{dialogue}", who_suffix="{/dialogue}", image="geo", ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="geo", callback=speaker("geo"))
define rud = Character('Rudolf', what_prefix="{dialogue}\"", what_suffix="\"{/dialogue}", who_prefix="{dialogue}", who_suffix="{/dialogue}", image="rud", ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="rud", callback=speaker("rud"))
define kir = Character('Kyrie', what_prefix="{dialogue}\"", what_suffix="\"{/dialogue}", who_prefix="{dialogue}", who_suffix="{/dialogue}", image="kir", ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="kir", callback=speaker("kir"))
define but = Character('Battler', what_prefix="{dialogue}\"", what_suffix="\"{/dialogue}", who_prefix="{dialogue}", who_suffix="{/dialogue}", image="but", ctc="ctc_blink", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="but", callback=speaker("but"))
define mar = Character('Maria', what_prefix="{dialogue}\"", what_suffix="\"{/dialogue}", who_prefix="{dialogue}", who_suffix="{/dialogue}", image="mar", ctc="ctc_blink", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="mar", callback=speaker("mar"))
define ros = Character('Rosa', what_prefix="{dialogue}\"", what_suffix="\"{/dialogue}", who_prefix="{dialogue}", who_suffix="{/dialogue}", image="ros", ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="ros", callback=speaker("ros"))
define nan = Character('Nanjo', what_prefix="{dialogue}\"", what_suffix="\"{/dialogue}", who_prefix="{dialogue}", who_suffix="{/dialogue}", image="nan", ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="nan", callback=speaker("nan"))
define gen = Character('Genji', what_prefix="{dialogue}\"", what_suffix="\"{/dialogue}", who_prefix="{dialogue}", who_suffix="{/dialogue}", image="gen", ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="gen", callback=speaker("gen"))
define sha = Character('Shannon', what_prefix="{dialogue}\"", what_suffix="\"{/dialogue}", who_prefix="{dialogue}", who_suffix="{/dialogue}", image="sha", ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="sha", callback=speaker("sha"))
define kan = Character('Kanon', what_prefix="{dialogue}\"", what_suffix="\"{/dialogue}", who_prefix="{dialogue}", who_suffix="{/dialogue}", image="kan", ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="kan", callback=speaker("kan"))
define goh = Character('Gohda Toshiro', what_prefix="{dialogue}\"", what_suffix="\"{/dialogue}", who_prefix="{dialogue}", who_suffix="{/dialogue}", image="goh", ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="goh", callback=speaker("goh"))
define kum = Character('Kumasawa', what_prefix="{dialogue}\"", what_suffix="\"{/dialogue}", who_prefix="{dialogue}", who_suffix="{/dialogue}", image="kum", ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="kum", callback=speaker("kum"))
define lam = Character('LAMBDADELTA', what_prefix="{dialogue}\"", what_suffix="\"{/dialogue}", who_prefix="{dialogue}", who_suffix="{/dialogue}", image="lam", ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="lam", callback=speaker("lam"))
define ber = Character('BERNKASTEL', what_prefix="{dialogue}\"", what_suffix="\"{/dialogue}", who_prefix="{dialogue}", who_suffix="{/dialogue}", image="ber", ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="ber", callback=speaker("ber"))
define ron = Character('Ronove', what_prefix="{dialogue}\"", what_suffix="\"{/dialogue}", who_prefix="{dialogue}", who_suffix="{/dialogue}", image="ron", ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="ron", callback=speaker("ron"))
define wal = Character('VIRGILIA', what_prefix="{dialogue}\"", what_suffix="\"{/dialogue}", who_prefix="{dialogue}", who_suffix="{/dialogue}", image="wal", ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="wal", callback=speaker("wal"))
define gap = Character('Gaap', what_prefix="{dialogue}\"", what_suffix="\"{/dialogue}", who_prefix="{dialogue}", who_suffix="{/dialogue}", image="gap", ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="gap", callback=speaker("gap"))
define luc = Character('Lucifer', what_prefix="{dialogue}\"", what_suffix="\"{/dialogue}", who_prefix="{dialogue}", who_suffix="{/dialogue}", image="luc", ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="luc", callback=speaker("luc"))
define lev = Character('Leviathan', what_prefix="{dialogue}\"", what_suffix="\"{/dialogue}", who_prefix="{dialogue}", who_suffix="{/dialogue}", image="lev", ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="lev", callback=speaker("lev"))
define sat = Character('Satan', what_prefix="{dialogue}\"", what_suffix="\"{/dialogue}", who_prefix="{dialogue}", who_suffix="{/dialogue}", image="sat", ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="sat", callback=speaker("sat"))
define bel = Character('Belphegor', what_prefix="{dialogue}\"", what_suffix="\"{/dialogue}", who_prefix="{dialogue}", who_suffix="{/dialogue}", image="bel", ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="bel", callback=speaker("bel"))
define mam = Character('Mammon', what_prefix="{dialogue}\"", what_suffix="\"{/dialogue}", who_prefix="{dialogue}", who_suffix="{/dialogue}", image="mam", ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="mam", callback=speaker("mam"))
define bee = Character('Beelzebub', what_prefix="{dialogue}\"", what_suffix="\"{/dialogue}", who_prefix="{dialogue}", who_suffix="{/dialogue}", image="bee", ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="bee", callback=speaker("bee"))
define asm = Character('Asmodeus', what_prefix="{dialogue}\"", what_suffix="\"{/dialogue}", who_prefix="{dialogue}", who_suffix="{/dialogue}", image="asm", ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="asm", callback=speaker("asm"))
define fea = Character('FEATHERINE', what_prefix="{dialogue}\"", what_suffix="\"{/dialogue}", who_prefix="{dialogue}", who_suffix="{/dialogue}", image="fea", ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="fea", callback=speaker("fea"))
define ev1 = Character('EVA-BEATRICE', what_prefix="{dialogue}\"", what_suffix="\"{/dialogue}", who_prefix="{dialogue}", who_suffix="{/dialogue}", image="ev1", ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="ev1", callback=speaker("ev1"))
define vir = Character('Virgilius', what_prefix="{dialogue}\"", what_suffix="\"{/dialogue}", who_prefix="{dialogue}", who_suffix="{/dialogue}", image="vir", ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="vir", callback=speaker("vir"))
define fla = Character('Flaurus', what_prefix="{dialogue}\"", what_suffix="\"{/dialogue}", who_prefix="{dialogue}", who_suffix="{/dialogue}", image="fla", ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="fla", callback=speaker("fla"))
define aya = Character('Ayato', what_prefix="{dialogue}\"", what_suffix="\"{/dialogue}", who_prefix="{dialogue}", who_suffix="{/dialogue}", image="aya", ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="aya", callback=speaker("aya"))
define ay1 = Character('otayA', what_prefix="{dialogue}\"", what_suffix="\"{/dialogue}", who_prefix="{dialogue}", who_suffix="{/dialogue}", image="ay1", ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="ay1", callback=speaker("ay1"))
define ay2 = Character('Ayato', what_prefix="{dialogue}\"", what_suffix="\"{/dialogue}", who_prefix="{dialogue}", who_suffix="{/dialogue}", image="ay2", ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="ay2", callback=speaker("ay2"))
define zer = Character('ZERO', what_prefix="{dialogue}\"", what_suffix="\"{/dialogue}", who_prefix="{dialogue}", who_suffix="{/dialogue}", image="zer", ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="zer", callback=speaker("zer"))
define yur = Character('Yuria', what_prefix="{dialogue}\"", what_suffix="\"{/dialogue}", who_prefix="{dialogue}", who_suffix="{/dialogue}", image="yur", ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="yur", callback=speaker("yur"))
define rik = Character('Rika', what_prefix="{dialogue}\"", what_suffix="\"{/dialogue}", who_prefix="{dialogue}", who_suffix="{/dialogue}", image="rik", ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="rik", callback=speaker("rik"))
define hoj = Character('Satoko', what_prefix="{dialogue}\"", what_suffix="\"{/dialogue}", who_prefix="{dialogue}", who_suffix="{/dialogue}", image="hoj", ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="hoj", callback=speaker("hoj"))
define ren = Character('Rena', what_prefix="{dialogue}\"", what_suffix="\"{/dialogue}", who_prefix="{dialogue}", who_suffix="{/dialogue}", image="ren", ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="ren", callback=speaker("ren"))
define mio = Character('Mion', what_prefix="{dialogue}\"", what_suffix="\"{/dialogue}", who_prefix="{dialogue}", who_suffix="{/dialogue}", image="mio", ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="mio", callback=speaker("mio"))
define ois = Character('Oishi', what_prefix="{dialogue}\"", what_suffix="\"{/dialogue}", who_prefix="{dialogue}", who_suffix="{/dialogue}", image="ois", ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="ois", callback=speaker("ois"))
define narrator = Character(what_prefix="{dialogue}\"", what_suffix="\"{/dialogue}", ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, window_background="gui/[narratorbox].png", voice_tag=None, callback=speaker(None), window_yoffset=-0)
#define narrator = Character(ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag=None, callback=speaker(None))
define nvltext = Character(what_prefix="{dialogue}\"", what_suffix="\"{/dialogue}", kind=nvl, ctc="ctc_blink", ctc_position="nestled-close", voice_tag=None, callback=speaker(None))

## Sprites for Characterscreen ##
define rud_char = "gui/chars/rud.png"
define kyr_char = "gui/chars/kyr.png"
define ros_char = "gui/chars/ros.png"
define jes_char = "gui/chars/jes.png"
define but_char = "gui/chars/but.png"
define mar_char = "gui/chars/mar.png"
define kum_char = "gui/chars/kum.png"
define geo_char = "gui/chars/geo.png"
define goh_char = "gui/chars/goh.png"
define sha_char = "gui/chars/sha.png"
define eva_char = "gui/chars/eva.png"
define hid_char = "gui/chars/hid.png"
define bea_char = "gui/chars/bea.png"
