class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        h1, h2 = {} , {}

        for i in range(len(s1)):
            h1[s1[i]] = h1.get(s1[i],0) + 1
            h2[s2[i]] = h2.get(s2[i],0) + 1

        if h1 == h2:
            return True

        i = 0
        j = len(s1)

        while j < len(s2):
            h2[s2[j]] = h2.get(s2[j],0)+1
            h2[s2[i]] -= 1
            if h2[s2[i]] == 0:
                del h2[s2[i]]
            if h1 == h2:
                return True
            i += 1
            j += 1
        
        return False

        