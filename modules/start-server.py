#!/usr/bin/env python3

# Valentin Lobstein 2022
# Default Project : https://github.com/EntySec/Ghost

from core.badges import badges
from core.ghost import ghost

class GhostModule:
    def __init__(self):
        self.badges = badges()
        self.ghost = ghost()

        self.name = "start-server"
        self.description = "Start ADB Server."
        self.usage = "Usage: start-server"
        self.type = "managing"
        self.args = 1

    def run(self, cmd_data):
        print(self.badges.G + "Starting ADB Server...")
        output = self.ghost.send_command("kill-server")
        if "daemon started successfully" in output:
            print(self.badges.G + "ADB Server started successfully")
        else:
            print(self.badges.E + "Cannot start ADB Server (already started ?)...")
        print(output)