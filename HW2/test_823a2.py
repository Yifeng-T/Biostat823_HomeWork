from HW2 import findprime
from HW2 import SlidWind
from HW2 import ExpMath
from sympy import *

def test_prime():
    Test1 = SlidWind(E, 10)
    Test2 = SlidWind(pi, 4)

    Test3 = findprime(11)
    Test4 = findprime(120)

    Test5 = ExpMath(pi, 4)
    Test6 = ExpMath(E, 10)
    Test7 = ExpMath(12345, 3)

    assert Test1 == 7427466391
    assert Test2 == 4159

    assert Test3 == True
    assert Test4 == False

    assert Test5 == "3141"
    assert Test6 == "2718281828"
    assert Test7 == "123"

if __name__ == '__main__':
    test_prime()
    print("pass the all tests")
