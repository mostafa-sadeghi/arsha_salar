# 0th
#10th
#100th
# 1st
# 2nd
# 3rd

# 11th
# 211th
# 12th
# 312th
# 13th
# 513th
#4th
#546th
# print(100 % 10)
# print(102 % 10)



number = int(input("enter a number: "))
def ordinal_suffix(number):
    if number % 100 in(11,12,13):
        print(f'{number}th')
    elif number % 10 == 0:
        print(f'{number}th')
    elif number % 10 == 1:
        print(f'{number}st')
    elif number % 10 == 2:
        print(f'{number}nd')
    elif number % 10 == 3:
        print(f'{number}rd')
    else:
        print(f'{number}th')

ordinal_suffix(number)