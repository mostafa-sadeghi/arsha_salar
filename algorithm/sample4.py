# def get_color(x, y):
#     if x % 2 == y % 2:
#         return "white"
#     else:
#         return "black"


# print(get_color(1, 2))
# print(get_color(1, 5))
# print(get_color(5, 5))
# print(get_color(4, 2))

# def get_h_m_s(time_sec):
#     if time_sec >= 3600:
#         hours = time_sec // 3600
#         time_sec = time_sec % 3600
#     else:
#         hours = 0

#     if time_sec >= 60:
#         minutes = time_sec // 60
#         time_sec = time_sec % 60

#     else:
#         minutes = 0

#     seconds = time_sec
#     return f'{hours}h:{minutes}m:{seconds}s'

# print(get_h_m_s(30))
# print(get_h_m_s(60))
# print(get_h_m_s(90))
# print(get_h_m_s(3600))
# print(get_h_m_s(3610))
# print(get_h_m_s(9640))

# def get_smallets(all_numbers):
#     s = all_numbers[0]
#     for number in all_numbers:
#         if number < s:
#             s = number
#     return s

# print(get_smallets([1,2,3,4,5]))
# print(get_smallets([5,4,3,2,1]))
# print(get_smallets([57,14,32,2,10]))

def calc_sum(x):
    r = 0
    for number in x:
        r += number

    return r

numbers = []
while True:
    n = int(input("> "))
    numbers.append(n)
    user_input = input("do you want to continue(y or n)? ")
    if user_input == "n":
        break
print(calc_sum(numbers))
