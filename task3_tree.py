import sys
from pathlib import Path

from colorama import Fore, Style, init

init(autoreset=True)


def print_tree(directory: Path, prefix: str = "") -> None:
    """Рекурсивно виводить вміст директорії: директорії синім, файли зеленим."""
    try:
        entries = sorted(directory.iterdir(), key=lambda p: (p.is_file(), p.name.lower()))
    except PermissionError:
        print(prefix + Fore.RED + "[немає доступу]")
        return
    for index, entry in enumerate(entries):
        last = index == len(entries) - 1
        connector = "┗ " if last else "┣ "
        if entry.is_dir():
            print(prefix + connector + Fore.BLUE + Style.BRIGHT + entry.name + "/")
            print_tree(entry, prefix + ("  " if last else "┃ "))
        else:
            print(prefix + connector + Fore.GREEN + entry.name)


def main() -> None:
    if len(sys.argv) != 2:
        print("Використання: python task3_tree.py <шлях_до_директорії>")
        sys.exit(1)
    root = Path(sys.argv[1])
    if not root.exists():
        print(f"Помилка: шлях не існує: {root}")
        sys.exit(1)
    if not root.is_dir():
        print(f"Помилка: шлях не є директорією: {root}")
        sys.exit(1)
    print(Fore.BLUE + Style.BRIGHT + root.name + "/")
    print_tree(root)


if __name__ == "__main__":
    main()
