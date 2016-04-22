""" Given an image represented by an NxN matrix, where each pixel in the image
is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this
in place?

(Note: I have assumed clockwise rotation)

>>> matrix = [[1, 1, 1, 2],
...           [4, 5, 6, 2],
...           [4, 7, 8, 2],
...           [4, 3, 3, 3]]
>>> rotate(matrix)
[[4, 4, 4, 1], [3, 7, 5, 1], [3, 8, 6, 1], [3, 2, 2, 2]]
"""

def rotate(matrix):
    n = len(matrix)
    # build empty result matrix
    rotated = []
    max = len(matrix)-1
    # read column from bottom to top and copy to row left to right
    for i in range(n):
        rotated.append([])
        for j in range(n):
            rotated[i].append(matrix[max-j][i])
    return rotated


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** all tests passed.\n"