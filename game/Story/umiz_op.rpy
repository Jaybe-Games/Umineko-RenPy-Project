label umiz_op:
    pause 3
    ##Kapitel 0 - Eröffnung
    $ chapter = "Eröffnung"
    $ songname = "-"
    $ save_name = _("Episode0 Resurrection of the golden witch\nEröffnung")
    show screen showch
    $ _game_menu_screen = "cleanmenu"
    pause 3
    play sound umise_028
    show text001
    pause 8
    hide text001 with dissolve
    pause 2
    play wind umilse_005
    play rain umilse_012
    pause 2