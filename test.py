s = "hello world"
for x in s[:].split():
    print(x)
    s = s.replace(x, x.capitalize())
print (s)