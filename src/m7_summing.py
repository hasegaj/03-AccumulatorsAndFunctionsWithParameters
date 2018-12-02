"""
This module lets you practice the ACCUMULATOR pattern
in its simplest classic forms:
   SUMMING:       total = total + number

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher, Mark Hays,
         Aaron Wilkin, their colleagues, and Josiah Hasegawa.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_sum_cosines()
    run_test_sum_square_roots()


def run_test_sum_cosines():
    """ Tests the   sum_cosines   function. """
    # -------------------------------------------------------------------------
    # Done: 2. Implement this function.
    #   It TESTS the  sum_cosines  function defined below.
    #   Include at least **   3   ** tests.
    #
    # Use the same 4-step process as in implementing previous
    # TEST functions, including the same way to print expected/actual.
    # -------------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_cosines   function:')
    print('--------------------------------------------------')
    #test1
    expected = 1
    answer = sum_cosines(1)
    print('test 1 expected', expected)
    print('     actual: ', answer)

    #test2
    expected = 2
    answer = sum_cosines(4)
    print('test 2 expected', expected)
    print('     actual: ', answer)

    #test3
    expected = 3
    answer = sum_cosines(10)
    print('test 3 expected', expected)
    print('     actual: ', answer)


def sum_cosines(n):
    """
    What comes in:  A non-negative integer n.
    What goes out:  The sum of the cosines of the integers
       0, 1, 2, 3, ... n, inclusive, for the given n.
    Side effects:   None.
    Example:
      If n is 3, this function returns
        cos(0) + cos(1) + cos(2) + cos(3)   which is about 0.13416.
        josiah: incorrect; it should be n = 4 gets .13416
    """
    # -------------------------------------------------------------------------
    # Done: 3. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #   That is called TEST-DRIVEN DEVELOPMENT (TDD).
    #
    #   No fair running the code of  sum_cosines  to GENERATE
    #   test cases; that would defeat the purpose of TESTING!
    # -------------------------------------------------------------------------
    import math
    t = 0
    for k in range(n):
        t = t + math.cos(k)

    return t



def run_test_sum_square_roots():
    """ Tests the   sum_square_roots   function. """
    # -------------------------------------------------------------------------
    # Done: 4. Implement this function.
    #   It TESTS the  sum_square_roots  function defined below.
    #   Include at least **   3   ** tests.
    #
    # Use the same 4-step process as in implementing previous
    # TEST functions, including the same way to print expected/actual.
    # -------------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_square_roots   function:')
    print('--------------------------------------------------')

    #test1
    expected = 11.854408
    answer = sum_square_roots(6)
    print('test 1 expected', expected)
    print('     actual: ', answer)

    #test2
    expected = 19.060167
    answer = sum_square_roots(8)
    print('test 2 expected', expected)
    print('     actual: ', answer)

    #test3
    expected = 27.30280778
    answer = sum_square_roots(10)
    print('test 3 expected', expected)
    print('     actual: ', answer)


def sum_square_roots(n):
    """
    What comes in:  A non-negative integer n.
    What goes out:  The sum of the square roots of the integers
       2, 4, 6, 8, ... 2n    inclusive, for the given n.
           So if n is 7, the last term of the sum is
           the square root of 14 (not 7).
    Side effects:   None.
    Example:
      If n is 5, this function returns
         sqrt(2) + sqrt(4) + sqrt(6) + sqrt(8) + sqrt(10),
      which is about 11.854408.
    """
    import math
    r = 0
    for k in range(n):
        r = r + math.sqrt(2*k)

    return r

    # -------------------------------------------------------------------------
    # Done: 5. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #   That is called TEST-DRIVEN DEVELOPMENT (TDD).
    #
    #   No fair running the code of  sum_square_roots  to GENERATE
    #   test cases; that would defeat the purpose of TESTING!
    # -------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
