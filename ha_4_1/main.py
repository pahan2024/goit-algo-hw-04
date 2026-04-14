import os
from clear_salary import get_cleaned_data
from salary_calculation import calculate_stats

def main():
    # Автоматично визначаємо шлях до папки, де лежить цей файл (main.py)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # З'єднуємо шлях папки з ім'ям файлу
    path_to_file = os.path.join(current_dir, "salary_file.txt")
    
    # Крок 1: Отримання очищених даних
    clean_salaries = get_cleaned_data(path_to_file)
    
    # Крок 2: Розрахунок статистики
    total, average = calculate_stats(clean_salaries)
    
    # Крок 3: Вивід результату
    if clean_salaries:
        print(f"Загальна сума заробітної плати: {total}")
        print(f"Середня заробітна плата: {average}")
    else:
        print(f"Дані відсутні. Додайте запис у файл: {path_to_file}")

if __name__ == "__main__":
    main()
