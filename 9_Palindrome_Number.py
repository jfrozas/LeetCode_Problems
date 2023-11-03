class Solution:
    def isPalindrome(self, number: int) -> bool:
        if number == 0:
            return True
            
        if number < 0 or number % 10 == 0:
            return False
        
        reversed_number = 0
        while reversed_number < number:
            reversed_number = reversed_number * 10 + number % 10
            number = number // 10

        return reversed_number == number or (reversed_number // 10) == number