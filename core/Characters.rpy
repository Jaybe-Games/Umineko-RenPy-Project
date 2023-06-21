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

define bea = Character('Beatrice {image=gui/wing.png}{alt}wing{/alt}', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="bea", callback=speaker("bea"))
define kin = Character('Ushiromiya Kinzo {image=gui/wing.png}{alt}wing{/alt}', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="kin", callback=speaker("kin"))
define cla = Character('Ushiromiya Krauss {image=gui/wing.png}{alt}wing{/alt}', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="cla", callback=speaker("cla"))
define nat = Character('Ushiromiya Natsuhi {image=gui/wing.png}{alt}wing{/alt}', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="nat", callback=speaker("nat"))
define jes = Character('Ushiromiya Jessica {image=gui/wing.png}{alt}wing{/alt}', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="jes", callback=speaker("jes"))
define eva = Character('Ushiromiya Eva {image=gui/wing.png}{alt}wing{/alt}', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="eva", callback=speaker("eva"))
define hid = Character('Ushiromiya Hideyoshi {image=gui/wing.png}{alt}wing{/alt}', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="hid", callback=speaker("hid"))
define geo = Character('Ushiromiya George {image=gui/wing.png}{alt}wing{/alt}', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="geo", callback=speaker("geo"))
define rud = Character('Ushiromiya Rudolf {image=gui/wing.png}{alt}wing{/alt}', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="rud", callback=speaker("rud"))
define kyr = Character('Ushiromiya Kyrie {image=gui/wing.png}{alt}wing{/alt}', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="kyr", callback=speaker("kyr"))
define but = Character('Ushiromiya Battler {image=gui/wing.png}{alt}wing{/alt}', ctc="ctc_blink", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="but", callback=speaker("but"))
define mar = Character('Ushiromiya Maria {image=gui/wing.png}{alt}wing{/alt}', ctc="ctc_blink", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="mar", callback=speaker("mar"))
define ros = Character('Ushiromiya Rosa {image=gui/wing.png}{alt}wing{/alt}', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="ros", callback=speaker("ros"))
define nan = Character('Nanjo Terumasa {image=gui/wing.png}{alt}wing{/alt}', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="nan", callback=speaker("nan"))
define gen = Character('Ronoue Genji {image=gui/wing.png}{alt}wing{/alt}', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="gen", callback=speaker("gen"))
define sha = Character('Shannon {image=gui/wing.png}{alt}wing{/alt}', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="sha", callback=speaker("sha"))
define kan = Character('Kanon {image=gui/wing.png}{alt}wing{/alt}', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="kan", callback=speaker("kan"))
define goh = Character('Gohda Toshiro {image=gui/wing.png}{alt}wing{/alt}', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="goh", callback=speaker("goh"))
define kum = Character('Kumasawa Chiyo {image=gui/wing.png}{alt}wing{/alt}', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="kum", callback=speaker("kum"))
define lam = Character('Lambdadelta {image=gui/wing.png}{alt}wing{/alt}', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="lam", callback=speaker("lam"))
define ber = Character('Bernkastel {image=gui/wing.png}{alt}wing{/alt}', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="ber", callback=speaker("ber"))
define ron = Character('Ronove {image=gui/wing.png}{alt}wing{/alt}', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="ron", callback=speaker("ron"))
define wal = Character('Virgilia {image=gui/wing.png}{alt}wing{/alt}', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="wal", callback=speaker("wal"))
define gap = Character('Gaap {image=gui/wing.png}{alt}wing{/alt}', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="gap", callback=speaker("gap"))
define luc = Character('Lucifer {image=gui/wing.png}{alt}wing{/alt}', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="luc", callback=speaker("luc"))
define lev = Character('Leviathan {image=gui/wing.png}{alt}wing{/alt}', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="lev", callback=speaker("lev"))
define sat = Character('Satan {image=gui/wing.png}{alt}wing{/alt}', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="sat", callback=speaker("sat"))
define bel = Character('Belphegor {image=gui/wing.png}{alt}wing{/alt}', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="bel", callback=speaker("bel"))
define mam = Character('Mammon {image=gui/wing.png}{alt}wing{/alt}', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="mam", callback=speaker("mam"))
define bee = Character('Beelzebub {image=gui/wing.png}{alt}wing{/alt}', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="bee", callback=speaker("bee"))
define asm = Character('Asmodeus {image=gui/wing.png}{alt}wing{/alt}', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="asm", callback=speaker("asm"))
define fea = Character('Featherine {image=gui/wing.png}{alt}wing{/alt}', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="fea", callback=speaker("fea"))
define ev1 = Character('EVA-Beatrice {image=gui/wing.png}{alt}wing{/alt}', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="ev1", callback=speaker("ev1"))
define vir = Character('Virgilius {image=gui/wing.png}{alt}wing{/alt}', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="vir", callback=speaker("vir"))
define fla = Character('Flaurus {image=gui/wing.png}{alt}wing{/alt}', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="fla", callback=speaker("fla"))
define aya = Character('Ayato {image=gui/wing.png}{alt}wing{/alt}', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="aya", callback=speaker("aya"))
define ay1 = Character('otayA {image=gui/wing.png}{alt}wing{/alt}', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="ay1", callback=speaker("ay1"))
define ay2 = Character('Ushiromiya Ayato {image=gui/wing.png}{alt}wing{/alt}', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="ay2", callback=speaker("ay2"))
define zer = Character('ZERO {image=gui/wing.png}{alt}wing{/alt}', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="zer", callback=speaker("zer"))
define yur = Character('Ushiromiya Yuria {image=gui/wing.png}{alt}wing{/alt}', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="yur", callback=speaker("yur"))
define rik = Character('Furude Rika {image=gui/wing.png}{alt}wing{/alt}', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="rik", callback=speaker("rik"))
define hoj = Character('Houjou Satoko {image=gui/wing.png}{alt}wing{/alt}', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="hoj", callback=speaker("hoj"))
define ren = Character('Ryuugu Rena {image=gui/wing.png}{alt}wing{/alt}', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="ren", callback=speaker("ren"))
define mio = Character('Sonozaki Mion {image=gui/wing.png}{alt}wing{/alt}', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="mio", callback=speaker("mio"))
define ois = Character('Kuraudo Oishi {image=gui/wing.png}{alt}wing{/alt}', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, voice_tag="ois", callback=speaker("ois"))
define narrator = Character(ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.2, window_background="gui/narratorbox.png", voice_tag=None, callback=speaker(None))
define nvltext = Character(kind=nvl, ctc="ctc_blink", ctc_position="nestled-close", voice_tag=None, callback=speaker(None))

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