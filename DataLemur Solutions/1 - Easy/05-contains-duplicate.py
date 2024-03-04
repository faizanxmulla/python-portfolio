# clever solution : sets only have unique elements.

def contains_duplicate(input: "list[int]") -> bool:
    return len(input) != len(set(input))


# 2 -> brute force solution :


def contains_duplicate(input):
    for i in range(len(input) - 1):
        for j in range(i + 1, len(input)):
            if input[i] == input[j]:
                return True
    return False


# 3 -> sorting and then check if each value is the same as the value directly before it:


def contains_duplicate(input):
    input.sort()
    for i in range(len(input) - 1):
        if input[i] == input[i + 1]:
            return True
    return False


# 4 -> using Dictionary.

def contains_duplicate(input):
    seen = {}
    for i in input:
        if i in seen:
            return True
        seen[i] = True
    return False
