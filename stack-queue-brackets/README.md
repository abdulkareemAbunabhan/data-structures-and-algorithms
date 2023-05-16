# Stack queue barckets

Write a function called validate brackets
Arguments: string
Return: boolean
representing whether or not the brackets in the string are balanced

## Whiteboard Process

![whiteBoard](./My_First_Board.jpg)

## Approach & Efficiency

The time complexity of this function is O(n), where n is the length of the input string. This is because the function iterates through each character in the string exactly once and performs constant time operations for each character. Additionally, the worst-case scenario is when all the brackets in the string are balanced, in which case the function will perform n/2 push operations and n/2 pop operations, giving it a space complexity of O(n).

## Solution

<pre>

 ``` python
    def validate_brackets(string):
    stack = []
    for char in string:
        if char in ['(', '{', '[']:
            stack.append(char)
        else:
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if char != ')':
                    return False
            if current_char == '{':
                if char != '}':
                    return False
            if current_char == '[':
                if char != ']':
                    return False
    if stack:
        return False
    return True

 ```
</pre>

