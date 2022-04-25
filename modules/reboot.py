#!/usr/bin/env python3

# Valentin Lobstein 2022
# Default Project : https://github.com/EntySec/Ghost

from core.badges import badges
from core.ghost import ghost

class GhostModule:
    def __init__(self):
        self.badges = badges()
        self.ghost = ghost()

        self.name = "reboot"
        self.description = "Reboot device."
        self.usage = "Usage: reboot"
        self.type = "boot"
        self.args = 1

    def run(self, cmd_data):
        print(self.badges.G + "Rebooting device...")
        self.ghost.send_command("reboot", "", True)
