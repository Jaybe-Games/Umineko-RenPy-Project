# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


# THIS_PATH is defined in chess_displayable.rpy
# define THIS_PATH = '00-chess-engine/'
init python:
    # for importing libraries
    import_dir = os.path.join(renpy.config.gamedir, THIS_PATH, 'python-packages')

# The game starts here.

label beatricechess:
    scene different_space_1a at bganistart
    $ songname = "Pitiful Sneerer"
    if persistent.showbgm == True:
        show screen showsong
    play music "audio/bgm/umib_1001_intro.ogg"
    queue music "audio/bgm/umib_1001_loop.ogg" loop
    show bea a11defo2 at rightedge with witchfadein 
    bea "Du denkst du kannst mich besiegen, Battlleeerrrr!!!"

label chess_game:
    # board notation
    $ fen = STARTING_FEN
    $ STOCKFISH_ENGINE = chess.engine.SimpleEngine.popen_uci(STOCKFISH, startupinfo=STARTUPINFO)
    $ depth = 25
    $ player_color = chess.WHITE

    window hide
    $ quick_menu = False

    # avoid rolling back and losing chess game state
    $ renpy.block_rollback()

    # disable Esc key menu to prevent the player from saving the game
    $ _game_menu_screen = None

    call screen chess(fen, player_color, depth)

    # re-enable the Esc key menu
    $ _game_menu_screen = 'save'

    # avoid rolling back and entering the chess game again
    $ renpy.block_rollback()

    # restore rollback from this point on
    $ renpy.checkpoint()

    # kill stockfish engine
    $ quit_stockfish()

    $ quick_menu = True
    window show

    if _return == DRAW:
        bea "Ein Unentschieden wie amüsant, kyahahaha!!."
    else: # RESIGN or CHECKMATE
        $ winner = "White" if _return == chess.WHITE else "Black"
        bea "Ich habe deine Schachfähigkeiten wohl unterschätzt, Battleerrr!!!"
        if player_color is not None: # PvC
            if _return == player_color:
                bea "<Congratulations>, Battler!"
            else:
                bea "Knie vor mir nieder und küss meine Schuhe, Battler."
    return
