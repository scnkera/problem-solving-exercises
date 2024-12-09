def merge_lists(list1, list2):
    i = 0 # index of list1
    j = 0 # index of list2
    merged_list = []

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
            
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1

    while j < len(list2):
        merged_list.append(list2[j])
        j += 1
    
    print(merged_list)
    return merged_list