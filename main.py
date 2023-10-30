def check(num):
    num=str(num)
    c2,c4,c8=0,0,0
    c2=num.count('2') 
    c4=num.count('4') 
    c8=num.count('8') 
    return c2>0 and c4==c8 and c4==c2

n=int(input())
count = 0
for i in range (1, n+1) :
    if check(i):
        count += 1
        print(i)
print(count)
