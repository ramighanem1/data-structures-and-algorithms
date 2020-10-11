def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    list0=[]
    list1=[]
    list2=[]
    for x in input_list:
        if x==0:
            list0.append(0)
        elif x==1:
            list1.append(1)
        else:
            list2.append(2)

    final_list=list0+list1+list2
    return final_list
    
            
            

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

print('Normal Cases:')
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
print('\n')

print('Edge Cases:')
test_function([0, 1, 1, 0, 1])
test_function([0, 0, 0])
test_function([])
