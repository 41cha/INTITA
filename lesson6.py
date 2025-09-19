#Користувач вводить список чисел. Напишіть програму, яка обчислює середнє арифметичне цих чисел
numbers = input("Введіть список чисел, розділених пробілом: ").split()
numbers = [float(num) for num in numbers]
average = sum(numbers) / len(numbers)
print(f"Середнє арифметичне: {average}")
