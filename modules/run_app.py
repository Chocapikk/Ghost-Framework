#!/usr/bin/env python3

# Valentin Lobstein 2022
# Default Project : https://github.com/EntySec/Ghost

from core.badges import badges
from core.ghost import ghost

class GhostModule:
    def __init__(self):
        self.badges = badges()
        self.ghost = ghost()

        self.name = "run_app"
        self.description = "Run an application from the target machine."
        self.usage = "Usage: run_app <package_name>"
        self.type = "managing"
        self.args = 2

    def run(self, cmd_data):
        output = self.ghost.send_command("shell", f"monkey -p {cmd_data.split(' ')[0]} -c android.intent.category.LAUNCHER 1")
        if "No activities found to run" in output:
            print(self.badges.E + "Application not installed...")
        else:
            print(self.badges.G + "Application Executed !")
