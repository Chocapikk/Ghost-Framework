#!/usr/bin/env python3

# Valentin Lobstein 2022
# Default Project : https://github.com/EntySec/Ghost

import os

class fsmanip:
    def __init__(self):
        self.error = '\033[1;31m[-] \033[0m'

    def exists_directory(self, path):
        if os.path.isdir(path):
            if os.path.exists(path):
                return (True, "directory")
            else:
                print(self.error + "Local directory: " + path + ": does not exist!")
                return (False, "")
        else:
            directory = os.path.split(path)[0]
            if directory == "":
                directory = "."
            if os.path.exists(directory):
                if os.path.isdir(directory):
                    return (True, "file")
                else:
                    print(self.error + "Error: " + directory + ": not a directory!")
                    return (False, "")
            else:
                print(self.error + "Local directory: " + directory + ": does not exist!")
                return (False, "")

    def file(self, path):
        if os.path.exists(path):
            if os.path.isdir(path):
                print(self.error + "Error: " + path + ": not a file!")
                return False
            else:
                return True
        else:
            print(self.error + "Local file: " + path + ": does not exist!")
            return False
