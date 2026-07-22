class Solution:
    def isPalindrome(self, s: str) -> bool:
        ptr1 = 0
        ptr2 = len(s) - 1

        while ptr1 < ptr2:
            # 1. Skip non-alphanumeric characters from the left
            while ptr1 < ptr2 and not s[ptr1].isalnum():
                ptr1 += 1
            
            # 2. Skip non-alphanumeric characters from the right
            while ptr1 < ptr2 and not s[ptr2].isalnum():
                ptr2 -= 1
            
            # 3. Compare characters after converting to lowercase
            if s[ptr1].lower() != s[ptr2].lower():
                return False

            # 4. Move both pointers inward
            ptr1 += 1
            ptr2 -= 1

        return True
