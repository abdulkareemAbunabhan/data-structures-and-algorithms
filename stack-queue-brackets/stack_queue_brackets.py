def validate_brackets(string):
    """this function used to check weather a string contains a validate brackets with validate openning and close or 
    not and return the answer as a boolean"""
    stack = []
    opening_brackets = ['(', '{', '[']
    closing_brackets = [')', '}', ']']
    bracket_pairs = {'(': ')', '{': '}', '[': ']'}
    
    for char in string:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack:
                return False
            top = stack[-1]
            if bracket_pairs[top] != char:
                return False
            stack.pop()

    if stack:
        return False
    return True
