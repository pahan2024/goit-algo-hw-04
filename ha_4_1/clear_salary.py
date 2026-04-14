import os

def get_cleaned_data(path):
    # Використовуємо словник для зберігання унікальних розробників {Ім'я: Зарплата}
    unique_developers = {}
    
    # Перевіряємо, чи існує файл. Якщо ні — створюємо порожній
    if not os.path.exists(path):
        print(f"Попередження: Файл '{path}' не знайдено. Створюю новий...")
        with open(path, 'w', encoding='utf-8') as f:
            pass
        return []

    try:
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
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
                    continue
        
        return list(unique_developers.values())

    except Exception as e:
        print(f"Сталася помилка при чистці даних: {e}")
        return []

    # except FileNotFoundError:
    #     # Обробка винятку, якщо файл не знайдено за вказаним шляхом
    #     print(f"Критична помилка: Файл за шляхом '{path}' не знайдено!")
    #     return None
