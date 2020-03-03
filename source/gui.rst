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
customize the game. The :numref:`uml-screen-flowchart` provides details on how
the menus connect.

Each menu is described in the following sections.

-------
General
-------
Unless otherwise noted, the information in this section applies to all menus.

The menus have translucent or blurred background that show the active
environment. This includes any animations or environment FX. Additionally, the
environment's sound track continues to play while the menus are open.


..  _ref-ui-main-menu:

---------
Main Menu
---------
The main menu provides a central point for users to navigate to the game's
various modes and settings. :numref:`fig-ui-main-menu` shows the main menu.

..  _fig-ui-main-menu:
..  figure:: img/ui/main-menu.*

    Main menu concept drawing.

1.  The title of the game is prominently displayed at the top of the menu.
2.  The :guilabel:`Resume Game` button is visible if there is a current game in
    progress. Selecting it closes the menu and returns the player to the game.
3.  New game buttons. The :guilabel:`Single-player` button navigates to the
    while the :ref:`ref-ui-single-player` screen while the
    :guilabel:`Multiplayer` button immediately starts a new multiplayer game.
4.  Miscellaneous buttons to open the :ref:`ref-ui-options`,
    :ref:`ref-ui-credits`, :ref:`ref-ui-help` screens.
5.  :guilabel:`Exit` closes the game and returns the user to their desktop.


..  _ref-ui-single-player:

-------------
Single-player
-------------
The single-player menu, shown in :numref:`fig-ui-single-player`, allows players
start new single-player games.

..  _fig-ui-single-player:
..  figure:: img/ui/single-player.*

    Single-player menu concept drawing.

1.  The :guilabel:`Play as` selector allows players to select the mark they
    wish to use throughout the games.
2.  The difficulty buttons select the difficulty then start a new single player
    game. Selecting one of these buttons closes the menu and launches a new
    single-player game with the requested settings.
3.  The :guilabel:`Speedrun` button navigates to the :ref:`ref-ui-speedrun` menu.
4.  The :guilabel:`Back` button returns to the main menu.


..  _ref-ui-speedrun:

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


..  _ref-ui-options:

-------
Options
-------
The options screen contains all of the game's player configurable options.
:numref:`fig-ui-options` shows this screen.

..  _fig-ui-options:
..  figure:: img/ui/options.*

    Options screen concept drawing.

1.  Music and Sound FX sliders to control the volume of these items. This allows
    players to mute some or all of the in-game sounds.
2.  :guilabel:`Reset to Defaults` rests all options to their default values.
3.  The :guilabel:`Back` button returns to the main menu.


..  _ref-ui-credits:

-------
Credits
-------
The credits screen displays information the game's developers and helps fulfill
the :doc:`misc/license-compliance` obligations. The credits screen is shown in
:numref:`fig-ui-credits`.

..  _fig-ui-credits:
..  figure:: img/ui/credits.*

    Credits screen concept drawing.

The credits screen contains the following items:

1.  Scrolling list of developer names, third party assets, and other information
    about the game.
2.  :guilabel:`Back` returns to the :ref:`ref-ui-main-menu`.

The credits screen uses a different background and soundtrack than the other
menus. The background consists of one or more Tic Tac Toe games being played
in a variety of environments. However, the environments are changed several times
per game. This showcases the many environments of the game.

The credits screen has its own sound track. The music and sound FX of the
individual environments are not used.

Once all of the credits have played the screen remains open with Tic Tac Toe
games being played in the background.


.. _ref-ui-loading-screen:

--------------
Loading Screen
--------------
If necessary for technical reasons, the loading screen provides feedback to the
player while assets are loaded. This screen is only shown when the game first
loads.


..  _ref-ui-help:

----
Help
----
The help screen provides information on how to play Tic Tac Toe, the application
version, how to report bugs, and other information. All information is hosted
locally; no internet access is required. [#localhelp]_


================
Screen Flowchart
================
The flow chart in :numref:`uml-screen-flowchart` visually shows how the screens
and menus are connected.

..  _uml-screen-flowchart:
..  uml::
    :caption: Connections between Tic Tac Toe's menus and screens.
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
    main_menu --> Help : Help

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
..  [#localhelp] The :ref:`ref-objective-free-of-charge` objective mentions not
        tracking players. Websites often contain trackers, advertisements, and
        other items that violate this objective.
