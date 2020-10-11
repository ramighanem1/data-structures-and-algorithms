def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if len(input_list) <= 1:
        return input_list
    
    input_list = sorted(input_list)
    left=''
    wright=''
    
    for indx,num in enumerate(input_list):
        if indx%2==0:
            left=str(num)+left
        else:
            wright=str(num)+wright

    return [int(left),int(wright)]




def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

print('Normal Cases:')
print('Test 1:')
list_num = [1, 2, 3, 4, 5]
result = rearrange_digits(list_num)
if result == [531, 42]:
    print('Pass \n')
else:
    print("Fail \n")

print('Test 2:')
list_num = [4, 6, 2, 5, 9, 8]
result = rearrange_digits(list_num)
if result == [852, 964]:
    print('Pass \n')
else:
    print("Fail \n")

print('Test 3:')
list_num = [1, 2, 3]
result = rearrange_digits(list_num)
if result == [31, 2]:
    print('Pass \n')
else:
    print("Fail \n")

# Edge cases
print('Edge Cases:')
print('Test 4:')
list_num = [1, 1, 1]
result = rearrange_digits(list_num)
if result == [11, 1]:
    print('Pass \n')
else:
    print("Fail \n")

print('Test 5:')
list_num = [1]
result = rearrange_digits(list_num)
if result == [1]:
    print('Pass \n')
else:
    print("Fail \n")

print('Test 6:')
list_num = []
result = rearrange_digits(list_num)
if result == []:
    print('Pass \n')
else:
    print("Fail \n")
