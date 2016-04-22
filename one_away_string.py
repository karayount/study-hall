""" There are three types of edits that can be performed on strings: insert a
character, remove a character, or replace a character. Given two strings, write
a function to check if they are one edit (or zero edits) away.

>>> strings_are_one_edit_away("pale", "ple")
True

>>> strings_are_one_edit_away("pales", "pale")
True

>>> strings_are_one_edit_away("pale", "bale")
True

>>> strings_are_one_edit_away("pale", "bae")
False
"""

def strings_are_one_edit_away(s1, s2):
    if s1 == s2:
        return True

    length_diff = abs(len(s1) - len(s2))

    if length_diff > 1:
        return False

    elif length_diff == 1:
        longer = s1 if len(s1)>len(s2) else s2
        shorter = s1 if len(s1)<len(s2) else s2

        long_index = 0
        short_index = 0
        mismatches = 0
        while long_index < len(longer) and short_index < len(shorter):
            if longer[long_index] != shorter[short_index]:
                if mismatches > 0:
                    return False
                else:
                    mismatches += 1
                    long_index += 1
            else:
                long_index += 1
                short_index += 1

    elif length_diff == 0:
        index = 0
        mismatches = 0
        while index < len(s1):
            if s1[index] != s2[index]:
                if mismatches > 0:
                    return False
                else:
                    mismatches += 1
                    index += 1
            else:
                index += 1

    return True


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** all tests passed.\n"