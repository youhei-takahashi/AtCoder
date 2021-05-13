import itertools,sys
s1 = input()
s2 = input()
s3 = input()

strlist = set(list(s1 + s2 + s3))
l = len(strlist)

if l > 10:
    print("UNSOLVABLE")
else:
    P = range(0,10)
    for p in itertools.permutations(P,l):
        x = dict(zip(strlist,p))
        if x[s1[0]] == 0 or x[s2[0]] == 0 or x[s3[0]] == 0 :continue
        if x[s3[-1]] == (x[s2[-1]] + x[s1[-1]])%10: # TLE回避(末尾だけチェック)
            ss1 = 0
            ss2 = 0
            ss3 = 0
            ba = 1
            bb = 1
            bc = 1
            for k in list(s1[::-1]):
                ss1 += x[k] * ba
                ba *= 10
            for l in list(s2[::-1]):
                ss2 += x[l] * bb
                bb *= 10
            for m in list(s3[::-1]):
                ss3 += x[m] * bc
                bc *= 10
            if ss1 + ss2 == ss3:
                print(ss1)
                print(ss2)
                print(ss3)
                break
    else:
        print("UNSOLVABLE")
