def assess_report(report: list) -> str:
    
    # determine direction, positive or negative
    direction = None
    direction_result = int(report[0]) - int(report[1])
    if direction_result > 0:
        direction = 'Negative'
    elif direction_result < 0:
        direction = 'Positive'
    elif direction_result == 0:
        return('Unsafe - No difference')
    
    # start looping
    value = int(report[0])
    for i in range(1,len(report)):
        difference = value - int(report[i])
        abs_difference = abs(difference)
        # if the levels differ by more than 3, or less than 1, mark as unsafe
        if abs_difference > 3 or abs_difference < 1:
            return(f'Unsafe - difference between {value} and {int(report[i])} is too large/small')
        # if levels are not all increasing or all decreasing, mark as unsafe
        elif (difference > 0 and direction == 'Positive') or (difference < 0 and direction == 'Negative'):
            return(f'Unsafe - direction is set to {direction} but difference is {0 - difference}')
        value = int(report[i])
        
    # else, return safe.
    return('Safe')
    
    


def main():
    
    # read file
    f = open("levels.txt","r")

    # setup_variables
    list_reports = []
    list_safety = []
    separator = ' '

    # read file, append lists
    for line in f:
        split_line = line.split(separator)
        split_line[-1] = split_line[-1].strip()
        list_reports.append(split_line)
    
    for report in list_reports:
        list_safety.append(assess_report(report))
    
    print(list_safety.count("Safe"))
        
        
        
if __name__ == '__main__':
    main()