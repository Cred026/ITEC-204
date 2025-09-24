lists: list = []

def main():
    while True:
        print("Choose a number to perform")
        print("\t1, Append")
        print("\t2, Insert")
        print("\t3, Remove")
        print("\t4, Pop")
        print("\t5, Clear")
        print("\t6, Index")
        print("\t7, Count")
        print("\t8, Sort")
        print("\t9, Reverse")
        print("\t10, View List")
        print("\t11, Exit")
        
        user_input = input("Enter your choice: ")
        choice: int | None = None

        try:
            choice = int(user_input)
        except Exception:
            print("Please enter number")
            continue

        if choice > 11:
            print("choose within the given")
            continue

        match choice:
            case 1:
                appends()
            case 2:
                inserts()
            case 3:
                remove_list()
            case 4:
                pop_list()
            case 5:
                clear()
            case 6:
                index_list()
            case 7:
                count_list()
            case 8:
                sort_list()
            case 9:
                reverse_list()
            case 10:
                view_list()
            case 11:
                print("Program ended")
                break

def appends():
    while True:
        john = input("How many do you wish to append?: ")
        types = input("What type do you want to insert ( 1(string), 2(int), 3(boolean), 4(float))")
        try:
            nums_append = int(john)
            types_num = int(types)

            value = 0
            while nums_append > value:
                match types_num:
                    case 1:
                        inputs = input("Enter the one you want to append: ")
                    case 2:
                        inputs = int(input("Enter the one you want to append: "))
                    case 3:
                        inputs = bool(input("Enter the one you want to append: "))
                    case 4:
                        inputs = float(input("Enter the one you want to append: "))
                if types_num not in [1,2,3,4]:
                    print("Please enter the correct input:")
                    continue
                lists.append(inputs)
            break
        except Exception:
            print("Please enter a number")
            continue

def inserts():
    while True:
        types_num = input("What type do you wish to enter: ")
        inputs = input("What index do you wish to insert: ")
        try: 
            choice = int(inputs)
            num_types = int(types_num)
            match num_types:
                case 1:
                    value = input("What do you want to insert: ")
                case 2:
                    value = int(input("What do you want to insert: "))
                case 3:
                    value = bool(input("What do you want to insert: "))
                case 4:
                    value = float(input("What do you want to insert: "))
            if num_types not in [1,2,3,4]:
                print("Please enter the correct input:")
                continue
            lists.insert(choice, value)
        except Exception:
            print("Please enter a number")
            continue
        break

def remove_list():
    if len(lists) <= 0:
        print("You cant remove since lists is empty")
        return
    while True:
        types_num = input("What type do you wish to enter: ")
        inputs_num = input("How many do you wish to remove? ")
        print("Do you wish to go back?(y/n)")

        try:
            if inputs_num.lower() == "y":
                break

            
            inputs_num = int(inputs_num)
        except Exception:
            print("Please enter a number")
            continue

        if inputs_num > len(lists):
            print("Please enter within the range")
            continue
        
        value = 0
        while inputs_num > value:
            inputs = input("Enter the value you want to remove: ")
            print("Do you wish to go back?(y/n)")

            if inputs.lower() == "y":
                break

            if inputs not in lists:
                print("Value not in lists")
                continue
            
            lists.remove(inputs)
            if inputs not in lists:
                print(f"Removed value")
                value += 1
        break

def pop_list():
    if len(lists) <= 0:
        print("You cant remove since lists is empty")
        return
    item = lists.pop()
    print(f"Removed {item}")

def clear():
    if len(lists) <= 0:
        print("You have no list")
        return
    lists.clear()
    print("You removed all the value")

def index_list():
    if len(lists) <= 0:
        print("You have no list")
        return
    while True:
        inputs = input("Enter the value to know the index: ")
        print("Do you wish to go back?(y/n)")

        if inputs.lower() == "y":
            return

        if inputs not in lists:
            print("Value not in lists")
            continue
        break
    value = lists.index(inputs)
    print(value)

def count_list():
    if len(lists) <= 0:
        print("You have no list")
        return
    inputs = input("enter the value you wish to know the occurances of: ")
    value =  lists.count(inputs)
    print(f"Occurance: {value}")

def sort_list():
    if len(lists) <= 0:
        print("You have no list")
    lists.sort()
    for i in lists:
        print(i, end=", ")

    print()

def reverse_list():
    if len(lists) <= 0:
        print("You have no list")

    lists.sort(reverse=True)
    for i in lists:
        print(i, end=", ")

    print()

def view_list():
    if len(lists) <= 0:
        print("You have no list")
    for i in lists:
        print(i, end=", ")
    print()


main()