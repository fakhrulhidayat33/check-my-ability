"""
Multiplication Table Project
Created by Fakhrul Hidayat
github: github.com/fakhrulhidayat33
Version 1.1: Static indent
Version 1.2: Dynamic indent based on the largest cell
Version 1.3: CLI interface for rows/columns and output format selection and CSV/text output
"""

import csv
import argparse
import os
from datetime import datetime

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
    parser.add_argument("--example", action="store_true", help="Run in example mode (3x3 table)")
    
    return parser.parse_args()

def pluralize_and_verb(count: int) -> tuple[str, str]:
    """Return (verb, plural_suffix) based on count, e.g., ('are','s') or ('is','')."""
    if count == 1:
        return "is", ""
    else:
        return "are", "s"


def log(r: int, c: int, exts, result) -> None:
    with open("log.txt", "a") as log_file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"Running at {timestamp} **************\n")
        verb_r, suffix_r = pluralize_and_verb(r)
        log_file.write(f"There {verb_r} {r} row{suffix_r}.\n")
        verb_c, suffix_c = pluralize_and_verb(c)
        log_file.write(f"There {verb_c} {c} column{suffix_c}.\n")
        for i, ext in enumerate(exts):
            log_file.write(f"File: table_{r}x{c}.{ext}.\n")


def center(text: str, indent: int) -> str:
    main = len(text)
    remain = indent - main
    right = remain // 2
    left = remain - right
    return " " * left + text + " " * right

def border_line(line: str, indent: int, n_col: int) -> str:
    return ("  " + line * indent + "  ") + (line * indent + " ") * n_col + (" \n")

def create_txt(n_row: int, n_col: int) -> str:
    """Build the pretty text version of the multiplication table."""
    dummy = f" {n_row} x {n_col} = {n_row * n_col} "
    indent = len(dummy)

    text = border_line("=", indent, n_col)
    
    # header row
    header = "||" + " " * indent + "||"
    for j in range(1, n_col + 1):
        header += center(str(j), indent) + "|"
    header += "|\n"
    text += header

    text += border_line("=", indent, n_col)

    # body
    for i in range(1, n_row + 1):
        row = "||" + center(str(i), indent) + "||"
        for j in range(1, n_col + 1):
            result = f"{i} x {j} = {i * j}"
            row += center(result, indent) + "|"
        row += "|\n"
        text += row
        
        border = "=" if i == n_row else "-"
        text += border_line(border, indent, n_col)

    return text

def create_csv(n_row: int, n_col: int) -> list[list[str]]:
    """Build the multiplication table as a list of rows for CSV export, including headers."""
    table = [] # list of strings

    # header
    header = [""] + [str(j) for j in range(1, n_col + 1)]
    table.append(header)

    # body
    for i in range(1, n_row + 1):
        row = [str(i)] + [f"{i} x {j} = {i * j}" for j in range(1, n_col + 1)]
        table.append(row)
    
    return table

def table_multiply(n_row: int, n_col: int, method: str):
    """
    n_row   : number of rows
    n_col   : number of columns
    method  : method I save the output
    """
    file = f"table_{n_row}x{n_col}"

    formats = ["csv", "txt"] if method == "both" else [method]
    results = []

    output_dir = "Data"
    os.makedirs(output_dir, exist_ok=True)

    for ext in formats:
        filename = os.path.join(output_dir, f"{file}.{ext}")
        if ext == "txt":
            result = create_txt(n_row, n_col)
            with open(filename, "w") as f:
                f.write(result)
        elif ext == "csv":
            result = create_csv(n_row, n_col)
            with open(filename, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerows(result)                
        results.append(result)
    os.chdir("..")
    log(n_row, n_col, formats, results)
    return results

if __name__ == "__main__":   
    args = parse_args()

    if args.example:
        r, c, m = 3, 3, "both"
    else:
        r, c, m = args.rows, args.cols, args.format

    if m == "text":
        m = "txt"

    table_multiply(r, c, m)