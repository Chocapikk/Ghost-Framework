#!/usr/bin/env python3

# Valentin Lobstein 2022
# Default Project : https://github.com/EntySec/Ghost

from core.badges import badges
from core.ghost import ghost

class GhostModule:
    def __init__(self):
        self.badges = badges()
        self.ghost = ghost()

        self.name = "upload"
        self.description = "Upload local file."
        self.usage = "Usage: download <local_file> <remote_path>"
        self.type = "managing"
        self.args = 3

    def run(self, cmd_data):
        self.ghost.upload(cmd_data.split(" ")[0], cmd_data.split(" ")[1])
