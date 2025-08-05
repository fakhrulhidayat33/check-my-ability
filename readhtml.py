"""
sistem yang ada mirip seperti sistem first in last out
[v] Membuat tulisan menjadi perline => program belum mengidentifikasi perpindahan antara head, informasi, dan tail
[v] Membuat penyimpanan sementara kemudian menambahkan setelah menayara perpindahan antara head, informasi, dan tail
[v] Membuat tulisan memperhatikan setelahnya untuk menambahkan
    [v] Head > Head => enter + indent bertambah (kecuali yang pertama)
    [v] Head > Tail => enter + indent tetap
    [v] Head > informasi => enter + indent bertambah
    # - Informasi > Head => pass [proses selanjutnya]
    [v] Informasi > Tail => enter + indent berkurang
    [v] Tail > Head => enter + indent tetap
    [v] Tail > Tail => enter + indent berkurang
    #- Tail > informasi => pass [proses selanjutnya]
[ ] Tidak memperhatikan tag yang berada di dalam tulisan (yang berada di dalam list Forget)
    [v] Menyimpan sementara nilai tag
    ...
[ ] Tidak menambah indent untuk memperhatikan tag yang berada di dalam tulisan (yang berada di dalam list Hide)

"""
from datetime import datetime

def debug(i, text, head, level):
    stop = input(f"{text}\n ")
    print(f"** {i} *********")
    print(f"level = {level}")
    print(f"head = {head}")
    if stop == "q":
        return True
    return False

test = "<!DOCTYPE html><html><head><title>One Line</title></head><body><h1>Hello World</h1></body></html>"

tag_list = []
hide = ["br", "hr", "img", "input", "meta", "link", "source", "area", "col", "embed", "param", "base", "wbr"]
forget = ["strong", "b", "em", "u", "q", "a", "small", "sup", "sub", "b", "ins", "del", "span", "abbr", "cite"]
text = ""
start = False
# status ada A, B, C, D, E
def main():
    indent = 4
    level = 0
    status = "s"
    text = ""
    part = ""
    head = True
    info = False
    indents = ""
    start = False
    for i in test:
        if status == "s":
            if i == "<":
                status = "a"
            
            part += i

        elif status == "a":
            if i == "/":
                if head:
                    level -= 1
                    indents = " " * level * indent
                else:
                    level -= 1
                    indents = " " * level * indent
                head = False
                status = "c"
            else:
                if head and start:
                    indents = " " * level * indent
                    level += 1
                elif not head:
                    level += 1
                head = True
                status = "b"
                tag = ""
            
            part += i

        elif status == "b":
            if i == " ":
                status = "d"
                part += i

            elif i == ">":
                status = "e"
                text += indents + part + i
                text += "\n"
                part = ""
                if debug(1, text, head, level): break
                
            else:
                part += i
                if head:
                    tag += i

        elif status == "c":
            part += i

            status = "b"
        elif status == "d":
            if i == ">":

                if not start: start = True
                status = "e"

                text += indents + part + i
                text += "\n"
                part = ""
                stop = input(f"{text}\n ")
                if debug(2, text, head, level): break

            else:
                part += i
        elif status == "e":
            if i == "<":
                status = "a"

                if not info:
                    text += part
                if info:
                    text += " " * indent + indents + part
                    text += "\n"

                if debug(3, text, head, level): break
                
                part = i
                info = False
            else:
                info = True
                part += i

    return text
if __name__ == "__main__":
    text = main()
    with open("test.txt", "a") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"Running at {timestamp} **************\n")
        f.write(text)