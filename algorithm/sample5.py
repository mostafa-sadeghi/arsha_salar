#  اگر تعداد دفعات تکرار دقیقا مشخص باشد، بهتر است از حلقه فور استفاده شود
# t = 0
# for i in range(3):
#     n = float(input('enter a number: '))
#     t += n  # t = t + n

# print("sum is:", t)

number = 0
t= 0
while number < 3:
    n = float(input('enter a number: '))
    t += n 
    number += 1

    
t = 0
while True:
    n = float(input('enter a number: '))
    t += n
    user_choice = input("do you want to continue?(y or n) ")
    if user_choice == "n":
        break
print("sum is:", t)