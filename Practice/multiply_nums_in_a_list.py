def product_of_nums_in_list(num_list):
    product = 1
    for num in num_list:
        product = product * num

    return product

num_list = [8, 2, 3, -1, 7]
print(product_of_nums_in_list(num_list))