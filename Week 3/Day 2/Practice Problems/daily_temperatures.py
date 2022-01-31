class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #Solution 1
        #answer = [0] * len(temperatures)
        #stack = []
        #for currDay in range(len(temperatures)):
        #    if len(stack) != 0:
        #        while len(stack) != 0 and temperatures[currDay] > temperatures[stack[-1]]:
        #            answer[stack[-1]] = currDay - stack[-1]
        #            stack.pop()
        #    stack.append(currDay)
        #return answer
        
        #Solution 2
        answer = [0] * len(temperatures)
        hottest = 0
        for currDay in range(len(temperatures) - 1, -1, -1):
            if temperatures[currDay] >= hottest:
                hottest = temperatures[currDay]
            else:
                days = 1
                while temperatures[currDay + days] <= temperatures[currDay]:
                    days += answer[currDay + days]
                answer[currDay] = days
        return answer