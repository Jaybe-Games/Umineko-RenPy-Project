screen nvl(dialogue, slow_effect = slow_fade, slow_effect_delay = 0, always_effect = None, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue, slow_effect = slow_effect, slow_effect_delay = slow_effect_delay, always_effect = always_effect)

        else:

            use nvl_dialogue(dialogue, slow_effect = slow_effect, slow_effect_delay = slow_effect_delay, always_effect = always_effect)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True.

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue, slow_effect = slow_fade, slow_effect_delay = 0, always_effect = None):

    for dick_prick in dialogue:

        window:
            id dick_prick.window_id

            fixed:
                yfit gui.nvl_height is None

                fancytext dick_prick.what id dick_prick.what_id slow_effect slow_effect slow_effect_delay slow_effect_delay always_effect always_effect at dialogue_gradient


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = 3