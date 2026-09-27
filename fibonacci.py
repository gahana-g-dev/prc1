
y=int(input("Enter the limit for fibonacci:"))
a=1
b=1

print(a)
print(b)

x=1
while x<=y-2:
    c=a+b
    print(c)
    a=b
    b=c
    x=x+1
