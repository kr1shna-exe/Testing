from calculations import multiply, subtract, sum, division


def main(a: int, b: int):
    addition = sum(a, b)
    subtraction = subtract(a, b)
    multiplication = multiply(a, b)
    try:
        division_result = division(a, b)
    except ZeroDivisionError:
        division_result = 0  # Handle division by zero
    result = multiplication + addition + subtraction + division_result
    return result


if __name__ == "__main__":
    output = main(4, 8)
    print(f"Result is: {output}")
