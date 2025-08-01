"""
Multiplication Table Project
Created by Fakhrul Hidayat
github: github.com/fakhrulhidayat33
Version 1.1: Static indent
Version 1.2: Dynamic indent based on the largest cell
Version 1.3: CLI interface for rows/columns and output format selection
"""

import csv, argparse

def parse_args():
    parser = argparse.ArgumentParser(
        description="Generate multiplication tables in text and/or CSV format"
    )
    parser.add_argument("--rows", "-r", type=int, default=10, help="Maximum value for first operand")
    parser.add_argument("--cols", "-c", type=int, default=10, help="Maximum value for second operand")
    parser.add_argument(
        "--format", "-f",
        choices=["text", "csv", "both"],
        default="both",
        help="Output format(s)"
    )
    return parser.parse_args()

def center(text: str, indent: int) -> str:
    main = len(text)
    remain = indent - main
    remain_1 = remain // 2
    remain_2 = remain - remain_1
    return " " * remain_2 + text + " " * remain_1

def border_line(line: str, indent: int, n_col: int) -> str:
    return ("  " + line * indent + "  ") + (line * indent + " ") * n_col + (" \n")

# function create_txt is building
def create_txt(n_row: int, n_col: int) -> str:
    dummy = f" {n_row} x {n_col} = {n_row * n_col} "
    indent = len(dummy)

    text = border_line("=", indent, n_col)
    lines = "||" + " " * indent + "||"
    for j in range(1, n_col + 1):
        lines += center(str(j), indent) + "|"
    lines += "|\n"
    text += lines
    # create a border line between header and body
    text += border_line("=", indent, n_col)

    # create the following rows with their borders
    for i in range(1, n_row + 1):
        lines = "||" + center(str(i), indent) + "||"
        for j in range(1, n_col + 1):
            result = f"{i} x {j} = {i * j}"
            lines += center(result, indent) + "|"
        lines += "|\n"
        text += lines
        
    border = "=" if i == n_row else "-"
    text += border_line(border, indent, n_col)
    return text

# function _ is bulding
def create_csv(n_row: int, n_col: int) -> {list, csv}: 
    rows = [] # list of strings
    compile = ""
    row = [""]
    for j in range(1, n_col + 1):
        row.append(str(j))
    rows.append(row)
    compile += ",".join(row) + "\n"
    for i in range(1, n_row + 1):
        row = [str(i)]
        for j in range(1, n_col + 1):
            result = f"{i} x {j} = {i * j}"
            row.append(result)
        rows.append(row)
        compile += ",".join(row) + "\n"
    return rows

def table_multiply(n_row: int, n_col: int, method: str) -> bool:
    # I need to add m to decide format to save the output
    """
    n_row   : number of rows
    n_col   : number of columns
    method  : method I save the output
    """
    if method == "text":
        ext = ".txt"
    elif method == "csv":
        ext = ".csv"
    filename = f"table_{n_row}x{n_col}" + ext


    with open(filename, "w") as file:

        # === 1st ======== FHs' line work  ===========

        # create the first line (header border)
        
        rows = [] # list of strings
        compile = ""

        # create the first row (header row)
        
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

        # === End ======== FHs' line work  ===========

    return rows

if __name__ == "__main__":    
    # n_row = int(input("Enter the maximum value for the first operand: "))
    # n_col = int(input("Enter the maximum value for the second operand: "))

    args = parse_args()
    r = args.rows
    c = args.rows
    m = args.format

    # CSV = table_multiply(r, c, m)
    # for i in CSV:
        # print(i)
    data = create_csv(r,c)
    print(type(data))
    print(data)
    pass # keep this block valid even when the example calls are commented out