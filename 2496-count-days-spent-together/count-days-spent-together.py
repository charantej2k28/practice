
class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        def to_days(date):
            month_days = [31, 28, 31, 30, 31, 30,
                          31, 31, 30, 31, 30, 31]

            month, day = map(int, date.split("-"))
            return sum(month_days[:month - 1]) + day

        start = max(to_days(arriveAlice), to_days(arriveBob))
        end = min(to_days(leaveAlice), to_days(leaveBob))

        return max(0, end - start + 1)
