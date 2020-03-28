################
Technical Design
################
The technical design of FoxXO is described in this chapter.

..  Note::
    The Technical Design chapter is intentionally incomplete in this version
    of the game design document. This chapter is pending completion of the
    throwaway prototype so the lessons learned during the prototyping phase
    can help inform the various design decisions.


===================
Throwaway Prototype
===================
The throwaway prototype fulfills the
:ref:`ref-objective-build-risk-reduction-prototype` objective. The development
team is new to the Rust game development ecosystem; the prototype allows us to
explore various techniques and come up with a design that fulfills the game
requirements listed in this document.

Technical aspects that are explored in the prototyping phase are:

*   Buttons, menus, and other GUI components as described in the :doc:`../gui`
    chapter.
*   User input from a mouse and keyboard. Includes determining the location of
    mouse clicks.
*   Camera, scene, and window management. E.g. looking at draw order and window
    resize behavior.
*   Drawing bitmap textures. Many environments make use of textures for their
    backgrounds.
*   Drawing marks and the gird for environments like the
    :ref:`ref-environment-blueprint` or :ref:`ref-environment-chalkboard`.
    Perhaps these have lines that could be generated with vector type graphics
    or bitmaps that follow paths?
*   Animations or sprints. Includes ability to adjust animations speed. Many
    environments animate drawing of the marks or a line through the winning marks.
*   Sound FX and music. Includes cross fading between tracks and knowing the
    length sound FX.
*   Lighting, blurring, and other special FX. For example, the
    :ref:`ref-environment-neon-lights` environment makes heavy use of lighting.
    Investigate using shaders to power these effects.
*   Particle systems. They might make a nice touch to many environments such as
    sparks when the :ref:`ref-environment-neon-lights` turn on or showing chalk
    dust from the :ref:`ref-environment-chalkboard`.
*   Ability to save and load structured data. This is needed for the user
    options and speedrun best times.
*   Internalization support.
*   Run the prototype on Windows, Mac, and Linux to address any platform
    specific issues.

As the name suggests, the prototype is discarded once the team has explored the
technical aspects in question. The prototype is not published to crates.io
and platform specific packages are not created for the prototype. Instead, the
lessons learned are documented in this chapter so a comprehensive production
application can be built.


..  TODO: Topics to describe in this chapter include:
    * Engine Overview?
    * File formats?
      * How are options saved and restored?
      * Speedrun best times stored in a SQLite database. Include the SQL schema.
      * What happens if the file(s) cannot be loaded or created?
    * How we are going to meet the licence compliance
      * Create YAML file that lists path to each asset, its license (CC-SA, etc),
        author, and URL(if available).
      * A tool or Rust integration test checks to ensure each asset has an entry
        in the file and the license is acceptable.
      * Part of the credits can be built from information in this file.
      * Create a "credits" section in the help pages that credit assets per
        environment.
      * Use `cargo metadata` to get all of the dependencies of the game. This
        can be used to create a bill of materials.
    * Development Aids
      - Tool that generates code needed for an environment
        - The generated environment should be fully playable so developers can
          test out the new code right away before they start making modifications.
      - Command line options
        - Option to launch into as specific environment.
      - Open to show the grid for centering purposes.
      - Can support simple environments via configuration file. E.g. point to
        background image, marks images, sound, and perhaps mark animation spec.
        More advanced environments will likely require editing code.
        This would allow developers to quickly add simple environments and
        gamers an easy way to mod the app without needing to compile code.
    * Testability
      - Use the logging system. Perform a test run where one or more complete
        games are played on every entrainment. Any warning or error level logs
        cause the test to fail.
      - be proactive in checking for problems. E.g. can all of the resources
        be located, and do other up front checking during the loading process.
    * Packaging
      - Windows Inno setup / Linux app package thing / Mac OS
      - Talk about branding and such
      - What about package signing? How do we get and manage our certificates?
