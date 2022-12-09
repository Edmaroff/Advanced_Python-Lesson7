from task_1_Stack import Stack


def check_balanced():
    sequence = list(input('Введите последовательность из скобок: '))
    stack = Stack()
    matching_brackets = {')': '(',
                         ']': '[',
                         '}': '{'
                         }
    for symbol in sequence:
        if symbol not in matching_brackets:
            stack.push(symbol)
        else:
            if matching_brackets[symbol] != stack.peek():
                return 'Несбалансированно'
            else:
                stack.pop()
    if stack.is_empty():
        return 'Cбалансированно'
    return 'Несбалансированно'
