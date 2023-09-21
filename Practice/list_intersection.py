def common_elements(list1, list2):
    list3 = []
    for e in list1:
        if e in list2:
            list3.append(e)
    return list3

list1 = [1,2,3,4,500,64,67,45,400]
list2 = [2,3,500,98,100,67,400]
new_list = common_elements(list1, list2)
print(new_list)
