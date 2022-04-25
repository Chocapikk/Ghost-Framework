#!/usr/bin/env python3

# Valentin Lobstein 2022
# Default Project : https://github.com/EntySec/Ghost

from core.badges import badges
from core.ghost import ghost

class GhostModule:
    def __init__(self):
        self.badges = badges()
        self.ghost = ghost()

        self.name = "netstat"
        self.description = "Get device network information."
        self.usage = "Usage: netstat"
        self.type = "settings"
        self.args = 1

    def run(self, cmd_data):
        print(self.badges.G + "Getting network information...")
        output = self.ghost.send_command("shell", "netstat")
        print(output)