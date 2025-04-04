import curses
from curses import window
from enum import Enum
from typing import List, Union


class Colors(Enum):
    BLACK = curses.COLOR_BLACK
    RED = curses.COLOR_RED
    GREEN = curses.COLOR_GREEN
    CYAN = curses.COLOR_CYAN
    BLUE = curses.COLOR_BLUE
    MAGENTA = curses.COLOR_MAGENTA
    YELLOW = curses.COLOR_YELLOW
    WHITE = curses.COLOR_WHITE


class MultipleChoice:
    """
    Contains the logics relating to let the user choose an option from
    a multiple choice prompt.

    Args:
        prompt: the prompt to show in the console.
        options: the options for the prompt.
        fg_color: the color of the texts in the options.
        bg_color: the background color of the options.
        default_option: the default selected option.
    """

    def __init__(
            self, prompt: str, options: List[Union[str, int]], fg_color: Colors = Colors.WHITE,
            bg_color: Colors = Colors.BLACK, default_option: int = 1
    ) -> None:
        self.__prompt = prompt
        self.__options = options
        self.__selected_index = None
        self.__fg_color = fg_color.value
        self.__bg_color = bg_color.value

        options_n = len(self.__options)
        if default_option > options_n:
            raise Exception(
                f'There are {options_n} available options, so {default_option} is not a valid option number.')
        self.__default_option_index = default_option - 1

    def __run(self, stdscr: window) -> None:
        """
        Run the main logic to handle the user inputs.

        Args:
            stdscr: the current screen.
        """
        curses.start_color()
        curses.init_pair(1, self.__fg_color, self.__bg_color)

        stdscr.clear()
        selected = self.__default_option_index

        while True:
            stdscr.clear()
            stdscr.addstr(self.__prompt + "\n")

            for i, option in enumerate(self.__options):
                if i == selected:
                    stdscr.addstr(f"> {option}\n", curses.color_pair(
                        1) | curses.A_BOLD)
                else:
                    stdscr.addstr(f"  {option}\n")

            try:
                key = stdscr.getch()
            except KeyboardInterrupt:
                print("Program terminated by the user.")
                exit(1)

            if key == curses.KEY_UP and selected > 0:
                selected -= 1
            elif key == curses.KEY_DOWN and selected < len(self.__options) - 1:
                selected += 1
            elif key == ord('\n'):
                self.__selected_index = selected
                break

            stdscr.refresh()

    def run(self, return_value: bool = True) -> Union[str, int]:
        """
        Wrapper to run the main logic to handle the user inputs.

        Args:
            return_value: indicates if either the selected option's text or
            the selected option's index should be returned.

        Returns:
            Either returns the selected option's text or the selected option's index.
        """
        curses.wrapper(self.__run)
        return self.__options[self.__selected_index] if return_value else self.__selected_index


def multiple_choice(
    prompt: str, options: List[Union[str, int]], fg_color: Colors = Colors.WHITE,
    bg_color: Colors = Colors.BLACK, default_option: int = 1, return_value: bool = True
) -> Union[str, int]:
    """
    Share a prompt with the user and wait for the user to select an option from the available options.

    Args:
        prompt: the prompt to show in the console.
        options: the options for the prompt.
        fg_color: the color of the texts in the options.
        bg_color: the background color of the options.
        default_option: the default selected option.
        return_value: indicates if either the selected option's text or
        the selected option's index should be returned.

    Returns:
        Either returns the selected option's text or the selected option's index.
    """
    return MultipleChoice(
        prompt=prompt, options=options, fg_color=fg_color,
        bg_color=bg_color, default_option=default_option
    ).run(return_value=return_value)
