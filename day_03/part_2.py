import re

# captures mul(x,y), do() and don't() text
mulpattern = "mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"

# returns the two numbers in mul(x,y) multiplied
def parse_mulpattern(mul_thing):
    inside = mul_thing[4:-1]
    inside = inside.split(',')
    return int(inside[0]) * int(inside[1])

def main():
    total = 0
    mul_enable = True
    f = open("corruptfile.txt","r")
    for line in f:
        # get a list of all texts that match the mulpattern
        line_result = re.findall(mulpattern,line)
        # add the mul total if mul_enable is True, otherwise skip
        for item in line_result:
            if item == 'do()':
                mul_enable = True
            elif item == "don't()":
                mul_enable = False
            else:
                if mul_enable:
                    total += parse_mulpattern(item)
    
    print(total)
    
    
if __name__ == '__main__':
    main()