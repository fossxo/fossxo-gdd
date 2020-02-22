##################
Project Objectives
##################
Creation of the Tic Tac Toe game described in this document is part of the
Pound of Rust project. This section describes the project's objectives.


=================================
Create Tic Tac Toe Game with Rust
=================================
The main deliverable of this project is the Tic Tac Toe game for Windows, Mac,
and Linux. This project is the follow-up to the Ounce of Rust project [#ounceOfRust]_
that resulted in the creation of a Rust based Tic Tac Toe logic library,
``open_ttt_lib``. [#openTTTlib]_

In addition to creating a fun game, the project provides more hand on experience
using Rust and is a showcase for ``open_ttt_lib``.


=======================================================
Provide Free of Charge and Under an Open Source License
=======================================================
Tic Tac Toe and all future releases of the game are free, open source, and
contain no advertisements or trackers. The game is released under a permissive
open source license and its code is available from a public repository
such as `<https://github.com/>`__.

Many of today's games casual games are released for free, but include
questionable monetization models such as microtransactions, pay-to-win schemes,
advertisements, and personal data harvesters. Tic Tac Toe stands apart from
these games by respecting player's who choose to spend their valuable time
playing the game.


========================
Release by RustConf 2020
========================
Tic Tac Toe's initial release is scheduled to coincide with RustConf 2020
on August 21, 2020. RustConf is the annual Rust developers conference; since
Tic Tac Toe is developed in Rust this makes an excellent time to launch a Rust
based game. [#rustconf]_

To help meet the target release date, the initial release of the game might
contain a subset of the environments described in this document.


================================
Easily Expandable and Modifiable
================================
Playing Tic Tac Toe in a variety of environments is a large part of what sets
this version of Tic Tac Toe apart from others. The game is designed such that
developers can easily add new environments. This allows developers to focus
their time and efforts creating stunning environments. Additionally, this
lowers the barrier of entry for users who are interested in modifying the game.
Finally, this allows quick turnaround of future releases of the game.

Automated tools, guides, checklists, and detailed documentation are some ways
that can help development speed.


==============================
Build Risk Reduction Prototype
==============================
The development team creating Tic Tac Toe is new to the Rust programming language
and the available Rust libraries for game development. To help mitigate this
risk, a throwaway prototype game is created early in the project that explores
various technical aspects.

Using the lessons learned from the prototype also helps the development team
design a code base that is easily expandable and modifiable per the above
objective.


..  rubric:: Footnotes

..  [#ounceOfRust] For details on the Ounce of Rust project see the
        `Ounce of Rust Project Manual <https://j-richey.github.io/project-documentation/ounce-of-rust/>`__
..  [#openTTTlib] ``open_ttt_lib`` is available at https://crates.io/crates/open_ttt_lib
        and source code is hosted at https://github.com/j-richey/open_ttt_lib
..  [#rustconf] For details on RustConf see their website: https://rustconf.com/
