import unittest

# 2
def is_palindrome(word):
    reversed_word = ""
    for i in range(len(word)-1,-1,-1):
        reversed_word += word[i]
    return reversed_word == word

print(is_palindrome("aba"))  
print(is_palindrome("word"))    

# 1
def reverseList(lst):
    for i in range(len(lst) //2 ):
        lst[i],lst[len(lst)-i-1] = lst[len(lst)-i-1],lst[i]
    return lst    
print(reverseList([1,2,3,4]))

# 4
def factorial(n):
    if n == 1:
        return 1
    fac = n* factorial(n-1)
    return fac  
print(factorial(5))
# 3
def coins(cents):
    if cents == 0:
        return 0
    quarters = cents //25 
    cents -= quarters*25
    dimes = cents //10
    cents -= dimes*10
    nickles = cents // 5
    cents -= nickles*5
    pennies = cents
    return [quarters,dimes,nickles,pennies]
print(coins(92))

# 5
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(5))
print(fibonacci(6))

class Test(unittest.TestCase):
    def test_palindrome(self):
        self.assertEqual(is_palindrome("aba"),True)
        self.assertEqual(is_palindrome("word"),False)

    def test_reverseList(self):
        self.assertEqual(reverseList([1,2,3,4]),[4,3,2,1])
        self.assertEqual(reverseList([4,3,2,1]),[1,2,3,4])
        self.assertEqual(reverseList([4,3,2,1]),[1,2,3,5])

    def test_factorial(self):
        self.assertEqual(factorial(5),120)    
        self.assertEqual(factorial(4),120)  

    def test_fibonacci(self):
        self.assertEqual(fibonacci(5),5)
        self.assertEqual(fibonacci(4),3)
        self.assertEqual(fibonacci(6),8)
    def test_coins(self):
        self.assertEqual(coins(92), [3, 1, 1, 2])

    def test_coins_0(self):
        self.assertEqual(coins(0), [0, 0, 0, 0])

    def test_coins_99(self):
        self.assertEqual(coins(99), [3, 2, 0, 4])

if __name__ == '__main__':
    unittest.main()