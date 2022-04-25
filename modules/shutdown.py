#!/usr/bin/env python3

# Valentin Lobstein 2022
# Default Project : https://github.com/EntySec/Ghost

from core.badges import badges
from core.ghost import ghost

class GhostModule:
    def __init__(self):
        self.badges = badges()
        self.ghost = ghost()

        self.name = "shutdown"
        self.description = "Shutdown device."
        self.usage = "Usage: shutdown"
        self.type = "boot"
        self.args = 1

    def run(self, cmd_data):
        print(self.badges.G + "Stopping the device...")
        self.ghost.send_command("reboot", "-p", True)