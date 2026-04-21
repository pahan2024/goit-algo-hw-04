import sys
from pathlib import Path
from colorama import Fore, Style, init

# Ініціалізація colorama для Windows
init(autoreset=True)

def visualize_directory(path: Path, indent: str = ""):
    try:
        # Отримуємо відсортований список вмісту (директорії спочатку)
        items = sorted(list(path.iterdir()), key=lambda x: (x.is_file(), x.name.lower()))
        
        for index, item in enumerate(items):
            # Визначаємо, чи це останній елемент у списку для коректного малювання гілок
            is_last = index == len(items) - 1
            connector = "┗ " if is_last else "┣ "
            
            if item.is_dir():
                # Виводимо папку синім кольором
                print(f"{indent}{connector}{Fore.BLUE}📂 {item.name}{Style.RESET_ALL}")
                
                # Додаємо відступ для вкладених елементів
                new_indent = indent + ("  " if is_last else "┃ ")
                visualize_directory(item, new_indent)
            else:
                # Виводимо файл зеленим кольором
                print(f"{indent}{connector}{Fore.GREEN}📜 {item.name}{Style.RESET_ALL}")
                
    except PermissionError:
        print(f"{indent}{Fore.RED}[Доступ заборонено]{Style.RESET_ALL}")

def main():
    # Перевірка наявності аргументу
    if len(sys.argv) < 2:
        print(f"{Fore.YELLOW}Будь ласка, вкажіть шлях до директорії як аргумент.{Style.RESET_ALL}")
        print("Приклад: python hw03.py ./my_folder")
        return

    root_path = Path(sys.argv[1])

    # Перевірка існування шляху
    if not root_path.exists():
        print(f"{Fore.RED}Помилка: Шлях '{root_path}' не існує.{Style.RESET_ALL}")
        return
    
    if not root_path.is_dir():
        print(f"{Fore.RED}Помилка: Шлях '{root_path}' не є директорією.{Style.RESET_ALL}")
        return

    # Початок візуалізації
    print(f"{Fore.CYAN}📦 {root_path.name}{Style.RESET_ALL}")
    visualize_directory(root_path)

if __name__ == "__main__":
    main()
