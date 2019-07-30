classes = ['Barbarian','Bard','Cleric','Druid','Fighter','Monk','Paladin','Ranger','Rouge','Sorcerer','Warlock','Wizard']
races = ['Human','Dwarf','Gnome','Elf']

def print_menu(classes):
    print ("Character/Race Selection")
    for key,classes_ in enumerate(classes, start=1):
        print('{}. {}'.format(key,classes_))
    print() 
    
        
    
print_menu(classes)
print_menu(races)