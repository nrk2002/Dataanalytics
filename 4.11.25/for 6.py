for num in range(1, 51):
    if num == 2 or num == 3 or num == 5 or num == 7:
        print(num)
    elif num > 1 and num % 2 != 0 and num % 3 != 0 and num % 5 != 0 and num % 7 != 0:
        print(num)
