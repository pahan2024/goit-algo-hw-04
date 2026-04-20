import os
import json # Використаємо для виводу у вигляді таблиці

def get_cats_info(path):
    cats_list = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                
                try:
                    cat_id, name, age = line.split(',')
                    cats_list.append({
                        "id": cat_id.strip(),
                        "name": name.strip(),
                        "age": age.strip()
                    })
                except ValueError:
                    print(f"Помилка формату у рядку: {line}")
        return cats_list

    except FileNotFoundError:
        print(f"Помилка: Файл за шляхом '{path}' не знайдено.")
        return []

# --- БЛОК ЗАПУСКУ ---
# Автоматично знаходимо файл cats_file.txt у тій же папці, де лежить скрипт
current_dir = os.path.dirname(os.path.abspath(__file__))
path_to_file = os.path.join(current_dir, "cats_file.txt")

cats_info = get_cats_info(path_to_file)

# Виводимо результат (indent=4 робить відступи)
print(json.dumps(cats_info, indent=4, ensure_ascii=False))
