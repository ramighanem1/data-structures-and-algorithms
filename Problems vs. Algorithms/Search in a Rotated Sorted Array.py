
def binary_search(input_list, number, start_index, end_index):
     
    if start_index > end_index:
        return -1
    
    m_index = (start_index + end_index) // 2
    if input_list[m_index] == number:
        return m_index

    index1 = binary_search(input_list, number, start_index, m_index - 1)
    index2 = binary_search(input_list, number, m_index + 1, end_index)

    if (index1!=-1):
        return index1
    else: 
         return index2
    
    


def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
   
    return  binary_search(input_list,number,0,len(input_list)-1)

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[6], 6])
test_function([[6], 2])

