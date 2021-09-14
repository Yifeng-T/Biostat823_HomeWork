import math

def sum_CuriousNum():
    """sum of all numbers which are equal to the sum of the factorial digits"""
    
    #we construct a dictionary for the factorial of each possible digit, so we do not need to calculate it in the loop
    digit_fac = {0:1, 1:1, 2:2, 3:6, 4:math.factorial(4), 5:math.factorial(5), 6:math.factorial(6), \
        7:math.factorial(7), 8:math.factorial(8), 9:math.factorial(9)}
    
    # the output variable, storing the sum of all numbers
    result = 0
    
    # by observation, we find the max digits only could be 7.
    low_bound = 3
    up_bound = math.factorial(9)*7

    for i in range(low_bound, up_bound):
        item = i
        digit_sum = 0 # initialize the sum of all digits of the target number
        
        # we find the reminder of target number divided by 10 each time to find the digit number.
        while item >= 1: 
            remin = item % 10
            digit_sum += digit_fac[remin]
            item = item // 10 # get the integer part
        if i == digit_sum:
            result += i
            print(f"one of the majic number is {i}")
    print(result)
    return result

if __name__ == '__main__':
    sum_CuriousNum()



