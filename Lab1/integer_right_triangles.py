from math import sqrt


def integer_right_triangle(length):  # must fulfil Pythagoras's theorem
    # output for each item: (a<=b<c)
    answer_lst = []
    half = int(length/2)
    for a in range(1, half):
        for b in range(a, half):
            c = sqrt(a**2 + b**2)
            if a+b+c == length:
                answer_lst.append((a, b, int(c)))
    # output will be automatically sorted
    return answer_lst


if __name__ == '__main__':
    print("Right triangle with len n")
    n = int(input("Enter an integer:"))
    print(integer_right_triangle(n))
