def total_salary(path):
    try:
        total_sum = 0
        developers_count = 0

        # Використовуємо менеджер контексту with та вказуємо кодування utf-8
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                # Видаляємо пробіли та символи переносу рядка
                line = line.strip()

                # Пропускаємо порожні рядки, щоб не виникало помилок
                if not line:
                    continue

                try:
                    # Розділяємо дані за комою
                    name, salary = line.split(",")
                    total_sum += float(salary)
                    developers_count += 1
                except ValueError:
                    print(f"Помилка формату у рядку: '{line}'. Пропускаємо.")

        # Перевірка на випадок порожнього файлу (щоб не було ділення на нуль)
        if developers_count == 0:
            return (0, 0)

        average_salary = total_sum / developers_count

        # Повертаємо кортеж із двох чисел
        return (total_sum, average_salary)

    except FileNotFoundError:
        print(f"Помилка: Файл за шляхом '{path}' не знайдено.")
        return None
    except Exception as e:
        print(f"Виникла непередбачувана помилка: {e}")
        return None


path_to_salary_file = "salary_file.txt"

result = total_salary(path_to_salary_file)

if result:
    total, average = result
    print(f"Загальна сума зарплат: {total}, Середня зарплата: {average}")
