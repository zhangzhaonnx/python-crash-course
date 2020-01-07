# def greet_user():
#     """显示简单的问候语"""
#     print("Hello!")
# greet_user()

# def greet_user(username):
#     """显示简单的问候语"""
#     print("Hello " + username + "!")
# greet_user("jesse")

def get_formatted_name(first_name, last_name, middle_name=''):
    """返回整洁的姓名"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

# 这是一个无限循环!
while True:
    print("Please enter you name")
    print("Enter 'q' at any time to quit")
    first = input("First name: ")
    if first == 'q':
        break
    last = input("Last name: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print('\nHello, ' + formatted_name + '!')
