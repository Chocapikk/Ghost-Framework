#!/usr/bin/env python3

# Valentin Lobstein 2022
# Default Project : https://github.com/EntySec/Ghost

from core.badges import badges
from core.ghost import ghost

class GhostModule:
    def __init__(self):
        self.badges = badges()
        self.ghost = ghost()

        self.name = "shell"
        self.description = "Open device shell."
        self.usage = "Usage: shell"
        self.type = "managing"
        self.args = 1

    def run(self, cmd_data):
        print(self.badges.G + "Opening device shell...")
        output = self.ghost.send_command("shell", "", True)
        if "error: more than one device/emulator" in output:
            print(self.badges.E + "Please kill-server and try again...")
            
