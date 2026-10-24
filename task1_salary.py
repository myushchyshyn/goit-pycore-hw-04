def total_salary(path: str) -> tuple[int, float]:
    """Повертає (загальна сума, середня зарплата) з файлу 'Прізвище,зарплата' по рядку.

    Якщо файл відсутній або має неправильний формат, повертає (0, 0) та виводить повідомлення.
    """
    total = 0
    count = 0
    try:
        with open(path, "r", encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                _, salary = line.split(",")
                total += int(salary)
                count += 1
    except FileNotFoundError:
        print(f"Файл не знайдено: {path}")
        return 0, 0
    except (ValueError, UnicodeDecodeError) as exc:
        print(f"Файл пошкоджено або має неправильний формат: {exc}")
        return 0, 0
    average = total / count if count else 0
    return total, average
