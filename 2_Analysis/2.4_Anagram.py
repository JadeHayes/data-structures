"""
Write a boolean function that will take two strings and return whether they are anagrams.
"""
str1 = "apple"
str2 = "pplae"
class Anagram:

    def quadratic(str1, str2) -> bool:
        """
        Check to see if 2 strings are anagrams in quadratic run time by checking to see
        if a letter from one list exists in another list.
        """
        if len(str1) == len(str2):
            str2_list = list(str2)
            for letter in str1:
                # TODO: TOM --> Do you know if the "not in" operation would make this quadratic? I think it does
                if letter not in str2_list:
                    return False
            return True
        return False


    def quadratic_with_sort(str1, str2) -> bool:
        """Check to see if 2 strings are anagrams in quadratic run time by sorting and comparing letters."""
        if not len(str1) == len(str2):
            return False

        lst1 = list(str1)
        lst2 = list(str2)

        # sorting operations dominate this iteration, they are either (n log n) or O(n^2).
        lst1.sort()
        lst2.sort()

        i = 0

        while i < len(lst1):
            if lst1[i] == lst2[i]:
                i += 1
            else:
                return False
        return True



    def linear(str1, str2) -> bool:
        """Check to see if 2 strings are anagrams in linear run time by sorting and comparing letters."""
        if not len(str1) == len(str2):
            return False

        def _letter_count(str: str) -> dict:
            str1_count = {}

            for letter in str:
                str1_count[letter] = str1_count.get(letter, 0) + 1
            return str1_count

        str1_count: dict =_letter_count(str1)
        str2_count: dict = _letter_count(str2)

        if not len(str1_count) == len(str2_count):
            return False

        for item in str1_count:
            if not str2_count.get(item) == str1_count.get(item):
                return False
        return True
