class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        if int(x)>=0:
            b=int(str(int(x))[::-1])
            if b >= 2147483647:
                return 0
            else:
                return b
        else:
            b=int(str(-1*int(x))[::-1])
            if b >= 2147483648:
                return 0
            else:
                return -b
       