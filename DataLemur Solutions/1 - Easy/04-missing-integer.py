# Solution 1 :

def missing_int(input: "list[int]") -> int:
    return ((n := len(input)) * (n + 1) / 2) - sum(input)


# Solution 2: using SORTING.

def missing_int(input: "list[int]") -> int:
    input.sort()
    for i in range(len(input)):
        if i != input[i]:
            return i
    return len(input)


# Solution 3: using SETS.

def missing_int(input: "list[int]") -> int:
    input_set = set(input)
    n = len(input) + 1
    for i in range(n):
        if i not in input_set:
            return i
