def is_balanced(expression):
    stack = []
    # checks if it contains parentheses, square brackets, or curly braces
    pairs = {')': '(', '}': '{', ']': '['}

    for character in expression:
        if character in pairs.values():
            stack.append(character)
        elif character in pairs.keys():
            if not stack or stack.pop() != pairs[character]:
                return False

    return len(stack) == 0
