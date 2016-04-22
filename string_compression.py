""" Implement a method to perform basic string compression using the counts of
repeated characters. For example, the string aabcccccaaa would become a2b1c5a3.
If the "compressed" string would not become smaller than the original string,
your method should return the original string. You can assume the string has
only uppercase and lowercase letters (a-z).

>>> compress_string("aabcccccaaa")
'a2b1c5a3'
"""

def compress_string(string):
    compressed = ""
    char = string[0]
    count = 1
    index = 1
    while index < len(string):
        if string[index] == char:
            count += 1
        else:
            compressed = compressed + char + str(count)
            char = string[index]
            count = 1
        index += 1
    compressed = compressed + char + str(count)

    if len(compressed) < len(string):
        return compressed
    else:
        return string


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** all tests passed.\n"