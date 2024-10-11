#Pyramid
num = int(input("Enter Number : "))
col = 0
row = (num-1)
for x in range(num):
    pyramid = (" "*row) + "*" +"*"*(2*col)
    col += 1
    row -= 1
    print(pyramid)