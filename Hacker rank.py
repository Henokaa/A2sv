num = int(input())
d = {}
for i in range(num) :
    line = input().split()
    d[line[0]] = list(map(float, line[1:]))
name = input()
sum = sum(d[name])
sum = sum/(len(d[name]))
print("%.2f" % sum)


#string split and join

def split_and_join(line):
    # write your code here
    
    
    line = line.split(" ")
    line = "-".join(line);
    return line
if __name__ == '__main__':

# set.add()
length = int(input())
data = set()

for i in range(0, length):
    data.add(input())
    
print (len(data))

# set.union 

n=input()
s1=set(map(int, input().split()))
n=input()
s2=set(map(int, input().split()))
print (len(s1.union(s2)))

# check sumbit
for _ in range(int(input())):
    x, a, z, b = input(), set(input().split()), input(), set(input().split())
    print(a.issubset(b))

# itertools.product
from itertools import product
a = map(int, input().split())
b = map(int, input().split())

print(*product(a, b))

#pilling
for t in range(int(input())):
    input()
    lst = [int(i) for i in input().split()]
    min_list = lst.index(min(lst))
    left = lst[:min_list]
    right = lst[min_list+1:]
    if left == sorted(left,reverse=True) and right == sorted(right):
        print("Yes")
    else:
        print("No")
