def remove_from_list(user_input,items):

    if user_input in items:

        items.remove(user_input)
        print(f"{user_input} has been removed")

    else:
        print("the item is not found")

items = ["apple", "banana", "cherry", "Data"]
user_input = input("enter an item to remove: ")

 remove_from_list(user_input,items)

   print("the list is:", items)

*****************************************************************************************

def calculate_factorial(number):
    result = 1
    for i in range(1,number + 1):
        result *= i


    return result


number = 10
print(calculate_factorial(number))
