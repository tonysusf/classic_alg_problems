# Implement a filtering engine/ class, for a given data set to filter out the data
from dataclasses import dataclass
import re

# @dataclass
class Filter:
    apply_filter: object

    def __call__(self, row):
        return self.apply_filter(row)

    def __and__(self, other):
        return Filter(lambda row: self(row) and other(row))

    def __or__(self, other):
        return Filter(lambda row: self(row) or other(row))

    def __invert__(self):
        return Filter(lambda row: not self(row))

def get_filter(field_name, op, target_val):
    print('field is', field_name, op, target_val)
    ops = {
        "==": lambda a, b: a == b,
        "!=": lambda a, b: a != b,
        ">": lambda a, b: a > b,
        ">=": lambda a, b: a >= b,
        "<": lambda a, b: a < b,
        "<=": lambda a, b: a <= b,
    }
    if op not in ops: raise ValueError("Invalid operator")

    def execute_filter(row):
        if field_name not in row: 
            raise ValueError(f"Field '{field_name}' not found in row")
        return ops[op](row[field_name], target_val)

    return Filter(execute_filter)

def apply_filter_for_data(rows, condition):
    result = [row for row in rows if condition(row)]
    print('result is', result)
    return result


############## Tests ###############################
data = [
    {"name": "Alice", "age": 30, "salary": 100, "gender": "F"},
    {"name": "Bob", "age": 20, "salary": 50, "gender": "M"},
    {"name": "Jim", "age": 40, "salary": 150, "gender": "M"},
    {"name": "David", "age": 22, "salary": 90, "gender": "M"},
]
# simple 
ft = get_filter("age", ">=", 30)
assert len(apply_filter_for_data(data, ft)) == 2

# AND
ft = (get_filter("age", ">=", 30) and get_filter("gender", "==", "F"))
result = apply_filter_for_data(data, ft)
assert [p["name"] for p in result] == ["Alice"]

# OR
ft = (
    get_filter("salary", ">", 120) | get_filter("gender", "==", "F")
)
result = apply_filter_for_data(data, ft)
assert [p["name"] for p in result] == ["Alice", "Jim"]

# NOT
ft = ~get_filter("gender", "==", "F")
result = apply_filter_for_data(data, ft)
assert [p["name"] for p in result] == ["Bob", "Jim", "David"]
