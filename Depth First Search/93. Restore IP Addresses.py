Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]


code:
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if not s:
            return []
        
        
        result = []
        self.dfs(s, 0, result, [])
        
        return result
    
    def dfs(self, s, index, result, path):
        #当所有的s都遍历过,并且path的长度为4
        if index == len(s) and len(path) == 4:
            result.append('.'.join(path))
            return
        
        #当path长度超过4,说明这个s被分为超过4部分,则不成立
        if len(path) > 4:
            return
        
        #数字最多3位
        for i in range(index, index + 3):
            #所有的s都遍历过了
            if i > len(s) - 1:
                break
            
            #string,num代表当前需要被加入path的值
            string = s[index:i+1]
            num = int(string)
            
            #当值不在范围内0～255
            if num > 255:
                break
            
            #当第一个为0开头的,即corner case eg:011,不成立
            if i > index and s[index] == '0':
                break
            
            path.append(string)
            self.dfs(s, i+1, result, path)
            path.pop()
            
