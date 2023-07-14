# numbers = [1,2]
# numbers[0] = 1000
# print(numbers)
# numbers.append("ali")
# numbers.append(3000)
# print(numbers)


# numbers = (1,2,3)
# print(numbers[0])

# numbers[0] = 1000 # error


# favorite_sports1 = {} #    دیکشنری خالی
# print(favorite_sports1)



favorite_sports = {
    "artin" : "football",
    "sara": "tennis",
    "armin":"football"
}

print("artin likes:", favorite_sports["artin"])
print(f"sara likes: {favorite_sports['sara']}")

name = input("enter a name: ")
sport = input("enter a sport: ")

favorite_sports[name] = sport

print(favorite_sports)