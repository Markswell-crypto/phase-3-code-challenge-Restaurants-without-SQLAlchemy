def is_balanced(expression):
    stack = []
    opening_brackets = "({["
    closing_brackets = ")}]"

    for char in expression:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if len(stack) == 0:
               return False
            if char == ')' and stack.pop() != '(':
               return False
            if char == '}' and stack.pop() != '{':
               return False
            if char == ']' and stack.pop() != '[':
               return False

    return not stack

# sample input = 
expression1 = "([]{})"
expression2 = "([)]"
print(is_balanced(expression1))  # Output: True
print(is_balanced(expression2))  # Output: False 


def remove_duplicates(sequence):
    stack = set()
    result = []
    for item in sequence:
        if item not in stack:
            stack.add(item)
            result.append(item)
    return result

# sample input = 
input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = remove_duplicates(input_sequence)
print(result)  # Output: [2, 3, 4, 5, 6, 7]

import string

def word_frequency(sentence):
    sentence = sentence.lower()
    sentence = sentence.translate(str.maketrans('', '', string.punctuation))
    words = sentence.split()    
    frequency_dict = {}
    
    for word in words:
        if word in frequency_dict:
           frequency_dict[word] += 1
        else:
           frequency_dict[word] = 1

    return frequency_dict

# sample input = 
sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)
