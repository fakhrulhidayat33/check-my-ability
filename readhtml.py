"""
sistem yang ada mirip seperti sistem first in last out
[v] menambahkan 
"""
test = "<!DOCTYPE html><html><head><title>One Line</title></head><body><h1>Hello World</h1></body></html>"

indent = 4
level = 0

print("===================================================")

tag_list = []
hide = ["br", "hr", "img", "input", "meta", "link", "source", "area", "col", "embed", "param", "base", "wbr"]
forget = ["strong", "b", "em", "u", "q", "a", "small", "sup", "sub", "b", "ins", "del", "span", "abbr", "cite"]
text = ""
start = False
# status ada A, B, C, D, E, F, G
# status ready untuk pemeriksaan tag
# status set untuk memasukkan parameter tag
# status go untuk memasukkan konten
delete = False
status = "go"
tag = None
part = ""
for i in test:
    if start:
        if status == "go":
            part = i
            if i == "<":
                status = "ready"
                tag = ""
            else:
                status = "off"
        elif status == "ready":
            part += i
            if i == "/":
                if delete:
                    level -= 1
                else:
                    delete = True
            elif i == " ":
                delete = False
                status = "set"
                tag_list.append(tag)
            elif i == ">":
                status = "go"
                text += part # benar
                text += "\n" # benar
                if delete:
                    tag_list.pop()
                    # assert tag == tag_list.pop(), f"seharusnya tag yang dikeluarkan sama dengan tag yang sedang diproses\n{text}"
                    # tag_list.pop()
                else:
                    tag_list.append(tag)
                    tag = ""
                    level += 1
                text += " " * indent * level
                part = ""
                # print("stop1")
                # print(text)
                # break
            else:
                tag += i
            
        elif status == "set":
            part += i
            if i == ">":
                status = "go"
                if tag in forget:
                    pass
                elif tag in hide:
                    print("masukkah?")
                else:
                    level += 1
                text += part
                text += "\n"
                text += " " * indent * level
                print("stop2")
                print(text)
                break
        elif status == "off":
            if i == "<":
                text += part
                level -= 1
                text += "\n"
                text += " " * indent * level
                part = "<"
                status = "ready"
                tag = ""
            else:
                part += i
        print(f"== {i} ==")
        print(status)
        print(tag)
        print(level)
        print(tag_list)
        print(f"part = {part}")
        print(text)
        stop = input()
        if stop == "q": break


        # if i == "<":
        #     text += "\n"
        # elif i == "baka":
        #     first += i
    else:
        text += i
        if i == ">":
            start = True
            text += "\n"