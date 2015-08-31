
import siparser

if __name__ == "__main__":
    # Just a temporary REPL thingy
    while True:
        ret = siparser.parse(raw_input("> "))
        print(ret)
