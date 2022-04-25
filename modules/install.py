#!/usr/bin/env python3

# Valentin Lobstein 2022
# Default Project : https://github.com/EntySec/Ghost

from core.badges import badges
from core.ghost import ghost

class GhostModule:
    def __init__(self):
        self.badges = badges()
        self.ghost = ghost()

        self.name = "install"
        self.description = "Install an application."
        self.usage = "Usage: install <app_name>"
        self.type = "managing"
        self.args = 2

    def run(self, cmd_data):
        print(self.badges.G + "Installing " + cmd_data.split(" ")[0] + "...")
        output = self.ghost.send_command("install",cmd_data.split(" ")[0])
        print(output)