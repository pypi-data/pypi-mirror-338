""" A simple array that can be efficiently searched using binary search."""


class BinaryArray:
    def __init__(self, values, b_is_sorted=True):
        """

        :param values: list/set/... of values that should be stored in the array
        :param b_is_sorted: boolean indicating whether the values are already sorted or not
        """
        self.values = list(values) if b_is_sorted else sorted(values)
