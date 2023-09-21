def second_largest(num_list):
    # Sort the list in descending order without modifying the original list
    sorted_list = sorted(num_list, reverse=True)
    
    # Get the second-largest element (if available)
    if len(sorted_list) >= 2:
        second_l = sorted_list[1]
        return second_l
    else:
        # Handle the case when the list has less than two elements
        return None

num_list = [2, 3, 56, 67, 500, 1234, 567, 893, 1000]

s_l = second_largest(num_list)

print(s_l)
