# Problem 1
def main():
    fruit_list = ["apple", "banana", "orange", "grape", "pineapple"]
    print("Length of fruit list:", len(fruit_list))
    fruit_list.append("mango")
    print("Updated fruit list:", fruit_list)


if __name__ == "__main__":
    main()

# Problem 2
def access_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Index out of range!"


def modify_element(lst, index, new_value):
    try:
        lst[index] = new_value
        return f"Element at index {index} updated to {new_value}"
    except IndexError:
        return "Index out of range - cannot modify!"


def slice_list(lst, start, end):
    try:
        return lst[start:end]
    except IndexError:
        return "Invalid slice indices!"


def print_current_list(lst):
    print("\nCurrent list:", lst)


def index_game():
    sample_list = [10, 20, 30, 40, 50, "apple", "banana", True, 3.14]

    while True:
        print("\nOptions:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print_current_list(sample_list)
            try:
                index = int(input("Enter index to access: "))
                result = access_element(sample_list, index)
                print(f"Element at index {index}: {result}")
            except ValueError:
                print("Please enter a valid integer index!")

        elif choice == "2":
            print_current_list(sample_list)
            try:
                index = int(input("Enter index to modify: "))
                new_value = input("Enter new value: ")
                try:
                    new_value = int(new_value)
                except ValueError:
                    try:
                        new_value = float(new_value)
                    except ValueError:
                        pass 
                result = modify_element(sample_list, index, new_value)
                print(result)
                print_current_list(sample_list)
            except ValueError:
                print("Please enter a valid integer index!")

        elif choice == "3":
            print_current_list(sample_list)
            try:
                start = int(input("Enter start index: "))
                end = int(input("Enter end index: "))
                result = slice_list(sample_list, start, end)
                print(f"Sliced list: {result}")
            except ValueError:
                print("Please enter valid integer indices!")

        elif choice == "4":
            print("Thanks for playing!")
            break

        else:
            print("Invalid choice. Please enter 1-4.")


if __name__ == "__main__":
    index_game()
