from calculations import multiply, subtract, sum


def main(a: int, b: int):
    addition = sum(a, b)
    subtraction = subtract(a, b)
    multiplication = multiply(a, b)
    result = multiplication + addition + subtraction
    return result


def power(base, exponent):
    """
    Calculates the power of a base number raised to an exponent.

    Args:
        base: The base number (numeric type: int or float).
        exponent: The exponent (numeric type: int or float).

    Returns:
        The result of base raised to the power of exponent (numeric type: int or float).
        Returns None if either base or exponent is not a number.
    """
    if not isinstance(base, (int, float)) or not isinstance(exponent, (int, float)):
        return None  # Handle invalid input types

    return base ** exponent


if __name__ == "__main__":
    output = main(4, 8)
    print(f"Result is: {output}")

    # Test cases for power function
    print(f"2^3 = {power(2, 3)}")
    print(f"5^0 = {power(5, 0)}")
    print(f"2.5^2 = {power(2.5, 2)}")
    print(f"2^-2 = {power(2, -2)}")
    print(f"String input: {power('a', 2)}")  # Testing invalid input
    print(f"Negative base and exponent: {power(-2, 3)}")
    print(f"Zero base: {power(0, 5)}")
    print(f"Negative exponent: {power(4, -2)}")
