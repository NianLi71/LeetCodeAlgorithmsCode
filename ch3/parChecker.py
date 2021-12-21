from stack import Stack

def parChecker(inputStr):
    '''
    Check if parentheses are pairing.
    '''
    left = '('
    right = ')'

    s = Stack()

    for c in inputStr:
        if c == left:
            s.push(c)
        else:
            if s.isEmpty() or s.pop() != left:
                return False
    
    if not s.isEmpty():
        return False

    return True


if __name__ == '__main__':
    s_list = [
        '()()',
        '()())',
        '(()()',
        '((())))',
        '(((()))'
    ]
    
    for s in s_list:
        print(f'{s}, {parChecker(s)}')