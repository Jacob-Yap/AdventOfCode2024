import re

mulpattern = "mul\(\d{1,3},\d{1,3}\)"

def parse_mulpattern(mul_thing):
    inside = mul_thing[4:-1]
    inside = inside.split(',')
    return int(inside[0]) * int(inside[1])

def main():
    total = 0
    f = open("corruptfile.txt","r")
    for line in f:
        line_result = re.findall(mulpattern,line)
        for item in line_result:
            total += parse_mulpattern(item)
    
    print(total)
    
    
if __name__ == '__main__':
    main()