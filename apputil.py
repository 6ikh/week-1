

# add code below ...

def palindrome(word):
    word = word.lower()
    word = word.replace(" ", "")
    word = word.replace(",", "")
    word = word.replace(".", "") 
    
    return word == word[::-1] 

print(palindrome("racecar"))
print(palindrome("Nurses Run"))
print(palindrome("Sit on a potato pan, Otis."))

def parentheses(sequence):
    count = 0
    
    for char in sequence:
        if char == "(":
            count += 1
        elif char == ")":
            count -= 1
        
        if count < 0:
            return False
    
    return count == 0

print(parentheses("((blah)()()())"))
print(parentheses("(((())blee))"))
print(parentheses("(()hello((())()))"))
print(parentheses("((((((())"))
print(parentheses("()))"))