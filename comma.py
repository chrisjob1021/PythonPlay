def comma(s):
    n = len(s)
    print s
    return comma(s[:n-3]) + "," + s[n-3:]


comma("1234")
