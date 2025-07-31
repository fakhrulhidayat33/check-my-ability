"""
Proyek Tabel perkalian
Dibuat oleh Fakhrul Hidayat
github: github.com/fakhrulhidayat33
Versi 1.1 indent statis
Versi 1.2 indent dinamis berdasearkan sel terbesar
Veris 1.3 indent dinamis berdasarkan sel terbesar pada masing-masing kolom (sedang diproses)
"""
def center(text: str, indent: int) -> str:
    main = len(text)
    remain = indent - main
    remain_1 = remain // 2
    remain_2 = remain - remain_1
    return " " * remain_2 + text + " " * remain_1

def border_line(line: str, indent: int, n_col: int) -> str:
    return ("  " + line * indent + "  ") + (line * indent + " ") * n_col + (" \n")

def table_multiply(n_row: int, n_col: int) -> bool:
    """
    n_row: banyak baris
    n_col: banyak kolom
    """
    dummy = f" {n_row} x {n_col} = {n_row * n_col} "
    indent = len(dummy)

    with open("table-multiplication.txt", "w") as file:
    
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
            border = "=" if i == n_row else "-"
            file.write(border_line(border, indent, n_col))

    return True

if __name__ == "__main__":    
    n_row = int(input("Berikan nilai terbesar operanda pertama: "))
    n_col = int(input("Berikan nilai terbesar operanda kedua: "))
    table_multiply(n_row, n_col)