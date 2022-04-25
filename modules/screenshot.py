#!/usr/bin/env python3

# Valentin Lobstein 2022
# Default Project : https://github.com/EntySec/Ghost

import os
import binascii

from core.badges import badges
from core.ghost import ghost

class GhostModule:
    def __init__(self):
        self.badges = badges()
        self.ghost = ghost()

        self.name = "screenshot"
        self.description = "Take device screenshot."
        self.usage = "Usage: screenshot <local_path>"
        self.type = "managing"
        self.args = 2

    def run(self, cmd_data):
        screenshot_filename = "/sdcard/" + str(binascii.hexlify(os.urandom(5))) + ".png"
        print(self.badges.G + "Taking screenshot...")
        self.ghost.send_command("shell", "screencap " + screenshot_filename, False, False)
        self.ghost.download(screenshot_filename, cmd_data)
        self.ghost.send_command("shell", "rm " + screenshot_filename, False, False)
