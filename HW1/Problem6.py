import numpy as np


def calculate():
    #BUild the array contains first 100 natural numbers
    origin = np.arange(1, 101, dtype = int)
    
    # sum_sq contains the sum of the squares
    sum_sq = sum(origin**2)

    # sq_sum contains the square of the sums
    sq_sum = sum(origin)**2

    print(f"sum of square is {sum_sq}, and square of sum is {sq_sum}, the differennce is {sq_sum-sum_sq}")
    return (sq_sum-sum_sq)


if __name__ == '__main__':
    calculate()




