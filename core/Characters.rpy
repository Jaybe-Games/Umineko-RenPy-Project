init python:
  
    # This is set to the name of the character that is speaking, or
    # None if no character is currently speaking.
    speaking = None
  
    # This returns speaking if the character is speaking, and done if the
    # character is not.
    def while_speaking(name, speak_d, done_d, st, at):
        if renpy.music.is_playing('voice') and speaking == name:
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

define bea = Character('Beatrice {image=gui/wing.png}{alt}wing{/alt}', callback=name_callback, cb_name='bea', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.1)
define kin = Character('Ushiromiya Kinzo {image=gui/wing.png}{alt}wing{/alt}', callback=name_callback, cb_name='kin', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.1)
define cla = Character('Ushiromiya Krauss {image=gui/wing.png}{alt}wing{/alt}', callback=name_callback, cb_name='cla', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.1)
define nat = Character('Ushiromiya Natsuhi {image=gui/wing.png}{alt}wing{/alt}', callback=name_callback, cb_name='nat', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.1)
define jes = Character('Ushiromiya Jessica {image=gui/wing.png}{alt}wing{/alt}', callback=name_callback, cb_name='jes', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.1)
define eva = Character('Ushiromiya Eva {image=gui/wing.png}{alt}wing{/alt}', callback=name_callback, cb_name='eva', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.1)
define hid = Character('Ushiromiya Hideyoshi {image=gui/wing.png}{alt}wing{/alt}', callback=name_callback, cb_name='hid', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.1)
define geo = Character('Ushiromiya George {image=gui/wing.png}{alt}wing{/alt}', callback=name_callback, cb_name='geo', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.1)
define rud = Character('Ushiromiya Rudolf {image=gui/wing.png}{alt}wing{/alt}', callback=name_callback, cb_name='rud', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.1)
define kyr = Character('Ushiromiya Kyrie {image=gui/wing.png}{alt}wing{/alt}', callback=name_callback, cb_name='kyr', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.1)
define but = Character('Ushiromiya Battler {image=gui/wing.png}{alt}wing{/alt}', callback=name_callback, cb_name='but', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.1)
define mar = Character('Ushiromiya Maria {image=gui/wing.png}{alt}wing{/alt}', callback=name_callback, cb_name='mar', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.1)
define ros = Character('Ushiromiya Rosa {image=gui/wing.png}{alt}wing{/alt}', callback=name_callback, cb_name='ros', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.1)
define nan = Character('Nanjo Terumasa {image=gui/wing.png}{alt}wing{/alt}', callback=name_callback, cb_name='nan', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.1)
define gen = Character('Ronoue Genji {image=gui/wing.png}{alt}wing{/alt}', callback=name_callback, cb_name='gen', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.1)
define sha = Character('Shannon {image=gui/wing.png}{alt}wing{/alt}', callback=name_callback, cb_name='sha', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.1)
define kan = Character('Kanon {image=gui/wing.png}{alt}wing{/alt}', callback=name_callback, cb_name='kan', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.1)
define goh = Character('Gohda Toshiro {image=gui/wing.png}{alt}wing{/alt}', callback=name_callback, cb_name='goh', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.1)
define kum = Character('Kumasawa Chiyo {image=gui/wing.png}{alt}wing{/alt}', callback=name_callback, cb_name='kum', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.1)
define lam = Character('Lambdadelta {image=gui/wing.png}{alt}wing{/alt}', callback=name_callback, cb_name='lam', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.1)
define ber = Character('Bernkastel {image=gui/wing.png}{alt}wing{/alt}', callback=name_callback, cb_name='ber', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.1)
define ron = Character('Ronove {image=gui/wing.png}{alt}wing{/alt}', callback=name_callback, cb_name='ron', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.1)
define wal = Character('Virgilia {image=gui/wing.png}{alt}wing{/alt}', callback=name_callback, cb_name='wal', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.1)
define gap = Character('Gaap {image=gui/wing.png}{alt}wing{/alt}', callback=name_callback, cb_name='gap', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.1)
define luc = Character('Lucifer {image=gui/wing.png}{alt}wing{/alt}', callback=name_callback, cb_name='luc', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.1)
define lev = Character('Leviathan {image=gui/wing.png}{alt}wing{/alt}', callback=name_callback, cb_name='lev', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.1)
define sat = Character('Satan {image=gui/wing.png}{alt}wing{/alt}', callback=name_callback, cb_name='sat', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.1)
define bel = Character('Belphegor {image=gui/wing.png}{alt}wing{/alt}', callback=name_callback, cb_name='bel', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.1)
define mam = Character('Mammon {image=gui/wing.png}{alt}wing{/alt}', callback=name_callback, cb_name='mam', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.1)
define bee = Character('Beelzebub {image=gui/wing.png}{alt}wing{/alt}', callback=name_callback, cb_name='bee', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.1)
define asm = Character('Asmodeus {image=gui/wing.png}{alt}wing{/alt}', callback=name_callback, cb_name='asm', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.1)
define fea = Character('Featherine {image=gui/wing.png}{alt}wing{/alt}', callback=name_callback, cb_name='fea', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.1)
define ev1 = Character('EVA-Beatrice {image=gui/wing.png}{alt}wing{/alt}', callback=name_callback, cb_name='ev1', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.1)
define vir = Character('Virgilius {image=gui/wing.png}{alt}wing{/alt}', callback=name_callback, cb_name='vir', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.1)
define fla = Character('Flaurus {image=gui/wing.png}{alt}wing{/alt}', callback=name_callback, cb_name='fla', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.1)
define aya = Character('Ayato {image=gui/wing.png}{alt}wing{/alt}', callback=name_callback, cb_name='aya', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.1)
define ay1 = Character('otayA {image=gui/wing.png}{alt}wing{/alt}', callback=name_callback, cb_name='ay1', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.1)
define zer = Character('ZERO {image=gui/wing.png}{alt}wing{/alt}', callback=name_callback, cb_name='zer', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.1)
define yur = Character('Yuria {image=gui/wing.png}{alt}wing{/alt}', callback=name_callback, cb_name='yur', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.1)
define rik = Character('Furude Rika {image=gui/wing.png}{alt}wing{/alt}', callback=name_callback, cb_name='rik', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.1)
define hoj = Character('Houjou Satoko {image=gui/wing.png}{alt}wing{/alt}', callback=name_callback, cb_name='hoj', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.1)
define ren = Character('Ryuugu Rena {image=gui/wing.png}{alt}wing{/alt}', callback=name_callback, cb_name='ren', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.1)
define mio = Character('Sonozaki Mion {image=gui/wing.png}{alt}wing{/alt}', callback=name_callback, cb_name='mio', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.1)
define ois = Character('Kuraudo Oishi {image=gui/wing.png}{alt}wing{/alt}', callback=name_callback, cb_name='ois', ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.1)
define narrator = Character(callback = name_callback, cb_name = None, ctc="ctc_blink", ctc_position="nestled-close", show_slow_effect = slow_fade, show_slow_effect_delay = 0.1, window_background="gui/narratorbox.png")

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