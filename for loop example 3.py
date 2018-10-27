start = int(input('Enter Starting Number:'))
end=int(input('Enter The End Number:'))

print('Number \t')
print('______________________________')

for number in range(start,end+1):
    square=number **2
    print(number,'\t',square)
