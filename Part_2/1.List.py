from typing import List


# Assign the list ['a', 'b', 'c', 'd', 'e'] to a variable.
# Reverse the list, then insert ‘z’ at index 3, and finally append ‘o’ to the end.
def transform_list(input_list: List[str]) -> List[str]:
    output_list: List[str] = []
    # ========================================================================

    print(input_list)
    input_list.reverse()
    input_list.insert(3, "z")
    input_list.append("o")

    print(input_list)
    
    input_list.sort()
    print(input_list)
    output_list = input_list
    # Reversing List, Inserting Item z, Appending o to the List, Sorting New List

    # ========================================================================
    return output_list


def main():
    result: List[str] = transform_list(["a", "b", "c", "d", "e"])
    expected: List[str] = ["e", "d", "c", "z", "b", "a", "o"]
    assert sorted(expected) == sorted(result)


if __name__ == "__main__":
    main()
