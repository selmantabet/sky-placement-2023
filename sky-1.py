"""
BANANA Removal Counter

Developed by Selman Tabet @ https://selman.io/
------------------------------------------------
Developed for the Sky Placement Test 2023
"""


def solution(S):
    """ Returns the maximum number of times the letters of "BANANA" can be removed from the input string S.

    Args:
        S (string): List of integers

    Returns:
        int: Number of times the letters of "BANANA" can be removed from the input string S.
    """

    banana = {
        'B': 1,
        'A': 3,
        'N': 2,
    }
    result = 0
    s_replaced = S
    s_prev = S
    while result < 17000:  # Rough approx. upper bound
        for i in banana:  # For all keys
            for j in range(banana[i]):  # Keep removing a letter one at a time
                s_replaced = s_prev.replace(i, "", 1)
                if s_replaced == s_prev:  # No change, end of the function.
                    return result
                else:
                    s_prev = s_replaced
        # All BANANA letters removed, increment result and do it again on s_prev.
        result += 1
