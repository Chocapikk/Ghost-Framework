#!/usr/bin/env python3

# Valentin Lobstein 2022
# Default Project : https://github.com/EntySec/Ghost

from core.badges import badges
from core.ghost import ghost

class GhostModule:
    def __init__(self):
        self.badges = badges()
        self.ghost = ghost()

        self.name = "activity"
        self.description = "Get device activity information."
        self.usage = "Usage: activity"
        self.type = "settings"
        self.args = 1

    def run(self, cmd_data):
        print(self.badges.G + "Getting activity information...")
        output = self.ghost.send_command("shell", "dumpsys activity")
        print(output)