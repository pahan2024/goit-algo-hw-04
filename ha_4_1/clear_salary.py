def get_cleaned_data(path):
    unique_developers = {}
    
    try:
        # Спроба відкрити файл для читання
        with open(path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        # Якщо файлу немає — створюємо порожній файл
        print(f"Файл '{path}' не знайдено. Створюю новий порожній файл...")
        with open(path, 'w', encoding='utf-8') as f:
            pass # Просто створюємо файл і нічого не записуємо
        return [] # Повертаємо порожній список

    # Обробка рядків (якщо файл був знайдений або щойно створений)
    for line in lines:
        line = line.strip()
        if not line or ',' not in line:
            continue
        
        try:
            name, salary = line.split(',')
            name = name.strip()
            salary_val = float(salary.strip())
            
            if name not in unique_developers:
                unique_developers[name] = salary_val
            else:
                print(f"Попередження: Дублікат '{name}' проігноровано.")
        except ValueError:
            print(f"Помилка: Некоректні дані у рядку '{line}'.")
            
    return list(unique_developers.values())
