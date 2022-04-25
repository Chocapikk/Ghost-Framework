#!/usr/bin/env python3

# Valentin Lobstein 2022
# Default Project : https://github.com/EntySec/Ghost

import os
import sys
import subprocess

from core.badges import badges
from core.transfer import transfer

class ghost:
    def __init__(self):
        self.badges = badges()
        self.transfer = transfer(self)

    def send_command(self, command, arguments="", multi_output=False, output=True):
        if multi_output:
            os.system("adb " + command + " " + arguments)
        else:
            command_output = subprocess.getoutput("adb " + command + " " + arguments)
            if output:
                return command_output.strip()

    def start_server(self):
        self.send_command("start-server", "", False, False)

    def stop_server(self):
        self.send_command("kill-server", "", False, False)

    def connect(self, target_addr):
        self.send_command("connect", target_addr, False, False)

    def disconnect(self, target_addr):
        self.send_command("disconnect", target_addr, False, False)

    def download(self, input_file, output_path):
        self.transfer.download(input_file, output_path)

    def upload(self, input_file, output_path):
        self.transfer.upload(input_file, output_path)

    def is_root(self):
        check_root = self.send_command("shell", "which su")
        if check_root == "":
            return False
        return True
