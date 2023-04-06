#git@github.com:ALLVIS-II/Project-week-7.git

items = []
item = input("Enter an item('STOP' to quit):")
while item.upper() != 'STOP':
    while item.capitalize() in items:
        print('Error:', item, 'already entered.')
        item = input('Enter another item:')
    if item.upper() != 'STOP':
        items.append(item.capitalize())
    if len(items) == 1:
        print('You have 1 item')
    else:
        print('You have', len(items), 'items')
    item = input("Enter an item('STOP' to quit):")
    num = 1
    for item in items:
        print('' + str(num)+'.'+ item)
        num += 1
