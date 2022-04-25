#!/usr/bin/env python3

# Valentin Lobstein 2022
# Default Project : https://github.com/EntySec/Ghost

from core.badges import badges
from core.ghost import ghost

class GhostModule:
    def __init__(self):
        self.badges = badges()
        self.ghost = ghost()

        self.name = "show_ip"
        self.description = "Get device IP."
        self.usage = "Usage: show_ip"
        self.type = "settings"
        self.args = 1

    def run(self, cmd_data):
        print(self.badges.G + "Getting device  IP...")
        output = self.ghost.send_command("shell", "ip addr show wlan0")
        print(output)