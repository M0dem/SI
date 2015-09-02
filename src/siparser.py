#!/usr/bin/python

class Token:
    def __init__(self, name):
        self.name = name


class String:
    def __init__(self, value):
        self.value = value

        
class Keyword:
    def __init__(self, name):
        self.name = name
        

parseTokens = [
    "(",
    ")",
    "=",
    "+",
    "-",
    "*",
    "/"
]

# organizers are basically lists that contain information in sequence ( [a, b, c] or (x, y, z) )
# an organizer could also contain arguments to functions
organizers = {
    "start": {
        "(",
        "["
    },
    "end": {
        ")",
        "]"
    }
}

organizerEnd = {
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

        # handle organizers
        elif code[i] in organizers["start"]:
						# handleOrganizers(code, i)
						
						subOrganizers = 0
						subCode = ""
						i += 1
						while i < len(code):
								if code[i] in organizers["end"]:
										if subOrganizers == 0:
												break

										elif subOrganizers > 0:
												subOrganizers -= 1

								elif code[i] in organizers["start"]:
										subOrganizers += 1

								subCode += code[i]
								i += 1

						codeL.append(parse(subCode))
						print(subCode)

        # handle keywords
        else:
            l = []
            while i < len(code) and (code[i] != "'" or code[i] != '"') and code[i] not in parseTokens:
                l.append(code[i])
                i += 1

            i -= 1

            codeL.append(Keyword("".join(l)))

        i += 1

    return codeL

# extracts list from organizer
# is recursive for sub-organizers
def handleOrganizers(code, i):
    l = []
    start = code[i]
    i += 1
    while i < len(code):
        try:
            if code[i] in organizers["start"]:
                tmpL, i = handleOrganizers(code, i)
                l.append(tmpL)

            else:
                l.append(code[i])

        except:
            pass


        i += 1
        
    return l, i

'''def tokenize(code):
    for token in parseTokens:
        code = code.replace(token, " " + token + " ")

    i = 0
    while i < len(code):
        if code[i] == "'" or code[i] == '"':
            startI = i
            start = code[i]
            l = []
            i += 1
            while i < len(code) and code[i] != start:
                l.append(code[i])
                i += 1

            print(String("".join(l)).value)

        i += 1

    code = code.split()
    for i in range(0, len(code)):
        if code[i] in parseTokens:
            code[i] = Token(code[i])

    return code'''
