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

        self.name = "root"
        self.description = "Check if device is rooted."
        self.usage = "Usage: root"
        self.type = "settings"
        self.args = 1

    def run(self, cmd_data):
        output = self.ghost.send_command("shell", "which su",False)
        if not "su" in output:
            print(self.badges.E + "Target System is not rooted...")
        else: 
            print(self.badges.G + "Target System is rooted !")




