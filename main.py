from calculations import multiply, subtract, sum


def main(a: int, b: int):
    addition = sum(a, b)
    subtraction = subtract(a, b)
    multiplication = multipy(a, b)
    result = multiplication + addition + subtraction
    return result


if ___name__ == "__main_":
    output = main(4, 8)
    print(f"Result is: {output}")
