#!/usr/bin/env python3

# Valentin Lobstein 2022
# Default Project : https://github.com/EntySec/Ghost

from core.badges import badges
from core.ghost import ghost

class GhostModule:
    def __init__(self):
        self.badges = badges()
        self.ghost = ghost()

        self.name = "openurl"
        self.description = "Open URL on device."
        self.usage = "Usage: openurl <url>"
        self.type = "managing"
        self.args = 2

    def run(self, cmd_data):
        if not cmd_data.startswith(("http://", "https://")):
            cmd_data = "http://" + cmd_data

        self.ghost.send_command("shell", "\"am start -a android.intent.action.VIEW -d "+cmd_data+"\"", True)
