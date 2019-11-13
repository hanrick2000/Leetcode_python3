Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]



DFS模板
注意一下递归出口


code:
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
         #定义一个用过的集合visited
         #注意visited的写法:要建立一个长度为len(nums),值都为False的list
        visited = [False] * len(nums)
            
        self.dfs(nums, visited, [], results)
        
        return results
    
    def dfs(self, nums, visited, temp, results):
        #递归出口:temp的长度
        #因为需要将所有的nums都排序
        if len(nums) == len(temp):
            results.append(list(temp))
        
        for i in range(len(nums)):
            #去重
            #用过了(当前temp里正在用)就跳过
            #对于[1,2,3],当1被加入进了temp,则visited[0]=True;temp后续加第二个值时,就只能在剩余的数(2,3)里面选
            #注意后续需要将visited[0]从新设置为False,因为到后面先将2加入temp时,这时的1应该在备选数据中,而不应在visited中
            if visited[i]:
                continue
                
            #后面的这些部分呈镜像对称
            temp.append(nums[i])
            #用的时候设置为True
            visited[i] = True
            self.dfs(nums, visited, temp, results)
            #用完了需要返回False
            visited[i] = False
            temp.pop()
