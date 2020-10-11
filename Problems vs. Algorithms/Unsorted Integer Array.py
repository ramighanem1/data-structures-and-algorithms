def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) == 0:
        return None
    
    min_num = float("inf")
    max_num = float("-inf")
    
    for num in ints:
        if num > max_num:
            max_num=num
        if num < min_num:
            min_num=num
            
    return min_num,max_num
    

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
