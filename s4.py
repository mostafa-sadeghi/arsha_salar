a = 4
b = 5

if a > b:
    print("a is greater than b")
    print("ok")

else:
    print("a is less than or equal to b")


# تمرین:
# دو عدد از ورودی بگیری و با هم مقایسه کنی
# نام، سن و نام کلاس برنامه نویس یمورد علاقه دو دانش آموز را از ورودی
# بگیری و مثلا به صورت زیر نمایش دهی
# arsha has 11 years old and likes python
# artin has 10 years old and likes scratch


name = input('Enter your name: ')
age = input('Enter your age: ')
course = input('Enter your course name: ')
# message = name + " has " + age + " years old and likes " + course + "."
message = f"{name} has {age} years old and likes {course}"
print(message)