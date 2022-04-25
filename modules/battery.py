#!/usr/bin/env python3

# Valentin Lobstein 2022
# Default Project : https://github.com/EntySec/Ghost

from core.badges import badges
from core.ghost import ghost

class GhostModule:
    def __init__(self):
        self.badges = badges()
        self.ghost = ghost()

        self.name = "battery"
        self.description = "Get device battery information."
        self.usage = "Usage: battery"
        self.type = "settings"
        self.args = 1

    def run(self, cmd_data):
        output = self.ghost.send_command("shell", "dumpsys battery")
        print(self.badges.I + "Device Battery Information:")
        print(output)