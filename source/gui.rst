##############
User Interface
##############

..  TODO:
      - Operations more than 1 second are animated

This chapter describes the user interface of Tic Tac Toe. This includes the main
game board, controls, and all game menus.


==========
Game Board
==========
The game board is where players spend the majority of their time. Additionally,
the game loads directly to this view ensuring players get to gameplay as quickly
as possible without menus getting in the way. [#firstview]_ A concept drawing of
the game board is shown in :numref:`fig-ui-game-board`.

..  _fig-ui-game-board:
..  figure:: img/ui/game-board.*

    Game board concept drawing.

The game board contains the following items of interest:

1.  The marks and grid. The appearance of these depend on the current environment
    being played. However, the marks for all environments use the same center
    point and have the same selectable hotspot. This ensures consistency between
    environments when using the mouse.
2.  The background of the game board depends on the current environment.
3.  The hamburger button opens the :ref:`ref-ui-main-menu`.
4.  Status text indicates who gets to make the next move and the outcome of
    the game. Once the game is over buttons to play the next game or return to
    the menu also appear in this area. The text is outlined or shaded such that
    it is visible over any possible background.

A major focus of the game is playing Tic Tac Toe in variety of stunning
environments that control how the marks, grid, and background look. Thus, a
minimalist approach is used for the game board view. The only UI widgets are a
menu button and some status text.

--------
Speedrun
--------
Additional UI widgets are added to the game board to facilitate speedrun mode.
:numref:`fig-ui-speedrun-game-board` shows the speedrun gameboard.

..  _fig-ui-speedrun-game-board:
..  figure:: img/ui/speedrun-game-board.*

    Speedrun game board concept drawing.

Items of interest are:

1.  The speedrun status display prominently shows the elapsed time of the run.
    This helps give the player a sense of urgency and lets them see if they are
    on track to get a best time.
2.  Splits for each game are additionally displayed. Dashes or other marks are
    used for games that have yet to be played. This allows players to quickly
    visually gauge how many games remain.
3.  Opening the game's menu ends the run. The run is disqualified.
4.  Status text indicates the current turn. If the player loses a game, the
    status text notes that the run is disqualified and the player is invited
    to try the run again or return to the Speedrun menu. [#speedrunloss]_

When a game is competed successfully the next game starts immediately allowing
players to go as fast as possible through the games.


========
Controls
========
The game can fully played with either a mouse or keyboard. New or casual players
may prefer to use a mouse where as speedrun players may prefer to use the
keyboard.

-----
Mouse
-----
Mouse left click is used to select free squares and menu press buttons. Right
click and other mouse buttons are unused.

------------
Key Bindings
------------
The game supports being played using the keyboard. :numref:`fig-ui-keybindings`
shows the game's keybindings for selecting squares.

..  _fig-ui-keybindings:
..  figure:: img/ui/keybindings.*

    Keybindings for selecting squares.

The :kbd:`numpad` keys are available for right handed players and the :kbd:`QWE`
set of keys are available for left handed players.

The :kbd:`arrow`, :kbd:`ESC`, :kbd:`Enter`, and :kbd:`Space` keys
allow users to navigate the game's menus.


=====
Menus
=====
The Tic Tac Toe menus allow players to select the various game modes and to
customize the game.

See :numref:`uml-game-menus` for details on how the menus connect.

..  _ref-ui-main-menu:

---------
Main Menu
---------
The main menu


..  _fig-ui-main-menu:
..  figure:: img/ui/main-menu.*

    Main menu concept drawing.

1.  The title of the game is prominently displayed at the top of the menu.
2.  Buttons.

..  TODO: main menu is overlaid on top of the active game board.


-------------
Single-player
-------------

..  _fig-ui-single-player:
..  figure:: img/ui/single-player.*

    Single-player menu concept drawing.

1.  The :guilabel:`Play as` selector allows players to select the mark they
    wish to use throughout the games.
2.  The difficulty buttons select the difficulty then start a new single player
    game.
3.  :guilabel:`Speedrun` goes to the Speedrun menu.
4.  The :guilabel:`Back` button returns to the main menu.


--------
Speedrun
--------



..  _fig-ui-speedrun-start:
..  figure:: img/ui/speedrun-start.*

    sadfsadfsadf

Text and lists and such.



..  _fig-ui-speedrun-best-time:
..  figure:: img/ui/speedrun-best-time.*

    sadfsadfsadf

Text and lists and such.


-------
Options
-------

..  _fig-ui-options:
..  figure:: img/ui/options.*

    sadfsadfsadf

Text and lists and such.

-------
Credits
-------

..  _fig-ui-credits:
..  figure:: img/ui/credits.*

    sadfsadfsadf

Text and lists and such.


.. _ref-ui-loading-screen:

--------------
Loading Screen
--------------

----
Help
----


==============
Menu Flowchart
==============

The

..  _uml-game-menus:
..  uml::
    :caption: Overview.
    :height: 8in

    hide empty description

    ' Create aliases for state names with spaces
    state "Tic Tac Toe Board" as game_board
    state "Main Menu" as main_menu
    state "Single-player" as singleplayer
    state "Speedrun" as speedrun
    state "Speedrun Board" as speedrun_game_board
    state "New Best Time!" as speedrun_best_time

    Loading --> game_board
    game_board --> main_menu : Menu / ESC

    main_menu --> game_board : Resume Game
    main_menu --> game_board : Multiplayer
    main_menu --> singleplayer : Single-player

    singleplayer --> game_board : Easy \n Medium \n Hard
    singleplayer --> speedrun : Speedrun
    singleplayer --> main_menu : Back

    speedrun --> singleplayer : Back
    speedrun --> speedrun_game_board : Start
    speedrun_game_board --> speedrun : Non Best Time
    speedrun_game_board --> speedrun_best_time
    speedrun_best_time --> speedrun : Close



..  rubric:: Footnotes

..  [#firstview] The loaded game is a single-player game using the last
        difficulty and player mark settings. The defaults for these are Medium
        difficulty and X marks.
..  [#speedrunloss] If the player loses a speedrun game, the board remains
        visible so the player can see where they made mistakes. This allows them
        to adjust their strategy for next time.
