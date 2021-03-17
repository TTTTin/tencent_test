
fpre = 1
current_index = 2
current_value = 1
while current_index != 20:
    temp = current_value
    current_value = fpre + current_value
    current_index += 1
    fpre = temp
print(current_value)



def fibo(n,memo):
    if n==0:
        return 0
    if n==1:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = fibo(n-1,memo)+fibo(n-2,memo)
    return memo[n]
memo = {}
print(fibo(20,memo))


fpre = 1
current_index = 2
current_value = 1
while current_value <= 100000:
    temp = current_value
    current_value = fpre + current_value
    current_index += 1
    fpre = temp
print(current_index-1)


#2.a None
#2.b


#3
int2sym=["厘","分","角","元","拾","佰","仟","万","拾","佰","仟","亿"]
int2ch=["零","叁","贰","叁","肆","伍","陆","柒","捌","玖"]

x = "100000000.103"
inte = x.split(".")
#print(inte)
l1 = len(inte[0])
v = 0
#flag = 0
s = ""
for i in range(l1-1,-1,-1):
    s += int2ch[int(x[v])]
    #print(int2ch[int(x[v])],end="")
    v += 1
    s += int2sym[i+3]
    #print(int2sym[i+3],end="")
if len(inte)>1:
    v = 0
    l2 = len(inte[1])
    for i in range(l2):
        s += int2ch[int(inte[1][v])]
        #print(int2ch[int(x[v])],end="")
        v += 1
        s += int2sym[2-i]
        #print(int2sym[2-i],end="")
flag = 0
flag_wan = 0
i = 0
#print(s)
while i < len(s):
    if s[i] == "零":
        #print(s)
        if s[i+1] == "元":
            s = s[0:i] + s[i+1:]
            flag = 1
        elif s[i+1] == "万" and flag_wan == 1:
            s = s[0:i] + s[i+1:]
        else:
            s = s[0:i] + s[i+2:]
        #print(s)
        i=(flag+flag_wan)%2
        continue
    elif i+1 < len(s) and s[i] in int2ch and  s[i+1] != "亿":

        flag_wan = 1
    i+=1
print(s)
#4

def qs(left,right,n):

    if right<=left:
        return left
    p = n[(left+right)//2]
    #print(p)
    l,r = left,right
    while l<=r:

        
        while l<=r and n[l]<p:
            l += 1
        while l<=r and n[r]>p:
            r -= 1
        if l>r:
            break
        n[l],n[r] = n[r],n[l]
        l += 1
        r -= 1
    print(n)
    qs(left,r,n)
    qs(l,right,n)


    

num = [6,1,2,7,9,3,4,5,10,8]

qs(0,len(num)-1,num)
print(num)

#5
# 
# select e.name from employee as e,
# (select employee_id from work where time>"2020-03-01 00:00" and time<"2020-03-01 12:00" group by time) as w
# where e.id == s.id
# 
# 
#from ts
