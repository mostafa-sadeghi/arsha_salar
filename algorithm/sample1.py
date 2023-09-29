# def is_even(number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False


# while not input('Do you want to know whether the number is even or not?(yes or no): ').lower().startswith('n'):
#     number = int(input("Enter a number: "))
#     if is_even(number):
#         print(f'{number} is even.')
#     else:
#         print(f'{number} is odd.')
# print("Good Bye")

# def area(width, height):
#     return width * height


# def perimeter(width, height):
#     return 2 * (width + height)


# w = int(input("enter the width: "))
# h = int(input("enter the height: "))
# selection = input("Area (a), or Perimeter(p)? ")
# if selection == "a":
#     print("area is:", area(w, h))

# elif selection == "p":
#     print(f'perimeter is: {perimeter(w,h)}')


# TODO
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 12, 13, 14, 15]
"""
برنامه ای بنویس که تعداد اعداد فرد موجود در لیست بالا را محاسبه کند

"""
def odd_numbers(numbers):
    count = 0
    for n in numbers:
        if n % 2 != 0:
            count += 1
    return count

print(f"count of odd numbers is:{odd_numbers(numbers)}")
print(f"count of odd numbers is:{odd_numbers((2,3,7,87,54))}")
print(f"count of odd numbers is:{odd_numbers({1,6,8,9,3,44})}")