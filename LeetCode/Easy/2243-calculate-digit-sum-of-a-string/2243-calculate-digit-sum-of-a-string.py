class Solution:
    def digitSum(self, s: str, k: int) -> str:
        n = len(s)
        curr_total = 0
        new_string = ''
        i = 0
        while len(s) > k:
            curr_total += int(s[i])
            is_last_digit = i == len(s) - 1

            if (i + 1) % k == 0 or is_last_digit:
                new_string += str(curr_total)
                curr_total = 0
            
            if is_last_digit:
                s = new_string
                new_string = ''
                i = 0
            
            else:
                i += 1
        
        return s
            
