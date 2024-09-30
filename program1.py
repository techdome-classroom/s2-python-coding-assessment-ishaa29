def is_valid(s: str) -> bool:
    # Create a stack to hold the opening brackets
    stack = []
    
    # Create a mapping of closing brackets to their corresponding opening brackets
    bracket_map = {')': '(', '}': '{', ']': '['}
    
    # Iterate through each character in the string
    for char in s:
        # If the character is a closing bracket
        if char in bracket_map:
            # Pop from the stack if it's not empty; otherwise use a dummy value
            top_element = stack.pop() if stack else '#'
            
            # Check if the popped bracket matches the current closing bracket
            if bracket_map[char] != top_element:
                return False
        else:
            # If it's an opening bracket, push it onto the stack
            stack.append(char)
    
    # Return true if the stack is empty (all brackets matched), false otherwise
    return not stack

# Test cases
print(is_valid("()"))       # Output: True
print(is_valid("()[]{}"))   # Output: True
print(is_valid("(]"))       # Output: False
print(is_valid("{[]}"))     # Output: True
print(is_valid("([)]"))     # Output: False







    



  

