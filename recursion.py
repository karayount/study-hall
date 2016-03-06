def doubler_no_loop(lst):
    """Print items in list, doubled."""

    if not lst:
        return

    x, rest = lst[0], lst[1:]
    print rest

    if isinstance(x, list):
        doubler_no_loop(x)
    else:
        print x * 2,

    doubler_no_loop(rest)


doubler_no_loop([1, 2, 3, [2, 3, 4], 1])