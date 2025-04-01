def square_or_root(x):
    """
    Returns the square root of x if x is very large, otherwise returns x squared.
    """
    large_threshold = 1000
    if x > large_threshold:
        return x ** 0.5
    else:
        return x ** 2