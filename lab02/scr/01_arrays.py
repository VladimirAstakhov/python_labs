def min_max(nums: list[float | int]):
    if (len(nums) == 0):
        return "ValueError"
    return (max(nums), min(nums))
def unique_sorted(nums: list[float | int]):
    return list(set(nums))
def flatten(mat: list[list | tuple]):
    for each_list in mat:
        if (not isinstance(each_list, list)) and (not isinstance(each_list, tuple)):
            return "ValueError"

    return [element for each_list in mat for element in each_list]
print("min_max tests")
test_min_max_1 = [3, -1, 5, 5, 0]
test_min_max_2 = [42]
test_min_max_3 = [-5, -2, -9]
test_min_max_4 = []
print(min_max(test_min_max_1))
print(min_max(test_min_max_2))
print(min_max(test_min_max_3))
print(min_max(test_min_max_4))
print()

print("unique_sorted tests")
test_unique_sorted_1 = [3, 1, 2, 1, 3]
test_unique_sorted_2 = []
test_unique_sorted_3 = [-1, -1, 0, 2, 2]
test_unique_sorted_4 = [1.0, 1, 2.5, 2.5, 0]
print(unique_sorted(test_unique_sorted_1))
print(unique_sorted(test_unique_sorted_2))
print(unique_sorted(test_unique_sorted_3))
print(unique_sorted(test_unique_sorted_4))
print()

print("flatten tests")
test_flatten_1 = [[1, 2], [3, 4]]
test_flatten_2 = [[1, 2], (3, 4, 5)]
test_flatten_3 = [[1], [], [2, 3]]
test_flatten_4 = [[1, 2], "ab"]
print(flatten(test_flatten_1))
print(flatten(test_flatten_2))
print(flatten(test_flatten_3))
print(flatten(test_flatten_4))
