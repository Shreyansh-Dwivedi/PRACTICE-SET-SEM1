import os

def display_menu():
    print("\nSimple File Manager Menu:")
    print("1. List current directory contents")
    print("2. Change current directory")
    print("3. Open a file")
    print("4. Create a new file")
    print("5. Rename a file")
    print("6. Delete a file")
    print("7. Exit")

def list_directory_contents():
    current_directory = os.getcwd()
    print(f"\nCurrent Directory: {current_directory}")
    
    files = os.listdir(current_directory)
    if not files:
        print("No files in the current directory.")
    else:
        print("Files in the current directory:")
        for file in files:
            print(file)

def change_directory():
    new_directory = input("Enter the path of the new directory: ")
    try:
        os.chdir(new_directory)
        print(f"Changed to: {os.getcwd()}")
    except FileNotFoundError:
        print("Directory not found.")

def open_file():
    file_name = input("Enter the name of the file to open: ")
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print(f"\nContents of {file_name}:\n{content}")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"Error opening file: {e}")

def create_new_file():
    file_name = input("Enter the name of the new file: ")
    try:
        with open(file_name, 'w') as file:
            print(f"File {file_name} created successfully.")
    except Exception as e:
        print(f"Error creating file: {e}")

def rename_file():
    old_name = input("Enter the current name of the file: ")
    new_name = input("Enter the new name of the file: ")
    try:
        os.rename(old_name, new_name)
        print(f"File {old_name} renamed to {new_name} successfully.")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"Error renaming file: {e}")

def delete_file():
    file_name = input("Enter the name of the file to delete: ")
    try:
        os.remove(file_name)
        print(f"File {file_name} deleted successfully.")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"Error deleting file: {e}")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            list_directory_contents()
        elif choice == '2':
            change_directory()
        elif choice == '3':
            open_file()
        elif choice == '4':
            create_new_file()
        elif choice == '5':
            rename_file()
        elif choice == '6':
            delete_file()
        elif choice == '7':
            print("Exiting File Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
