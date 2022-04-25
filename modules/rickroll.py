#!/usr/bin/env python3
media volume --stream 3 --set 100
# Valentin Lobstein 2022
# Default Project : https://github.com/EntySec/Ghost

from core.badges import badges
from core.ghost import ghost

class GhostModule:
    def __init__(self):
        self.badges = badges()
        self.ghost = ghost()

        self.name = "rickroll"
        self.description = "Rickrolling the device."
        self.usage = "Usage: rickroll"
        self.type = "trolling"
        self.args = 1

    def run(self, cmd_data):
        cmd_data = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        self.ghost.send_command("shell", "\"am start -a android.intent.action.VIEW -d "+cmd_data+"\"", False)
        self.ghost.send_command("shell", "media volume --stream 3 --set 100", False)
        print(self.badges.G + "🎶 Never Gonna Give You Up, Never Gonna Let You Down 🎶")
