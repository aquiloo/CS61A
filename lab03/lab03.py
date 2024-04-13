HW_SOURCE_FILE=__file__


def pascal(row, column):
    """Returns a number corresponding to the value at that location
    in Pascal's Triangle.
    >>> pascal(0, 0)
    1
    >>> pascal(0, 5)	# Empty entry; outside of Pascal's Triangle
    0
    >>> pascal(3, 2)	# Row 4 (1 3 3 1), 3rd entry
    3
    """
    # row 0 or 1
    if row == 0 or row == 1:
        if row == 0 and column <= 0:
            return 1
        if row == 1 and column <= 1:
            return 1
        return 0
    # boundary check
    if column > row:
        return 0
    pascal_i = [1, 1]
    # compute (row-1)th pascal triangle
    for i in range(2, row):
        size = len(pascal_i)
        for ith in range(len(pascal_i) - 1):
            pascal_i.append(pascal_i[ith]+pascal_i[ith+1])
        pascal_i = pascal_i[size:]
        pascal_i.append(1)
        pascal_i.insert(0, 1)
    # compute the column th element
    if column == 0 or column == len(pascal_i):
        return 1
    elif column == 1 or column == len(pascal_i)-1:
        return 1 + pascal_i[column - 1]
    else:
        return pascal_i[column-1] + pascal_i[column]


def compose1(f, g):
    """"Return a function h, such that h(x) = f(g(x))."""
    def h(x):
        return f(g(x))
    return h

def repeated(f, n):
    """Return the function that computes the nth application of func (recursively!).

    >>> add_three = repeated(lambda x: x + 1, 3)
    >>> add_three(5)
    8
    >>> square = lambda x: x ** 2
    >>> repeated(square, 2)(5) # square(square(5))
    625
    >>> repeated(square, 4)(5) # square(square(square(square(5))))
    152587890625
    >>> repeated(square, 0)(5)
    5
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'repeated',
    ...       ['For', 'While'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n == 0:
        return lambda x: x
    if n == 1:
        return f
    return compose1(f, repeated(f, n-1))

def num_eights(x):
    """Returns the number of times 8 appears as a digit of x.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    if x < 10 and x != 8:
        return 0
    if x < 10 and x == 8:
        return 1
    if x % 10 == 8:
        return num_eights(x//10) + 1
    if x % 10 != 8:
        return num_eights(x//10)

def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    def helper(i, switch, res):
        """res is the value of the i th element"""
        if i == n:
            return res
        if num_eights(i) >= 1 or i % 8 == 0:
            return helper(i + 1, switch*-1, res - switch)
        else:
            return helper(i + 1, switch, res + switch)
    return helper(1,1,1)
