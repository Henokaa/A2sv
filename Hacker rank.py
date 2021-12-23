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