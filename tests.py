from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

def main():
    print('Results for "main.py"')
    print(run_python_file("calculator", "main.py"))
    print()
    print('Results for "main.py", ["3 + 5"]')
    print(run_python_file("calculator", "main.py", ["3 + 5"]))
    print()
    print('Results for "tests.py"')
    print(run_python_file("calculator", "tests.py"))
    print()
    print('Results for "../main.py"')
    print(run_python_file("calculator", "../main.py"))
    print()
    print('Results for "nonexistent.py"')
    print(run_python_file("calculator", "nonexistent.py"))

if __name__ == "__main__":
    main()