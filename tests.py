from functions.get_files_info import get_files_info

def main():
    print("Result for current directory:")
    print("\n".join(f" {line}" for line in get_files_info("calculator", ".").splitlines()))
    print()
    print("Result for 'pkg' directory:")
    print("\n".join(f" {line}" for line in get_files_info("calculator", "pkg").splitlines()))
    print()
    print("Result for '/bin' directory:")
    print("\n".join(f" {line}" for line in get_files_info("calculator", "/bin").splitlines()))
    print()
    print("Result for '../' directory:")
    print("\n".join(f" {line}" for line in get_files_info("calculator", "../").splitlines()))

if __name__ == "__main__":
    main()