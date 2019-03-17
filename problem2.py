l = [1, 2]
t, c = 2, 0
for n in range(4000000):
    z = l[-2] + l[-1]
    if z < 4000000:
        if z % 2 == 0:
            t += z
        l.append(z)
print (l)
print ("total:", t)
