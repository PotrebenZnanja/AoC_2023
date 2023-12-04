with open("input/day_01.txt","r") as f:
    data = f.read()

data = data.split("\n")


num = {"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
num_reverse = {}
for k,v in num.items():
    num_reverse[k[::-1]]=v

vs = 0
for x in data:
    vs_1 = ""
    #print(x)
    for i in range(0,len(x)):
        if x[i]>='0' and x[i]<='9':
            vs_1+=x[i]
            #print(int(x[i]),x )
            break
    for i in range(len(x)-1,-1,-1):
        if x[i]>='0' and x[i]<='9':
            vs_1+=x[i]
            #print(int(x[i]),x)
            break
    vs+=int(vs_1)
print(vs)
#part II
vs=0
for x in data:
    vs_1 = ""
    lowest_pair=[len(x),0] #index, number
    for n in num:
        found = x.find(n)
        if lowest_pair[0]>found and found!=-1:
            lowest_pair = [found,num[n]]
    for i in range(0,len(x)):
        if i == lowest_pair[0]:
            vs_1 += str(lowest_pair[1])
            break
        if x[i]>='0' and x[i]<='9':
            vs_1+=x[i]
            break
    lowest_pair=[len(x),0]
    x = x[::-1]
    for n in num_reverse:
        found = x.find(n)
        if lowest_pair[0]>found and found!=-1:
            lowest_pair = [found,num_reverse[n]]
    for i in range(0,len(x)):
        if i == lowest_pair[0]:
            vs_1 += str(lowest_pair[1])
            break
        if x[i]>='0' and x[i]<='9':
            vs_1+=x[i]
            break
    
    vs+=int(vs_1)
    print(x[::-1])
    print(vs_1)
print(vs)
#part II
