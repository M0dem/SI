
#!/usr/bin/python

def assignVariable(name, value):
    globalVariables[name] = value

SYNTAX_KEYWORDS = {"=": assignVariable}
globalVariables = {}

def execute(code):
    return code
