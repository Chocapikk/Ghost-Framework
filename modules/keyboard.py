#!/usr/bin/env python3

# Valentin Lobstein 2022
# Default Project : https://github.com/EntySec/Ghost

from core.badges import badges
from core.ghost import ghost
from core.keyboard import keyboard

class GhostModule:
    def __init__(self):
        self.badges = badges()
        self.ghost = ghost()
        self.keyboard = keyboard()

        self.name = "keyboard"
        self.description = "Control target keyboard."
        self.usage = "Usage: keyboard"
        self.type = "managing"
        self.args = 1

    def run(self, cmd_data):
        print(self.badges.G + "Connecting to keyboard...")
        print(self.badges.I + "Press Ctrl-C to stop.")
        while True:
            char = self.keyboard.get_char()
            self.keyboard.send_char(char)