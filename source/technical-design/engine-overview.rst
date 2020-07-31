###############
Engine Overview
###############

FoxXO is developed using the Rust programming language per the
:ref:`ref-objective-create-ttt-game-with-rust` objective. To help reduce the
development effort, FoxXO makes extensive use of existing Rust libraries.
:numref:`uml-notable-foxxo-libraries` shows notable libraries used by FoxXO.

..  _uml-notable-foxxo-libraries:
..  uml::
    :caption: Notable libraries used by FoxXO.

    [FoxXO] <-- [open_ttt_lib]
    [FoxXO] <-- [amethyst]
    [amethyst] <-- [specs]
    [amethyst] <-- [gfx-rs]
    [gfx-rs] <-- [Vulkan]
    [amethyst] <-- [nalgebra]

FoxXO uses the Amethyst engine and makes use of the
`open_ttt_lib <https://github.com/j-richey/open_ttt_lib>`__ library that
provides tic-tac-toe logic and AI algorithms.

========
Amethyst
========
`Amethyst <https://github.com/amethyst/amethyst>`__ is a data-driven and game
engine written in Rust. Amethyst uses a entity component system (ECS) architecture
where entity represents a single object in the game. Components store data about
one aspect of the object. Systems contain logic that is executed on collections
of components every loop. Amethyst additionally contains support for states,
resources, and events. [#amethystbook]_

In addition to the ECS architecture, Amethyst provides a rendering engine that
supports various backends including Vulkan, a basic UI framework, audio support,
and IO utilities.

FoxXO's makes extensive use of the features provided by Amethyst. Each of these
are described in detail in the following sections.

..  rubric:: Footnotes

..  [#amethystbook] `The Amethyst Engine book <https://book.amethyst.rs/stable/>`__
        contains detailed information about each of these concepts and how they
        are used in the Amethyst engine.
