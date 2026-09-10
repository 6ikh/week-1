# add code below ...
#defining function palindrome
def palindrome(word):
#converting the word to lower case, removing any spaces, commas, and periods from it
    word = word.lower()
    word = word.replace(" ", "")
    word = word.replace(",", "")
    word = word.replace(".", "") 
#reverse the string and store it in word   
    return word == word[::-1] 
#checking each word 
#print(palindrome("racecar"))
#print(palindrome("Nurses Run"))
#print(palindrome("Sit on a potato pan, Otis."))

#defining function parentheses 
def parentheses(sequence):
#start counter at 0
    count = 0
#for every char in the sequence, add a 1 to counter if there's (
#subtract -1 for every ) in the sequence, if it becomes negative then return false
    for char in sequence:
        if char == "(":
            count += 1
        elif char == ")":
            count -= 1
        
        if count < 0:
            return False
#return count 0 so there isnt any unmatched parentheses left     
    return count == 0
#checking each sequence
#print(parentheses("((blah)()()())"))
#print(parentheses("(((())blee))"))
#print(parentheses("(()hello((())()))"))
#print(parentheses("((((((())"))
#print(parentheses("()))"))