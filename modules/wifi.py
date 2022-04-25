#!/usr/bin/env python3

# Valentin Lobstein 2022
# Default Project : https://github.com/EntySec/Ghost

from core.badges import badges
from core.ghost import ghost

class GhostModule:
    def __init__(self):
        self.badges = badges()
        self.ghost = ghost()

        self.name = "wifi"
        self.description = "Control device wifi service."
        self.usage = "Usage: wifi [on|off]"
        self.type = "settings"
        self.args = 2

    def run(self, cmd_data):
        if cmd_data in ['on', 'off']:
            if cmd_data == "on":
                self.ghost.send_command("shell", "svc wifi enable", False, False)
            else:
                self.ghost.send_command("shell", "svc wifi disable", False, False)
        else:
            print(self.usage)
