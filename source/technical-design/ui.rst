##############################
UI Widgets, Layout, and Styles
##############################

..  TODO: talk about the user interface widgets layout and styles and how
    there are supporting code to help with this
    * Sections
      * Intro / what things Amethyst provides and what it is lacking
        * Our system provides a single interface
        * Is specific for our application
      * Low level tools
        * Creates the Amethyst transforms and widgets using the provided styles


In addition to showing the game board, FossXO's :doc:`../gui` allows players to
select different game modes, configure options, and view speed run best times.
Amethyst provides a UI module, but it is intended to be used as building blocks
for a game UI instead of being used directly.

Therefore, FossXO provides a ``ui`` module that provides a high level interface
around the low level Amethyst functionality. This section describes how high
level UI widgets are constructed from the Amethyst building blocks, including
how the UI is styled, laid out, and incorporated into the rest of the game.

====================
Amethyst UI Overview
====================
The `amethyst_ui <https://docs.amethyst.rs/master/amethyst_ui/index.html>`_
module provides the building blocks for creating game UIs. It actually contains
three separate ways to create a UI.

1.  The UI can be constructed directly using ``UiTransform``, ``UiText``,
    ``UiImage``, and ``Interactable`` components. [#additionalcomponents]_
    All fields of each component structure must be provided during creation.
    Also, this is the method described in the Amethyst book.
#.  The UI can be loaded from a ``.ron`` file using the ``UiCreator``. The entity
    that defines the root of the UI is provided. Additionally, the ``UiFinder`` is
    used to locate child elements. The down side of this approach is creating
    the ``.ron`` files gets tedious and there is no style sheet support making
    changes difficult. The Amethyst repository contains several examples of this
    method. [#weirdbug]_
#.  The ``UiButtonBuilder`` and ``UiLabelBuilder`` builders can be used to help
    build buttons and labels. The builders use default values for any missing
    fields.

Based on initial experimentation and the Amethyst documentation, building
widgets directly from Amethyst components seems  like the best method to base
the higher level functionality around. This ensures we have visibility into the
exact set of entities and components being created. Additionally, our high level
API hides the verbosity of creating widgets using this method.

==============
High Level API
==============
FossXO's ``ui`` module provides a high level API to construct game menus and the
in game controls. [#apiusecase]_ The ``Menu`` structure holds the entities for
the game :ref:`ref_ui-menus` and provides UI event handling logic.
The ``MenuBuilder`` allows users to easily create a new menu. These types are
shown in :numref:`uml-ui-menu-types`,

..  _uml-ui-menu-types:
..  uml::
    :caption: Menu and menu builder types.

    !include rust_types.uml
    hide empty members

    struct(Menu) {
        - ui_entities
        - click_event_dispatcher
        - value_changed_event_dispatcher
        + handle_ui_event(ui_event)
        + delete(world)
    }

    struct(MenuBuilder) {
        + new()
        + build(world) -> Menu
        + set_title(text)
        + set_close_button(text, on_close)
        + with_paragraph(text, height)
        + with_button(text, on_press)
        + with_link_button(text, on_press)
        + with_separator()
        + with_player_selector(initial_player, on_changed(player))
        + with_text_box(label, initial_text, on_changed(text))
        + with_custom(entities, height)
    }

The ``GameControls`` structure holds the controls shown during an in progress
game. This includes the hamburger menu button, status text, and next game button.
The ``GameControlsBuilder`` constructs new ``GameControls`` instances.
:numref:`uml-ui-game-controls-types` shows these types.

..  _uml-ui-game-controls-types:
..  uml::
    :caption: Game controls and game controls builder types.

    !include rust_types.uml
    hide empty members

    struct(GameControls) {
        - ui_entities
        - click_event_dispatcher
        + handle_ui_event(ui_event)
        + delete(world)
        + show_game_over_button(button_text)
        + hide_game_over_button()
        + next_speed_run_game_started(final_game_split)
    }

     struct(GameControlsBuilder) {
        - ui_entities
        - click_event_dispatcher
        + new()
        + build(world) -> GameControls
        + set_show_menu_handler(on_press)
        + set_game_over_button_handler(on_press)
        + with_status_text(text)
        + show_speed_run_time()
    }

The builders hide the details of constructing widgets with Amethyst from the
rest of the game. They also ensure the widgets are constructed with a consistent
style and layout as discussed in the :ref:`ref-ui-styling` section.

The builders ensure the necessary components are created so the game's
:doc:`systems` can take care of automatically updating the UI. Therefore, once
constructed there are not many *update* type methods. For example, the game's
status text is automatically updated by the game state display system, thus
there is no need to have a status text update method in ``GameControls``.

Some additional items of interest are:

*   Builder's ``with_*`` methods add new elements to UI. The order
    in which the  ``with_*`` methods are called determines the order the
    elements appear in the UI.
*   Builder's ``set_*`` methods add or overwrite a specific UI element. For
    example, menus have at most one title element that is provided via the
    builder's ``set_title()`` method.
*   Calling the builder's  ``build()`` method takes care of fetching the style
    resource from the world, creating all UI and support entities, and creating
    event dispatchers so the provided callbacks are invoked at the correct times.
*   Builders can be reused. This is allows a state to specify the UI once then
    quickly recreate it when ``on_start()`` is called.
*   The types are specific for FossXO. For example instead of providing a
    generic toggle switch, the menu builder provides the
    ``with_player_selector()`` method to create the :ref:`ref-ui-single-player`
    menu :guilabel:`Play as` selector. This allows us to focus on creating the
    controls needed for the game without having to handle potentially many
    different use cases of generic controls.

The ``EventDispatcher`` structure, shown in :numref:`uml-ui-event-dispatcher`,
maps UI events to callbacks registered during the building process. This makes
it easy for other code to react to the UI events without long ``if`` / ``else if``
chains.

..  _uml-ui-event-dispatcher:
..  uml::
    :caption: Event dispatcher struct.

    !include rust_types.uml
    hide empty members

    struct(EventDispatcher) {
        - handlers: Map<entity, FnMut>
        + add_handler(entity, callback)
        + dispatch(entity)
    }

The necessary event dispatchers are created during the UI build phase and are
manged by the corresponding menu or game controls types.

.. _ref-ui-styling:

=======
Styling
=======
An important part of any user interface is to have a consistent style throughout.
FossXO achieves this by specifying common UI widget properties in a style
resource as shown in :numref:`uml-ui-style-resource`.

..  _uml-ui-style-resource:
..  uml::
    :caption: UI style resources. Additional style structures are added as needed.

    !include rust_types.uml
    hide empty members

    struct(UiStyle) {
        + menu
        + title
        + button
        + hamburger_button
        + game_status
    }

    struct(MenuStyle) {
        background_image
    }

    struct(ButtonStyle) {
        + text_style
        + width
        + height
        + margin
        + border_thickness
        + border_color
        + color
        + hover_color
        + press_color
    }

    struct(TextStyle) {
        + font
        + font_size
        + color
    }

    struct(HamburgerButtonStyle) {
        + icon
        + size
    }

The style resource holds the common properties to all the UI widgets. When the
widgets are being constructed, the UI style is fetched from the world and its
properties are used instead of hard coding values for each individual UI widget
as done in ``.ron`` files. For example, if the UI designer wishes to use a
different font, every widget gets updated.

The ``ui`` module provides a ``load_style()`` function that loads assets
required by the style such as fonts, icons, and background images. This ensures
these resources are available when the game board or menus are displayed.


.. index:: projection matrix

======
Layout
======
In addition to having consistent style, it is important to have consistent and
predictable locations of UI widgets. Requiring the UI designer to manually
specify coordinates to place widgets is both tedious and error prone. FossXO's
``ui`` module automatically determines where UI widgets should be placed. This
feature is known as automatic layout.

The Amethyst ``UiTransform`` component controls where the UI widget is drawn.
The position is specified using :ref:`ref-world-coordinates` with x-right and y-up.
The Z value controls the draw order with widgets with a higher Z order drawn
over those with a lower Z order. Also, the UI uses its own projection matrix,
thus its scale is different than used for the environments.

The origin of each component is selectable via the ``Anchor`` enum, shown in
:numref:`fig-ui-anchor-points`.

..  _fig-ui-anchor-points:
..  figure:: ../img/ui-anchor-points.*

    The anchor point sets the origin of the widget.







.. TODO: Layout?
..  TODO:
      * Layout / style overview
        * Goal: want consistency and the ability to eaisly change things.
        * Uses world coordinates (but can be at a different scale than the environments)
      * Show graphic of border thickness, margin, how titles live at the top etc.
      * describe the with_seperator method.
      * Buttons and main content is centered?



..  rubric:: Footnotes

..  [#additionalcomponents] There are additional components that are useful such
        as ``Selectable``. See the ``amethyst_ui`` documentation for additional
        components.
..  [#weirdbug] A weird bug was encountered where creating buttons
        using the ``UiLabelBuilder`` would cause buttons loaded from via the
        ``UiCreator`` to render in weird places and not be deleted when the root
        element was deleted.
..  [#apiusecase] FossXO's UI APIs are designed specifically around FossXO's
        interface requirements. They are no intended to construct general
        purpose user interfaces.
