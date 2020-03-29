..  only:: builder_html and (not singlehtml)

    ##########################
    FoxXO Game Design Document
    ##########################

    Welcome to FoxXO game design document. FoxXO is a free and open example of
    tic-tac-toe created using the Rust programming language. This document
    describes in detail the design considerations of the game.

    The FoxXO game design document is also available in these other formats:

    * |pdf_download|
    * `Single HTML page <singlepage.html>`__

    ==================
    Overview Documents
    ==================
    These short overview documents introduce the FoxXO game and provide the
    scope of the project.

    * `Handout <foxxo-overview-handout.pdf>`__ - start here
    * `Slides <foxxo-overview-slides.pdf>`__ - a short presentation about the game

    ================
    Useful Resources
    ================
    Below are links to resources developers working on the game might find useful.

    * `OpenGameArt.org <https://opengameart.org/>`_

    ..  Place a list of frequently used external resources here so developers
        can quickly find what they need.
        Note: the list below might be worth adding.
        - https://itch.io/game-assets
        - https://gist.github.com/EndangeredMassa/6b177f36b08a5b0798cf
        - Piston documentation
        - Rust documentation
        - open TTT docs

    =================
    Table of Contents
    =================


..  Include top level heading for the single page design document.
..  only:: singlehtml

    ##########################
    FoxXO Game Design Document
    ##########################


..  toctree::
    :maxdepth: 2
    :numbered:

    introduction
    gameplay
    gui
    environments
    misc/index
    technical-design/index
    glossary
    references

..  only:: builder_html and (not singlehtml)

    Also See:

    * :ref:`genindex`
    * :ref:`search`
