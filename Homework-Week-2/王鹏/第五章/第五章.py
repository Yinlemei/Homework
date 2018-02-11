stuff={'rope':1,'torch':6,'gold coin':42,'dagger':1,'arroe':12}

def displayInventory(inventory):
    print('Inventory:')
    item_total=0
    for k,v in inventory.items():
        print(str(v)+' '+k)
        item_total+=v
    print('Total munber of items:'+str(item_total))

displayInventory(stuff)
    
