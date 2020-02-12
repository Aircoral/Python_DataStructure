#若a+b+c=1000,且a^2+b^2=c^2(a,b,c为自然数)，如何求出所有a、b、c的组合？

import time
start_time = time.time()
#01.枚举法
for a in range (0,1001):
    for b in range (0,1001):
        for c in range (0,1001):
            if a+b+c==1000 and a**2+b**2==c**2:
                print ("a, b, c: %d, %d, %d" % (a, b, c))
#执行时间：T=1000 * 1000 * 1000 * 2
#        T= 2000 * 2000 * 2000 *2
#        T= N * N * N *2
# T(n) = N^3 *2
# T(n) = N^3 *10
# T(n) = g(n) = N^3
# 时间复杂度：O(n^3) //大O表示法

for a in range (0,1001):
    for b in range (0,1001):
        c = 1000-a-b
        if a**2+b**2==c**2:
            print ("a, b, c: %d, %d, %d" % (a, b, c))

#T(n) = g(n) =N^2+2
#  O(n^2)

end_time = time.time()

print("time:%d" % (end_time - start_time))
print ("finished")
