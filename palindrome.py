n = input("Enter the word \n").lower()
r=""
for i in n:
    r=i+r

if n == r:
    print("Palindrome")
else:
    print("Not a palindrome")
