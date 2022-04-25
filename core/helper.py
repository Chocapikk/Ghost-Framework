#!/usr/bin/env python3

# Valentin Lobstein 2022
# Default Project : https://github.com/EntySec/Ghost

class helper:
    def __init__(self):
        self.rport = 5555
        self.version = "v6.0"

    def show_commands(self, target_commands):
        settings_commands = []
        managing_commands = []
        stealing_commands = []
        trolling_commands = []
        boot_commands = []

        commands = dict()
        commands.update(target_commands)

        for i in sorted(commands):
            if commands[i].type == "settings": settings_commands.append(commands[i])
            if commands[i].type == "managing": managing_commands.append(commands[i])
            if commands[i].type == "stealing": stealing_commands.append(commands[i])
            if commands[i].type == "trolling": trolling_commands.append(commands[i])
            if commands[i].type == "boot": boot_commands.append(commands[i])

        print("")
        print("Core Commands")
        print("=============")
        print("")
        print("    Command        Description")
        print("    -------        -----------")
        print("    clear          Clear terminal window.")
        print("    local          Execute local system command.")
        print("    exit           Exit and close current session.")
        print("    help           Show available session commands.")
        print("")

        if len(settings_commands) > 0:
            bigger = len(settings_commands[0].name)
            for i in settings_commands:
                if len(i.name) > bigger:
                    bigger = len(i.name)

            if bigger >= 14:
                bigger = bigger - 5
            else:
                bigger = 8

            print("Settings Commands")
            print("=================")
            print("")
            print("    Command" + " " * (bigger) + "Description")
            print("    -------" + " " * (bigger) + "-----------")
            for i in settings_commands:
                print("    " + i.name + " " * (7 - len(i.name) + bigger) + i.description)
            print("")

        if len(managing_commands) > 0:
            bigger = len(managing_commands[0].name)
            for i in managing_commands:
                if len(i.name) > bigger:
                    bigger = len(i.name)

            if bigger >= 14:
                bigger = bigger - 5
            else:
                bigger = 8

            print("Managing Commands")
            print("=================")
            print("")
            print("    Command" + " " * (bigger) + "Description")
            print("    -------" + " " * (bigger) + "-----------")
            for i in managing_commands:
                print("    " + i.name + " " * (7 - len(i.name) + bigger) + i.description)
            print("")

        if len(stealing_commands) > 0:
            bigger = len(stealing_commands[0].name)
            for i in stealing_commands:
                if len(i.name) > bigger:
                    bigger = len(i.name)

            if bigger >= 14:
                bigger = bigger - 5
            else:
                bigger = 8

            print("Stealing Commands")
            print("=================")
            print("")
            print("    Command" + " " * (bigger) + "Description")
            print("    -------" + " " * (bigger) + "-----------")
            for i in stealing_commands:
                print("    " + i.name + " " * (7 - len(i.name) + bigger) + i.description)
            print("")

        if len(trolling_commands) > 0:
            bigger = len(trolling_commands[0].name)
            for i in trolling_commands:
                if len(i.name) > bigger:
                    bigger = len(i.name)

            if bigger >= 14:
                bigger = bigger - 5
            else:
                bigger = 8

            print("Trolling Commands")
            print("=================")
            print("")
            print("    Command" + " " * (bigger) + "Description")
            print("    -------" + " " * (bigger) + "-----------")
            for i in trolling_commands:
                print("    " + i.name + " " * (7 - len(i.name) + bigger) + i.description)
            print("")

        if len(boot_commands) > 0:
            bigger = len(boot_commands[0].name)
            for i in boot_commands:
                if len(i.name) > bigger:
                    bigger = len(i.name)

            if bigger >= 14:
                bigger = bigger - 5
            else:
                bigger = 8

            print("Boot Commands")
            print("=============")
            print("")
            print("    Command" + " " * (bigger) + "Description")
            print("    -------" + " " * (bigger) + "-----------")
            for i in boot_commands:
                print("    " + i.name + " " * (7 - len(i.name) + bigger) + i.description)
            print("")
