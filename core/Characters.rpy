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



define bea = Character('        BEATRICE        ', color="#fff", callback=name_callback, cb_name='bea')
define kin = Character('        Kinzo        ', color="#fff", callback=name_callback, cb_name='kin')
define cla = Character('        Krauss        ', color="#fff", callback=name_callback, cb_name='cla')
define nat = Character('        Natsuhi        ', color="#fff", callback=name_callback, cb_name='nat')
define jes = Character('        Jessica        ', color="#fff", callback=name_callback, cb_name='jes')
define eva = Character('        Eva        ', color="#fff", callback=name_callback, cb_name='eva')
define hid = Character('        Hideyoshi        ', color="#fff", callback=name_callback, cb_name='hid')
define geo = Character('        George        ', color="#fff", callback=name_callback, cb_name='geo')
define rud = Character('        Rudolf        ', color="#fff", callback=name_callback, cb_name='rud')
define kyr = Character('        Kyrie        ', color="#fff", callback=name_callback, cb_name='kyr')
define but = Character('        Battler        ', color="#fff", callback=name_callback, cb_name='but')
define mar = Character('        Maria        ', color="#fff", callback=name_callback, cb_name='mar')
define ros = Character('        Rosa        ', color="#fff", callback=name_callback, cb_name='ros')
define nan = Character('        Nanjo        ', color="#fff", callback=name_callback, cb_name='nan')
define gen = Character('        Genji        ', color="#fff", callback=name_callback, cb_name='gen')
define sha = Character('        Shannon        ', color="#fff", callback=name_callback, cb_name='sha')
define kan = Character('        Kanon        ', color="#fff", callback=name_callback, cb_name='kan')
define goh = Character('        Gohda        ', color="#fff", callback=name_callback, cb_name='goh')
define kum = Character('        Kumasawa        ', color="#fff", callback=name_callback, cb_name='kum')
define lam = Character('        LAMBDADELTA        ', color="#fff", callback=name_callback, cb_name='lam')
define ber = Character('        BERNKASTEL        ', color="#fff", callback=name_callback, cb_name='ber')
define ron = Character('        Ronove        ', color="#fff", callback=name_callback, cb_name='ron')
define wal = Character('        Virgilia        ', color="#fff", callback=name_callback, cb_name='wal')
define gap = Character('        Gaap        ', color="#fff", callback=name_callback, cb_name='gap')
define luc = Character('        Lucifer        ', color="#fff", callback=name_callback, cb_name='luc')
define lev = Character('        Leviathan        ', color="#fff", callback=name_callback, cb_name='lev')
define sat = Character('        Satan        ', color="#fff", callback=name_callback, cb_name='sat')
define bel = Character('        Belphegor        ', color="#fff", callback=name_callback, cb_name='bel')
define mam = Character('        Mammon        ', color="#fff", callback=name_callback, cb_name='mam')
define bee = Character('        Beelzebub        ', color="#fff", callback=name_callback, cb_name='bee')
define asm = Character('        Asmodeus        ', color="#fff", callback=name_callback, cb_name='asm')
define fea = Character('        FEATHERINE        ', color="#fff", callback=name_callback, cb_name='fea')
define ev1 = Character('        EVA-Beatrice        ', color="#fff", callback=name_callback, cb_name='ev1')
define vir = Character('        Virgilius        ', color="#fff", callback=name_callback, cb_name='vir')
define fla = Character('        Flaurus        ', color="#fff", callback=name_callback, cb_name='fla')
define aya = Character('        Ayato        ', color="#fff", callback=name_callback, cb_name='aya')
define ay1 = Character('        otayA        ', color="#fff", callback=name_callback, cb_name='ay1')
define zer = Character('        ZERO        ', color="#fff", callback=name_callback, cb_name='zer')
define yur = Character('        Yuria        ', color="#fff", callback=name_callback, cb_name='yur')
define rik = Character('        Rika        ', color="#fff", callback=name_callback, cb_name='rik')
define hoj = Character('        Satoko        ', color="#fff", callback=name_callback, cb_name='hoj')
define ren = Character('        Rena        ', color="#fff", callback=name_callback, cb_name='ren')
define mio = Character('        Mion        ', color="#fff", callback=name_callback, cb_name='mio')
define ois = Character('        Oishi        ', color="#fff", callback=name_callback, cb_name='ois')
define narrator = Character(callback = name_callback, cb_name = None)

## Sprites for Characterscreen ##
define rud_char = "images/sprites/rud/rud_a11_warai1.png"
define kyr_char = "images/sprites/kyr/kir_a11_defo1.png"
define ros_char = "images/sprites/ros/ros_a11_warai1.png"
define jes_char = "images/sprites/jes/jes_a11_warai1.png"
define but_char = "images/sprites/but/but_b11_warai2.png"
define mar_char = "images/sprites/mar/mar_a11_warai1.png"
define kum_char = "images/sprites/kum/kum_a11_defo1.png"
define geo_char = "images/sprites/geo/geo_a11_defo1.png"
define goh_char = "images/sprites/goh/goh_a11_defo1.png"
define sha_char = "images/sprites/sha/sha_a11_defo1.png"
define eva_char = "images/sprites/eva/eva_b21_akire1go.png"
define hid_char = "images/sprites/hid/hid_a11_defo1.png"
define bea_char = "images/sprites/bea/bea_a11_defo2.png"

## Battler a11

#image but_a11_1_0 = LiveComposite(
    #(937, 1227),
    #(0, 0), "images/sprites/but_a11_1_base.png",
    #(0, 0), WhileSpeaking("but", "but_a11_1_mouth", "images/sprites/but_a11_1_3_mouth.png",),
    #)

#image but_a11_1_mouth:
    #"but_a11_1_1_mouth"
    #pause 0.10
    #"but_a11_1_2_mouth"
    #pause 0.10
    #"but_a11_1_3_mouth"
    #pause 0.10
    #repeat