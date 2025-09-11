
def prob_1():
    while(True):
        try:
            fn = int(input("Enter the first number: "))
            sn = int(input("Enter the first number: "))
        except ValueError:
            print("Input must be a number")
            continue
        except ZeroDivisionError:
            print("Second input must not be zero")
            continue
        except Exception as e:
            print(f"Error: {e}")
            continue
        if(sn == 0):
            print("Second input must not be zero")
            continue
        break

    odd_total = 0
    even_total = 0
    all_total = 0

    for i in range(fn, sn + 1):
        all_total += i
        
        if(i % 2 == 0):
            even_total += i
            print(f"Even {i}")

        if(i % 2 != 0):
            odd_total += i
            print(f"Odd {i}")


    print(f"Total odd number: {odd_total}")
    print(f"Total even number: {even_total}")
    print(f"Total all number: {all_total}")


def prob_2():
    collectionss = [1, 2, 3, 4, 5, 6, 7]

    middle = len(collectionss) / 2

    if((middle - int(middle)) == 0):
        middle -= 1
        print(f"Corrected: {middle}")

    print(f"First: {collectionss[0]}")
    print(f"Last: {collectionss[-1]}")
    print(f"Middle: {collectionss[int(middle)]}")

def prob_3():
    orig_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    odd_list = []
    even_list = []

    for i in orig_list:
        if (i % 2 == 0):
            even_list.append(i)
        if (i % 2 != 0):
            odd_list.append(i)

    print("Even Number:")
    for i in even_list:
        print(f"\t{i}")

    print("Odd Number:")
    for i in odd_list:
        print(f"\t{i}")

def prob_4():
    orig_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    odd_list = []
    even_list = []
    i = 0

    while (i < len(orig_list)):

        if (i % 2 == 0):
            even_list.append(orig_list[i])

        if (i % 2 != 0):
            odd_list.append(orig_list[i])
            
        i += 1

    print("Even Number:")
    for i in even_list:
        print(f"\t{i}")

    print("Odd Number:")
    for i in odd_list:
        print(f"\t{i}")

def prob_5():
    orig_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    i = 0

    while(i < len(orig_list)):
        print(f"Index: {i}\tData: {orig_list[i]}")
        i += 1    

prob_4()