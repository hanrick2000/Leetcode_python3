Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?




code:
#坐标型DP
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = [[1] * (i + 1) for i in range(rowIndex + 1)]
        
        for i in range(2, rowIndex + 1):
            for j in range(1, len(dp[i]) - 1):
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
        
        return dp[-1]
    
    
    
Follow up 1: 滚动数组:所有的i/i-1 都%2
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = [[1] * (rowIndex + 1), [1] * (rowIndex + 1)]
        
        for i in range(2, rowIndex + 1):
            #这里不再是dp的length了,而是i;注意也不是i+1,因为最后一位不需要计算
            for j in range(1, i):
                dp[i % 2][j] = dp[(i - 1) % 2][j - 1] + dp[(i - 1) % 2][j]
                index = i
        
        #注意不再是取最后一行
        return dp[rowIndex % 2]
        
        
Follow up 2: 给出制定坐标(a,b)的值
class Solution:
    def getRow(self, rowIndex) -> List[int]:
        if a < 0 or b < 0 or b > a:
            return None
        
        a = rowIndex
        b = 3
        
        dp = [[1] * (a + 1), [1] * (a + 1)]
        
        for i in range(2, a + 1):
            for j in range(1, i):
                dp[i % 2][j] = dp[(i - 1) % 2][j] + dp[(i - 1) % 2][j - 1]
        
        print(dp[a % 2][b])
