# Створіть функцію, яка приймає функцію як аргумент і виконує її кілька разів поспіль із одним і тим самим значенням.
# Наприклад, repeat(lambda x:x+1, 3, 5) має повернути результат застосування функції x+1 три рази до числа 5 (тобто 8).
def repeat(func, times, value):
    for _ in range(times):
        value = func(value)
    return value

print(repeat(lambda x: x + 1, 3, 5))