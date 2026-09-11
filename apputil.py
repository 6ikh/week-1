# add code below ...
# defining function palindrome
def palindrome(word):
    """_summary_

    Args:
        word (_type_): _description_

    Returns:
        _type_: _description_
    """
    # converting the word to lower case, removing any spaces, commas, and periods from it
    word = word.lower()
    word = word.replace(" ", "")
    word = word.replace(",", "")
    word = word.replace(".", "")
    # reverse the string and store it in word   
    return word == word[::-1]


# defining function parentheses 
def parentheses(sequence):
    """_summary_

    Args:
        sequence (_type_): _description_

    Returns:
        _type_: _description_
    """
    # start counter at 0
    count = 0
    # for every char in the sequence, add a 1 to counter if there's (
    # subtract -1 for every ) in the sequence, if it becomes negative then return false
    for char in sequence:
        if char == "(":
            count += 1
        elif char == ")":
            count -= 1
        if count < 0:
            return False
    # return count 0 so there isnt any unmatched parentheses left     
    return count == 0