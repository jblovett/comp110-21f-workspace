"""Utility functions."""

__author__ = "123456789"

from csv import DictReader

# Define your functions below


def read_csv_rows(path: str) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    file_handle = open(path, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    
    # TODO 0.1) Complete the implementation of this function here.
    # where row is a dict[str, str]
    for row in csv_reader:
        rows.append(row)
    file_handle.close()
    return rows


def column_values(rows: list[dict[str, str]], column: str) -> list[str]:
    returned = list()
    # where each dict is a row of data. Each value is associated with a column/key. 
    # in the excel sheet, there's a single column 'name' for multiple values (vertically)
    # in code, the column name shows up across multiple dicts, because we're only representing a single row at a time
    for row in rows:
        returned.append(row[column])
    return returned


def columnar(table_rows: list[dict[str, str]]) -> dict[str, list[str]]:
    returned: dict[str, list[str]] = {}
    for row in table_rows:
        for column in row:
            values = column_values(table_rows, column)
            returned[column] = values
    return returned


def head(table: dict[str, list[str]], row_count: int) -> dict[str, list[str]]:
    returned: dict[str, list[str]] = {}
    for column in table:
        current_column: list[str] = table[column]
        i = 0
        while i < row_count:
            if column in returned:
                returned[column].append(current_column[i])
            else:
                returned[column] = [current_column[i]]
            i += 1
    return returned


def select(table: dict[str, list[str]], to_copy: list[str]) -> dict[str, list[str]]:
    returned: dict[str, list[str]] = {}
    for column in table:
        if column in to_copy:
            returned[column] = table[column]
    return returned