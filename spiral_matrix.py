
def spiral_print_existing_matrix(matrix):
    """ Prints elements of 2D array in spiral order
    :param matrix: 2D array
    :return: None
    """

    rows = len(matrix)
    cols = len(matrix[0])
    top = 0
    bottom = rows-1
    left = 0
    right = cols-1
    dir = 0

    while top <= bottom and left <= right:
        if dir == 0:
            for i in range(left, right+1):
                print matrix[top][i]
            top += 1
            dir = 1
        elif dir == 1:
            for i in range(top, bottom+1):
                print matrix[i][right]
            right -= 1
            dir = 2
        elif dir == 2:
            for i in range(right, left-1, -1):
                print matrix[bottom][i]
            bottom -= 1
            dir = 3
        elif dir == 3:
            for i in range(bottom, top-1, -1):
                print matrix[i][left]
            left += 1
            dir = 0


def spiral_fill_matrix_outside_in(n):
    """ Fill nxn matrix counting to n^2
    :param n: len of side of square
    :return: matrix
    """

    matrix = [[None]*n for i in range(n)]
    top = 0
    bottom = n-1
    left = 0
    right = n-1
    dir = 0
    next_num = 1

    while next_num <= n**2:
         # move right (left to right)
        if dir == 0:
            for i in range(left, right+1):
                matrix[top][i] = next_num
                next_num += 1
            top += 1
            dir = 1
        # move down (top to bottom)
        elif dir == 1:
            for i in range(top, bottom+1):
                matrix[i][right] = next_num
                next_num += 1
            right -= 1
            dir = 2
        # move left (right to left)
        elif dir == 2:
            for i in range(right, left-1, -1):
                matrix[bottom][i] = next_num
                next_num += 1
            bottom -= 1
            dir = 3
        # move up (bottom to top)
        elif dir == 3:
            for i in range(bottom, top-1, -1):
                matrix[i][left] = next_num
                next_num += 1
            left += 1
            dir = 0

    return matrix


def spiral_matrix(n):
    if n == 1:
        matrix = [[1]]
        return matrix

    # all other cases
    matrix = spiral_matrix(n-1)
    next_num = (n-1)**2 + 1
    larger_matrix = [[None]*n for i in range(n)]
    if n%2 == 0:
        bottom = n-1
        right = n-1
        # fill in top left with smaller
        for i in range(right):
            for j in range(bottom):
                larger_matrix[i][j] = matrix[i][j]
        # fill in bottom right with new numbers
        for i in range(bottom + 1):
            larger_matrix[i][right] = next_num
            next_num += 1
        for j in range(right-1, -1, -1):
            larger_matrix[bottom][j] = next_num
            next_num += 1
        matrix = larger_matrix
    else:
        # fill in bottom right with smaller
        for i in range(1, n):
            for j in range(1, n):
                larger_matrix[i][j] = matrix[i-1][j-1]
        # fill in top left with new numbers
        for i in range(n-1, -1, -1):
            larger_matrix[i][0] = next_num
            next_num += 1
        for j in range(1, n):
            larger_matrix[0][j] = next_num
            next_num += 1
        matrix = larger_matrix

    return matrix

print spiral_matrix(6)