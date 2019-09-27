contact={}
def add_contact(name,phno):
        if(name in contact.keys()):
            print(name,"contact already exists...!!")
        else:
            contact[name]=phno
            print("contact saved successfully")
def display_contact():
    i=0
    if(i<len(contact)):
        for name,phone in contact.items():
            print(i+1,"name",name,"phno=",phone)
            if(i>len(contact)):
                break
                i=i+1
def delete_contact(name):
    if name in contact.keys():
        contact.popitem()
        print("contact deleted")
    else:
        print(name,"contact doesnt exist")                
def update_contact(name,phno):
    if name in contact.keys():
        contact.update({name:phno})
        print("updated sucessfully")
    else:
        print("contact doesnt exist")
def search_contact(name):
    
    if name in contact.keys():
        print(name,"existed")
        display_contact()
    else:
        print(name,"doesn exist")        