from calculations import multiply, subtract, sum, division


def main(a: int, b: int):
    addition = sum(a, b)
    subtraction = subtract(a, b)
    multiplication = multiply(a, b)
    div = division(a, b)
    result = multiplication + addition + subtraction + div
    return result


if __name__ == "__main__":
    output = main(4, 8)
    print(f"Result is: {output}")
