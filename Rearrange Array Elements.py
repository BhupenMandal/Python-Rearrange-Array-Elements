import random

def rearrange_digits(input_list):
    if not input_list:
        return None

    first_max_sum = str()
    second_max_sum = str()

    sort_descend = merge_sort(input_list)

    for index, element in enumerate(sort_descend):
        if index % 2 == 0:
            first_max_sum += str(element)
        else:
            second_max_sum += str(element)

    return int(first_max_sum), int(second_max_sum)


def merge_sort(input_list):
    if len(input_list) <= 1:
        return input_list

    mid_index = len(input_list) // 2

    left_half = input_list[:mid_index]
    right_half = input_list[mid_index:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


def merge(left_half, right_half):
    merged_list = []
    left_index = 0
    right_index = 0

    while left_index < len(left_half) and right_index < len(right_half):

        if left_half[left_index] < right_half[right_index]:
            merged_list.append(right_half[right_index])
            right_index += 1
        else:
            merged_list.append(left_half[left_index])
            left_index += 1

    merged_list += left_half[left_index:]
    merged_list += right_half[right_index:]

    return merged_list


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]

    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])

print(rearrange_digits([]))


print(rearrange_digits(None))

l = [i for i in range(0, 1000)]  # a list containing 0 - 999
random.shuffle(l)

print("First max sum :-")
print(rearrange_digits(l)[0])
print()
print("Second max sum :-")
print(rearrange_digits(l)[1])
