# check the numbers is binary ot not
n=int(input('enter the number=:\n'))
while n>0:
    m=n%10
    if m!=0 and m!=1:
        print('not a binary number')
        break
    n = n // 10
    if m==0:
        print('Binary')