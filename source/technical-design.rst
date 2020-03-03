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
    * Development Aids
      - Tool that generates code needed for an environment
        - The generated environment should be fully playable so developers can
          test out the new code right away before they start making modifications.
      - Command line options
        - Option to launch into as specific environment.
      - Open to show the grid for centering purposes.
    * Packaging
      - Windows Inno setup / Linux app package thing / Mac OS
