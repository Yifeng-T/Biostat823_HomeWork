#problem 206
# the time efficiency of the function is terrible *.*. It requires approximate 3mins to get the output
def find_num(l):
    """find out the unique number"""
    
    # variable number is to store the unique number
    number = 0
    
    forma = "23456789"
    
    for j in range(0, len(a)-1):
        index = a[j]
        
        # convert the number to string, easy to find out the speficif digit
        s = str(index**2)
        less_index = s[2]+s[4]+s[6]+s[8]+s[10]+s[12]+s[14]+s[16]
        
        if less_index == forma:
            number = a[j]
    print(f"number is {number} and its square is {number**2}")
    return number

if __name__ == '__main__':
    
    #based on problem, here is the lower bound and upper bound for searching range:
    minn = int(1020304050607080900**0.5)
    maxx = int(1929394959697989900**0.5)+1
    
    # list a is to store the whole group of possible target unique numbers.
    a = []
    for i in range(minn, maxx+1):
        
        # convert the number to string
        obj = str(i)
        if obj[9] == '0':
            if obj[8] == '3' or obj[8] == '7':
                a.append(i)
    find_num(a)