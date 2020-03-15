################
Technical Design
################

..  TODO: Topics to describe here include:
    * Prototype
      - List of things to demonstrate
        - textures
        - animations / sprites
        - lighting effects or shaders
        - particles
        - user input
        - music / sound FS
          - Can music be cross faded between levels?
        - Buttons / menus / and other GUI components
    * Engine Overview?
    * File formats?
      * How are options saved and restored?
      * Speedrun best times stored in a SQLite database.
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
