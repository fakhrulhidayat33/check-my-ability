"""
sistem yang ada mirip seperti sistem first in last out
[v] Membuat tulisan menjadi perline => program belum mengidentifikasi perpindahan antara head, informasi, dan tail
[v] Membuat penyimpanan sementara kemudian menambahkan setelah menayara perpindahan antara head, informasi, dan tail
[ ] Membuat tulisan memperhatikan setelahnya untuk menambahkan
    - Head > Head => enter + indent bertambah (kecuali yang pertama)
    - Head > Tail => enter + indent tetap
    - Head > informasi => enter + indent bertambah
    # - Informasi > Head => pass [proses selanjutnya]
    - Informasi > Tail => enter + indent berkurang
    - Tail > Head => enter + indent tetap
    - Tail > Tail => enter + indent berkurang
    #- Tail > informasi => pass [proses selanjutnya]
[ ] Tidak memperhatikan tag yang berada di dalam tulisan
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
    part = ""
    head = True
    info = False
    for i in test:
        if status == "s":
            if i == "<":
                status = "a"
            
            part += i

        elif status == "a":
            if i == "/":
                head = False
                status = "c"
            else:
                head = True
                status = "b"
            
            part += i

        elif status == "b":
            if i == " ":
                status = "d"

                part += i

            elif i == ">":
                status = "e"

                text += part + i
                text += "\n"
                part = ""
                if debug(text): break
                
            else:
                part += i

        elif status == "c":
            part += i

            status = "b"
        elif status == "d":
            if i == ">":
                status = "e"

                text += part + i
                text += "\n"
                part = ""
                stop = input(f"{text}\n ")
                if debug(text): break

            else:
                part += i
        elif status == "e":
            if i == "<":
                status = "a"

                text += "\n"
                text += part
                if info:
                    print("disini kan?")
                    text += "\n"
                    info = False
                if debug(text): break
                
                part = i
                info = False
            else:
                info = True
                part += i
                # print("masukkah?")
                if part == "One Line":
                    print("masuk kaka")
                    input()

    print("===============")
    print(text)
    return text
if __name__ == "__main__":
    main()
    with open("test.txt", "w") as f:
        f.write(text)