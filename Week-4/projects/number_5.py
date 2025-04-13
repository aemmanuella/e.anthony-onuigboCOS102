def swap_first_last(my_list):
    if len(my_list) >= 2:
        my_list[0], my_list[-1] = my_list[-1], my_list[0]
    return None

nums = [1, 2, 3, 4, 5]
swap_first_last(nums)
print(swap_first_last(nums))  # Output: [5, 2, 3, 4, 1]
