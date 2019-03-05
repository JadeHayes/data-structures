# Lists-Notes: Two common operations are indexing and assigning to an index position.
# Both of these operations take the same amount of time no matter how large
# the list becomes. When an operation like this is independent of the size of the list they are O(1).
# Another common task is to grow a list. You can append O(1) <-- adds to the end of a list
# Other is concatenation O(k) <-- k depends on the size of the list.

"""Generate a list of n integers"""
from timeit import Timer


class ListOfInts:

    @staticmethod
    def concat(n):
        """ O(k) runtime, depends on the size of the list"""
        lst = []
        for i in range(n):
            lst += [i]

    @staticmethod
    def append(n):
        """O(1) runtime, adds to the end of the list"""
        lst = []
        for i in range(n):
            lst.append(i)

    @staticmethod
    def lst_comprehension(n):
        lst = [i for i in range(n)]

    @staticmethod
    def lst(n):
        lst = list(range(n))


def time_all_methods() -> None:
    """ Prints out the time it takes in milliseconds for all methods to run"""
    # method_names = All mthods in the class
    for method_name in method_names:
        time_all_methods(method_name)


def time_method(method_name: str) -> None:
    """ Prints out the time it takes in milliseconds for one methods to run"""
    t1 = Timer(method_name, f"from__main__ import {method_name}")
    print(f"{method_name}, {t1.timeit(number=1000)} milliseconds")
