def isAnagram1(s, t):
    dic1, dic2 = {}, {}
    for item in s:
        dic1[item] = dic1.get(item, 0) + 1
        print dic1
    for item in t:
        dic2[item] = dic2.get(item, 0) + 1
        print dic2
    return dic1 == dic2

def isAnagram2(s, t):
    dic1, dic2 = [0]*26, [0]*26
    print dic1
    print dic2
    # ord('a') returns 97
    for item in s:
        dic1[ord(item)-ord('a')] += 1
    for item in t:
        dic2[ord(item)-ord('a')] += 1
    return dic1 == dic2

s = "anagram"
t = "nagaram"
print isAnagram1(s, t)
print isAnagram2(s, t)

print sorted(s) 
print sorted(t)