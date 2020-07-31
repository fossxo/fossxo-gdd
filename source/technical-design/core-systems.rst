############
Core Systems
############

..  TODO: What is a system?
    How does the engine provide systems, e.g. list traits
    Note that even though systems are implemented as structs, these should not
    store data! instead use private resources.
    List the core systems, their responablilites, etc.
    Note that other systems can be added as needed by environments, e.g. particle
    systems or such.


..  _uml-player-event-enum:
..  uml::
    :caption: sadfsadf

    !include rust_types.uml
    hide empty members

    enum(PlayerEvent) {
        RequestMove(Player, Position)
    }

    enum(Player) {
        PlayerX
        PlayerO
    }
