###############
Engine Overview
###############

FossXO is developed using the Rust programming language per the
:ref:`ref-objective-create-ttt-game-with-rust` objective. To help reduce the
development effort, FossXO makes extensive use of existing Rust libraries.
:numref:`uml-notable-fossxo-libraries` shows notable libraries used by FossXO.

..  _uml-notable-fossxo-libraries:
..  uml::
    :caption: Notable libraries used by FossXO.

    [FossXO] <-- [open_ttt_lib]
    [FossXO] <-- [amethyst]
    [amethyst] <-- [specs]
    [amethyst] <-- [gfx-rs]
    [gfx-rs] <-- [Vulkan]
    [amethyst] <-- [nalgebra]

FossXO uses the Amethyst engine and makes use of the
`open_ttt_lib <https://github.com/j-richey/open_ttt_lib>`__ library that
provides tic-tac-toe logic and AI algorithms.

========
Amethyst
========
`Amethyst <https://github.com/amethyst/amethyst>`__ is a data-driven and game
engine written in Rust. [#otherengines]_ Amethyst uses a entity component system
(ECS) architecture where entity represents a single object in the game.
Components store data about one aspect of the object. Systems contain logic that
is executed on collections of components every loop. Amethyst additionally
contains support for states, resources, and events. [#amethystbook]_ [#amethystguide]_

In addition to the ECS architecture, Amethyst provides a rendering engine that
supports various backends including Vulkan, a basic UI framework, audio support,
and IO utilities.

FossXO's makes extensive use of the features provided by Amethyst. Each of these
are described in detail in the following sections.

..  rubric:: Footnotes

..  [#otherengines] During the prototyping phase two other popular Rust game
        engines were considered:
        `Piston <https://github.com/PistonDevelopers/piston>`__
        and `ggez <https://github.com/ggez/ggez>`__.

        Piston is a large collection of modules that requires the game developer
        to understand each of the modules then pick the ones that are needed.
        Additionally, Piston's documentation was confusing on where to get
        started.

        ggez provides all the tools needed to make simple 2D games and provides
        good documentation along with examples. However, it does not provide
        features that are required for this game such as UIs, entity management,
        events, or state machines. Spending time making these items would mean
        less time spent creating the actual game.

..  [#amethystbook] The Amethyst Engine book contains detailed information about
        each of these concepts and how they are used in the Amethyst engine. [Amethyst-book]_

..  [#amethystguide] Readers might find this unofficial
    `Amethyst Architectural Guidelines <https://github.com/bonsairobo/amethyst-architecture-guidelines>`_
    `(archive) <https://web.archive.org/web/20200807215439/https://github.com/bonsairobo/amethyst-architecture-guidelines>`_
    useful, especially when designing game states, systems, components, and resources.
