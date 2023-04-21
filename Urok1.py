# Функция для сложения двух чисел
def add(x, y):
    return x + y

# Функция для вычитания двух чисел
def subtract(x, y):
    return x - y

# Функция для умножения двух чисел
def multiply(x, y):
    return x * y

# Функция для деления двух чисел
def divide(x, y):
    return x / y

# Выводим сообщение пользователю
print("Выберите операцию.")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")

# Получаем выбор пользователя
choice = input("Введите номер операции (1/2/3/4): ")

# Получаем два числа от пользователя
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

# Выполняем выбранную операцию
if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))

elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))

elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))

elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))

else:
    print("Неверный выбор операции")

# Выполняем выбранную операцию 2
# Выполняем выбранную операцию 22