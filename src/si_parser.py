#!/usr/bin/python

from __future__ import print_function


class String:
    def __init__(self, value):
        self.value = value

        
class Keyword:
    def __init__(self, name):
        self.name = name
        

PARSE_TOKENS = [
    "(",
    ")",
    "[",
    "]",
    "=",
    "+",
    "-",
    "*",
    "/",
    ","
]

# ORGANIZERS are basically lists that contain information in sequence ( [a, b, c] or (x, y, z) )
# an organizer could also contain arguments to functions
ORGANIZERS = {
    "start": [
        "(",
        "["
    ],
    "end": [
        ")",
        "]"
    ]
}

ORGANIZER_END = {
    "(": ")",
    "[": "]"
}

def parse(code):
    code = tokenize(code)
    return code

def tokenize(code):
    codeL = []
    i = 0
    while i < len(code):
        # handle strings
        if code[i] == "'" or code[i] == '"':
            startI = i
            start = code[i]
            l = []
            i += 1
            while i < len(code) and code[i] != start:
                l.append(code[i])
                i += 1

            codeL.append(String("".join(l)))
            
            print("string!")
            print("  " + "".join(l))
            print("\n")

        # handle organizers
        elif code[i] in ORGANIZERS["start"]:
                        
            subOrganizers = 0
            subCode = ""
            i += 1
            while i < len(code):
                    if code[i] in ORGANIZERS["end"]:
                        if subOrganizers == 0:
                            break

                        elif subOrganizers > 0:
                            subOrganizers -= 1

                    elif code[i] in ORGANIZERS["start"]:
                        subOrganizers += 1

                    subCode += code[i]
                    i += 1

            subCode = parse(subCode)
            codeL.append(subCode)
            
            print("organizer!")
            print("  ", end = "")
            print(subCode)
            print("\n")
        
        # handle keywords
        elif code[i] != " " and (code[i] != "'" and code[i] != '"') and code[i] not in PARSE_TOKENS:
            l = []
            while i < len(code) and (code[i] != "'" and code[i] != '"') and code[i] != " " and code[i] not in PARSE_TOKENS:
                l.append(code[i])
                i += 1

            i -= 1

            codeL.append(Keyword("".join(l)))
            
            print("keyword!")
            print("  " + "".join(l))
            print("\n")

        i += 1
        

    return codeL
