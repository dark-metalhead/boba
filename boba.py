# Функция для фильтрации строк длиной <= 3 символов
def filter_short_strings(input_array):
    # Подсчитываем количество строк, длина которых <= 3
    count = 0
    for string in input_array:
        if len(string) <= 3:
            count += 1
    
    # Создаем массив фиксированной длины
    result_array = [""] * count
    
    # Заполняем массив строками длиной <= 3
    index = 0
    for string in input_array:
        if len(string) <= 3:
            result_array[index] = string
            index += 1
            
    return result_array

# Ввод массива строк с клавиатуры
input_array = input("Введите строки, разделенные пробелами: ").split()

# Фильтрация строк и вывод результата
result_array = filter_short_strings(input_array)
print("Строки длиной <= 3 символов:", result_array)