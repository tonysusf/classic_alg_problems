# Implement a filtering engine/ class, for a given data set to filter out the data

from dataclasses import dataclass

@dataclass
class Filter:
    fn: object

    def __call__(self, row):
        return self.fn(row)

    def __and__(self, other):
        return Filter(lambda row: self(row) and other(row))

    def __or__(self, other):
        return Filter(lambda row: self(row) or other(row))

    def __invert__(self):
        return Filter(lambda row: not self(row))


def field(name, op, target):
    print('field is', name, op, target)
    ops = {
        "==": lambda a, b: a == b,
        "!=": lambda a, b: a != b,
        ">": lambda a, b: a > b,
        ">=": lambda a, b: a >= b,
        "<": lambda a, b: a < b,
        "<=": lambda a, b: a <= b,
    }
    if op not in ops: raise ValueError("Unsupported operator")

    def match(row):
        if name not in row: return False
        try:
            return ops[op](row[name], target)
        except TypeError:
            return False

    return Filter(match)


def select(rows, condition):
    print('select', rows, condition)
    return [row for row in rows if condition(row)]


############## Tests ###############################

data = [
    {"name": "Alice", "age": 30, "salary": 100, "type": "A"},
    {"name": "Bob", "age": 20, "salary": 50, "type": "B"},
    {"name": "Charlie", "age": 40, "salary": 150, "type": "A"},
    {"name": "David", "age": 22, "salary": 90},
]

# simple filter
age_filter = field("age", ">=", 30)
assert len(select(data, age_filter)) == 2

# AND case
combined = (
    field("age", ">=", 30) & field("type", "==", "A")
)
result = select(data, combined)
assert [p["name"] for p in result] == ["Alice", "Charlie"]

# OR case
combined = (
    field("salary", ">", 120) | field("type", "==", "B")
)
result = select(data, combined)
assert [p["name"] for p in result] == ["Bob", "Charlie"]

# NOT case
not_type_a = ~field("type", "==", "A")
result = select(data, not_type_a)
assert [p["name"] for p in result] == ["Bob", "David"]

# Missing field
missing = field("city", "==", "SF")
assert select(data, missing) == []

# Empty input
assert select([], age_filter) == []

# Invalid operator
try:
    field("age", "contains", 30)
    assert False, "Expected ValueError"
except ValueError:
    pass

# Combined AND, OR, NOT
complex_filter = (
    (field("age", ">=", 30) | field("salary", "<", 60))
    & ~field("type", "==", "B")
)
result = select(data, complex_filter)
assert [p["name"] for p in result] == ["Alice", "Charlie"]

print("All tests passed!")
