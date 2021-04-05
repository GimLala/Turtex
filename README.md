# Turtex

This is an extension for the built-in turtle module. It provides functions for ease of development.

## Installation

Run the following to install:

```python
pip install turtex
```

## Usage

### Different Functions

1. draw\_poly
2. draw\_line
3. draw\_x

#### draw\_poly(number\_of\_sides, length, turtle\_obj = turtle.Turtle())

Draws regular polygons (shapes) from the current position which will become the bottom left / top right corner of the shape (It depends on the orientation of the turtle).

|        Arguments         |                                                                    Description                                                                   |
| :-----------------------------:| :----------------------------------------------------------------------------------------------------------------------------------- |
| number\_of\_sides | An integer indicating number of sides of the polygon to be drawn.                                     |
|            length             | An integer indicating the length of each side in pixels.                                                           |
|         turtle\_obj         | A turtle object to draw with. The default value is the default turtle in the turtle module. |

##### Implementation

```python
import turtex

# Configure the turtle to draw different coloured lines and of different thickness.

t = turtex.Turtle()
t.pensize(5)
t.color("black")

# The following code draws a pentagon (shape with 5 sides) with each side of length 15 using t as turtle_obj.

turtex.draw_poly(5, 15, t)

```

#### draw\_line(start\_pos, length, direction\_in\_angle, turtle\_obj = turtle.Turtle())

Draws a line from a given point. Turtle object remains at the end of the line after drawing it.

|         Arguments         |                                                                                      Description                                                                                      |
| :------------------------------:| :------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|         start\_pos          | A list/tuple indicating the starting position of the line.                                                                                                |
|             length              | An integer or float indicating the length of the line in pixels.                                                                                      |
| direction\_in\_angle | An integer or float indicating the direction of the line in degrees. Follow table below for general directions. |
|          turtle\_obj          | A turtle object to draw with. The default value is the default turtle in the turtle module.                                     |

| Standard Mode | Logo Mode |
| :----------------------: | :----------------: |
|        0 - East        |   0 - North    |
|      90 - North     |   90 - East    |
|     180 - West     | 180 - South |
|    270 - South     | 270 - West  |

##### Implementation

```python
import turtex

# Configure the turtle to draw different coloured line and of different thickness.

t = turtex.Turtle()
t.pensize(5)
t.color("black")

# The following code produces a line from (0, 0) of 50 length at 90 degrees(North) using t as turtle_obj.

turtex.draw_line((0, 0), 50, 90, t)

```

#### draw\_x(start\_pos, length, line\_colour\_top\_left, line\_colour\_top\_right, line\_colour\_bottom\_left, line\_colour\_bottom\_right, turtle\_obj = turtle.Turtle())

Draws an 'x' shape.

|                Arguments                |                                                                                       Description                                                                                        |
| :------------------------------------------:| :--------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                start\_pos                 | A list/tuple indicating the starting position of the 'x'. This is the center of the 'x'.                                                    |
|                    length                     | An integer or float indicating the length of each line in pixels.                                                                                     |
|     line\_colour\_top\_left      | A list/tuple of rgb values if the colormode is 255 else a string indicating the colour of the top left line.            |
|    line\_colour\_top\_right     | A list/tuple of rgb values if the colormode is 255 else a string indicating the colour of the top right line.         |
|  line\_colour\_bottom\_left  | A list/tuple of rgb values if the colormode is 255 else a string indicating the colour of the bottom left line.    |
| line\_colour\_bottom\_right | A list/tuple of rgb values if the colormode is 255 else a string indicating the colour of the bottom right line. |
|                 turtle\_obj                | A turtle object to draw with. The default value is the default turtle in the turtle module.                                       |

##### Implementation

```python
import turtex

# Configure the turtle to draw lines of different thickness.

t = turtex.Turtle()
t.pensize(5)

# The following code produces a line from (0, 0) of 50 length with
# colors red, orange, yellow, green for the top_left, top_right, bottom_left,
# bottom_right lines respectively using t as turtle_obj.

turtex.draw_x((0, 0), 50, "red", "orange", "yellow", "green", t)

# Changing colormode to enter colors in rgb values.

turtex.colormode(255)
turtex.draw_x((0, 0), 50, (255, 0, 0), (255, 127, 0), (255, 255, 0), (0, 255, 0), t)

```
