#!/usr/bin/env python3

# Valentin Lobstein 2022
# Default Project : https://github.com/EntySec/Ghost

from core.badges import badges
from core.ghost import ghost

class GhostModule:
    def __init__(self):
        self.badges = badges()
        self.ghost = ghost()

        self.name = "sysinfo"
        self.description = "Get device system information."
        self.usage = "Usage: sysinfo"
        self.type = "settings"
        self.args = 1

    def run(self, cmd_data):
        system = "Android"
        hostname = self.ghost.send_command("shell", "getprop net.hostname")
        username = self.ghost.send_command("shell", "getprop ro.product.name")
        version = self.ghost.send_command("shell", "getprop ro.build.version.release")
        architecture = self.ghost.send_command("shell", "getprop ro.product.cpu.abi")
        information = ""
        information += f"{self.badges.I}Operating System: {system}\n"
        information += f"{self.badges.I}Computer Hostname: {hostname}\n"
        information += f"{self.badges.I}Computer Username: {username}\n"
        information += f"{self.badges.I}Release Version: {version}\n"
        information += f"{self.badges.I}Processor Architecture: {architecture}"
        print(information)
