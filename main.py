from calculations import multiply, subtract, sum, division


def main(a: int, b: int):
    addition = sum(a, b)
    subtraction = subtract(a, b)
    multiplication = multiply(a, b)
    division_result = division(a, b)
    result = multiplication + addition + subtraction + division_result
    return result


if __name__ == "__main__":
    output = main(4, 8)
    print(f"Result is: {output}")
