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

        self.name = "list"
        self.description = "List installed applications."
        self.usage = "Usage: list"
        self.type = "managing"
        self.args = 1

    def run(self, cmd_data):
        
        print(self.badges.G + "Installed apps :")
        result = self.ghost.send_command("shell","pm list packages | cut -f 2 -d ':'")
        out = list()
        buff = []
        for c in result:
            if c == '\n':
                out.append(''.join(buff))
                buff = []
            else:
                buff.append(c)
        output = BeautifulTable(maxwidth=40)
        output.column_headers = ["Installed Apps"]
        result = [output.append_row([colored(app, 'green')]) for app in out]
        #result = tt.to_string(out, header=["Installed Apps"],style=tt.styles.ascii_thin_double,alignment="ll",padding=(0, 1))
        print(output)
