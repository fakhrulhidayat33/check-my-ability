"""
sistem yang ada mirip seperti sistem first in last out
[ ] Membuat tulisan menjadi perline
"""

def debug(text):
    stop = input(f"{text}\n ")
    print("***********")
    if stop == "q":
        return True
    return False

test = "<!DOCTYPE html><html><head><title>One Line</title></head><body><h1>Hello World</h1></body></html>"

indent = 4
level = 0

print("===================================================")

tag_list = []
hide = ["br", "hr", "img", "input", "meta", "link", "source", "area", "col", "embed", "param", "base", "wbr"]
forget = ["strong", "b", "em", "u", "q", "a", "small", "sup", "sub", "b", "ins", "del", "span", "abbr", "cite"]
text = ""
start = False
# status ada A, B, C, D, E
def main():
    status = "s"
    tag_list = []
    text = ""
    head = True
    info = False
    for i in test:
        if status == "s":
            if i == "<":

                text += "\n"
                if debug(text): break

                status = "a"
            
            text += i

        elif status == "a":
            if i == "/":
                head = False
                status = "c"
            else:
                head = True
                status = "b"
            
            text += i

        elif status == "b":
            if i == " ":
                status = "d"

                text += i

            elif i == ">":
                status = "e"
                text += i
                text += "\n"
                if debug(text): break
                
            else:
                text += i

        elif status == "c":
            text += i

            status = "b"
        elif status == "d":
            if i == ">":
                status = "e"

                text += i
                text += "\n"
                stop = input(f"{text}\n ")
                if debug(text): break

            else:
                text += i
        elif status == "e":
            if i == "<":
                status = "a"

                text += "\n"
                if debug(text): break
                
                text += i
                info = False
            else:
                info = True
                text += i

    print("===============")
    print(text)
    return text
if __name__ == "__main__":
    main()
    with open("test.txt", "w") as f:
        f.write(text)