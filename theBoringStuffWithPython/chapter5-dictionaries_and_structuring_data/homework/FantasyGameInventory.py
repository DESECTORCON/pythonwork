
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory, item):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        item_total = item_total + v.get(item, 0)
        print(a)

displayInventory(stuff, 'rope')
'''실패'''
