s = input()

m = 0
for x in range(0,len(s)+1):
    for y in range(x,len(s)+1):
        ss = s[x:y]
        a = ss.count("A")
        c = ss.count("C")
        g = ss.count("G")
        t = ss.count("T")
        if a + c + g + t == len(ss):
            if m < len(ss):
                m = len(ss)
print(m)