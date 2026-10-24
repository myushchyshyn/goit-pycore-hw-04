def get_cats_info(path: str) -> list[dict]:
    """Читає файл 'id,name,age' по рядку і повертає список словників про котів.

    Якщо файл відсутній або рядок пошкоджено, повертає порожній список (для відсутнього файлу)
    або пропускає некоректні рядки з повідомленням.
    """
    cats = []
    try:
        with open(path, "r", encoding="utf-8") as fh:
            for line_no, line in enumerate(fh, start=1):
                line = line.strip()
                if not line:
                    continue
                parts = line.split(",")
                if len(parts) != 3:
                    print(f"Пропущено некоректний рядок {line_no}: {line!r}")
                    continue
                cat_id, name, age = parts
                cats.append({"id": cat_id, "name": name, "age": age})
    except FileNotFoundError:
        print(f"Файл не знайдено: {path}")
        return []
    except UnicodeDecodeError as exc:
        print(f"Файл пошкоджено: {exc}")
        return []
    return cats
