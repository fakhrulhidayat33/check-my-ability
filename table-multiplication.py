"""
Multiplication Table Project
Created by Fakhrul Hidayat
github: github.com/fakhrulhidayat33
Version 1.1: Static indent
Version 1.2: Dynamic indent based on the largest cell
Version 1.3: Dynamic indent based on the largest cell in each column (in progress)
"""

import csv 

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
    n_row: number of rows
    n_col: number of columns
    """
    dummy = f" {n_row} x {n_col} = {n_row * n_col} "
    indent = len(dummy)

    with open("table-multiplication.txt", "w") as f1, \
        open(f"table_{n_row}x{n_col}.txt", "w") as f2, \
        open(f"multiply_{n_row}x{n_col}.csv", "w") as data:
    
        # create the first line (header border)
        text = border_line("=", indent, n_col)
        rows = [] # list of strings
        compile = ""

        # create the first row (header row)
        lines = "||" + " " * indent + "||"
        row = [""]
        for j in range(1, n_col + 1):
            lines += center(str(j), indent) + "|"
            row.append(str(j))
        lines += "|\n"
        text += lines

        # create a border line between header and body
        text += border_line("=", indent, n_col)
        rows.append(row)
        compile += ",".join(row) + "\n"

        # create the following rows with their borders
        for i in range(1, n_row + 1):
            lines = "||" + center(str(i), indent) + "||"
            row = [str(i)]
            
            for j in range(1, n_col + 1):
                result = f"{i} x {j} = {i * j}"
                lines += center(result, indent) + "|"
                row.append(result)
            lines += "|\n"
            text += lines
            
            border = "=" if i == n_row else "-"
            text += border_line(border, indent, n_col)
            rows.append(row)
            compile += ",".join(row) + "\n"
        
        f1.write(text)
        f2.write(text)
        data.write(compile)

    return rows

if __name__ == "__main__":    
    n_row = int(input("Enter the maximum value for the first operand: "))
    n_col = int(input("Enter the maximum value for the second operand: "))
    CSV = table_multiply(n_row, n_col)
    for i in CSV:
        print(i)