#git@github.com:ALLVIS-II/Project-week-7.git

item_List = []
item = input("Enter an item('STOP' to quit):")
while item.upper() != 'STOP':
    while item.capitalize() in item_List:
        print('Error:', item, 'already entered.')
        item = input('Enter another item:')

if item.upper() != 'STOP':
