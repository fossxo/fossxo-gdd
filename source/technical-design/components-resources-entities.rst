###################################
Components, Resources, and Entities
###################################
The game's data is organized as components, resources, and entities. An entity
represents a single object in the game. A component represents one aspect of an
entity and store the data related to that aspect. Entities do not store any
actual data but instead are associated with one or more components.

For example, a Pong type game might have a ball entity that is composed of a
position component, sprint component and a ball component.

Resources store global data that is not specific to any one entity. For example,
the score in a pong game is global to the entire game.

This section describes the notable components, resources, entities, and
supporting types used in the game. Additional components, resources, and
entities are created for environment specific features as needed.


============
Environments
============

..  TODO:
    * Env(ironment) Trait
      * setup (base game state / board)
      * destroy
      * place_mark (mark, position)
      * game_over (winning_positions)
    * Environment Resource / Collection / Controller
      * Debug Environment
      * Current active environment
      * Get next random environment
      * Place mark
      * Game over
      * Start next game
    * Grid component?
      * Need a way to convert between positions and corrdinates

A major feature of FoxXO is its many environments. Environments are responsible
for managing required assets and spawning / destroying entities as the game
progresses. This is similar responsibility as *maps* in other games.

Each environment implements the Environment trait shown in
:numref:`uml-environment-trait`.

..  _uml-environment-trait:
..  uml::
    :caption: Environment trait.

    !include rust_types.uml
    hide empty members

    trait(Environment) {
        +name()
        +load_assets()
        +initialize(current_board)
        +destroy()
        +spawn_mark(player, position)
        +spawn_game_over(winning_positions, outcome_affinity)
    }


..  TODO: describe each method in detail

The Environments resource is responsible for holding all of the environments.

..  _uml-environment-collection-struct:
..  uml::
    :caption: Environment collection structure.

    !include rust_types.uml
    hide empty members

    struct(Environments) {
        +environments: vec<Environment>
        +dbg_environment
        +active_environment_idx
    }



==================
Notable Components
==================


..  _uml-core-components:
..  uml::
    :caption: Public types provided by the ``environment`` module.

    !include rust_types.uml
    hide empty members

    enum(Player) {
        + X
        + O
    }

    struct(Ai) {
        + ai_opponent
        + move_delay
    }

    struct(Mark) {
        + owner: Player
        + position: Board::Position
    }


Player
    The Player component stores if the player is playing as X or as O.
Mark
    The Mark component indicates the owner of a given position on the board.
Ai
    The AI component provides the underlying AI opponent to use when selecting
    positions. Additionally, a delay can be specified to prevent the AI from
    instantly selecting a position.


============================
Provided Amethyst Components
============================
Amethyst provides several components that are used when building game entities:

SpriteRender
    Provides information for rendering a sprite.
Transform
    Stores local position, rotation, and scale.

See the Amethyst documentation for details about these components and their
fields.


=================
Notable Resources
=================

..  _uml-core-resources:
..  uml::
    :caption: asdfsadfsadf.

    !include rust_types.uml
    hide empty members

    struct(Game) {
        + game: ttt::Game
        + last_move_time
        + isPlayersMove(player) -> bool
    }

The game resource provides access to the underlying tic-tac-toe game logic and
the last time a move was done on the game. Helper methods are provided to make
tasks such as seeing if it is a given player's turn.

