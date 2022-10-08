print("-----------------------")
print("-------FIBONACCI-------")
print("-----------------------")
#processing
a = 1
b = 2
c = a + b
while c < 1000:
    print(a,"+",b ,"=", c)
    a = b
    b = c
    c = a + b
