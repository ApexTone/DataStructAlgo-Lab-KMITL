from Lab2.stack import Stack


def is_match(p1, p2):
    pair = {
        '(': ')',
        '{': '}',
        '[': ']',
        ')': '(',
        '}': '{',
        ']': '['
    }
    return pair[p1] == p2


def is_balance(exp):
    s = Stack()
    error = False
    for character in exp:
        if character in '([{':
            s.push(character)
        elif character in ')]}':
            if s.is_empty():
                error = True
                break
            else:
                if not is_match(s.pop(), character):
                    error = True
                    break
    if error:
        print('Mismatch')
    else:
        if not s.is_empty():  # close parenthesis can't pair with open parenthesis
            print('Mismatch: excessive open parenthesis')
        else:
            print('Match')


if __name__ == '__main__':
    text = input('Enter the expression: ')
    is_balance(text)
