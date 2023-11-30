def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    num1_dict = {num:str(num1).count(num) for num in str(num1)}
    num2_dict = {num:str(num2).count(num) for num in str(num2)}
    # print (num1_dict)
    # print (num2_dict)
    return num1_dict == num2_dict
    #return {l:lower_phrase.count(l) for l in lower_phrase if l in 'aeiou'}