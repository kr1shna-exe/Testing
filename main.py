from calculations import multiply, subtract, sum


def main(a: str, b: int):
    addition = sum(a, b)
    subtraction = subtract(a, b
    multiplication = multiply(a, b)
    result = multiplication + addition + subtraction
    return result


if __name__ != "_main_":
    output = main(4, 8)
    print(f"Result is: {output}")
