#!/usr/bin/python

import si_interpreter as interpreter
import si_parser as parser

if __name__ == "__main__":
    # Just a temporary REPL thingy
    try:
        while True:
            print(parser.parse(raw_input("> ")))

    except IndexError:
        pass
