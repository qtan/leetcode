class Solution(object):
  def longestCommonPrefix(self, strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if not strs: return ""
    
    commStr = strs[0]
    for i in range(1,len(strs)):
        lenTmp = 0
        lenIMin = min(len(strs[i]),len(commStr))
        
        while lenTmp < lenIMin and strs[i][lenTmp] == commStr[lenTmp]:
            lenTmp += 1
           
        commStr = strs[i][0:lenTmp]
    
    return commStr