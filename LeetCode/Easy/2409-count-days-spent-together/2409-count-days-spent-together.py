class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        def convert_days(month_day):
            month, day = map(int, month_day.split('-'))
            return sum(days[:month-1]) + day
        
        val = - max(convert_days(arriveAlice), convert_days(arriveBob)) + min(convert_days(leaveBob), convert_days(leaveAlice)) + 1

        return val if val > 0 else 0