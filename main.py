def create_battlefield():
    # Список букв для обозначения вертикалей (A - К)
    letters = [chr(i) for i in range(ord('А'), ord('К') + 1)]
    # Список чисел для обозначения горизонталей (1 - 10)
    numbers = [str(i) for i in range(1, 11)]
    
    # Создаем игровое поле
    battlefield = []
    for letter in letters:
        for number in numbers:
            battlefield.append(f"{letter}{number}")
    
    return battlefield


def display_battlefield():
    # Вывод игрового поля в виде таблицы
    letters = [chr(i) for i in range(ord('А'), ord('К') + 1)]
    numbers = [str(i) for i in range(1, 11)]

    # Печать заголовков столбцов
    print("   " + " ".join(numbers))
    
    # Печать строк поля
    for i, letter in enumerate(letters):
        row = [f"{letter}{num}" for num in numbers]
        print(f"{letter} {' '.join(row)}")


# Создание игрового поля
battlefield = create_battlefield()
print("Все клетки игрового поля:")
print(battlefield)

# Отображение игрового поля
print("\nИгровое поле:")
display_battlefield()
