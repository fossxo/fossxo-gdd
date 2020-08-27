##################
Coordinate Systems
##################

A critical part of any video game is to show the games graphics on the user's
screen. However, most games does not directly control the contents of individual
pixels. Instead geometry is submitted to the graphics pipeline to be rendered.
The pipeline then determines the final color to write to each screen pixel. The
geometry is described in terms of world coordinates. A projection matrix, e.g.
the game's camera, describes how to transform the points from world coordinates
to screen coordinates.

This section describes these coordinate systems and how they relate. This is of
particular importance when handling mouse input provided by the operating system
as the mouse's screen coordinates need converted to a tic-tac-toe board position
to know where the user would like to place their mark.


==================
Screen Coordinates
==================
Screen coordinates, also known as normalized device coordinates, is how the
operating system thinks of the game's window. The window is a 2D image with the
origin in the top left corner of the window. The y values increase down and the
x values increase to the right as shown in :numref:`fig-screen-coordinates`.

..  _fig-screen-coordinates:
..  figure:: ../img/screen-coordinates.*

    The screen coordinate system with x-right and y-down. The origin is the top
    left of the window.

The game uses the screen point type, shown in :numref:`uml-screen-point`
represent screen coordinates in terms of X and Y position.

..  _uml-screen-point:
..  uml::
    :caption: Representation of a screen point.

    !include rust_types.uml
    hide empty members

    struct(ScreenPoint) {
        + x: f32
        + y: f32
        + from((f32, f32))
        + to_point() -> Point2
    }

When the user clicks on part of the window, the OS reports the mouse position
in terms of screen coordinates. The mouse raycast system converts the position
to world coordinates and a corresponding tic-tac-toe board position.

.. _ref-world-coordinates:

=================
World Coordinates
=================
All of the game's objects described in 3D space using the world coordinates
shown in :numref:`fig-world-coordinates`.

..  _fig-world-coordinates:
..  figure:: ../img/world-coordinates.*

    World coordinate system with x-right, y-up, and z-out. The origin is an
    arbitrary point in the world.

The game's camera contains a projection matrix describes how the 3D scene is
transformed to the 2D pixels. Likewise, the inverse operation mapping screen
pixels to world points can be performed. [#cameratransforms]_

The game uses the nalgebra ``Point3`` type to represent world points in terms of
X, Y, and Z position.


.. _ref-ttt-board-position:

===========================
Tic-tac-toe Board Positions
===========================
The tic-tac-toe game describes marks in terms of their row and column position
as shown in :numref:`fig-board-position`.

..  _fig-board-position:
..  figure:: ../img/board-position.*

    Tic-tac-toe board positions with rows-up, columns-right. The origin is the
    bottom left square.

The open_ttt_lib ``Position`` type is use for board positions.

For a tic-tac-toe game there are several data types that are useful when
describing the board including lines and rectangles.
:numref:`uml-ttt-board-math-helper-types` shows some examples of these types.

..  _uml-ttt-board-math-helper-types:
..  uml::
    :caption: Helper data types for describing the tic-tac-toe board.

    !include rust_types.uml
    hide empty members

    struct(Line) {
        + start: Point3
        + end: Point3
    }

    struct(Square) {
        + center_point() -> Point3
        + size() -> f32
        + top_left() -> Point3
        + top_right() -> Point3
        + bottom_left() -> Point3
        + bottom_right() -> Point3
        + horizontal() -> Line
        + vertical() -> Line
    }

A line can be used to describe the board's grid or the line drawn through
winning positions.

An axis aligned rectangle is useful for describing one of the grid's cells.
Several helper methods provide access to the corners, center point, and lines
going through the center point. :numref:`fig-grid-square-points` visually shows
these points.

..  _fig-grid-square-points:
..  figure:: ../img/grid-square-points.*

    Points of interest in the rectangle structure.

1.  The square's center point.
2.  The bottom left of the square.
3.  The vertical line's starting point is always defined at the bottom of the
    square.
4.  The horizontal line's starting point always defined at the left side of the
    square.


..  rubric:: Footnotes

..  [#cameratransforms] The Amethyst ``Camera::screen_to_world_point()`` and
      ``Camera::world_to_screen()`` functions are useful when converting between
      screen and world positions.

