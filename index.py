number = int(input())
if 0 <= number <= 36:
    if number == 0:
        print("зеленый")
    elif 0 < number < 11:
        if number % 2 == 0:
            print("черный")
        else:
            print("красный")
    elif 10 < number < 19:
        if number % 2 == 0:
            print("красный")
        else:
            print("черный")
    elif 18 < number < 29:
        if number % 2 == 0:
            print("черный")
        else:
            print("красный")
    elif 28 < number < 37:
        if number % 2 == 0:
            print("красный")
        else:
            print("черный")
else:
    print("ошибка ввода")





