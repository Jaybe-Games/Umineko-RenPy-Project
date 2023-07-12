image blackpic = "images/system/black.png"

label supersecret:

$ discord.update(state = "Talking with the Author")
$ discord.update(details = "Unknown")
$ chapter = 404
$ songname = "-"
$ _game_menu_screen = None
play sound "audio/sfx/umise_1006.ogg"
show ware2
stop music fadeout 2.0
pause(3)
scene black with dissolve
pause (2)
show moon_1p
call rainlayer from _call_rainlayer
play wind "audio/sfx/umilse_005.ogg" fadein 3.0
play rain "audio/sfx/umilse_012.ogg" fadein 3.0
play sound "audio/sfx/umise_052.ogg"
with gradientcirclefade
pause(2)
$ _game_menu_screen = "cleanmenu"
"“Hey!"
extend " Du da!"
extend " Erklär mir bitte, wie du hierher gekommen bist."
window hide
call butterfly1 from _call_butterfly1
window show
"Du kannst mir jetzt nicht erzählen, dass du einfach nur irgendwo drauf geklickt hast und dann bist du einfach nur durch Zufall hier gelandet."
"Ich könnte Wetten abschließen, dass es dir irgendjemand erzählt hat."
"Willst du alle Trophäen haben und hast deshalb im Internet nach diesem Ort gesucht? Hat diese Visual Novel überhaupt eine Community?"
"Jedenfalls kann ich dir jetzt, da du hier bist, auch etwas erzählen."
$ Achievement.add(achievement_silver2)
"Ich habe keinen Namen, ich bin nur der Autor und habe die Macht die Dinge so zu lenken, wie ich will."
"Ich hatte viel Freude daran, dieses Narrativ zum Leben zu erwecken."
"Wisst ihr, wie lange diese Geschichte in meinem Kopf herumgeisterte, bevor ich sie endlich niederschrieb?"
"Ich bin mir sicher, es waren eine Quadrillion Jahre."
"Das Problem bei dieser Geschichte wird sein, dass die Umineko-Community jeden Goldenen Schmetterling zehn Mal umdrehen wird, um so schnell wie möglich eine Lösung zu finden, und da habe ich einen Tipp für jeden von euch."
"Wenn ihr denkt, etwas müsse so und so sein, weil es im ursprünglichen Umineko so ist, dann habt ihr verloren."
"Es gibt nichts Befriedigenderes, als eine ganze Community zu verschaukeln, weil es Umineko ist, aber vergesst nicht, dass Umineko eine Katzenbox voller Geheimnisse ist."
"Und diese Katzenbox ist eine ganz besondere, denn hier werden Dinge gemacht, die untypisch für die Katzenbox von Beatrice sind. Also lasst euch nicht reinlegen und fangt an nachzudenken."
"Damit sollte ich eure grauen Gehirnzellen zum Arbeiten gebracht haben, obwohl dieser Ort dafür gar nicht nötig gewesen wäre, da diese Katzenbox schon genug Verwirrung stiftet."
"Mensch," 
extend " hast du gar nichts zu sagen?"
extend " Dann benutze ich jetzt meine Macht als Autor, um dich zurück zum Hauptmenü zu bringen."
"Aber denk daran, wenn du zurückkommst, werde ich mich nicht mehr an dich erinnern, denn ich bin nur der Autor, ich weiß nicht, wer mich an diesem stillen Ort belästigt."
"Ich bin sicher, dass ich dir genau dasselbe noch einmal erzählen werde."
"Also dann, lebe wohl.”"
window hide
call hidebf1 from _call_hidebf1
pause(2)
call chapterendsecret from _call_chapterendsecret
stop wind fadeout 2.0
stop rain fadeout 2.0
pause(3)
return
