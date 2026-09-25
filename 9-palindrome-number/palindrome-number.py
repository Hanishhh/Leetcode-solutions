class Solution:
    def isPalindrome(self,x):
        if x<0:
            return False
        store=0
        original=x
        while x!=0: 
            rev=x%10
            store=(store*10)+rev
            x=x//10
        if original==store:
            return True
        else:
            return False