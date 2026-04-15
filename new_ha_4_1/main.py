def total_salary(path):
    try:
        total_sum = 0
        developers_count = 0
        processed_names = set()  # Множина для відстеження унікальних імен

        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:  # Пропускаємо порожні рядки
                    continue

                try:
                    # Розділяємо дані на ім'я та зарплату
                    name, salary = line.split(",")
                    name = name.strip()

                    # Перевірка на дублікати імен
                    if name in processed_names:
                        print(
                            f"Попередження: Розробник '{name}' із сумою {salary} вже є у списку. "
                            f"Рядок проігноровано. Будь ласка, перевірте файл salary_file.txt"
                        )
                        continue

                    total_sum += float(salary)
                    developers_count += 1
                    processed_names.add(name)  # Додаємо ім'я до списку оброблених

                except ValueError:
                    # Обробка випадку, якщо дані в рядку некоректні
                    print(f"Помилка формату у рядку: '{line}'. Пропускаємо.")

        # Перевірка, щоб уникнути ділення на нуль, якщо файл порожній
        if developers_count == 0:
            return (0, 0)

        average_salary = total_sum / developers_count
        return (total_sum, average_salary)

    except FileNotFoundError:
        # Обробка випадку, якщо файл не знайдено за вказаним шляхом
        print(f"Помилка: Файл за шляхом '{path}' не знайдено.")
        return None
    except Exception as e:
        # Обробка будь-яких інших непередбачуваних помилок
        print(f"Виникла непередбачувана помилка: {e}")
        return None


# --- Блок запуску програми ---
# Обов'язково вказати назву вашого файлу salary_file.txt (він має бути в тій же папці, що і скрипт)

path_to_salary_file = "salary_file.txt"

result = total_salary(path_to_salary_file)

if result:
    total, average = result
    # Використовую формат :g, щоб прибрати зайві нулі після коми в середньому значенні, та .2f для загальної суми
    print(f"Загальна сума зарплат: {total:.2f}, Середня зарплата: {average:g}")
