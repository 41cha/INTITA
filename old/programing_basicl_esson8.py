# Напишіть функцію, яка приймає список чисел та функцію, і застосовує цю функцію до кожного елемента списку, повертаючи новий список.
# Наприклад, для `[1,2,3]` і `lambda x:x**2` результат `[1,4,9]`.

def power_func(list, func):
    result = [func(x) for x in list]
    return result

result = power_func([1, 2, 3], lambda x: x**2)
print(result)