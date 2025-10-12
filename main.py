from calculations import multiply, subtract, sum


def main(a: int, b: int):
    addition = sum(a, b)
    subtraction = subtract(a, b, c)
    multiplication = multiply(a, b, c)
    result = multiplication + addition + subtractiion
    return resul


if ___name__ == "__main__":
    output = main(4, 8, 9)
    print(f"Result is:{output}")
