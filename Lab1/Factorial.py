def factorial(n):
    val = n
    for i in range(n-1, 0, -1):  # n-1 to 1
        val *= i
    return val


if __name__ == '__main__':
    print('Factorial!')
    inp = int(input('Enter an integer:'))
    res = factorial(inp)
    print(res)
