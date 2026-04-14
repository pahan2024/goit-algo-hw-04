def calculate_stats(salaries):
    if not salaries:
        return 0, 0
    total = sum(salaries)
    average = total / len(salaries)
    return total, average
