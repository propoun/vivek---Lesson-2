#find if the number entered by the user is a panagram or not
numString = input('enter the number: ' )
numCount = {
    '1' : 0,
    '2' : 0,
    '3' : 0,
    '4' : 0,
    '5' : 0,
    '6' : 0,
    '7' : 0,
    '8' : 0,
    '9' : 0,
}
for num in numString:
    if num in numCount:
       numCount[num] += 1 

print (numCount)

panagram = True
for count in numCount.values():
    if count == 0:
        panagram = False

if panagram:
    print('Entered Number is a panagram')
    print (numCount)
else:
    print('Entered Number is not a panagram')
    print (numCount)