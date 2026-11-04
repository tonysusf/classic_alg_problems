# Implement a filtering engine/ class, for a given data set to filter out the data
from dataclasses import dataclass

@dataclass
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

    def match_filter(row):
        if field_name not in row: 
            raise ValueError(f"Field '{field_name}' not found in row")
        return ops[op](row[field_name], target_val)

    return Filter(match_filter)

def apply_filter_for_data(rows, condition):
    print('select', rows, condition)
    return [row for row in rows if condition(row)]


############## Tests ###############################
data = [
    {"name": "Alice", "age": 30, "salary": 100, "type": "A"},
    {"name": "Bob", "age": 20, "salary": 50, "type": "B"},
    {"name": "Charlie", "age": 40, "salary": 150, "type": "A"},
    {"name": "David", "age": 22, "salary": 90},
]
# simple 
test_filter = get_filter("age", ">=", 30)
assert len(apply_filter_for_data(data, test_filter)) == 2

# AND
test_filter = (get_filter("age", ">=", 30) & get_filter("type", "==", "A"))
result = apply_filter_for_data(data, test_filter)
assert [p["name"] for p in result] == ["Alice", "Charlie"]

# OR
test_filter = (
    get_filter("salary", ">", 120) | get_filter("type", "==", "B")
)
result = apply_filter_for_data(data, test_filter)
assert [p["name"] for p in result] == ["Bob", "Charlie"]

# NOT
test_filter = ~get_filter("type", "==", "A")
result = apply_filter_for_data(data, test_filter)
assert [p["name"] for p in result] == ["Bob", "David"]

# Combined AND, OR, NOT
test_filter = (
    (get_filter("age", ">=", 30) | get_filter("salary", "<", 60))
    & ~get_filter("type", "==", "B")
)
result = apply_filter_for_data(data, complextest_filter_filter)
assert [p["name"] for p in result] == ["Alice", "Charlie"]
