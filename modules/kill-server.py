#!/usr/bin/env python3

# Valentin Lobstein 2022
# Default Project : https://github.com/EntySec/Ghost

from core.badges import badges
from core.ghost import ghost

class GhostModule:
    def __init__(self):
        self.badges = badges()
        self.ghost = ghost()

        self.name = "kill-server"
        self.description = "Kill ADB Server."
        self.usage = "Usage: kill-server"
        self.type = "managing"
        self.args = 1

    def run(self, cmd_data):
        print(self.badges.G + "Killing ADB Server...")
        output = self.ghost.send_command("kill-server")
        if "cannot connect to daemon" in output:
            print(self.badges.W + "ADB Server already killed")
        else:
            print(self.badges.G + "Killed ADB Server...")