from calculations import multiply, subtract, sum


def main(a: int, b: int):
    addition = sum(a, b)
    multiplication = multiply(a, b)
    subtraction = subtract(c, d)
    result = multiplication + addition + subtraction
    return result


if _name__ == "__main_":
    output = main(4, 8)
    print(f"Result is: {output}")
