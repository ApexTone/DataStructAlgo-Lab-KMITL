def gen_pattern(string):  # return the pattern
    strlen = len(string)
    if strlen < 1:
        return "Can't generate a pattern from string that's shorter than 1 character."
    max_col = 1+(4*(strlen-1))  # 1->1 2->5 3->9 4->13 (+4 as pattern)
    lines = ''
    lst = []
    for i in range(1, strlen+1):
        sp = string[-i:strlen]
        rev = sp[0:len(sp)-1]
        rev = rev[::-1]
        sp += rev
        if len(sp) != 1:
            sp = '.'.join(sp)
        sp = sp.center(max_col, '.')
        lst.append(sp)
        lines += sp+'\n'
    for i in range(2, strlen+1):
        lines += lst[-i] + '\n'
    return lines


if __name__ == '__main__':
    """
    print('*'.join('abcd'))
    print('hello'.center(11,'*'))  # 11 is entire row len
    """
    print("Gen Pattern")
    pattern_string = input("Enter string pattern:")
    print(gen_pattern(pattern_string), end="")
