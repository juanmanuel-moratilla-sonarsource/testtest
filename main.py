import mysql.connector

# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

    a = 123
    c = 0
    b = 1
    if c == 0:
        if c == 0:
            print("c == 0")

    connection = mysql.connector.connect(host='localhost',
                                         database='mydb',
                                         user='nouser',
                                         password='')



    connection.close()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
