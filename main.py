
"""
Team exercise git
"""
def feature1(word):  
    """
    This feature returns to the user the first letter in the word
    """
    first_char = user_input[0]
    return first_char

def feature2(word):
    """
    This feature returns to the user the second letter in the word
    """
    return word[1]
  
def feature3(word):
    """
    This feature returns the user the first half of the word
    """
    end = int(len(word) / 2)
    print(input[0:end])

def feature4(word):
    """
    This feature returns the user the second half of the word
    """
    half_index = int(len(word) / 2)
    return  word[half_index:]