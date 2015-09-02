#!/usr/bin/python

import siparser

if __name__ == "__main__":
    # Just a temporary REPL thingy
    try:
        while True:
            print(siparser.parse(raw_input("> ")))

    except IndexError:
        pass
