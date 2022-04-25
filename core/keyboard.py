#!/usr/bin/env python3

# Valentin Lobstein 2022
# Default Project : https://github.com/EntySec/Ghost

import sys
import tty
import termios

from core.ghost import ghost

class keyboard:
    def __init__(self):
        self.ghost = ghost()

    def get_char(self):
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            return sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)

    def send_char(self, char):
        self.ghost.send_command("shell", "input text " + char, False, False)