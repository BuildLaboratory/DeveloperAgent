"""Powers and roots."""


def square(x: float) -> float:
    """Return x squared."""
    return x * x


def cube(x: float) -> float:
    """Return x cubed."""
    return x * x * x


def power(base: float, exponent: int) -> float:
    """Return base raised to an integer exponent (exponent >= 0)."""
    if exponent < 0:
        raise ValueError("Exponent must be >= 0.")
    result = 1
    for _ in range(exponent):
        result *= base
    return result


def square_root(x: float) -> float:
    """Return the square root of x. Raises ValueError for negative x."""
    if x < 0:
        raise ValueError("Cannot take the square root of a negative number.")
    return x ** 0.5
