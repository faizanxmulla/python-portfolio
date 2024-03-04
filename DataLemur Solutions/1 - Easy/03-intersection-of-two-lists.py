def intersection(a: "list[int]", b: "list[int]") -> "list[int]":
    return list(set(a).intersection(b))

assert intersection([1, 2, 3, 4, 5], [0, 1, 3, 7]) == [1, 3]
