###########################
User Interface and Controls
###########################

..  TODO:
      - Mouse
      - Numpad / keyboard
      - Both can fully control the game
      - Concept drawing of each menu
        - Main Menu
          - Easy / Medium / Hard difficulty select
          - Speed Run / Fastest Runs
          - Options
          - Credits
          - Exit / Quit
        - Options
          - Music on / off
          - Sound FX on / Off
          - Show numpad mapping numbers
        - Credits
        - Main menu music or how in progress game music plays during the menu.
      - Flow chart of screens
      - Show the grid and how clicking / numpad maps to it
      - Operations more than 1 second are animated
      - main game board
        - additional widgets for speed run mode like splits for each game
          and a total running time.
        - The game starts here on the difficulty last played (normal by default)

==========
Game Board
==========


More text here

..  _fig-ui-game-board:
..  figure:: img/ui/game-board.*

    sadfsadfsadf

Text andlists and such.

=====
Menus
=====



..  _fig-ui-main-menu:
..  figure:: img/ui/main-menu.*

    sadfsadfsadf

Text and lists and such.



..  _fig-ui-single-player:
..  figure:: img/ui/single-player.*

    sadfsadfsadf

Text and lists and such.

..  _fig-ui-options:
..  figure:: img/ui/options.*

    sadfsadfsadf

Text and lists and such.


..  _fig-ui-credits:
..  figure:: img/ui/credits.*

    sadfsadfsadf

Text and lists and such.



========
Speedrun
========

..  _fig-ui-speedrun-game-board:
..  figure:: img/ui/speedrun-game-board.*

    sadfsadfsadf

Text and lists and such.



..  _fig-ui-speedrun-start:
..  figure:: img/ui/speedrun-start.*

    sadfsadfsadf

Text and lists and such.



..  _fig-ui-speedrun-best-time:
..  figure:: img/ui/speedrun-best-time.*

    sadfsadfsadf

Text and lists and such.


=====
Other
=====

.. TODO: Help, and loading screen



..  _uml-game-screens-states:
..  uml::
    :caption: asdfsadfsadf.

    hide empty description

    ' Create aliases for state names with spaces
    state "Tic Tac Toe Board" as game_board
    state "Main Menu" as main_menu
    state "Single-player" as singleplayer
    state "Speedrun Board" as speedrun_game_board
    state "New Best Time!" as speedrun_best_time

    [*] --> Loading

    Loading --> game_board
    game_board --> main_menu : Menu / ESC
    main_menu --> game_board : Resume Game
    main_menu --> singleplayer : Single-player
    singleplayer --> game_board : Easy \n Medium \n Hard
    singleplayer --> Speedrun : Speedrun
    singleplayer --> main_menu
    main_menu --> game_board : Multiplayer

    Speedrun --> speedrun_game_board : Start
    Speedrun --> singleplayer
    speedrun_game_board --> Speedrun : Non Best Time
    speedrun_game_board --> speedrun_best_time
    speedrun_best_time --> Speedrun : Close

    main_menu --> [*] : Exit
