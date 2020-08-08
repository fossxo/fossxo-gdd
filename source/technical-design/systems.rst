#######
Systems
#######

Systems contain small pieces of the game's logic that is applied to collections
of components or resources. The systems can be grouped be grouped into bundles
that provide a specific game feature.

This section describes how systems are constructed and provides details about
core systems used by the game.


============
System Trait
============
In Amethyst systems implement the `System trait <https://docs.amethyst.rs/stable/specs/trait.System.html>`__.
A summary of the System trait is shown in :numref:`uml-system-trait`.

..  _uml-system-trait:
..  uml::
    :caption: Notable methods provided by the System trait.

    !include rust_types.uml
    hide empty members

    trait(System) {
        +SystemData: type
        +run(SystemData)
    }

The ``SystemData`` field specifies what types of components and resources the
system operates on. The ``run()`` method is provided the specified system data
every time it is called. This is typically once per game loop.


============================
System Design Considerations
============================
The list below provides some items to consider when designing systems.

*   Systems contain small pieces of functionality. For example in a Pong type
    game, one system would be responsible for moving the ball and a second
    system for moving the paddles.
*   The ``run()`` method often uses database like queries when accessing
    components using the ``join()`` method. For example, a Pong move ball system
    would join the ``Ball`` and ``Transform`` components.
*   Systems should not assume the number of components they are operating on.
    For example, the Pong move ball system should not assume there is exactly
    one ball. This ensures new gameplay modes can be easily added in the future.
*   Systems should be designed with re-usability in mind. For example, if making
    a system to move spark particles, consider making a generic particle system
    that can be used for other particle types.
*   Systems should not store any data in as a local field.

..  note::
    Even though systems are implemented as structures, they should not store any
    state in as a local fields. If a system needs private data, store the data
    in a resource object that has private fields.  [#amethystguide]_ In fact,
    the next major version of Amethyst uses loose functions for systems and the
    System trait is removed.


============
Core Systems
============
There are several notable systems the game uses to provide the game's core
functionality. This includes getting player input and managing AI opponents.
Additional systems for environment specific features are added as needed.

-------------
Player System
-------------
The player system is responsible for translating mouse clicks and button
presses into player events that indicate where the player would like to move.

The pseudocode in :numref:`code-player-system-pseudocode` describes the player
system logic.

..  _code-player-system-pseudocode:
..  code-block:: text
    :caption: Player system pseudocode.

    For each non-AI player:
        Get the any active button presses from the input bindings.
        For keyboard buttons, extract the direct mappings to the board position.
        For mouse buttons, translate the coordinates to the board position.
        Send the request move player event with the indicated position.

The player system allows players to request moves even when it is not their turn ---
it delegates filtering invalid moves to other systems. Checking the keyboard
bindings takes prescience over the mouse.

---------
AI System
---------
The AI system generates player events for the AI opponents.

:numref:`code-ai-system-pseudocode` shows the pseudocode that describes the AI
system logic.

..  _code-ai-system-pseudocode:
..  code-block:: text
    :caption: AI system pseudocode.

    For each AI player:
        Check to see if is the player's turn, if not skip the player.
        Check the AI's move delay to see if sufficient time has elapsed since
            the last game move.
        Get the position the AI wishes to mark using it's opponent field.
        Send the request move player event with the indicated position.

To prevent burning CPU cycles evaluating positions that will not be used the
AI system skips players if it is not the player's turn.

-------------------
Environments System
-------------------
The environments system is responsible for managing the game's various
environments. This includes telling environments when marks are placed and when
to transition to a new environment.

The environments system receives events from other systems or states shown in
:numref:`uml-environment-data-enum`.

..  _uml-environment-data-enum:
..  uml::
    :caption: Environment related events.

    !include rust_types.uml
    hide empty members

    enum(EnvironmentEvent) {
        Next
        Destroy
        PlaceMark(Position, Player)
        ShowGameOver(OutcomeAffinity)
    }

    enum(OutcomeAffinity) {
        Win
        Loss
        Neutral
    }

The environment events do the following:

Next
    Shows the next environment. All entities belonging to the current
    environment are deleted, the next environment is selected using a random
    shuffle algorithm, then its entities are create from the current game state.
Destroy
    Delete all entities from the current environment. Useful when switching to
    the game menu.
PlaceMark
    Spawns a new mark in the environment at the indicated position.
ShowGameOver
    Indicates the game as been completed. The environment system gets the
    winning positions from the game resource. The outcome affinity is useful for
    single player games allowing environments to react to the player winning or
    losing. Neutral is useful for multiplayer games.


========================
Builtin Amethyst Systems
========================
Amethyst provides several system bundles that are used by the game:

TransformBundle
    Handles updating transform component's position matrix.
InputBundle
    Provides access to OS input events and is required for the UI systems.
AudioBundle
    Provides basic audio playing support.
UiBundle
    Provides support for rendering user interfaces and processing UI input events.
RenderingBundle
    Provides the game's rendering support.

See the Amethyst documentation for details on each of these bundles and the
systems they provide.


..  rubric:: Footnotes

..  [#amethystguide] Readers might find this unofficial
    `Amethyst Architectural Guidelines <https://github.com/bonsairobo/amethyst-architecture-guidelines>`_
    useful, especially when designing game states, systems, components, and resources.
