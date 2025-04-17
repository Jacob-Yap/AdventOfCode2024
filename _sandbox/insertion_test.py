def insert_into_list(item, list):
    i = 0
    # if an empty list, append.
    if len(list) == 0:
        list.append(item)
    # if not an empty list, run insertion
    else:
        while i < len(list):
            if item < list[i]:
                list.insert(i,item)
                return(f"placed item {item} at index {i}")
            i += 1
            
        # if we reach the end of the list, append
        list.append(item)
        return (f"placed item {item} at index {i}")

test_list = [1,5,2,3,7,10,123,405,221]
output_list = []

for item in test_list:
    insert_into_list(item,output_list)

print(output_list)