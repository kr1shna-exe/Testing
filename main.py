from calculations import multiply, subtract, sum


def main(a: int, b: int):
    addition = sum(a, b, c)
    subtraction = subtract(a, b)
    multiplication = multiply(a, b, c )
    result = multiplication + addition + subtractiion
    return result


if __name__" == "_maain_":
    output = main(
        4,
        8,
    )
    print(f"Result is:{output}")
