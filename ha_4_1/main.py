from clear_salary import get_cleaned_data
from salary_calculation import calculate_stats

def main():
    # Шлях до вашого текстового файлу
    path_to_file = "salary_file.txt"
    
    # Крок 1: Отримання очищених даних
    clean_salaries = get_cleaned_data(path_to_file)
    
    # Крок 2: Перевірка, чи вдалося прочитати файл
    if clean_salaries is not None:
        # Виконуємо розрахунок, якщо дані існують
        total, average = calculate_stats(clean_salaries)
        
        if clean_salaries:
            print(f"Загальна сума заробітної плати: {total}")
            print(f"Середня заробітна плата: {average}")
        else:
            print("Файл знайдено, але він не містить коректних даних для розрахунку.")
    else:
        # Повідомлення, якщо виникла помилка FileNotFoundError
        print("Розрахунок неможливий через відсутність файлу.")

if __name__ == "__main__":
    main()
