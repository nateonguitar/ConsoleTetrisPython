from game.matrix import Matrix
import os


class ConsolePrinter():
    
    ansi_start = "\033["
    ansi_end = "\033[0m"

    def __init__(self):

        self.previous_screen = self.get_empty_screen()
        self.terminal_size = os.get_terminal_size()


    def get_empty_screen(self):
        self.terminal_size = os.get_terminal_size()
        screen = Matrix.empty_sized(
            rows=self.terminal_size.lines,
            columns=self.terminal_size.columns,
            value=' '
        )
        return screen


    def clear_screen(self):
        terminal_size = os.get_terminal_size()
        # print a space on every character of the terminal
        for line in range(0, terminal_size.lines):
            line_str = ''
            for column in range(0, terminal_size.columns):
                line_str += ' '
            print(f"{self.ansi_start}{column+1};0H{line_str}{self.ansi_end}")


    # TODO: colors not working yet
    def print_character_at(self, x: int, y: int, char: str, color: str = 'white', end: str = ''):
        position = f"{y+1};{x+1}H"
        print(f"{self.ansi_start}{position}{char}{self.ansi_end}", end=end)

    
    def draw_screen(self, screen: Matrix):
        _terminal_size = os.get_terminal_size()
        if self.terminal_size.columns != _terminal_size.columns or self.terminal_size.lines != _terminal_size.lines:
            self.terminal_size = _terminal_size
            self.previous_screen = self.get_empty_screen()
        # Print over the entire screen with what has been stored
        # in our screen representation.
        # Only prints over characters that have changed since the last print.
        lines = min(len(screen), self.terminal_size.lines)
        columns = min(len(screen[0]), self.terminal_size.columns)
        for line in range(0, lines):
            for column in range(0, columns):
                prev_char = self.previous_screen[line][column]
                new_char = screen[line][column]
                if new_char != prev_char:
                    self.print_character_at(column, line, new_char)

        # So we don't leave the cursor in an annoying place between draws
        # we will draw the final character at the bottom right corner.
        # Also, changes don't seem to reflect on the screen until "enter"
        # is pressed, this adds "end='\n'" which accomplishes that.
        # If "end=''" changes don't draw on the screen any more."
        bottom_right_char = screen[lines-1][columns-1]
        self.print_character_at(columns-1, lines-2, bottom_right_char, end='\n')

        # Store the current state of the screen so we can
        # use it again next cycle
        self.previous_screen = screen
