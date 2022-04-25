#!/usr/bin/env python3

# Valentin Lobstein 2022
# Default Project : https://github.com/EntySec/Ghost

import os

from core.badges import badges
from core.ghost import ghost

class GhostModule:
    def __init__(self):
        self.badges = badges()
        self.ghost = ghost()

        self.name = "screen"
        self.description = "Control device screen."
        self.usage = "Usage: screen"
        self.type = "managing"
        self.args = 1

    def run(self, cmd_data):
        print(self.badges.G + "Opening device screen...")
        os.system("scrcpy &> /dev/null")
