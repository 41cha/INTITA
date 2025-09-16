N = int(input("enter your N number: "))

for i in range(0, N + 1):
    if i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    elif i % 3 == 0 and i % 5 == 0:
        print("fizz buzz")
    else:
        print(i)

