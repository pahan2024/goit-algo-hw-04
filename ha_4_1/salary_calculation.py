def calculate_stats(salaries):
    # Якщо список порожній (наприклад, у файлі були тільки помилки)
    if not salaries:
        return 0, 0
    
    # Розрахунок загальної суми
    total = sum(salaries)
    # Розрахунок середнього значення
    average = total / len(salaries)
    
    return total, average
