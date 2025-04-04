# SmartInputs

The more dynamic ways of asking for the user's inputs and handle the entered values in the real time.

# Installation

`pip install smart-inputs`

# Requirements

- windows-curses

# GitHub link

`https://github.com/farbod-mahdian/smart_inputs`

# Usage

smart_input:

```
from smart_inputs.smart_input import smart_input

fav_color = smart_input('What is your favorite color:', default='Red')
print(fav_color)
```

multiple_choice:

```
from smart_inputs.multiple_choice import multiple_choice, Colors

fav_color = multiple_choice(
    'What is your favorite color:', options=['Blue', 'Red'], fg_color=Colors.GREEN)
print(fav_color)
```
