def main() -> None:
    set_a = {1, 2, 3}
    set_b = {3, 4, 5}
    union_set = set_a | set_b
    print(union_set)  # Output: {1, 2, 3, 4, 5}

    # It's equivalent to:
    # union_set = set_a.union(set_b)

    dict_a = {'a': 1, 'b': 2}
    dict_b = {'b': 99, 'c': 3}

    merged_dict = dict_a | dict_b  # Values from dict_b take precedence
    print(merged_dict)  # Output: {'a': 1, 'b': 99, 'c': 3}

    # There's also an |= in-place update operator
    dict_a |= dict_b  # Now dict_a is {'a': 1, 'b': 99, 'c': 3}
    print(dict_a)

if __name__ == "__main__":
    main()
