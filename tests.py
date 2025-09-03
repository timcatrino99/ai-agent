from functions.get_file_content import get_file_content

def main():
    print("Results for main.py in working directory calculator")
    print(get_file_content("calculator", "main.py"))
    print()
    print("Results for pkg/calculator.py in working directory calculator")
    print(get_file_content("calculator", "pkg/calculator.py"))
    print()
    print("Results for /bin/cat in working directory calculator")
    print(get_file_content("calculator", "/bin/cat"))
    print()
    print("Results for pkg/does_not_exist.py in working directory calculator")
    print(get_file_content("calculator", "pkg/does_not_exist.py"))

if __name__ == "__main__":
    main()