#!/usr/bin/env python3

# Valentin Lobstein 2022
# Default Project : https://github.com/EntySec/Ghost

from core.badges import badges
from core.ghost import ghost

class GhostModule:
    def __init__(self):
        self.badges = badges()
        self.ghost = ghost()

        self.name = "send_sms"
        self.description = "Send a SMS to a specified number."
        self.usage = "Usage: send_sms <phone_number> <text>"
        self.type = "managing"
        self.args = 3

    def run(self, cmd_data):
        output = self.ghost.send_command("shell",f'service call isms 7 i32 0 s16 "com.android.mms.service" s16 {cmd_data.split(" ")[0]} s16 "null" s16 {cmd_data.split(" ")[1]} s16 "null" s16 "null"')
        if "Service isms does not exist" in output:
            print(self.badges.E + "Can't send SMS with this target system...")
        else:
            print(self.badges.W + f"SMS Sent to {cmd_data.split(' ')[0]}...")

        print(output)