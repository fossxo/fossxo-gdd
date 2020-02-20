..  only:: builder_html and (not singlehtml)

    ###################################
    Pound of Rust Project Documentation
    ###################################

    Welcome to Pound of Rust Project Documentation. This project results in the
    creation of a Tic Tac Toe game using the Rust programming language.

    ==================
    Overview Documents
    ==================
    These short overview documents introduce the Tic Tac Toe game and provide
    the scope of the project.

    * `Handout <tic-tac-toe-overview-handout.pdf>`__ - start here
    * `Slides <tic-tac-toe-overview-slides.pdf>`__ - a short presentation about the game

    ================
    Useful Resources
    ================

    ..  TODO:
        Place a list of useful resources here so developers can quicky find what they need.
        - https://opengameart.org/
        - https://itch.io/game-assets
        - https://gist.github.com/EndangeredMassa/6b177f36b08a5b0798cf
        - Piston documentation
        - Rust documentation
        - open TTT docs

    ===============
    Design Document
    ===============
    The Tic Tac Toe Design Document describes in detail the design
    considerations of the game.

    .. warning::  The design document is a work in progress.


..  Include top level heading for the single page design document.
..  only:: singlehtml

    ###########################
    Tic Tac Toe Design Document
    ###########################


..  toctree::
    :maxdepth: 2
    :numbered:

    introduction
    overview/index
    gui
    environments
    license-compliance
    technical-design
    glossary
    references


..  only:: builder_html and (not singlehtml)

    The design document is also available in other formats:

    * |pdf_download|
    * `View as single page <singlepage.html>`__

    Also See:

    * :ref:`genindex`
    * :ref:`search`
