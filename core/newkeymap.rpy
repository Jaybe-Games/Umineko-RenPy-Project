init python:

    renpy.clear_keymap_cache()

    #Keyboard & Mouse

    config.keymap['rollback'].remove('any_K_PAGEUP')
    config.keymap['rollback'].remove('any_KP_PAGEUP')
    config.keymap['rollback'].remove('K_AC_BACK')
    #config.keymap['rollback'].remove('mousedown_4')

    config.keymap['self_voicing'].remove('alt_K_v')
    config.keymap['self_voicing'].remove('K_v')

    config.keymap['clipboard_voicing'].remove('alt_shift_K_c')
    config.keymap['clipboard_voicing'].remove('shift_K_c')

    config.keymap['debug_voicing'].remove('alt_shift_K_v')
    config.keymap['debug_voicing'].remove('meta_shift_K_v')

    config.keymap['toggle_afm'].append('K_a')

    config.keymap['screenshot'].remove('alt_shift_K_s')
    config.keymap['screenshot'].remove('noshift_K_s')

    config.keymap['accessibility'].remove('K_a')

    config.keymap['save_delete'].remove('K_DELETE')
    config.keymap['save_delete'].remove('KP_DELETE')

    config.pad_bindings['pad_leftshoulder_press'].remove('rollback')
    config.pad_bindings['pad_lefttrigger_pos'].remove('rollback')
    config.pad_bindings['pad_back_press'].remove('rollback')

    config.pad_bindings['repeat_pad_leftshoulder_press'].remove('rollback')
    config.pad_bindings['repeat_pad_lefttrigger_pos'].remove('rollback')
    config.pad_bindings['repeat_pad_back_press'].remove('rollback')

    config.pad_bindings['pad_x_press'] = ['game_menu']

    config.pad_bindings['pad_b_press'].append('game_menu')

    config.pad_bindings['pad_leftshoulder_press'].append('toggle_afm')

    config.pad_bindings['pad_back_press'].append('fast_skip')
    config.pad_bindings['pad_rightshoulder_press'].append('toggle_skip')

    config.pad_bindings['pad_lefttrigger_pos'].append('dismiss')

