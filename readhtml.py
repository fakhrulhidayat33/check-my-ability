"""
sistem yang ada mirip seperti sistem first in last out
[v] menambahkan 
"""
test = "<!DOCTYPE html><html><head><title>One Line</title></head><body><h1>Hello World</h1></body></html>"

indent = 4
level = 0

tag_list = []
hide = ["br", "hr", "img", "input", "meta", "link", "source", "area", "col", "embed", "param", "base", "wbr"]
forget = ["strong", "b", "em", "u", "q", "a", "small", "sup", "sub", "b", "ins", "del", "span", "abbr", "cite"]
text = ""
start = False
# status ada A, B, C, D, E, F, G
delete = False
status = "off"
tag = None
part = ""
for i in test:
    if start:
        part += i
        if i == "<":
            status = "ready"
            tag = ""
        elif status == "ready":
            if i == "/":
                delete = True
            elif i == " ":
                status = "set"
                tag_list.append(tag)
            elif i == ">":
                if delete:
                    tag_list.pop()
            else:
                tag += i
            
        elif status != "off" and i == ">":
            status = "off"
            if tag in forget:
                pass
            elif tag in hide:
                print("masukkah?")
                text += "\n"
                text += " " * indent * level
            print("stop")
            print(text)
            break
        elif status == "set":
            if i == " ":
                status = "go"
                tag_list.append(tag)
                level += 1
            else:
                tag += i
        print(f"== {i} ==")
        print(status)
        print(tag)
        print(level)


        # if i == "<":
        #     text += "\n"
        # elif i == "baka":
        #     first += i
    else:
        text += i
        if i == ">":
            start = True
            text += "\n"