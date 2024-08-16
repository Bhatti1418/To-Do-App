import time
print("Time : ",time.strftime("%H:%M"))
print("Date : ",time.strftime("%D"))
my_list = []

while True:
    user_prompt = input("Type add or show or edit or remove or exit: ")
    user_prompt = user_prompt.strip()
    match user_prompt:
        case 'add':
            value = input("Enter a todo : ")
            values = value.title()
            my_list.append(values)
        case 'edit':
            num = int(input("Enter the number of todo which you want to edit : "))
            new_val = input("Enter the edit todo value : ")
            my_list[num-1] = new_val
            print("Task has done!")
        case 'show':
            if my_list == []:
                print("your list is empty")
            for index,item in enumerate(my_list):
                print(index + 1,'-',item)
        case 'remove':
            num = int(input("Enter the item number which you want to remove : "))
            my_list.pop(num-1)
            print("Item is removed successfully!")
        case 'exit':
            break
        case whatever:
            print("You entered an unknown command")
print("bye!")
