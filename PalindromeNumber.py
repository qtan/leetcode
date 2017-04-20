class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        n=x
        y=0
        if n<0:
            return False
        while n>0:
            a=n%10
            #print "a" , a
            n=n//10
            #print "this is n" , n
            if n>=0:
                y=y*10+a
                #print "changed y",y
        #print "y",y,"and x",x         
        return y==x