import importlib.util
import pathlib
import sys

# Locate and load your script (dash in filename prevents normal import)
script_path = pathlib.Path(__file__).parent / "table-multiplication.py"
spec = importlib.util.spec_from_file_location("table_multiplication", script_path)
table_mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(table_mod)


def test_create_csv_table_small():
    # Use the helper to build the 2x2 table structure
    table = table_mod.create_csv_table(2, 2)

    # Header row should be ["", "1", "2"]
    assert table[0] == ["", "1", "2"], f"Header row wrong: {table[0]}"

    # First data row: ["1", "1 x 1 = 1", "1 x 2 = 2"]
    assert table[1][1] == "1 x 1 = 1"
    assert table[1][2] == "1 x 2 = 2"

    # Second data row: ["2", "2 x 1 = 2", "2 x 2 = 4"]
    assert table[2][1] == "2 x 1 = 2"
    assert table[2][2] == "2 x 2 = 4"


def test_create_txt_contains_expected_line():
    # Generate text for 2x2 and do some simple substring checks
    text = table_mod.create_txt(2, 2)
    # Should include the header labels
    assert "1" in text and "2" in text
    # Should include a sample multiplication
    assert "1 x 2 = 2" in text
    assert "2 x 2 = 4" in text


if __name__ == "__main__":
    # Simple fallback runner if pytest is not installed
    try:
        test_create_csv_table_small()
        test_create_txt_contains_expected_line()
    except AssertionError as e:
        print("TEST FAILED:", e)
        sys.exit(1)
    print("All basic tests passed.")