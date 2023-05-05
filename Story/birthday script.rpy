label birthday:

    pause (3)
    scene different_spiral_1a with dissolve
    pause (2)
    scene different_space_1a with gradientcirclefade
    pause 2.0
    $ play_music(face)
    pause 1
    play sound "audio/sfx/umise_052.ogg"
    show bea_a14_1_warai1 at m,ah('bea') with witchfadein
    pause 1
    bea "\"<Congratulations>"
    extend " Alles Gute zum Geburtstag Aiyla-chan!\""
    pause 1
    play sound "audio/sfx/umise_057.ogg"
    show lam_a11_akuwarai1 at r,ah('lam') with flash
    pause 1
    lam "\"Ich wusste es zuerst!"
    extend " ...Du gratulierst doch nur, weil ich es dir erzählt habe.\""
    hide bea_a14_1_warai1
    show bea_a13_majime2 at m,ah('bea')
    bea "\"Das ist aber gemein von Euch Fräulein Lambdadelta."
    extend " Darum darf ich ihr doch trotzdem gratulieren oder etwa nicht?\""
    pause 1
    play sound "audio/sfx/umise_052.ogg"
    show ber_a11_defo1 at l,ah('ber') with witchfadein
    pause 1
    ber "\"Du hast es doch auch von jemand anderes erfahren"
    extend " ...Lambda."
    ber "Fürst Zero hat dir gesagt, du sollst jedem sagen, dass sie Geburtstag hat."
    extend " ...Im Traum würde ich nicht daran denken, diesen Befehl zu verweigern.\""
    hide bea_a13_majime2
    show bea_a11_defo2 at m,ah('bea')
    hide lam_a11_akuwarai1
    show lam_a11_futeki3 at r,ah('lam')
    lam "\"Unser Herr hat uns befohlen ihr zu gratulieren, also bin ich die nächste!"
    lam "Herzlichen Glückwunsch zum Geburtstag, Aiyla-chan!"
    lam "Jetzt bist du dran, Bern...\""
    hide ber_a11_defo1
    show ber_a21_niramu1 at l,ah('ber')
    ber "\"Dass ich gezwungen werde einem einfachen Menschen zu gratulieren, ist echt lästig."
    extend " Aber wenn ich es verweiger, wird Fürst Zero mich mit Leichtigkeit zu feinen Staubpartikeln zermalmen, also habe ich keine Wahl."
    hide ber_a21_niramu1
    show ber_a21_shian1 at l,ah('ber')
    ber "*Räusper*"
    hide ber_a21_shian1
    show ber_a21_defo2 at l,ah('ber')
    ber "Alles gute....." 
    extend " Aiyla-chan........\""
    hide bea_a11_defo2
    show bea_a13_warai4 at m,ah('bea')
    bea "\"Gar nicht schlecht, Großes Fräulein Bernkastel!\""
    hide ber_a21_defo2
    show ber_a21_niramu1 at l,ah('ber')
    ber "\"Bitte töte mich..."
    extend " Fürst Zero........\""
    call chapterenda
    pause 2.0
    return

