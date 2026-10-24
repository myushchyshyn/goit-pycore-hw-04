import os
import subprocess
import sys
import tempfile
from pathlib import Path

from task1_salary import total_salary
from task2_cats import get_cats_info
from task4_bot import parse_input, add_contact, change_contact, show_phone, show_all

tmp = Path(tempfile.mkdtemp())

salary = tmp / "salary.txt"
salary.write_text("Alex Korp,3000\nNikita Borisenko,2000\nSitarama Raju,1000\n", encoding="utf-8")
assert total_salary(str(salary)) == (6000, 2000), total_salary(str(salary))
assert total_salary(str(tmp / "missing.txt")) == (0, 0)

cats = tmp / "cats.txt"
cats.write_text("60b90c1c13067a15887e1ae1,Tayson,3\n60b90c2413067a15887e1ae2,Vika,1\n", encoding="utf-8")
assert get_cats_info(str(cats)) == [
    {"id": "60b90c1c13067a15887e1ae1", "name": "Tayson", "age": "3"},
    {"id": "60b90c2413067a15887e1ae2", "name": "Vika", "age": "1"},
], get_cats_info(str(cats))
assert get_cats_info(str(tmp / "missing.txt")) == []

assert parse_input("  ADD  John 123 ") == ("add", ["John", "123"])
contacts = {}
assert add_contact(["John", "1234567890"], contacts) == "Contact added."
assert add_contact(["John", "1"], contacts).startswith("Contact already exists")
assert change_contact(["John", "0987654321"], contacts) == "Contact updated."
assert change_contact(["Nobody", "1"], contacts).startswith("Contact 'Nobody' not found")
assert show_phone(["John"], contacts) == "0987654321"
assert show_all(contacts) == "John: 0987654321"

out = subprocess.run([sys.executable, "task3_tree.py", str(tmp)], capture_output=True, text=True)
assert out.returncode == 0 and "salary.txt" in out.stdout, out.stdout + out.stderr
bad = subprocess.run([sys.executable, "task3_tree.py", str(tmp / "nope")], capture_output=True, text=True)
assert bad.returncode == 1 and "не існує" in bad.stdout

print("ALL HW4 TESTS PASSED")
