from clear_salary import get_cleaned_data
from salary_calculation import calculate_stats

def main():
    path_to_file = "salary_file.txt"
    
    # Отримуємо дані (тепер файл створиться автоматично, якщо його нема)
    clean_salaries = get_cleaned_data(path_to_file)
    
    # Виконуємо розрахунок
    total, average = calculate_stats(clean_salaries)
    
    if clean_salaries:
        print(f"Загальна сума заробітної плати: {total}")
        print(f"Середня заробітна плата: {average}")
    else:
        print("Дані відсутні. Будь ласка, заповніть створений файл 'salary_file.txt' у форматі: Ім'я,Зарплата")

if __name__ == "__main__":
    main()
