"""
sistem yang ada mirip seperti sistem first in last out
[v] menambahkan 
"""
test = "<!DOCTYPE html><html><head><title>One Line</title></head><body><h1>Hello World</h1></body></html>"

indent = 4
c_indent = 0

tag_list = []
hide = ["br", "hr", "img", "input", "meta", "link", "source", "area", "col", "embed", "param", "base", "wbr"]
forget = ["strong", "b", "em", "u", "q", "a", "small", "sup", "sub", "b", "ins", "del", "span", "abbr", "cite"]
text = ""
start = False
# status ada 3 ready, set, go, dan off
status = "off" 
for i in test:
    if start:
        print("stop")
        print(text)
        break
        if i == "<":
            text += "\n"
        elif i == "baka":
            first += i
    else:
        text += i
        if i == ">":
            start = True
            text += "\n"