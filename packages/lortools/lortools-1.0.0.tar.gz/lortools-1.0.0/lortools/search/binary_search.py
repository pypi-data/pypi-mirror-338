# Adapted from https://stackoverflow.com/questions/9501337/binary-search-algorithm-in-python
# Also: https://stackoverflow.com/questions/212358/binary-search-bisection-in-python


class BinarySearch:
    @staticmethod
    def find(array, target, b_return_pos=True):
        """

        :param array: the array to be searched.
        :param target: the target to look for.
        :param b_return_pos: if the target is not found in the array and b_return_pos == True, then the returned value\
        will represent the position the target would take if it were inserted into the array (more concretely, it will\
        return -(insert_pos+1)), else it will simply return -1.
        :return:
        """
        lo = 0
        hi = len(array)

        while True:
            x = lo + (hi - lo)//2
            val = array[x]
            if target == val:
                return x
            elif target > val:
                if lo == x:  # The current value of lo represents the position of the element
                             # 'target' would be inserted after
                    x = -(x+2)  # We return the "insert position" of the target '+1'!
                                # The insert position is the current position +1, hence, we do +2!
                    break
                lo = x
            elif target < val:
                if lo == hi == 0:
                    x = -(x+1)
                    break
                hi = x

        return x if x >= 0 else (x if b_return_pos else -1)

    @staticmethod
    def find_in_array(array, target, endpos_entries=None, fixed_size=None, b_return_pos=True):
        """
        Same principle as "find", only this method assumes the input is a contiguous array. 'endpos_entries' is expected\
        to be a iterable of size (number of elements in array), where each entry contains to the end position in the\
        array of the corresponding element.

        :param array: the array to be searched.
        :param target: the target to look for.
        :param endpos_entries: list containing the end index of the entries in the array; if None, it is assumed\
        that each position in the array contains a single entry.
        :param fixed_size: if all entries in the array have the same size, you can specify this using this parameter.\
        If its value is an integer, endpos_entries will be ignored.
        :param b_return_pos: if the target is not found in the array and b_return_pos == True, then the returned value\
        will represent the position the target would take if it were inserted into the array (more concretely, it will\
        return -(insert_pos+1)), else it will simply return -1.
        :return:
        """
        if endpos_entries is None and fixed_size is None:
            b_fixed_size = True
            fixed_size = 1
        # If both endpos_entries AND fixed_size are specified, ignore endpos_entries
        elif fixed_size is not None:
            b_fixed_size = True
        else:
            b_fixed_size = False

        lo = 0
        hi = len(array)//fixed_size if b_fixed_size else len(endpos_entries)

        while True:
            x = lo + (hi - lo)//2

            # x represents an index in endpos_entries; now get the corresponding starting position
            if b_fixed_size:
                end = (x+1)*fixed_size
            else:
                end = endpos_entries[x]
            if b_fixed_size:
                start = x*fixed_size
            else:
                if x == 0:
                    start = 0
                else:
                    start = endpos_entries[x-1]

            # Read entry 'x'
            val = array[start:end]
            if target == val:
                return x
            elif target > val:
                if lo == x:  # The current value of lo represents the position of the element
                             # 'target' would be inserted after
                    x = -(x+2)  # We return the "insert position" of the target '+1'!
                                # The insert position is the current position +1, hence, we do +2!
                    break
                lo = x
            elif target < val:
                if lo == hi == 0:
                    x = -(x+1)
                    break
                hi = x

        return x if x >= 0 else (x if b_return_pos else -1)

    @staticmethod
    def find_in_file(file, target, startpos_lines=None, b_binary=False, b_return_pos=True):
        """
        Same principle as "find", only this method assumes the input is a text or binary file where each line
        contains one value.

        :param file: the file to be searched.
        :param target: the target to look for.
        :param startpos_lines: sorted list containing the starting positions of the lines in the file;\
        if None, will initialize here
        :param b_binary: whether the file is a binary file or not.
        :param b_return_pos: if the target is not found in the array and b_return_pos == True, then the returned value\
        will represent the position the target would take if it were inserted into the array (more concretely, it will\
        return -(insert_pos+1)), else it will simply return -1.
        :return:
        """
        mode = 'rb' if b_binary else 'r'

        # Get positions of newlines in file
        if startpos_lines is None:
            startpos_lines = [0]
            with open(file, mode) as fin:
                for _ in fin:
                    startpos_lines.append(fin.tell())
            # Remove last item, which is EOF position
            startpos_lines = startpos_lines[:-1]

        lo = 0
        hi = len(startpos_lines)

        with open(file, mode) as fin:
            while True:
                x = lo + (hi - lo)//2

                # Set position in file at start of line x
                fin.seek(startpos_lines[x])

                # Read line at position x
                val = fin.readline().strip()
                if target == val:
                    return x
                elif target > val:
                    if lo == x:  # The current value of lo represents the position of the element
                                 # 'target' would be inserted after
                        x = -(x+2)  # We return the "insert position" of the target '+1'!
                                    # The insert position is the current position +1, hence, we do +2!
                        break
                    lo = x
                elif target < val:
                    if lo == hi == 0:
                        x = -(x+1)
                        break
                    hi = x

        return x if x >= 0 else (x if b_return_pos else -1)
