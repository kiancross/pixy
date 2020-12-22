pixy
====

[![PyPI version](https://badge.fury.io/py/pixy.svg)](https://pypi.org/project/pixy/)
![Continuous Integration](https://github.com/kiancross/pixy/workflows/Continuous%20Integration/badge.svg)
[![codecov](https://codecov.io/gh/kiancross/pixy/branch/master/graph/badge.svg?token=P490PT52VR)](https://codecov.io/gh/kiancross/pixy)

pixy is a Python library for adding colour and style to terminal text.

* [Getting Started](#getting-started)
  * [Installation](#installation)
  * [Usage](#usage)
* [Documentation](#documentation)
* [Examples](#examples)
* [Tests](#tests)
* [License](#license)

Terminal output can be styled using [ANSII escape code][ansii_escape_codes]. pixy provides a simple to use yet comprehensive wrapper, abstracting away the complexities.

pixy supports:
  - 3-bit, 4-bit and 8-bit colour;
  - 24-bit true colour RGB;
  - changing the foreground and background colour;
  - text decorators e.g. blink, underline, bold, italic, strike-through;
  - custom fonts for compliant terminals;
  - custom ANSII codes for development on non-spec-compliant terminals.

[ansii_escape_codes]: https://en.wikipedia.org/wiki/ANSI_escape_codes

Getting Started
---------------

### Installation

pixy can be installed using `pip`.
```
$ python3 -m pip install pixy
```

### Usage

pixy lets you style text straight out of the box.

```python
import pixy

# Print "Hello World" in red.
print(pixy.red("Hello World"))
```

It provides the flexibility to format text as you wish.

```python
import pixy

# Create a string "Hello" with bold text and blue background.
s1 = pixy.pring("Hello", pixy.decorators.bold + pixy.background.blue)

# Concatenate the two strings, giving everything a red background (the
# red background won't be applied to "Hello" because we've already
# given it a blue background!)
print(pixy.pring(s1 + " World. Lorem ipsum dolor...", pixy.background.red))
```

Documentation
-------------
Not all terminals support all ANSII escape codes. Please check the terminal you are testing on supports the features you are using before opening an issue.

### Helpers 
You can create a string of a certain colour using the helper functions below:

  - `pixy.black(text)`
  - `pixy.red(text)`
  - `pixy.green(text)`
  - `pixy.yellow(text)`
  - `pixy.blue(text)`
  - `pixy.magenta(text)`
  - `pixy.cyan(text)`
  - `pixy.white(text)`

#### Example
```python
import pixy

# Print "Hello World" in red.
print(pixy.red("Hello World"))
```

### `pixy.pring(text, style)`
`pixy.pring` allows you to generate a string with any of the styles documented below. You can use more than one style by adding them together.

  - `text` - the text to apply the style to.
  - `style` - the style to apply to the text.

#### Example
```python
import pixy

# Print "Hello World" with green text and white background.
print(pixy.pring(
	"Hello World",
	pixy.foreground.green + pixy.background.white
))
```

### `pixy.foreground`, `pixy.background`
`pixy.foreground` and `pixy.background` contain the variables: `black`,
`red`, `green`, `yellow`, `blue`, `magenta`, `cyan`, `white`. 

Using the `pixy.foreground` variant of the colour will apply the colour
to the foreground and the `pixy.background` variant will apply it to the
background.

These colours are known as the 3-bit colours and almost all terminals support
them. Most terminals also let you make them bright by adding the
`pixy.decorators.bold` style.

#### Example
```python
import pixy

# Print "Hello World" with green text.
print(pixy.pring("Hello World", pixy.foreground.green))
```

### `pixy.decorators`
Decorators let you apply other styles to the text.

| Decorator | Description | Support |
|--|--|--|
| `pixy.decorators.bold` | Bold/bright |
| `pixy.decorators.faint` | Faint/dimmed |
| `pixy.decorators.italic` | Italicised |
| `pixy.decorators.underline` | Underlined |
| `pixy.decorators.slow_blink` | Slow blink (less than 150 per minute) |
| `pixy.decorators.rapid_blink` | Rapid blink (150+ per minute) | Not widely supported |
| `pixy.decorators.invert` | Swap foreground and background colours |
| `pixy.decorators.conceal` | Hide | Not widely supported |
| `pixy.decorators.strike` | Strike-through |
| `pixy.decorators.fraktur` | [Fraktur](https://en.wikipedia.org/wiki/Fraktur) | Rarely supported |
| `pixy.decorators.double_underline` | Double underline |
| `pixy.decorators.framed` | | Not widely supported |
| `pixy.decorators.encircled` |  | Not widely supported |
| `pixy.decorators.overlined` | Overlined |

(Descriptions adapted from [Wikipedia](https://en.wikipedia.org/wiki/ANSI_escape_code#SGR_parameters))

#### Example
```python
import pixy

# "Hello World" underlined.
print(pixy.pring("Hello World", pixy.decorators.underline))
```

### `pixy.ExtendedColour(code, background=False)`
With `pixy.ExtendedColour` you can select from a pre-defined selection of 256
colours.

  - `code` - corresponds to a colour code found
     [here](https://en.wikipedia.org/wiki/ANSI_escape_code#8-bit). 

  - `background` - boolean value indicating if this is a background or
     foreground colour.

#### Example
```python
import pixy

# Print "Hello World" in violet.
print(pixy.pring("Hello World", pixy.ExtendedColour(99)))

# Print "Hello World" with a violet background.
print(pixy.pring("Hello World", pixy.ExtendedColour(99, True)))
```

### `pixy.TrueColour(red, green, blue, background=False)`
With `pixy.TrueColour` you can create an RGB colour.

  - `red` - value between `0` and `255` indicating the intensity of the
    red component.

  - `green` - value between `0` and `255` indicating the intensity of the
    green component.

  - `blue` - value between `0` and `255` indicating the intensity of the
    blue component.

  - `background` - boolean value indicating if this is a background  or
    foreground colour.

#### Example
```python
import pixy

# Print "Hello World" in violet.
print(pixy.pring("Hello World", pixy.TrueColour(238, 130, 238)))

# Print "Hello World" with a violet background.
print(pixy.pring("Hello World", pixy.TrueColour(238, 130, 238, True)))
```

### `pixy.Font(code)`
Allows you to change the font used. Most terminals do not support this.

  - `code` - a number between `0` and `8` corresponding to a font.

#### Example
```python
import pixy

print(pixy.pring("Hello World", pixy.Font(3)))
```

### `pixy.EscapeSequence(...)`
`pixy.EscapeSequence` can be used in instances that you want to defined your own ANSII escape sequence.

`pixy.EscapeSequence` takes a variable number of arguments - each argument should be an ANSII code.

#### Example
```python
import pixy

# Bright blue using ANSII code 94 supported by some terminals
print(pixy.pring("Hello World", pixy.EscapeSequence(94)))
``` 
## Examples

### Blinking Text
```python
import pixy

print(pixy.pring("Hello World", pixy.decorators.slow_blink))
```

### Concatenation
```python
import pixy

# "Hello" in red.
s1 = pixy.pring("Hello", pixy.foreground.red)

# " World" in blue.
s2 = pixy.pring(" World", pixy.foreground.blue)

# Concatenate the strings, add a white background and make
# them bold.
s3 = pixy.pring(s1 + s2, pixy.background.white + pixy.decorators.bold)

print(s3)
```

### Colour shades
```python
import pixy

for i in range(0, 0xFF, 3): 
    colour = pixy.TrueColour(i, 0, 0, background=True)
    print(pixy.pring(" ", colour), end="")

print()

for i in range(0, 0xFF, 3): 
    colour = pixy.TrueColour(0, i, 0, background=True)
    print(pixy.pring(" ", colour), end="")

print()

for i in range(0, 0xFF, 3): 
    colour = pixy.TrueColour(0, 0, i, background=True)
    print(pixy.pring(" ", colour), end="")

print()
```

### Colour gradient
```python
import pixy

def gradient(colour_a, colour_b):
    
    output = []

    for i in range(0, 100, 2): 

        p = i / 100 

        output.append((
            int(colour_a[0] + p * (colour_b[0] - colour_a[0])),
            int(colour_a[1] + p * (colour_b[1] - colour_a[1])),
            int(colour_a[2] + p * (colour_b[2] - colour_a[2]))
        ))

    return output

red_to_green = gradient((255, 0, 0), (0, 255, 0)) 
green_to_blue = gradient((0, 255, 0), (0, 0, 255))
blue_to_red = gradient((0, 0, 255), (255, 0, 0)) 

for colour in red_to_green:
    print(pixy.pring(" ", pixy.TrueColour(*colour, background=True)), end="")

print()

for colour in green_to_blue:
    print(pixy.pring(" ", pixy.TrueColour(*colour, background=True)), end="")

print()

for colour in blue_to_red:
    print(pixy.pring(" ", pixy.TrueColour(*colour, background=True)), end="")

print()
```

Tests
-----

Unit tests are written using the unittest module. They can be run by executing `make test`.

`make style-fix` can be run to fix any code styling issues.

License
-------

pixy is licensed under the [MIT license](https://github.com/kiancross/pixy/blob/master/LICENSE).
