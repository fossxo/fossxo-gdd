#################
Development Tools
#################
This section describes the tools used to help with the development of the game,
and to ensure future maintainability.


..  TODO:
    command line optoins
    Logging levels

=================
Debug Environment
=================
The debug environment shows the canonical location of the grid, marks, and hit
boxes. This can can optionally be overlaid on the current environment allowing
developers to ensure the positioning of their entities is correct. [#firstenv]_

================================
Building and Packaging Workflows
================================
There are several step to building and packing the game. This includes, but is
not limited to compiling the application, running tests, rendering the user
manual, and running the packaging process. Additionally, the details of some of
these steps are different depending on current platform.

`cargo-make <https://crates.io/crates/cargo-make>`_ is a tool that allows build
steps and workflow to be managed. Workflows can include:

*   Preform a user build from source. This can include building the application
    in release mode and launching it when finished. Items such as running tests
    are not needed.
*   Prepare the system for development. E.g. automatically acquire build
    dependencies.
*   Do a development build. This includes running the lint checks, formatting
    checks, and unit tests.
*   Run the full test suite, including slow tests.
*   Package the game for the current platform.


======================
Continuous Integration
======================
A continuous integration system is used to build and test every commit
allowing potential problems to be found as soon as possible. This allows
developers to work right on the ``development`` branch and have confidence their
changes are not breaking existing functionality.


========================
Automated License Checks
========================
Automated tools are used to quickly and accurately check the
:ref:`ref-distribution-license-compliance`.
`cargo-deny <https://crates.io/crates/cargo-deny>` is an existing tool for
checking library licenses. A similar approach using information in the
:ref:`ref-asset-license-info-files` is taken for the third party assets.

These tools are part of the development, test, and continuous integration
workflows.


=======
Logging
=======
Logging is used to help developers and users troubleshoot potential issues with
the game.

The available logging levels are:

error
    Used when there is a problem executing part of the application. One such
    example is being unable to load an asset file.

warn
    Warns of an unexpected event in the application.

info
    Provides information about the system the application is running on and the
    games general flow. Examples include the application's version and
    transitions of :doc:`game-states`.

debug
    Used to provide context when debugging potential issues. Examples include
    noting when events are processed, new environments are loaded, or when
    players switch turns.

trace
    Not used.

The log file of the current game session is stored in the user's data directory.
The file is overwritten each time the game is launched. This ensures the space
taken up by logging is not too large yet ensures logging information is
available in the event the game crashes.

The default log level is **info**.


====================
Command Line Options
====================
The game provides command line options allowing developers to launch the game
in different configurations without having to recompile.

..  option:: --debug

    Enables development aids including the debug environment, FPS counter, and
    any other utilities that might be useful for debugging.

..  option:: --environment <environment>

    Forces the game to use a specific environment instead of selecting them at
    random. This is useful when creating new environments.



..  rubric:: Footnotes

..  [#firstenv] The debug environment should be created early in the development
        process as it allows the game to be played without needing additional
        environments.
