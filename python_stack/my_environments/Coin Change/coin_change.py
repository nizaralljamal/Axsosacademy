import unittest

# --- The Function to be Tested ---
# --- الدالة المطلوب اختبارها ---
def coin(cents):
    """
    Calculates the minimum number of coins (quarters, dimes, nickels, pennies)
    for a given amount of cents using a greedy approach.
    
    تحسب أقل عدد من العملات المعدنية (أرباع، دايمات، نيكل، بنسات)
    لمبلغ معين من السنتات باستخدام نهج طماع.
    """
    if not isinstance(cents, int) or cents < 0:
        return "Input must be a non-negative integer."

    coins = []
    
    # 1. Quarters (25)
    quarters = cents // 25
    coins.append(quarters)
    remaining_cents = cents % 25
    
    # 2. Dimes (10)
    dimes = remaining_cents // 10
    coins.append(dimes)
    remaining_cents %= 10 # Shortcut for: remaining_cents = remaining_cents % 10
    
    # 3. Nickels (5)
    nickels = remaining_cents // 5
    coins.append(nickels)
    remaining_cents %= 5
    
    # 4. Pennies (1)
    pennies = remaining_cents
    coins.append(pennies)
    
    return coins

# --- The Test Cases ---
# --- حالات الاختبار ---
class CoinChangeTests(unittest.TestCase):
    # Test 1: The example from the problem
    def test_example_87(self):
        self.assertEqual(coin(87), [3, 1, 0, 2])

    # Test 2: A value that uses all coin types
    def test_all_coins_41(self):
        self.assertEqual(coin(41), [1, 1, 1, 1])

    # Test 3: A value that is a perfect number of quarters
    def test_perfect_quarters_100(self):
        self.assertEqual(coin(100), [4, 0, 0, 0])

    # Test 4: A small value with only pennies
    def test_only_pennies_4(self):
        self.assertEqual(coin(4), [0, 0, 0, 4])

    # Test 5: A value with no quarters
    def test_no_quarters_24(self):
        self.assertEqual(coin(24), [0, 2, 0, 4])

    # Test 6: The edge case of zero
    def test_zero_cents(self):
        self.assertEqual(coin(0), [0, 0, 0, 0])

# This allows the tests to be run from the command line
# هذا يسمح بتشغيل الاختبارات من سطر الأوامر
if __name__ == '__main__':
    unittest.main()