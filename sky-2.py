"""
Maximum sum of two numbers with the same digit sum

Developed by Selman Tabet @ https://selman.io/
------------------------------------------------
Developed for the Sky Placement Test 2023
"""


def solution(A):
    """Maximum sum of two numbers with the same digit sum

    Args:
        A (list): List of integers

    Returns:
        int: Highest sum of two numbers with the same digit sum, -1 if no such sum exists
    """
    b = []
    for i in A:
        # Sum of digits of each number in A
        b.append(sum(list(map(int, str(i)))))
    # Sort to prepare for seeking same digit sums
    sorted_joined = sorted(zip(A, b), key=lambda x: x[1], reverse=True)
    sorted_a = [i[0] for i in sorted_joined]
    sorted_b = [i[1] for i in sorted_joined]
    max_sum = -1
    flag = False  # Flag to indicate if a group of same digit sums has been found
    # Marks the location of the first number in the group of same digit sums
    flag_raise_location = 0

    for i in range(len(sorted_b)):
        if i == len(sorted_b) - 1:
            if not flag:  # Unique digit sum
                break
            else:  # Reached end of list but it's also the end of an unprocessed group of same digit sums
                same_digit_sum = sorted_a[flag_raise_location: i + 1]
                test_sum = max_sum_from_group(same_digit_sum)
                if test_sum > max_sum:
                    max_sum = test_sum
                break
          # Reached end of list, avoid index out of range
        if sorted_b[i] == sorted_b[i + 1]:  # Same digit sum
            if not flag:  # Marks the start of a group of same digit sums
                flag = True
                flag_raise_location = i

            test_sum = sorted_a[i] + sorted_a[i + 1]
            if test_sum > max_sum:
                max_sum = test_sum
        else:
            if flag:  # End of a group of same digit sums, seek is now complete.
                flag = False
                same_digit_sum = sorted_a[flag_raise_location: i + 1]
                test_sum = max_sum_from_group(
                    same_digit_sum)  # Process the group and find its highest sum pair
                if test_sum > max_sum:
                    max_sum = test_sum
    return max_sum


def max_sum_from_group(group):  # All will always have the same digit sum
    group_sorted = sorted(group, reverse=True)
    # The highest sum would be the sum of the first two numbers of a sorted descending list
    if len(group_sorted) < 2:
        return -1
    return group_sorted[0] + group_sorted[1]


print(solution([51, 71, 17, 42]))
print(solution([42, 33, 60]))
print(solution([51, 32, 43]))
