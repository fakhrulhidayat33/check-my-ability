def center(text: str, indent: int) -> str:
    main = len(text)
    remain = indent - main
    remain_1 = remain // 2
    remain_2 = remain - remain_1
    # 6 - 1 = 5 => 5 // 2 = 2
    # 6 - 2 = 4 => 4 / 2 = 2
    return " " * remain_2 + text + " " * remain_1

def border_line(line: str, indent: int, n_col: int) -> str:
    return ("  " + line * indent + "  ") + (line * indent + " ") * n_col + (" \n")

def check(text: str, indent: int = 8) -> None:
    print("|", end="")
    print(center(text, 8), end="")
    print("|")


def table_multiply(n_row: int, n_col: int) -> bool:
    """
    n_row: banyak baris
    n_col: banyak kolom
    """
    # | 10 x 10 = 100 |
    # | 1234567890123 |
    # indent = n_row + n_col + 8 + len(str(n_row * n_col))
    indent = 15
    
    file = open("table-multiplication.txt", "w")
    
    # menambahkan garis baris pertama (head)
    file.write(border_line("=", indent, n_col))
    
    # menambahkan baris pertama (head)
    lines = "||" + " " * indent + "||"
    for j in range(1, n_col + 1):
        lines += center(str(j), indent) + "|"
    lines += "|\n"
    file.write(lines)

    # menambahkan garis pembatas antara head dan body tabel
    file.write(border_line("=", indent, n_col))

    # menambahkan baris selanjutnya beserta pembatasnya
    for i in range(1, n_row + 1):
        lines = "||" + center(str(i), indent) + "||"
        for j in range(1, n_col + 1):
            lines += center(f"{i} x {j} = {i * j}", indent) + "|"
        lines += "|\n"
        file.write(lines)
        if i == n_row: border = "="
        else: border = "-"
        file.write(border_line(border, indent, n_col))

    file.close()

    # for i in range(a + 1):

    print (n_row * n_col)
    return True

if __name__ == "__main__":    
    # check("saya")
    # check("kamu")
    # check("aku")
    table_multiply(10, 10)
    pass