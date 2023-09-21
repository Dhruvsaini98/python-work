def remove_duplicates(input_list):
    unique_elements = set()
    new_list = []
    
    for item in input_list:
        if item not in unique_elements:
            unique_elements.add(item)
            new_list.append(item)
    
    return new_list

# Test case
original_list = [1, 2, 2, 3, 4, 3, 5, 6, 5]
result_list = remove_duplicates(original_list)
print(result_list)  # Output: [1, 2, 3, 4, 5, 6]
