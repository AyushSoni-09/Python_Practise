def sort(s):
    s_ch=sorted(s)
    s_s = "".join(s_ch)
    return s_s

def isAnagram(s , t):
    if len(s) != len(t):
        return False
    s = sort(s)
    t = sort(t)
    for i in range (len(s)):
        if s[i] != t[i]:
            return False
    
    return True
    
s="silent"
t="listen"
print(isAnagram(s,t))
