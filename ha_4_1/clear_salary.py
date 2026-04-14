def get_cleaned_data(path):
    # Використовуємо словник для зберігання унікальних розробників {Ім'я: Зарплата}
    unique_developers = {}
    
    try:
        # Відкриваємо файл для читання з правильним кодуванням
        with open(path, 'r', encoding='utf-8') as f:
            
            for line in f:
                # Видаляємо зайві пробіли та символи переносу
                line = line.strip()
                # Пропускаємо порожні рядки або рядки без коми
                if not line or ',' not in line:
                    continue
                
                try:
                    # Розділяємо рядок на ім'я та зарплату
                    name, salary = line.split(',')
                    name = name.strip()
                    salary_val = float(salary.strip())
                    
                    # Перевірка на унікальність: якщо ім'я вже є, пропускаємо дублікат
                    if name not in unique_developers:
                        unique_developers[name] = salary_val
                    else:
                        print(f"Попередження: Дублікат для співробітника '{name}' проігноровано.")
                except ValueError:
                    # Обробка випадку, якщо зарплата вказана не числом
                    print(f"Помилка: Некоректні дані у рядку '{line}'.")
                    continue
        
        # Повертаємо список зарплат для подальших обчислень
        return list(unique_developers.values())

    except FileNotFoundError:
        # Обробка винятку, якщо файл не знайдено за вказаним шляхом
        print(f"Критична помилка: Файл за шляхом '{path}' не знайдено!")
        return None
