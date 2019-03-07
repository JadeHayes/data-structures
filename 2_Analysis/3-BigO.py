"""
Write two Python functions to find the minimum number in a list.
The first function should compare each number to every other number on the list. O(n2).
The second function should be linear O(n).
"""

lst = [4, 7, 8, 4, 3, 10, 2]
lst = [-400, 3, 2, 7, -7, 10000, 2]

class Analysis:

    def quadratic_min_num(int_lst: lst) -> int:
        """find min number in a list in O(n^2) time"""
        min_num = None
        i = 0
        for num in lst:
            if min_num is None:
                min_num = num
            i += 1
            for next_num in lst[i:]:
                if next_num < min_num:
                    min_num = next_num
        return min_num


    def linear_min_num(int_lst: lst) -> int:
        """find min number in a list in O(n) time"""
        min_num = None
        for num in int_lst:
            if min_num is None:
                min_num = num
            else:
                if num < min_num:
                    min_num = num
        return min_num








