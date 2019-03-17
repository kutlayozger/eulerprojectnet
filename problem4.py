n = range(100, 999)
l = 0
for i in n:
    for j in n:
        z = i * j
        s = str(z)
        if len(s) == 6:
            if (s == s[::-1]):
                if l < s:
                    l = s
                print("s:", s)
print ("solution:", l)
