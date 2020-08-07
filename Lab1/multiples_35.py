def multiples_of_3_5_sum(limit):
    res = 0
    lst = []
    for i in range(3, limit):
        if i % 3 == 0 or i % 5 == 0:
            lst.append(i)
            res += i
    return res,lst


if __name__ == '__main__':
    print('Multiples of 3 and 5 sums that less than n')
    n = int(input('Enter an integer:'))
    out = multiples_of_3_5_sum(n)
    print('Value:',out[0])
    print('List of numbers:', out[1])