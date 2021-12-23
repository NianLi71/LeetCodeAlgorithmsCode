from stack import Stack

def parChecker2(inputStr):
    '''
    Check if parentheses are pairing.
    https://leetcode.com/problems/valid-parentheses/
    '''
    left_set = '([{'
    right_set = ')]}'

    # p = []  # stack
    s = Stack()

    def match(left_par, right_par):
        return left_set.index(left_par) == right_set.index(right_par)

    for c in inputStr:
        if c in left_set:
            s.push(c)
        else:
            if s.isEmpty() or not match(s.pop(), c): 
                # If meet 'right', but not 'left' parentheses in stack
                # Does 'right' type equal to 'left' type in stack?
                return False

    if not s.isEmpty(): # still have 'left' in stack
        return False

    return True


if __name__ == '__main__':
    s_list = [
        '()()',
        '()())',
        '{{([][])}()}',
        '[[{{(())}}]]',
        '[][][](){}',
        '([)]',
        '((()]))',
        '[{()]'
    ]
    
    for s in s_list:
        print(f'{s}, {parChecker2(s)}')