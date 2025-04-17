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
        
def main():
    
    # read file
    f = open("two_lists.txt","r")

    # setup_variables
    list_one = []
    list_two = []
    list_output = []
    separator = '   '

    # read file, append lists
    for line in f:
        split_line = line.split(separator)
        split_line[-1] = split_line[-1].strip()
        insert_into_list(int(split_line[0]), list_one)
        insert_into_list(int(split_line[1]), list_two)
    
    #  append difference to a single list
    for i in range(0,len(list_one)):
        output = list_one[i] * list_two.count(list_one[i])
        list_output.append(output)

    total = 0
    for item in list_output:
        total += item
    print(total)
    
        
if __name__ == '__main__':
    main()
    